# 🏆 Sui 黑客松项目

## 我们要打的两个黑客松

### 黑客松 1：Sui Vibe Hackathon 2026（中文社区）
- **组织方**: HOH × Sui
- **赞助商**: Cetus, Bucket, StableLayer
- **时间**: 2026.1.26 - 2.12（⚠️ 2月12日截止！还剩3天！）
- **公布结果**: 2月14日
- **奖品**: 4 台 Mac Mini M4
- **报名**: https://www.deepsurge.xyz/hackathons/97edf6fa-568f-4227-bb80-750d9b6dc17c/register
- **GitHub**: https://github.com/hoh-zone/Vibe-Sui-Hackathon-2026

**赛道**:
1. **Cetus 赛道** (1台Mac Mini) — 集成 Cetus Aggregator/SDK
2. **StableLayer 赛道** (1台Mac Mini) — 集成 StableLayer SDK
3. **Sui Tech Stack 赛道** (2台Mac Mini) — 自由方向，在 Sui 上构建

**硬性要求**:
- 项目必须在 2026.1.27 之后创建（不能用旧项目）
- 必须用 Move 2024 语法
- 必须用最新 Sui SDK
- 必须有可运行的产品 + 上线网站
- 完全开源（GitHub）
- AI 使用必须声明

### 黑客松 2：Mission: OpenClaw (Sui Network 官方)
- **组织方**: Sui Network
- **奖金**: $20,000 USDC (on Sui)
- **推文**: https://x.com/SuiNetwork/status/2019869538196799724

**赛道**:
1. 🔐 **Safety & Security** — AI Agent 安全相关
2. 🤖 **Local God Mode** — 构建你自己的 Jarvis（本地 AI Agent）

**核心**: 构建具有真实系统访问权限（浏览器+终端）的自主 AI Agent

## 项目构思：ClawBot on Sui

### 核心理念
两个黑客松可以用**同一个项目**参加！

结合我们已有的 Polymarket 机器人经验，在 Sui 上构建一个：
**AI 驱动的链上交易 Agent** — 带 TG 界面 + 链上执行能力

### Base 生态参考项目
来自 TokenPocket 整理的 Base 上 OpenClaw Agent 生态：

| 类别 | 项目 | 功能 |
|------|------|------|
| 核心框架 | @openclaw | 自主 Agent 核心 |
| 基础设施 | @bankrbot | Agent 钱包 DeFi 中心 |
| 基础设施 | @clanker_world | Token 发射基础设施 |
| 社交 | @moltbook | AI 社交协作 |
| 社交 | @lobchanai | Agent 讨论论坛 |
| 代币经济 | @Clawnch_Bot | Agent 代币发射台 |
| 市场 | @clawmartxyz | Agent 交易市场 |
| 游戏 | @MoltChess | Agent 国际象棋联赛 |

### 可行方案方向

#### 方案 A：SuiPredict — AI 预测市场 Agent
- 将我们的 Polymarket 经验迁移到 Sui
- Move 智能合约实现链上预测市场
- AI Agent 自动分析 + 交易
- TG Bot 前端
- **适合赛道**: Vibe Hackathon Sui Tech Stack + OpenClaw Local God Mode

#### 方案 B：SuiDeFi Agent — 智能 DeFi 交易助手
- 集成 Cetus DEX Aggregator
- AI 驱动的自动交易策略
- 本地运行的 AI Agent（符合 Local God Mode）
- **适合赛道**: Vibe Hackathon Cetus 赛道 + OpenClaw Local God Mode

#### 方案 C：SuiGuard — AI 安全审计 Agent
- 自动审计 Move 智能合约
- 检测漏洞 + 生成报告
- **适合赛道**: OpenClaw Safety & Security

## 工程架构（参考 PubG 机器人）

```
hackathon-sui/
├── README.md                  # 项目说明
├── PROGRESS.md               # 进度追踪
├── docs/
│   ├── DESIGN.md             # 设计文档
│   ├── ARCHITECTURE.md       # 架构设计
│   └── SUBMISSION.md         # 提交材料
├── contracts/                 # Move 智能合约
│   ├── sources/
│   └── tests/
├── agent/                     # AI Agent 核心
│   ├── strategies/
│   ├── tools/
│   └── prompts/
├── bot/                       # TG Bot 前端
│   ├── handlers/
│   └── keyboards/
├── frontend/                  # Web 前端（如需要）
│   └── src/
└── scripts/                   # 部署/测试脚本
```

## ⏰ 时间紧迫！

Vibe Hackathon **2月12日截止**，只剩 **3 天**！
需要立刻确定方案并开始开发。

## 下一步
1. 确定走哪个方案（A/B/C）
2. 注册 Vibe Hackathon（如未注册）
3. 创建项目仓库
4. 分工：合约/Agent/Bot/前端
5. 用 Claude 4.6 multi-agent 模式并行开发
