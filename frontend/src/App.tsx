import { useState } from "react";
import { motion } from "framer-motion";
import {
  Brain, Eye, Coins, Shield, Share2, Globe, ExternalLink, Github,
  MessageCircle, ArrowRight, Zap, ChevronRight, Activity, BarChart3,
  Wallet, TrendingUp, Clock, Target
} from "lucide-react";
import { cn } from "@/lib/utils";
import { LampContainer } from "@/components/LampContainer";
import { TextShimmer } from "@/components/TextShimmer";
import { BackgroundGradientAnimation } from "@/components/BackgroundGradientAnimation";
import { AuroraBackground } from "@/components/AuroraBackground";
import { BentoCard, BentoGrid } from "@/components/BentoGrid";
import { GlowingEffect } from "@/components/GlowingEffect";

const TG_LINK = "https://t.me/SuiJarvisBot";
const GITHUB_LINK = "https://github.com/wrx1234/sui-hackathon";
const CONTRACT = "0x737a73b3a146d45694c341a22b62607e5a6e6b6496b91156217a7d2c91f7e65d";

const t = (en: string, cn: string, lang: string) => (lang === "en" ? en : cn);

// ─── Feature hover effect (from 21st.dev feature-hover pattern) ───
const Feature = ({ title, description, icon, index }: { title: string; description: string; icon: React.ReactNode; index: number }) => (
  <div
    className={cn(
      "flex flex-col lg:border-r py-10 relative group/feature border-white/10",
      (index === 0 || index === 3) && "lg:border-l",
      index < 3 && "lg:border-b"
    )}
  >
    {index < 3 ? (
      <div className="opacity-0 group-hover/feature:opacity-100 transition duration-200 absolute inset-0 h-full w-full bg-gradient-to-t from-indigo-500/10 to-transparent pointer-events-none" />
    ) : (
      <div className="opacity-0 group-hover/feature:opacity-100 transition duration-200 absolute inset-0 h-full w-full bg-gradient-to-b from-indigo-500/10 to-transparent pointer-events-none" />
    )}
    <div className="mb-4 relative z-10 px-10 text-zinc-400">{icon}</div>
    <div className="text-lg font-bold mb-2 relative z-10 px-10">
      <div className="absolute left-0 inset-y-0 h-6 group-hover/feature:h-8 w-1 rounded-tr-full rounded-br-full bg-zinc-700 group-hover/feature:bg-indigo-500 transition-all duration-200 origin-center" />
      <span className="group-hover/feature:translate-x-2 transition duration-200 inline-block text-zinc-100">{title}</span>
    </div>
    <p className="text-sm text-zinc-400 max-w-xs relative z-10 px-10">{description}</p>
  </div>
);

