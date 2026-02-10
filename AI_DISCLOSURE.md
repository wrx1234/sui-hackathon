# 🤖 AI Usage Disclosure

> This document is required by Sui Vibe Hackathon 2026 rules.
> All AI tool usage during development is disclosed below.

## AI Tools Used

| Tool | Models | Usage Count |
|------|--------|-------------|
| OpenClaw | claude-opus-4.6 | 32 |

## Summary

- **Total AI interactions**: 32
- **Development period**: 2026-02-09 to 2026-02-11
- **Primary tool**: OpenClaw (autonomous AI agent framework)
- **Primary model**: Claude Opus 4.6 (Anthropic)

## Usage by Category

### Code (9 interactions)

**#1** [2026-02-09T18:12]
- Prompt: `创建 AI prompt logger 工具，满足黑客松 AI 使用声明要求`
- Response summary: tools/ai-logger.py — 记录所有 AI 交互，自动生成 AI_DISCLOSURE.md

**#2** [2026-02-09T18:34]
- Prompt: `Commit: init: project scaffolding + AI prompt logger + disclosure | Files: tools/auto-log-hook.sh,`
- Response summary: Auto-logged from git commit

**#3** [2026-02-09T19:26]
- Prompt: `Commit: docs: frontend landing page design spec | Files: .env.example,.gitignore,agent/logger.ts,agent/swap.ts,agent/wallet.ts,bot/main.ts,package-lock.json,package.json,tsconfig.json,`
- Response summary: Auto-logged from git commit

**#4** [2026-02-09T19:41]
- Prompt: `Commit: docs: tech reference with code snippets for all integrations | Files: agent/risk.ts,agent/strategy.ts,`
- Response summary: Auto-logged from git commit

**#5** [2026-02-09T19:45]
- Prompt: `Commit: feat: strategy engine (trend/mean_reversion) + risk management module | Files: agent/main.ts,contracts/Move.toml,contracts/sources/vault.move,scripts/setup.sh,`
- Response summary: Auto-logged from git commit

**#6** [2026-02-09T21:56]
- Prompt: `Commit: fix: Cetus SDK field mapping (amountOut/paths) + mainnet quotes working

- SDK returns amountOut (hex BN) not outputAmount, paths not routes
- 1 SUI = 0.936660 USDC (via CETUS)
- 1 SUI = 60.26`
- Response summary: Auto-logged from git commit

**#7** [2026-02-10T00:27]
- Prompt: `Commit: docs: updated PROGRESS.md with full test results and verified integrations | Files: contracts/Move.lock,contracts/Move.toml,contracts/Published.toml,`
- Response summary: Auto-logged from git commit

**#8** [2026-02-10T23:46]
- Prompt: `Commit: feat: vault.move deployed to Sui testnet! Package: 0x737a73b3...7e65d | Files: bot/data/jarvis.log,bot/data/operations.json,bot/data/wallets.json,bot/jarvis_bot.py,bot/main.ts,docs-site/assets`
- Response summary: Auto-logged from git commit

**#9** [2026-02-11T01:46]
- Prompt: `Commit: feat: frontend v4 — real Aceternity UI components + bot lang toggle button | Files: bot/data/jarvis.log,bot/data/operations.json,frontend/src/App.tsx,frontend/src/components/AuroraBackground.t`
- Response summary: Auto-logged from git commit

### Design (4 interactions)

**#1** [2026-02-09T18:12]
- Prompt: `整理项目 README、进度追踪 PROGRESS.md、方案建议（SuiPredict/SuiDeFi/SuiGuard）`
- Response summary: 创建项目框架文档

**#2** [2026-02-09T18:58]
- Prompt: `Commit: docs: add competitor analysis from Moltbook comments | Files: ARCHITECTURE.md,`
- Response summary: Auto-logged from git commit

**#3** [2026-02-09T19:01]
- Prompt: `Commit: docs: system architecture for Sui DeFi Jarvis | Files: ARCHITECTURE.md,README.md,`
- Response summary: Auto-logged from git commit

**#4** [2026-02-09T19:29]
- Prompt: `Commit: feat: core modules - wallet + swap + logger + TG bot

- wallet.ts: Ed25519 keypair, balance query, transfer (tested ✅)
- swap.ts: Cetus Aggregator integration, quote + execute
- logger.ts: Wal`
- Response summary: Auto-logged from git commit

### Docs (11 interactions)

**#1** [2026-02-09T18:39]
- Prompt: `Commit: feat: auto AI prompt logging via git pre-commit hook | Files: docs/MOLTBOOK-TIPS.md,docs/SUI-AI-TOOLS.md,`
- Response summary: Auto-logged from git commit

**#2** [2026-02-09T18:44]
- Prompt: `Commit: docs: Sui AI tools research + Moltbook community tips | Files: RESEARCH.md,`
- Response summary: Auto-logged from git commit

**#3** [2026-02-09T18:46]
- Prompt: `Commit: docs: update RESEARCH with full Mission OpenClaw details + refined strategy | Files: RESEARCH.md,`
- Response summary: Auto-logged from git commit

**#4** [2026-02-09T18:47]
- Prompt: `Commit: docs: complete Mission OpenClaw rules - judging, voting, eligibility, deadline | Files: RESEARCH.md,`
- Response summary: Auto-logged from git commit

