---
title: "Where teams and agents work together"
source: "https://www.notion.so/Huggle-Invitation-33250e88a6f680acac6adcba842674cf"
author:
published:
created: 2026-04-13
description: "A collaborative AI workspace, built on your company context. Build and orchestrate agents right alongside your team's projects, meetings, and connected apps."
tags:
  - "clippings"
---
## Huggle Invitation — 部署与配置指南

### 架构概览

平台：GCP Cloud Run（europe-west1）

镜像仓库：Google Container Registry（ [gcr.io](http://gcr.io/) ）

构建工具：Cloud Build

域名： [invitation.wordleap.co.uk](http://invitation.wordleap.co.uk/)

Cloud Run 服务名：huggle-invitation

GCP 项目 ID：huggle-invitation

### 一、首次部署

#### 前置条件

安装 [gcloud CLI](https://cloud.google.com/sdk/docs/install)

设置项目：

gcloud config set project huggle-invitation

启用必要 API（首次运行时会提示，选 Y 即可）：

Cloud Build API

Cloud Run API

Container Registry API

#### 部署命令

gcloud builds submit --config cloudbuild.yaml.

构建大约需要 3-5 分钟。

### 二、Cloud Run 环境变量配置

路径：Cloud Run → huggle-invitation → 编辑并部署新版本 → 变量和 Secret

以下变量需要在 Cloud Run 运行时设置（服务器端私密变量）：

| 变量名 | 说明 |
| --- | --- |
| FIREBASE\_ADMIN\_PROJECT\_ID | Firebase 项目 ID，如  huggle-invitation |
| FIREBASE\_ADMIN\_CLIENT\_EMAIL | Firebase 服务账号 email |
| FIREBASE\_ADMIN\_PRIVATE\_KEY | Firebase 私钥（见下方注意事项） |
| STRIPE\_SECRET\_KEY | Stripe Secret Key，  sk\_live\_... |
| STRIPE\_WEBHOOK\_SECRET | Stripe Webhook 签名密钥，  whsec\_... |
| ANTHROPIC\_API\_KEY | Anthropic Claude API Key |

#### ⚠️ FIREBASE\_ADMIN\_PRIVATE\_KEY 格式

在 Cloud Run 中粘贴时，必须是一行，

\\\\n

保留为字面字符（反斜杠+n），不是真正的换行：

\-----BEGIN PRIVATE KEY-----\\\\nMIIEvQ...\\\\n-----END PRIVATE KEY-----\\\\n

不要加外层引号，不要换行。代码会自动把

\\\\n

转成真正换行。

#### NEXT\_PUBLIC\_\* 变量说明

NEXT\_PUBLIC\_

开头的变量（Firebase 前端配置、Stripe publishable key、APP\_URL）已在构建时通过 Docker build-arg 烧录进 JS 包，不需要在 Cloud Run 中设置。

#### MOCK\_CLAUDE（仅本地调试用）

MOCK\_CLAUDE=true

可在

.env.local

中设置，开启后跳过真实 Claude AI 调用，直接返回假内容，用于本地调试支付流程。不要在 Cloud Run 中设置此变量，生产环境必须使用真实 AI 生成。

### 三、Firebase 配置

#### 1\. 授权域名

路径：Firebase 控制台 → Authentication → Settings → Authorized domains

需要添加以下域名：

huggle-invitation-239352118264.europe-west1.run.app

（Cloud Run 默认域名）

invitation.wordleap.co.uk

（自定义域名）

如果不添加，Google 登录弹框会一闪而过无法完成登录。

### 四、Stripe 配置

#### 1\. 支付方式

路径：Stripe Dashboard → Settings → Payment methods

Payment Element 使用

automatic\_payment\_methods: { enabled: true }

自动展示所有已启用的支付方式，包括：

信用卡 / 借记卡

Alipay

WeChat Pay

等

如需禁用某种支付方式，在 Stripe Dashboard 中关闭即可。

#### 2\. Webhook 配置

路径：Stripe Dashboard → Developers → Webhooks → Add endpoint

Endpoint URL：

https://invitation.wordleap.co.uk/api/stripe-webhook

监听事件：

payment\_intent.succeeded

创建后，复制 Signing secret（

whsec\_...

），更新到 Cloud Run 的

STRIPE\_WEBHOOK\_SECRET

变量

#### 3\. 优惠码（Promotion Code）配置

路径：Stripe Dashboard → Billing → Coupons

先创建 Coupon（设置折扣百分比，如 20%）

打开该 Coupon，页面下方点击 Create promotion code

设置一个客户可以输入的 code（如

HUGGLE20

）

客户在支付页面输入 Promotion Code，系统会自动验证并更新支付金额

> 注意：必须是 Promotion Code，不是 Coupon ID。Coupon 是内部的折扣规则，Promotion Code 才是客户可以输入的兑换码。

### 五、自定义域名配置

#### 方式一：通过 Cloud Run 域名映射

路径：Cloud Run → huggle-invitation → 自定义域名 → 添加映射

输入

invitation.wordleap.co.uk

Cloud Run 会给出一个 DNS 记录（CNAME 或 A 记录）

在域名注册商（如 Cloudflare、GoDaddy）处添加该 DNS 记录

等待 DNS 生效（通常 5-30 分钟）

#### 方式二：通过负载均衡器（可选）

适合需要更多控制（CDN、WAF 等）的场景，配置较复杂，一般用方式一即可。

### 六、更新部署

每次修改代码后，重新运行：

gcloud builds submit --config cloudbuild.yaml.

Cloud Run 会自动创建新版本并切换流量，无需停机。

#### ⚠️ 关于环境变量的重要说明

cloudbuild.yaml

使用

\--update-env-vars

而非

\--set-env-vars

，因此每次部署只会更新

NODE\_ENV

，不会覆盖 Cloud Run 中手动设置的其他环境变量（Firebase 私钥、Stripe Key 等）。如果发现部署后出现 401 / Firebase 初始化失败，很可能是之前某次部署用了

\--set-env-vars

把所有变量清空了。解决方法：回到 Cloud Run → 编辑并部署新版本 → 变量和 Secret，重新填入"二、Cloud Run 环境变量配置"中列出的所有变量。

### 七、常见问题排查

#### 页面无法加载 / This page couldn't load

检查 Cloud Run 日志（Cloud Run → 日志 → 筛选 ERROR）

常见原因：Cloud Run 环境变量缺失或格式错误

检查

FIREBASE\_ADMIN\_PRIVATE\_KEY

是否为单行格式

#### Google 登录弹框一闪而过

Firebase Authentication 的授权域名未添加，见"三、Firebase 配置"。

#### Stripe 支付 400 错误

Alipay/WeChat Pay 400：PaymentIntent 未设置

automatic\_payment\_methods

（已在代码中修复）通用 400：

confirmPayment

缺少

return\_url

（已在代码中修复）

#### 优惠码无效

确认在 Stripe Dashboard 中创建的是 Promotion Code（在 Coupon 页面下方创建），而不是直接用 Coupon ID。

#### 部署后出现 401 Unauthorized

原因：之前版本的

cloudbuild.yaml

使用

\--set-env-vars

会在每次部署时清除所有 Cloud Run 环境变量，导致 Firebase Admin 私钥等丢失，token 验证失败。解决方法：重新在 Cloud Run 中填入所有环境变量（见"二"）。现版本已改为

\--update-env-vars

，不会再出现此问题。

#### Cloud Build 权限错误 PERMISSION\_DENIED

需要在 GCP IAM 中给 Cloud Build 服务账号赋予以下角色：

Cloud Run Admin

Service Account User

Storage Admin