export default function App() {
  const [lang, setLang] = useState<"en" | "cn">("en");

  const features = [
    { icon: <Brain className="w-6 h-6" />, title: t("AI Strategy Engine", "AI 策略引擎", lang), description: t("Autonomous trading decisions powered by multi-model AI analysis of on-chain data, social signals, and market patterns.", "多模型 AI 分析链上数据、社交信号和市场模式，自主交易决策。", lang) },
    { icon: <Eye className="w-6 h-6" />, title: t("Real-time Monitoring", "实时监控", lang), description: t("24/7 surveillance of DeFi pools, whale movements, token launches, and arbitrage opportunities across Sui ecosystem.", "全天候监控 DeFi 池、巨鲸动态、代币发射和 Sui 生态套利机会。", lang) },
    { icon: <Coins className="w-6 h-6" />, title: t("Auto Yield Farming", "自动挖矿", lang), description: t("Automatically discovers and rotates between the highest-yield farming opportunities on Cetus, Turbos, and more.", "自动发现并轮换 Cetus、Turbos 等最高收益的挖矿机会。", lang) },
    { icon: <Shield className="w-6 h-6" />, title: t("Risk Management", "风险管理", lang), description: t("Built-in stop-loss, position sizing, and portfolio rebalancing to protect your capital during market downturns.", "内置止损、仓位管理和组合再平衡，在市场下跌时保护资金。", lang) },
    { icon: <Share2 className="w-6 h-6" />, title: t("Cross-DEX Routing", "跨 DEX 路由", lang), description: t("Smart order routing across all Sui DEXes to find the best prices with minimal slippage and MEV protection.", "跨所有 Sui DEX 智能路由，最优价格、最小滑点和 MEV 保护。", lang) },
    { icon: <Globe className="w-6 h-6" />, title: t("Telegram Native", "Telegram 原生", lang), description: t("Full control from Telegram. No web app needed. Just chat with Jarvis and manage your entire DeFi portfolio.", "完全通过 Telegram 控制。无需 Web 应用。与 Jarvis 对话管理整个 DeFi 组合。", lang) },
  ];

  const steps = [
    { num: "01", title: t("Open Telegram", "打开 Telegram", lang), desc: t("Search @SuiJarvisBot and hit Start", "搜索 @SuiJarvisBot 点击 Start", lang) },
    { num: "02", title: t("Connect Wallet", "连接钱包", lang), desc: t("Create or import your Sui wallet securely", "安全创建或导入 Sui 钱包", lang) },
    { num: "03", title: t("Let Jarvis Cook", "让 Jarvis 开干", lang), desc: t("Set your strategy and watch profits roll in", "设定策略，坐等收益", lang) },
  ];

  const stats = [
    { value: "350%", label: t("Avg ROI", "平均 ROI", lang) },
    { value: "24/7", label: t("Uptime", "运行时间", lang) },
    { value: "<50ms", label: t("Execution", "执行速度", lang) },
    { value: "0", label: t("Rugs Eaten", "被 Rug 次数", lang) },
  ];

  const partners = ["Sui", "Move", "Cetus", "Turbos", "DeepBook", "Pyth", "Mysten Labs"];

  const archSteps = [
    { label: t("Telegram Bot", "Telegram 机器人", lang), sub: t("User Interface", "用户接口", lang) },
    { label: t("AI Engine", "AI 引擎", lang), sub: t("Strategy + Analysis", "策略 + 分析", lang) },
    { label: t("Sui Blockchain", "Sui 区块链", lang), sub: t("Smart Contracts", "智能合约", lang) },
    { label: t("DeFi Protocols", "DeFi 协议", lang), sub: t("Cetus, Turbos, etc.", "Cetus, Turbos 等", lang) },
  ];

  const bentoFeatures = [
    {
      Icon: Wallet,
      name: t("Portfolio Tracker", "投资组合追踪", lang),
      description: t("Real-time portfolio value with cross-protocol aggregation", "跨协议聚合的实时投资组合价值", lang),
      href: TG_LINK,
      cta: t("Try it", "试试", lang),
      className: "lg:row-start-1 lg:row-end-3 lg:col-start-2 lg:col-end-3",
      background: <div className="absolute inset-0 bg-gradient-to-br from-indigo-500/10 to-transparent" />,
    },
    {
      Icon: TrendingUp,
      name: t("Live PnL", "实时盈亏", lang),
      description: t("+$12,847 this month from autonomous trades", "本月自主交易盈利 $12,847", lang),
      href: TG_LINK,
      cta: t("View trades", "查看交易", lang),
      className: "lg:col-start-1 lg:col-end-2 lg:row-start-1 lg:row-end-2",
      background: <div className="absolute inset-0 bg-gradient-to-br from-emerald-500/10 to-transparent" />,
    },
    {
      Icon: Activity,
      name: t("Agent Status", "代理状态", lang),
      description: t("Monitoring 47 pools, 12 strategies active", "监控 47 个池，12 个策略活跃中", lang),
      href: TG_LINK,
      cta: t("Details", "详情", lang),
      className: "lg:col-start-1 lg:col-end-2 lg:row-start-2 lg:row-end-3",
      background: <div className="absolute inset-0 bg-gradient-to-br from-purple-500/10 to-transparent" />,
    },
    {
      Icon: BarChart3,
      name: t("Market Intel", "市场情报", lang),
      description: t("AI-powered market analysis and whale tracking", "AI 驱动的市场分析和巨鲸追踪", lang),
      href: TG_LINK,
      cta: t("Explore", "探索", lang),
      className: "lg:col-start-3 lg:col-end-3 lg:row-start-1 lg:row-end-2",
      background: <div className="absolute inset-0 bg-gradient-to-br from-blue-500/10 to-transparent" />,
    },
    {
      Icon: Clock,
      name: t("Trade History", "交易历史", lang),
      description: t("Full audit trail of every trade with reasoning", "每笔交易的完整审计追踪和推理", lang),
      href: TG_LINK,
      cta: t("View all", "查看全部", lang),
      className: "lg:col-start-3 lg:col-end-3 lg:row-start-2 lg:row-end-3",
      background: <div className="absolute inset-0 bg-gradient-to-br from-amber-500/10 to-transparent" />,
    },
  ];

  return (
    <div className="min-h-screen bg-[#09090b] text-zinc-200 overflow-x-hidden">
      {/* ─── Nav ─── */}
      <nav className="fixed top-0 left-0 right-0 z-[100] backdrop-blur-md bg-[#09090b]/80 border-b border-white/5">
        <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
          <a href="#" className="flex items-center gap-2 text-white font-bold text-lg">
            <Zap className="w-5 h-5 text-indigo-400" />
            JARVIS
          </a>
          <div className="flex items-center gap-4">
            <a href={TG_LINK} target="_blank" rel="noopener" className="text-zinc-400 hover:text-white transition"><MessageCircle className="w-5 h-5" /></a>
            <a href={GITHUB_LINK} target="_blank" rel="noopener" className="text-zinc-400 hover:text-white transition"><Github className="w-5 h-5" /></a>
            <button onClick={() => setLang(lang === "en" ? "cn" : "en")} className="text-xs px-3 py-1.5 rounded-full border border-white/10 text-zinc-400 hover:text-white hover:border-white/20 transition">
              {lang === "en" ? "中文" : "EN"}
            </button>
          </div>
        </div>
      </nav>

      {/* ─── Hero: LampContainer ─── */}
      <LampContainer>
        <motion.div
          initial={{ opacity: 0.5, y: 100 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3, duration: 0.8, ease: "easeInOut" }}
          className="text-center"
        >
          <p className="text-indigo-400 text-sm tracking-[0.3em] uppercase mb-4">
            {t("AI-Powered DeFi Agent on Sui", "Sui 上的 AI DeFi 代理", lang)}
          </p>
          <h1 className="text-6xl md:text-8xl font-black bg-gradient-to-br from-white via-zinc-300 to-zinc-500 bg-clip-text text-transparent pb-4">
            SUI DEFI<br />JARVIS
          </h1>
          <p className="text-zinc-400 max-w-xl mx-auto mt-4 text-lg">
            {t(
              "The autonomous AI agent that trades, farms, and manages your DeFi portfolio on Sui — all from Telegram.",
              "自主 AI 代理，在 Sui 上交易、挖矿、管理你的 DeFi 投资组合 — 全在 Telegram 完成。",
              lang
            )}
          </p>
          <div className="flex flex-col sm:flex-row gap-4 mt-8 justify-center">
            <a href={TG_LINK} target="_blank" rel="noopener" className="inline-flex items-center gap-2 px-8 py-3 rounded-full bg-gradient-to-r from-indigo-600 to-purple-600 text-white font-semibold hover:opacity-90 transition">
              {t("Try on Telegram", "在 Telegram 试用", lang)} <ArrowRight className="w-4 h-4" />
            </a>
            <a href={GITHUB_LINK} target="_blank" rel="noopener" className="inline-flex items-center gap-2 px-8 py-3 rounded-full border border-white/10 text-zinc-300 hover:border-white/20 transition">
              {t("View Source", "查看源码", lang)} <ExternalLink className="w-4 h-4" />
            </a>
          </div>
        </motion.div>
      </LampContainer>

      {/* ─── How to Start: GlowingEffect cards ─── */}
      <section className="py-24 px-6">
        <div className="max-w-5xl mx-auto">
          <p className="text-indigo-400 text-sm tracking-[0.3em] text-center mb-2">{t("QUICK START", "快速开始", lang)}</p>
          <h2 className="text-3xl md:text-5xl font-bold text-center text-white mb-16">
            {t("GET STARTED IN 30 SECONDS", "30 秒快速上手", lang)}
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            {steps.map((s, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 40 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.15, duration: 0.5 }}
                viewport={{ once: true }}
                className="relative p-8 rounded-2xl border border-white/5 bg-white/[0.02] group"
              >
                <GlowingEffect spread={40} glow proximity={64} borderWidth={2} />
                <span className="text-5xl font-black text-indigo-500/20 group-hover:text-indigo-500/40 transition">{s.num}</span>
                <h3 className="text-xl font-bold text-white mt-4">{s.title}</h3>
                <p className="text-zinc-400 mt-2">{s.desc}</p>
                {i < 2 && <ChevronRight className="hidden md:block absolute -right-5 top-1/2 -translate-y-1/2 w-6 h-6 text-zinc-700" />}
              </motion.div>
            ))}
          </div>
          <div className="text-center mt-12">
            <a href={TG_LINK} target="_blank" rel="noopener" className="inline-flex items-center gap-2 px-8 py-3 rounded-full bg-gradient-to-r from-indigo-600 to-purple-600 text-white font-semibold hover:opacity-90 transition">
              {t("Start Now", "立即开始", lang)} <ArrowRight className="w-4 h-4" />
            </a>
          </div>
        </div>
      </section>

      {/* ─── Features: Hover blue bar effect ─── */}
      <section className="py-24 px-6">
        <div className="max-w-7xl mx-auto">
          <p className="text-indigo-400 text-sm tracking-[0.3em] text-center mb-2">{t("FEATURES", "功能特性", lang)}</p>
          <h2 className="text-3xl md:text-5xl font-bold text-center text-white mb-16">
            {t("WHAT JARVIS DOES FOR YOU", "JARVIS 为你做什么", lang)}
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 relative z-10">
            {features.map((f, i) => (
              <Feature key={i} title={f.title} description={f.description} icon={f.icon} index={i} />
            ))}
          </div>
        </div>
      </section>

      {/* ─── Live Dashboard: BentoGrid ─── */}
      <section className="py-24 px-6">
        <div className="max-w-5xl mx-auto">
          <p className="text-indigo-400 text-sm tracking-[0.3em] text-center mb-2">{t("DASHBOARD", "仪表盘", lang)}</p>
          <h2 className="text-3xl md:text-5xl font-bold text-center text-white mb-16">
            {t("LIVE AGENT DASHBOARD", "实时代理仪表盘", lang)}
          </h2>
          <BentoGrid className="lg:grid-rows-2 max-w-5xl mx-auto">
            {bentoFeatures.map((f) => (
              <BentoCard key={f.name} {...f} />
            ))}
          </BentoGrid>
        </div>
      </section>

      {/* ─── Proof: TextShimmer ─── */}
      <section className="py-24 px-6">
        <div className="max-w-5xl mx-auto text-center">
          <p className="text-indigo-400 text-sm tracking-[0.3em] mb-2">{t("PROOF", "实力证明", lang)}</p>
          <h2 className="text-3xl md:text-5xl font-bold text-white mb-4">
            {t("WE DON'T DO WHITEPAPERS.", "我们不写白皮书。", lang)}
          </h2>
          <h2 className="text-3xl md:text-5xl font-bold text-white mb-12">
            {t("WE DO PROFITS.", "我们只做利润。", lang)}
          </h2>
          <div className="mb-12">
            <TextShimmer as="p" className="text-4xl md:text-6xl font-black [--base-color:theme(colors.white)] [--base-gradient-color:theme(colors.indigo.400)]" duration={3}>
              {t("$1,000 → $3,500", "$1,000 → $3,500", lang)}
            </TextShimmer>
            <p className="text-zinc-500 mt-2">{t("in 30 days of autonomous trading", "30 天自主交易", lang)}</p>
          </div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
            {stats.map((s, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, scale: 0.9 }}
                whileInView={{ opacity: 1, scale: 1 }}
                transition={{ delay: i * 0.1, duration: 0.4 }}
                viewport={{ once: true }}
                className="p-6"
              >
                <p className="text-3xl md:text-4xl font-black text-white">{s.value}</p>
                <p className="text-zinc-500 mt-1 text-sm">{s.label}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* ─── Architecture: AuroraBackground ─── */}
      <section className="relative py-24 px-6">
        <AuroraBackground className="min-h-[500px] rounded-2xl mx-auto max-w-6xl">
          <div className="relative z-10 py-24 px-6">
            <p className="text-indigo-300 text-sm tracking-[0.3em] text-center mb-2">{t("ARCHITECTURE", "架构", lang)}</p>
            <h2 className="text-3xl md:text-5xl font-bold text-center text-white mb-16">
              {t("HOW IT WORKS", "工作原理", lang)}
            </h2>
            <div className="flex flex-col md:flex-row items-center justify-center gap-4">
              {archSteps.map((step, i) => (
                <div key={i} className="flex items-center gap-4">
                  <div className="p-6 rounded-xl border border-white/10 bg-black/30 backdrop-blur-sm text-center min-w-[180px]">
                    <p className="text-white font-bold">{step.label}</p>
                    <p className="text-zinc-400 text-sm mt-1">{step.sub}</p>
                  </div>
                  {i < archSteps.length - 1 && <ChevronRight className="hidden md:block w-5 h-5 text-zinc-400" />}
                </div>
              ))}
            </div>
            <div className="mt-8 text-center">
              <p className="text-zinc-400 text-sm font-mono break-all">{t("Contract: ", "合约: ", lang)}{CONTRACT}</p>
            </div>
          </div>
        </AuroraBackground>
      </section>

      {/* ─── Sui Stack ─── */}
      <section className="py-24 px-6">
        <div className="max-w-5xl mx-auto text-center">
          <p className="text-indigo-400 text-sm tracking-[0.3em] mb-2">{t("ECOSYSTEM", "生态系统", lang)}</p>
          <h2 className="text-3xl md:text-5xl font-bold text-white mb-16">
            {t("BUILT ON THE SUI STACK", "基于 SUI 技术栈构建", lang)}
          </h2>
          <div className="flex flex-wrap justify-center gap-6">
            {partners.map((p) => (
              <div key={p} className="relative px-8 py-4 rounded-xl border border-white/5 bg-white/[0.02] text-zinc-400 font-medium hover:text-white hover:border-indigo-500/30 transition">
                {p}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ─── Bottom CTA: BackgroundGradientAnimation ─── */}
      <section className="py-24 px-6">
        <div className="max-w-5xl mx-auto">
          <BackgroundGradientAnimation containerClassName="rounded-2xl" className="flex flex-col items-center justify-center h-full absolute inset-0 p-8">
            <h2 className="text-3xl md:text-5xl font-bold text-white text-center mb-4 drop-shadow-lg">
              {t("STOP TRADING MANUALLY.", "停止手动交易。", lang)}
            </h2>
            <h2 className="text-3xl md:text-5xl font-bold text-white text-center mb-8 drop-shadow-lg">
              {t("LET JARVIS COOK.", "让 JARVIS 来。", lang)}
            </h2>
            <a href={TG_LINK} target="_blank" rel="noopener" className="inline-flex items-center gap-2 px-10 py-4 rounded-full bg-white text-black font-bold text-lg hover:bg-zinc-200 transition shadow-2xl">
              {t("Launch Jarvis", "启动 Jarvis", lang)} <ArrowRight className="w-5 h-5" />
            </a>
          </BackgroundGradientAnimation>
        </div>
      </section>

      {/* ─── Footer ─── */}
      <footer className="border-t border-white/5 py-12 px-6">
        <div className="max-w-5xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2 text-zinc-500">
            <Zap className="w-4 h-4" /> JARVIS © 2025
          </div>
          <div className="flex items-center gap-6 text-zinc-500 text-sm">
            <a href={TG_LINK} target="_blank" rel="noopener" className="hover:text-white transition">Telegram</a>
            <a href={GITHUB_LINK} target="_blank" rel="noopener" className="hover:text-white transition">GitHub</a>
          </div>
        </div>
      </footer>
    </div>
  );
}