**#5** [2026-02-09T19:03]
- Prompt: `Commit: feat: complete architecture with sponsor integrations + polished README | Files: docs/PRD.md,`
- Response summary: Auto-logged from git commit

**#6** [2026-02-09T19:13]
- Prompt: `Commit: docs: PRD with user stories, features, and current progress | Files: docs/FEASIBILITY.md,`
- Response summary: Auto-logged from git commit

**#7** [2026-02-09T19:14]
- Prompt: `Commit: docs: technical feasibility analysis + real Polymarket proof + revised dev plan | Files: docs/FRONTEND-SPEC.md,`
- Response summary: Auto-logged from git commit

**#8** [2026-02-09T19:38]
- Prompt: `Commit: feat: core modules - wallet + swap + logger + social sniper + TG bot | Files: docs/TECH-REFERENCE.md,`
- Response summary: Auto-logged from git commit

**#9** [2026-02-09T20:02]
- Prompt: `Commit: feat: Move vault contract + agent main entry + setup script | Files: .env.example,agent/logger.ts,agent/wallet.ts,bot/main.ts,docs/MOLTBOOK-TESTING.md,docs/SECURITY-AUDIT.md,tests/integration.`
- Response summary: Auto-logged from git commit

**#10** [2026-02-09T22:01]
- Prompt: `Commit: fix: Walrus upload working! nodes.guru publisher + verified read

Blobs uploaded and readable. Cetus mainnet quotes also working. | Files: PROGRESS.md,`
- Response summary: Auto-logged from git commit

**#11** [2026-02-10T23:47]
- Prompt: `Commit: feat: add frontend landing page + bot i18n + viral social | Files: bot/data/jarvis.log,docs-md/FEASIBILITY.md,docs-md/FRONTEND-SPEC.md,docs-md/MOLTBOOK-TESTING.md,docs-md/MOLTBOOK-TIPS.md,docs`
- Response summary: Auto-logged from git commit

### Research (6 interactions)

**#1** [2026-02-09T18:12]
- Prompt: `深度调研 Sui Vibe Hackathon 规则、Mission OpenClaw 赛道、Base 生态 AI Agent 项目（Clanker/ClawMart/Moltbook/LobChan 等）`
- Response summary: 输出完整调研报告 RESEARCH.md，覆盖三个信息源的详细分析

**#2** [2026-02-10T23:59]
- Prompt: `Commit: chore: setup GitHub Pages in /docs | Files: bot/data/jarvis.log,docs/assets/index-Coz85c12.css,docs/assets/index-DDWZGibn.js,docs/index.html,frontend/index.html,frontend/package.json,frontend/`
- Response summary: Auto-logged from git commit

**#3** [2026-02-11T00:49]
- Prompt: `Commit: fix: update docs with latest build | Files: bot/data/jarvis.log,bot/data/operations.json,docs/assets/index-BSMPJ7FW.js,docs/assets/index-plkEc-8p.css,docs/index.html,frontend/components.json,f`
- Response summary: Auto-logged from git commit

**#4** [2026-02-11T01:15]
- Prompt: `Commit: feat: 21st.dev/ibelick style rebuild with CardSpotlight, BadgeShine, ButtonGradient | Files: bot/data/jarvis.log,bot/data/lang_prefs.json,bot/jarvis_bot.py,docs/assets/index-Cksbj3K1.css,docs/`
- Response summary: Auto-logged from git commit

**#5** [2026-02-11T04:17]
- Prompt: `Commit: feat: frontend v5 — all 7 Aceternity/21st.dev components integrated | Files: bot/data/jarvis.log,bot/data/lang_prefs.json,bot/data/operations.json,bot/data/user_langs.json,bot/i18n.py,bot/jarv`
- Response summary: Auto-logged from git commit

**#6** [2026-02-11T05:06]
- Prompt: `Commit: feat: add Social Sniper section + i18n locale system | Files: bot/data/jarvis.log,docs/assets/boolean-DnW06Vcs.js,docs/assets/gaussian-splat-compression-CH16aANn.js,docs/assets/howler-Dj3Ec2Vz`
- Response summary: Auto-logged from git commit

### Test (2 interactions)

**#1** [2026-02-09T21:25]
- Prompt: `Commit: test: 33 unit tests + integration test + security audit + P0 fixes

- wallet: 5/5, strategy: 4/4, risk: 10/10, logger: 4/4, social: 4/4
- integration: 6/6 (full user flow simulation)
- securit`
- Response summary: Auto-logged from git commit

**#2** [2026-02-09T21:51]
- Prompt: `Commit: test: E2E integration test 24/24 — full trading cycle verified

7 phases: init → market analysis → risk check → trade execution → logging → social broadcast → multi-round | Files: agent/swap.t`
- Response summary: Auto-logged from git commit

## Disclosure Statement

This project was developed with significant assistance from AI tools. Specifically:

1. **OpenClaw** (https://openclaw.ai) — Autonomous AI agent framework used for project management, research, code generation, and documentation
2. **Claude Opus 4.6** (Anthropic) — Primary LLM model for all AI interactions
3. **Claude Code** — CLI tool within OpenClaw for code generation and editing

All prompts and AI outputs are logged in `ai-logs/prompts.jsonl`.
Sensitive information (API keys, passwords) has been redacted.

We believe in full transparency about AI usage in software development.
