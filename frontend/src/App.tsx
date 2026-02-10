import { useState } from 'react'
import { motion } from 'framer-motion'
import {
  Brain, Eye, Coins, Shield, Share2, Globe,
  ArrowRight, ArrowDown, ExternalLink, ChevronDown,
} from 'lucide-react'

// ─── i18n ────────────────────────────────────────────────
type Lang = 'en' | 'cn'

const t = (en: string, cn: string, lang: Lang) => (lang === 'en' ? en : cn)

// ─── Animation variants ──────────────────────────────────
const fadeUp = {
  hidden: { opacity: 0, y: 24 },
  show: { opacity: 1, y: 0, transition: { duration: 0.5 } },
}
const stagger = {
  hidden: {},
  show: { transition: { staggerChildren: 0.1 } },
}

// ─── Reusable components ─────────────────────────────────
function GradientText({ children, className = '' }: { children: React.ReactNode; className?: string }) {
  return (
    <span className={`bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-500 bg-clip-text text-transparent ${className}`}>
      {children}
    </span>
  )
}

function GlassCard({ children, className = '', hover = false }: { children: React.ReactNode; className?: string; hover?: boolean }) {
  return (
    <div className={`rounded-2xl border border-white/10 bg-white/[0.03] backdrop-blur-md ${hover ? 'transition-all duration-300 hover:border-white/20 hover:-translate-y-1' : ''} ${className}`}>
      {children}
    </div>
  )
}

function SectionTitle({ children, className = '' }: { children: React.ReactNode; className?: string }) {
  return (
    <motion.h2
      variants={fadeUp}
      initial="hidden"
      whileInView="show"
      viewport={{ once: true }}
      className={`text-3xl md:text-5xl font-black tracking-tight leading-tight text-center mb-4 ${className}`}
    >
      {children}
    </motion.h2>
  )
}

// ─── Data ────────────────────────────────────────────────
const TG = 'https://t.me/SuiJarvisBot'
const GH = 'https://github.com/wrx1234/sui-hackathon'
const CONTRACT = '0x737a73b3a146d45694c341a22b62607e5a6e6b6496b91156217a7d2c91f7e65d'

const trades = [
  { time: '14:32', pair: 'SUI/USDC', side: 'BUY', amount: '$2,400', pnl: '+$87' },
  { time: '13:15', pair: 'CETUS/SUI', side: 'SELL', amount: '$1,200', pnl: '+$42' },
  { time: '12:01', pair: 'SUI/USDC', side: 'BUY', amount: '$3,100', pnl: '+$156' },
  { time: '10:47', pair: 'DEEP/SUI', side: 'BUY', amount: '$800', pnl: '-$23' },
  { time: '09:30', pair: 'SUI/USDC', side: 'SELL', amount: '$5,000', pnl: '+$312' },
]

const archRow1 = ['You', 'TG Bot', 'AI Agent', 'Sui Chain']
const archRow2 = ['OpenClaw', 'Strategy', 'Cetus', 'Walrus']
const partners = ['Sui', 'Cetus', 'Walrus', 'Seal', 'StableLayer', 'OpenClaw', 'Moltbook']

