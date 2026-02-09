# 📋 Sui 黑客松项目 · 进度追踪

## 项目阶段

### Phase 0：调研（当前）⏳
- [ ] 深度调研 Vibe Hackathon 规则、赛道、SDK
- [ ] 深度调研 Mission: OpenClaw 规则、赛道
- [ ] 调研 Base 生态 AI Agent 项目（功能、技术栈、可参考点）
- [ ] 输出调研报告 RESEARCH.md
- [ ] 团队一起阅读讨论

### Phase 1：Ideation（创意 & 方案设计）
- [ ] 确定项目方向和核心功能
- [ ] 确定要打的赛道（可以一个项目同时打两个黑客松）
- [ ] 竞品分析（同赛道其他参赛者可能做什么）
- [ ] 输出产品设计文档 DESIGN.md
- [ ] 确定技术栈和架构

### Phase 2：Architecture（架构设计）
- [ ] 系统架构图
- [ ] Move 合约设计
- [ ] AI Agent 模块设计
- [ ] 前端/Bot 交互设计
- [ ] API 接口定义
- [ ] 输出架构文档 ARCHITECTURE.md

### Phase 3：Development（开发）
- [ ] Move 智能合约开发
- [ ] AI Agent 核心逻辑
- [ ] TG Bot / 前端开发
- [ ] 集成赞助商 SDK（Cetus/StableLayer）
- [ ] 各模块联调

### Phase 4：Testing（测试）
- [ ] 合约单元测试
- [ ] Agent 策略测试
- [ ] 端到端测试
- [ ] Sui Testnet 部署验证
- [ ] 性能压测

### Phase 5：Deploy & Polish（部署 & 打磨）
- [ ] Sui Mainnet/Testnet 部署
- [ ] 上线可访问的 Web App / dApp
- [ ] UI/UX 打磨
- [ ] 准备 Demo 演示

### Phase 6：Submission（提交）
- [ ] 完善 README（部署指南、运行说明）
- [ ] AI 使用声明（必须声明用了哪些 AI 工具+Prompt）
- [ ] 录制 Demo 视频
- [ ] 提交到 deepsurge 平台
- [ ] 提交 OpenClaw Hackathon（如有单独提交入口）

### Phase 7：Demo Day（展示）
- [ ] 准备 Pitch Deck
- [ ] 练习演示
- [ ] 参加 Demo Day

## ⏰ 时间线

| 日期 | 里程碑 |
|------|--------|
| 2/9 (今天) | Phase 0 调研 + Phase 1 确定方案 |
| 2/10 | Phase 2 架构 + Phase 3 开始开发 |
| 2/11 | Phase 3 核心开发 + Phase 4 测试 |
| 2/12 | Phase 5 部署 + Phase 6 提交 ⚠️ **Vibe 截止** |
| 2/14 | Vibe Hackathon 公布结果 |
| TBD | Mission: OpenClaw 截止（待确认） |

## 开发模式
采用 **Claude 4.6 Multi-Agent 并行开发**：
- Agent 1：Move 合约专家
- Agent 2：AI Agent/策略专家
- Agent 3：前端/Bot 开发
- 主 Agent：协调 + 集成 + 文档
