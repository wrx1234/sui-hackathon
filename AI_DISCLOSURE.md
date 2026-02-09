# 🤖 AI Usage Disclosure

> This document is required by Sui Vibe Hackathon 2026 rules.
> All AI tool usage during development is disclosed below.

## AI Tools Used

| Tool | Models | Usage Count |
|------|--------|-------------|
| OpenClaw | claude-opus-4.6 | 11 |

## Summary

- **Total AI interactions**: 11
- **Development period**: 2026-02-09 to 2026-02-09
- **Primary tool**: OpenClaw (autonomous AI agent framework)
- **Primary model**: Claude Opus 4.6 (Anthropic)

## Usage by Category

### Code (2 interactions)

**#1** [2026-02-09T18:12]
- Prompt: `创建 AI prompt logger 工具，满足黑客松 AI 使用声明要求`
- Response summary: tools/ai-logger.py — 记录所有 AI 交互，自动生成 AI_DISCLOSURE.md

**#2** [2026-02-09T18:34]
- Prompt: `Commit: init: project scaffolding + AI prompt logger + disclosure | Files: tools/auto-log-hook.sh,`
- Response summary: Auto-logged from git commit

### Design (3 interactions)

**#1** [2026-02-09T18:12]
- Prompt: `整理项目 README、进度追踪 PROGRESS.md、方案建议（SuiPredict/SuiDeFi/SuiGuard）`
- Response summary: 创建项目框架文档

**#2** [2026-02-09T18:58]
- Prompt: `Commit: docs: add competitor analysis from Moltbook comments | Files: ARCHITECTURE.md,`
- Response summary: Auto-logged from git commit

**#3** [2026-02-09T19:01]
- Prompt: `Commit: docs: system architecture for Sui DeFi Jarvis | Files: ARCHITECTURE.md,README.md,`
- Response summary: Auto-logged from git commit

### Docs (5 interactions)

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

### Research (1 interactions)

**#1** [2026-02-09T18:12]
- Prompt: `深度调研 Sui Vibe Hackathon 规则、Mission OpenClaw 赛道、Base 生态 AI Agent 项目（Clanker/ClawMart/Moltbook/LobChan 等）`
- Response summary: 输出完整调研报告 RESEARCH.md，覆盖三个信息源的详细分析

## Disclosure Statement

This project was developed with significant assistance from AI tools. Specifically:

1. **OpenClaw** (https://openclaw.ai) — Autonomous AI agent framework used for project management, research, code generation, and documentation
2. **Claude Opus 4.6** (Anthropic) — Primary LLM model for all AI interactions
3. **Claude Code** — CLI tool within OpenClaw for code generation and editing

All prompts and AI outputs are logged in `ai-logs/prompts.jsonl`.
Sensitive information (API keys, passwords) has been redacted.

We believe in full transparency about AI usage in software development.
