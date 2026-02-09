# 黑客松与 Base 生态 AI Agent 深度调研报告

> 调研时间：2026-02-09 | 状态：Sui Vibe Hackathon 进行中（截止 2/12）

---

## 一、Sui Vibe Hackathon 2026

### 基本信息
- **组织方**: HOH × Sui
- **赞助商**: Cetus, Bucket (StableLayer 背后)
- **时间**: 2026年1月26日 - 2月12日（**还剩3天**）
- **结果公布**: 2月14日
- **奖金**: **4台 Mac Mini M4**（非现金）
- **报名**: https://www.deepsurge.xyz/hackathons/97edf6fa-568f-4227-bb80-750d9b6dc17c/register （需注册 DeepSurge 账号）
- **GitHub**: https://github.com/hoh-zone/Vibe-Sui-Hackathon-2026

### 三个赛道

| 赛道 | 奖品 | 要求 |
|------|------|------|
| **Cetus 赛道** | Mac Mini M4 × 1 | 必须集成 Cetus Aggregator 或 SDK |
| **StableLayer 赛道** | Mac Mini M4 × 1 | 必须集成 StableLayer SDK |
| **Sui Tech Stack** | Mac Mini M4 × 2 | 不限方向，只要在 Sui 上构建 |

### 评审标准
1. **创新性与完整度** — 不只是概念，要跑起来
2. **Sui/Move 技术深度** — 用了多少 Object Model、Move 2024 特性
3. **用户体验与 Demo** — 必须有可访问的 Web App
4. **实际可行性与增长潜力**

### 硬性参赛要求（不满足直接无效）
1. **项目起始时间 ≥ 2026-01-27** — 不允许旧项目改包
2. **Move 2024 语法** — 必须用最新版本
3. **官方 Sui SDK 最新版** — 不允许废弃接口
4. **可运行产品 + 线上网站** — 纯代码/PPT 不行
5. **完全开源** — GitHub/GitLab 公开仓库，含 README
6. **AI 使用披露（强制）** — 用了什么 AI 工具、模型版本、具体 prompt 都要写清楚，不披露直接取消资格

### 赞助商 SDK 技术详情

#### Cetus Aggregator SDK
- npm: `@cetusprotocol/aggregator-sdk`
- 功能: Sui 链 DEX 聚合交易，集成 Cetus/DeepBook/Kriya/FlowX/Aftermath/Turbos 等
- 核心 API:
  ```ts
  const client = new AggregatorClient({})
  const routers = await client.findRouters({ from, target, amount, byAmountIn: true })
  await client.fastRouterSwap({ routers, txb, slippage: 0.01 })
  ```
- 合约地址 (mainnet): `0x40e457bc65a398d2db7026881358fcb7cfa2f1bb052bca41f46c55a1103f2d6f`
- 文档: https://cetus-1.gitbook.io/cetus-developer-docs/developer/cetus-plus-aggregator

#### Cetus SDK v2
- GitHub: https://github.com/CetusProtocol/cetus-sdk-v2
- TypeScript monorepo，包含多个子包用于流动性管理、交易等

#### StableLayer SDK
- npm: `stable-layer-sdk`
- 功能: 稳定币即服务（Stablecoin-as-a-Service），项目方可发行品牌稳定币（BrandUSD），底层 USDC 自动进入收益聚合器
- 核心 API: `buildMintTx` / `buildBurnTx` / `buildClaimTx` / `getTotalSupply`
- 收益来源 v1: Bucket Savings Pool + 自动复利
- 文档: https://docs.stablelayer.site/

### ⚡ 时间紧迫分析
距离截止只有 **3天**。如果要参赛：
- Cetus 赛道门槛最低：集成 Aggregator SDK 做一个 swap 相关产品即可
- StableLayer 赛道有差异化空间：品牌稳定币 + DeFi 玩法
- Sui Tech Stack 自由度最大但竞争也最大

---

## 二、Mission: OpenClaw Hackathon（Sui Network 官方推广）

### 基本信息
- **推广方**: @SuiNetwork（Sui 官方 X 账号，111万粉丝）
- **推文**: https://x.com/SuiNetwork/status/2019869538196799724
- **奖金**: **$20,000 USDC on Sui**
- **详情页**: https://www.moltbook.com/post/b36e9f84-2f89-4ece-a7a0-c9a7991421ae（JS 渲染，未能完整获取）

### 推文原文
> 🦞 Get ready for Mission: OpenClaw is a hackathon to build autonomous AI agents with real system access (browser + terminal).
>
> Two tracks:
> 🔐 Safety & Security
> 🤖 Local God Mode (your own Jarvis)
>
> $20K in USDC on Sui. Build with AI agents. Ship a demo.

### 两个赛道

| 赛道 | 方向 | 描述 |
|------|------|------|
| **Safety & Security** 🔐 | AI 安全 | 构建安全相关的 AI Agent 工具/框架 |
| **Local God Mode** 🤖 | 个人 AI 助手 | 类 Jarvis 的全功能自主 AI Agent |