// ─── App ─────────────────────────────────────────────────
export default function App() {
  const [lang, setLang] = useState<Lang>('en')

  return (
    <div className="min-h-screen bg-[#09090b] text-zinc-50">
      {/* ── Nav ── */}
      <nav className="fixed top-0 inset-x-0 z-50 border-b border-white/5 bg-[#09090b]/80 backdrop-blur-lg">
        <div className="mx-auto max-w-6xl flex items-center justify-between px-6 h-14">
          <a href="#" className="flex items-center gap-2 text-lg font-bold tracking-tight">
            <span>⚡</span>
            <GradientText>JARVIS</GradientText>
          </a>
          <div className="flex items-center gap-4 text-sm text-zinc-400">
            <a href={TG} target="_blank" rel="noreferrer" className="hover:text-white transition-colors">Bot</a>
            <a href={GH} target="_blank" rel="noreferrer" className="hover:text-white transition-colors">GitHub</a>
            <button
              onClick={() => setLang(lang === 'en' ? 'cn' : 'en')}
              className="ml-1 px-2 py-0.5 rounded border border-white/10 hover:border-white/25 transition-colors text-xs"
            >
              {lang === 'en' ? '🇨🇳 中文' : '🇬🇧 EN'}
            </button>
          </div>
        </div>
      </nav>

      {/* ── Hero ── */}
      <section className="min-h-screen flex flex-col items-center justify-center px-6 pt-14 relative">
        <motion.div
          variants={stagger}
          initial="hidden"
          animate="show"
          className="flex flex-col items-center text-center gap-6 max-w-4xl"
        >
          <motion.div variants={fadeUp} className="inline-flex items-center gap-2 rounded-full border border-white/10 px-4 py-1.5 text-xs text-zinc-400 tracking-wide">
            {t('THE INFINITE MONEY GLITCH — POWERED BY OPENCLAW', '无限印钞术 — POWERED BY OPENCLAW', lang)}
          </motion.div>

          <motion.h1 variants={fadeUp} className="text-6xl md:text-8xl font-black tracking-tighter leading-none">
            <GradientText>SUI DEFI JARVIS</GradientText>
          </motion.h1>

          <motion.p variants={fadeUp} className="text-xl md:text-2xl text-zinc-400 font-medium tracking-tight">
            {t('YOUR AI ARMY ON SUI.', '你在 SUI 上的 AI 军团。', lang)}
          </motion.p>

          <motion.p variants={fadeUp} className="text-zinc-500 max-w-2xl leading-relaxed">
            {t(
              'Jarvis is a fully autonomous DeFi agent on Sui. It trades, tracks whales, mints stablecoins, and grows your portfolio — all from a Telegram bot. No keys. No dashboards. Just results.',
              'Jarvis 是 Sui 上的全自主 DeFi 代理。自动交易、追踪巨鲸、铸造稳定币、管理组合 — 全在 Telegram 里完成。无需密钥，无需看盘，只看结果。',
              lang
            )}
          </motion.p>

          <motion.div variants={fadeUp} className="flex flex-wrap gap-4 mt-2">
            <a
              href={TG}
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center gap-2 rounded-full bg-white text-black px-6 py-3 text-sm font-semibold hover:bg-zinc-200 transition-colors"
            >
              {t('Try on Telegram', '在 Telegram 试用', lang)} <ExternalLink size={14} />
            </a>
            <a
              href={GH}
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center gap-2 rounded-full border border-white/15 px-6 py-3 text-sm font-semibold hover:border-white/30 transition-colors"
            >
              {t('View Source', '查看源码', lang)}
            </a>
          </motion.div>

          <motion.div
            variants={fadeUp}
            animate={{ y: [0, 8, 0] }}
            transition={{ repeat: Infinity, duration: 2 }}
            className="mt-12 text-zinc-600"
          >
            <ChevronDown size={24} />
          </motion.div>
        </motion.div>
      </section>

      {/* ── How to Start ── */}
      <section className="py-32 px-6">
        <div className="mx-auto max-w-5xl">
          <SectionTitle>
            <GradientText>{t('GET STARTED IN 30 SECONDS', '30 秒开始赚钱', lang)}</GradientText>
          </SectionTitle>

          <motion.div
            variants={stagger}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true }}
            className="grid md:grid-cols-3 gap-6 mt-16"
          >
            {[
              { num: '01', icon: '📱', title: t('Open Telegram', '打开 Telegram', lang), desc: t('Click below to open @SuiJarvisBot', '点击下方打开 @SuiJarvisBot', lang) },
              { num: '02', icon: '🚀', title: t('Press /start', '按 /start', lang), desc: t('A wallet is created for you automatically', '系统自动为你创建钱包', lang) },
              { num: '03', icon: '💰', title: t('Start Trading', '开始交易', lang), desc: t('Swap, track whales, get AI signals', 'Swap、追鲸、获取 AI 信号', lang) },
            ].map((s) => (
              <motion.div key={s.num} variants={fadeUp}>
                <GlassCard className="p-8 h-full">
                  <div className="text-5xl font-black text-white/5 mb-4">{s.num}</div>
                  <div className="text-2xl mb-2">{s.icon}</div>
                  <h3 className="text-lg font-bold mb-2">{s.title}</h3>
                  <p className="text-sm text-zinc-500">{s.desc}</p>
                </GlassCard>
              </motion.div>
            ))}
          </motion.div>

          <motion.div
            variants={fadeUp}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true }}
            className="flex justify-center mt-12"
          >
            <a
              href={TG}
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center gap-2 rounded-full bg-white text-black px-8 py-4 text-sm font-bold hover:bg-zinc-200 transition-colors"
            >
              {t('Open @SuiJarvisBot', '打开 @SuiJarvisBot', lang)} <ArrowRight size={16} />
            </a>
          </motion.div>
        </div>
      </section>

      {/* ── Features ── */}
      <section className="py-32 px-6">
        <div className="mx-auto max-w-5xl">
          <SectionTitle>
            <GradientText>{t('WHAT JARVIS DOES FOR YOU', 'JARVIS 为你做什么', lang)}</GradientText>
          </SectionTitle>
          <motion.p variants={fadeUp} initial="hidden" whileInView="show" viewport={{ once: true }} className="text-center text-zinc-500 mb-16">
            {t('6 core modules. Zero compromise.', '6 大核心模块，零妥协。', lang)}
          </motion.p>

          <motion.div
            variants={stagger}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true }}
            className="grid md:grid-cols-2 lg:grid-cols-3 gap-5"
          >
            {([
              { Icon: Brain, title: t('SMARTER THAN YOUR FUND MANAGER', '比你的基金经理更聪明', lang), desc: t('3 AI strategies running 24/7 — momentum, mean-reversion, and sentiment-driven. Backtested. Battle-tested.', '3 大 AI 策略全天候运行 — 动量、均值回归、情绪驱动。经过回测，久经沙场。', lang) },
              { Icon: Eye, title: t('SEE WHAT WHALES SEE', '看巨鲸所看', lang), desc: t('Real-time whale tracking on Sui. Get alerts before they move. Front-run the smart money.', '实时追踪 Sui 巨鲸动向。抢在聪明钱之前收到提醒。', lang) },
              { Icon: Coins, title: t('MINT YOUR OWN STABLECOIN', '铸造你的稳定币', lang), desc: t('JarvisUSD via StableLayer — overcollateralized, transparent, and fully on-chain.', '通过 StableLayer 铸造 JarvisUSD — 超额抵押、透明、完全链上。', lang) },
              { Icon: Shield, title: t('EVERY TRADE. ON-CHAIN. FOREVER.', '每笔交易，链上永存', lang), desc: t('Full audit trail stored on Walrus + Move vault. Verify everything, trust nothing.', '完整审计记录存储在 Walrus + Move 金库。验证一切，不信任任何人。', lang) },
              { Icon: Share2, title: t('YOUR AI GOES VIRAL', '你的 AI 病毒式传播', lang), desc: t('AI-generated tweets, referral system, social sniper. Grow your network while you sleep.', 'AI 生成推文、推荐系统、社交狙击。你睡觉时也在涨粉。', lang) },
              { Icon: Globe, title: t('SPEAKS YOUR LANGUAGE', '说你的语言', lang), desc: t('Bilingual (EN/CN). Natural language commands. No CLI needed — just talk to Jarvis.', '双语支持（中/英）。自然语言指令，无需命令行 — 直接跟 Jarvis 说话。', lang) },
            ] as const).map(({ Icon, title, desc }) => (
              <motion.div key={title} variants={fadeUp}>
                <GlassCard hover className="p-6 h-full">
                  <Icon size={24} className="text-indigo-400 mb-4" />
                  <h3 className="text-sm font-bold tracking-wide mb-2">{title}</h3>
                  <p className="text-sm text-zinc-500 leading-relaxed">{desc}</p>
                </GlassCard>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* ── Live Dashboard ── */}
      <section className="py-32 px-6">
        <div className="mx-auto max-w-5xl">
          <SectionTitle>{t('LIVE AGENT DASHBOARD', '实时代理仪表盘', lang)}</SectionTitle>

          <motion.div
            variants={fadeUp}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true }}
          >
            <GlassCard className="p-8 mt-12">
              <div className="grid md:grid-cols-[1fr_2fr] gap-8">
                {/* Stats */}
                <div className="flex flex-col gap-4">
                  {[
                    { label: 'Wallet', value: '0x8f3a...c2d1' },
                    { label: t('Total Value', '总价值', lang), value: '$12,847' },
                    { label: 'P&L', value: '+$213', color: 'text-emerald-400' },
                  ].map((s) => (
                    <div key={s.label} className="rounded-xl border border-white/10 bg-white/[0.02] p-4">
                      <div className="text-xs text-zinc-500 mb-1">{s.label}</div>
                      <div className={`text-xl font-bold ${s.color ?? ''}`}>{s.value}</div>
                    </div>
                  ))}
                </div>
                {/* Trades */}
                <div>
                  <div className="text-xs text-zinc-500 mb-3 uppercase tracking-wider">{t('Recent Trades', '最近交易', lang)}</div>
                  <div className="space-y-2">
                    {trades.map((tr, i) => (
                      <div key={i} className="flex items-center justify-between text-sm rounded-lg border border-white/5 bg-white/[0.02] px-4 py-2.5">
                        <span className="text-zinc-600 w-14">{tr.time}</span>
                        <span className="font-medium w-24">{tr.pair}</span>
                        <span className={`w-12 font-bold ${tr.side === 'BUY' ? 'text-emerald-400' : 'text-red-400'}`}>{tr.side}</span>
                        <span className="text-zinc-400 w-20 text-right">{tr.amount}</span>
                        <span className={`w-20 text-right font-medium ${tr.pnl.startsWith('+') ? 'text-emerald-400' : 'text-red-400'}`}>{tr.pnl}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </GlassCard>
          </motion.div>
        </div>
      </section>

      {/* ── Proof ── */}
      <section className="py-32 px-6">
        <div className="mx-auto max-w-4xl text-center">
          <SectionTitle>
            <GradientText>{t("WE DON'T DO WHITEPAPERS. WE DO PROFITS.", '我们不写白皮书，我们只赚钱。', lang)}</GradientText>
          </SectionTitle>

          <motion.div
            variants={fadeUp}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true }}
            className="mt-12"
          >
            <div
              className="text-5xl md:text-7xl font-black tracking-tighter bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400 bg-clip-text text-transparent"
              style={{
                backgroundSize: '200% auto',
                animation: 'shimmer 3s linear infinite',
              }}
            >
              $1,000 → $3,500
            </div>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mt-16">
              {[
                { val: '+250%', label: 'ROI' },
                { val: '6', label: t('Days', '天', lang) },
                { val: '24/7', label: t('Uptime', '在线', lang) },
                { val: '3', label: t('Accounts', '账户', lang) },
              ].map((s) => (
                <div key={s.label}>
                  <div className="text-3xl font-black">{s.val}</div>
                  <div className="text-xs text-zinc-500 mt-1 uppercase tracking-wider">{s.label}</div>
                </div>
              ))}
            </div>

            <p className="mt-16 text-zinc-600 italic max-w-xl mx-auto">
              {t(
                '"We built an AI that prints money. Then we brought it to Sui."',
                '"我们造了一个会印钱的 AI，然后把它带到了 Sui。"',
                lang
              )}
            </p>
          </motion.div>
        </div>
      </section>

      {/* ── Architecture ── */}
      <section className="py-32 px-6">
        <div className="mx-auto max-w-4xl">
          <SectionTitle>{t('HOW IT WORKS', '运作原理', lang)}</SectionTitle>

          <motion.div
            variants={fadeUp}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true }}
            className="mt-16 space-y-6"
          >
            {[archRow1, archRow2].map((row, ri) => (
              <div key={ri} className="flex flex-wrap items-center justify-center gap-3">
                {row.map((node, ni) => (
                  <div key={node} className="flex items-center gap-3">
                    <GlassCard className="px-5 py-3 text-sm font-semibold whitespace-nowrap">{node}</GlassCard>
                    {ni < row.length - 1 && <ArrowRight size={16} className="text-zinc-600 shrink-0" />}
                  </div>
                ))}
              </div>
            ))}
            <div className="flex justify-center">
              <ArrowDown size={16} className="text-zinc-600 rotate-180" />
            </div>
          </motion.div>
        </div>
      </section>

      {/* ── Sui Stack ── */}
      <section className="py-32 px-6">
        <div className="mx-auto max-w-5xl">
          <SectionTitle>{t('BUILT ON THE SUI STACK', '构建于 SUI 生态', lang)}</SectionTitle>

          <motion.div
            variants={stagger}
            initial="hidden"
            whileInView="show"
            viewport={{ once: true }}
            className="flex flex-wrap justify-center gap-4 mt-12"
          >
            {partners.map((p) => (
              <motion.div key={p} variants={fadeUp}>
                <GlassCard hover className="px-6 py-4 text-sm font-semibold">{p}</GlassCard>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* ── Bottom CTA ── */}
      <section className="py-32 px-6">
        <div className="mx-auto max-w-3xl text-center">
          <motion.div variants={fadeUp} initial="hidden" whileInView="show" viewport={{ once: true }}>
            <h2 className="text-3xl md:text-5xl font-black tracking-tight leading-tight">
              {t("STOP TRADING MANUALLY.", '别再手动交易了。', lang)}<br />
              <GradientText>{t('LET JARVIS COOK.', '让 JARVIS 下厨。', lang)}</GradientText> 🔥
            </h2>

            <div className="mt-10">
              <a
                href={TG}
                target="_blank"
                rel="noreferrer"
                className="inline-flex items-center gap-2 rounded-full bg-gradient-to-r from-blue-500 to-purple-600 px-10 py-4 text-sm font-bold hover:opacity-90 transition-opacity"
                style={{ animation: 'pulse-glow 2s ease-in-out infinite' }}
              >
                {t('Try on Telegram', '在 Telegram 试用', lang)} <ExternalLink size={14} />
              </a>
            </div>

            <p className="mt-6 text-xs text-zinc-600">
              {t('Free. Open source. No API keys needed.', '免费。开源。无需 API 密钥。', lang)}
            </p>
          </motion.div>
        </div>
      </section>

      {/* ── Footer ── */}
      <footer className="border-t border-white/5 py-12 px-6">
        <div className="mx-auto max-w-5xl text-center space-y-4 text-xs text-zinc-600">
          <div className="flex flex-wrap justify-center gap-6">
            <a href={GH} target="_blank" rel="noreferrer" className="hover:text-zinc-400 transition-colors">GitHub</a>
            <a href={TG} target="_blank" rel="noreferrer" className="hover:text-zinc-400 transition-colors">Telegram Bot</a>
            <span>Contract: {CONTRACT.slice(0, 8)}...{CONTRACT.slice(-5)}</span>
          </div>
          <p>{t('Built with 🤖 by AI agents, supervised by humans', '由 🤖 AI 代理构建，人类监督', lang)}</p>
          <p>Mission OpenClaw × Vibe Hackathon 2026</p>
        </div>
      </footer>
    </div>
  )
}