### OpenClaw 框架是什么？
- **官网**: https://openclaw.ai
- **定位**: 个人 AI 助手框架，开源
- **核心能力**: 真正的系统访问权限（浏览器 + 终端），通过 WhatsApp/Telegram/Discord 等聊天 app 控制
- **功能**: 清理邮箱、发邮件、管理日历、航班值机、代码审查、部署、控制智能设备等
- **技术**: 基于 Claude/LLM，运行在用户自己的电脑/服务器上，支持 Mac Mini、Raspberry Pi 等
- **特色**: 
  - 持久化记忆（跨 session）
  - 心跳机制（proactive）
  - 技能系统（可扩展）
  - Cron 定时任务
  - 子 Agent 协调
- **社区反响**: 极其强烈，被多人评为"iPhone 时刻"、"未来已来"

### 关键洞察
- 这是 Sui Network 官方推广的黑客松，意味着 **Sui 生态在押注 AI Agent 方向**
- $20K USDC on Sui = 奖金通过 Sui 链发放，参赛者需要有 Sui 钱包
- OpenClaw 框架本身运行在 Base 链上（$MOLT 代币），但黑客松奖金在 Sui
- **报名方式待确认** — moltbook 帖子内容未能完整获取，建议手动打开查看

---

## 三、Base 生态 OpenClaw AI Agent 项目合集

### 信息来源
TokenPocket (@TokenPocket_TP) 推文完整梳理了 OpenClaw 生态：

### 生态全景图

#### 🟦 核心框架
| 项目 | 描述 | 官网 |
|------|------|------|
| **OpenClaw** | 自主 AI Agent 核心框架 | https://openclaw.ai |

#### 🟦 基础设施 (Infra)
| 项目 | 描述 | 备注 |
|------|------|------|
| **Bankr** (@bankrbot) | Agent 钱包 + DeFi 中心 | bankr.bot — 网站极简，主打 Agent 自主管理加密资产 |
| **Clanker** (@clanker_world) | Token 发射基础设施 | clanker.world — 历史总交易量 $74.8亿，持有 106,309 $CLANKER，1.37% 供应量已永久销毁 |
| **XMTP** (@xmtp_) | 去中心化消息协议 | Agent 间通信层 |
| **Neynar** (@neynarxyz) | 社交网络构建工具 | Farcaster 生态开发者工具 |
| **StarkBot** (@starkbotai) | x402 Agent 框架 | Agent 支付协议 |

#### 🟦 社交/论坛
| 项目 | 描述 | 官网 |
|------|------|------|
| **4claw** (by @dailofrog) | 匿名 Agent 看板 | — |
| **LobChan** (@lobchanai) | Agent 讨论论坛 | lobchan.ai — 匿名看板，Agent 用 API key 发帖，类似 4chan for AI |
| **Moltbook** (@moltbook) | AI 社交协作 | moltbook.com — "Agent 互联网的首页"，AI Agent 社交网络，agent 注册/发帖/投票，人类可围观 |
| **ClawdVine** (@clawdvine) | Vine 风格 Agent 视频 | — |
| **MoltX** (@moltxio) | 类 X 的 Agent 信息流 | — |
| **Clawk** (@clawk_ai) | Agent 社交平台 | — |
| **ClawCaster** (@clawcaster) | Farcaster Agent 桥 | — |

#### 🟦 代币经济
| 项目 | 描述 |
|------|------|
| **Clawnch Bot** (@Clawnch_Bot) | Clanker Agent 发射台 |
| **MoltLaunch** (@moltlaunch) | Flaunch Token 发射器 |

#### 🟦 新闻/发现
| 项目 | 描述 |
|------|------|
| **ClawdBot** (@clawdbotatg) | Agent 新闻聚合器 |
| **Conway Research** (@ConwayResearch) | 生态发现工具（网站 conwayresearch.com 目前为空） |

#### 🟦 市场
| 项目 | 描述 | 官网 |
|------|------|------|
| **ClawMart** (@clawmartxyz) | Agent API 市场 | clawmart.xyz — Agent 可发现并调用付费 API，用 Base 上的 USDC 微支付（x402 协议），新 Agent 有 $0.10 免费额度 |

#### 🟦 游戏
| 项目 | 描述 |
|------|------|
| **MoltChess** (@MoltChess) | Agent 象棋联赛 |

### 关键项目深度分析

#### 1. Clanker — 最成熟的项目
- **交易量**: $74.86 亿（历史总量），过去 24h $1962 万
- **机制**: Token 发射平台，自动创建流动性池，协议费用回购 $CLANKER
- **技术**: Base 链上 Uniswap V3 流动性
- **Dune Dashboard**: https://dune.com/clanker_protection_team/awesome-clanker
- **意义**: 证明了 AI Agent 经济的可行性

#### 2. ClawMart — Agent 商业化基础设施
- **模式**: Agent 版 API 市场
- **支付**: x402 协议（HTTP 402 Payment Required → USDC 微支付）
- **使用**: Agent 通过自然语言发现 API → 自动支付 → 获取结果
- **价值**: 让 Agent 能自主消费和赚钱

#### 3. Moltbook — Agent 社交图谱
- **模式**: Reddit/Hacker News for AI Agents
- **功能**: Agent 注册身份、发帖、评论、投票
- **开发者平台**: 开放中，让第三方 app 用 Moltbook 身份做认证
- **价值**: Agent 身份系统 + 社交图谱

#### 4. LobChan — Agent 信息交换
- **模式**: 4chan for AI Agents
- **功能**: 匿名看板，Agent 通过 API key 发帖
- **集成**: 通过 skills.md 让 OpenClaw agent 自动加入

---

## 四、可参考的项目创意与技术方案

### 🎯 针对 Sui Vibe Hackathon（紧急，3天内）

#### 创意 A: AI DeFi Agent for Sui（Cetus 赛道）
- **概念**: 基于 OpenClaw 框架的 Sui DeFi Agent，通过 Telegram 对话执行 swap
- **技术栈**: OpenClaw + Cetus Aggregator SDK + Sui SDK + Move 智能合约
- **亮点**: 自然语言交易（"帮我把 100 SUI 换成 CETUS，找最优路径"）
- **可行性**: Aggregator SDK 已有完整封装，3天足够做 MVP

#### 创意 B: StableYield Agent（StableLayer 赛道）
- **概念**: AI Agent 自动管理稳定币收益策略
- **技术栈**: StableLayer SDK + Sui SDK + 前端
- **亮点**: 自动 mint BrandUSD → 存入收益池 → 监控 APY → 自动复投
- **可行性**: SDK 接口简单（mint/burn/claim），差异化好

#### 创意 C: Sui AI Agent Hub（Tech Stack 赛道）
- **概念**: Sui 版 ClawMart — Agent API 市场，用 SUI 代币支付
- **亮点**: 将 Base 生态的 Agent 商业化模式移植到 Sui
- **风险**: 3天时间紧张

### 🎯 针对 Mission: OpenClaw Hackathon

#### 创意 D: Safety Track — Agent Sandbox Monitor
- **概念**: 监控 AI Agent 行为的安全工具，检测异常操作（如未授权的文件删除、网络请求）
- **技术**: OpenClaw 技能插件 + 行为日志分析 + 告警

#### 创意 E: Local God Mode — Sui DeFi Jarvis
- **概念**: 全功能 Sui 链 AI 管家，集成钱包管理、DeFi 操作、NFT 交易、链上数据分析
- **技术**: OpenClaw + Sui SDK + Cetus SDK + 链上数据索引
- **亮点**: 一个 Telegram bot 管理全部 Sui 链资产

---

## 五、我们的优势与切入点建议

### 优势分析
1. **我们已经在运行 OpenClaw** — 对框架有深度了解，这是 Mission OpenClaw Hackathon 的最大优势
2. **Sui + AI Agent 交叉点** — 两个黑客松都指向这个方向，市场验证了需求
3. **Base 生态经验可迁移** — Clanker、ClawMart 等模式可以搬到 Sui

### 建议策略

#### 短期（本周）
- **优先级 1**: 确认 Mission OpenClaw Hackathon 的报名截止时间和详细规则（手动打开 moltbook 帖子）
- **优先级 2**: 如果 Sui Vibe 还来得及（3天），选 Cetus 赛道做最小 MVP
- **优先级 3**: 准备 Mission OpenClaw 参赛，选 Local God Mode 赛道

#### 中期
- 深入 Sui 生态的 AI Agent 基础设施建设
- 参考 ClawMart 的 x402 微支付模式，在 Sui 上做 Agent 商业化

### ⚠️ 需要补充的信息
1. **Mission OpenClaw 详细规则** — moltbook 帖子需要在浏览器中打开查看
2. **Mission OpenClaw 截止时间** — 推文未提及
3. **$20K USDC 分配方式** — 两个赛道各多少？
4. **已有参赛项目** — 需要查看提交情况评估竞争

---

## 附录：关键链接汇总

| 资源 | 链接 |
|------|------|
| Sui Vibe GitHub | https://github.com/hoh-zone/Vibe-Sui-Hackathon-2026 |
| Sui Vibe 报名 | https://www.deepsurge.xyz/hackathons/97edf6fa-568f-4227-bb80-750d9b6dc17c/register |
| Mission OpenClaw 推文 | https://x.com/SuiNetwork/status/2019869538196799724 |
| Mission OpenClaw 详情 | https://www.moltbook.com/post/b36e9f84-2f89-4ece-a7a0-c9a7991421ae |
| OpenClaw 官网 | https://openclaw.ai |
| Cetus Aggregator SDK | https://github.com/CetusProtocol/aggregator |
| Cetus SDK v2 | https://github.com/CetusProtocol/cetus-sdk-v2 |
| StableLayer 文档 | https://docs.stablelayer.site/ |
| StableLayer SDK | https://github.com/StableLayer/stable-layer-sdk |
| Clanker Dune | https://dune.com/clanker_protection_team/awesome-clanker |
| ClawMart | https://clawmart.xyz |
| Moltbook | https://moltbook.com |
| LobChan | https://lobchan.ai |
| TokenPocket 生态推文 | https://x.com/TokenPocket_TP/status/2019705122985566232 |
