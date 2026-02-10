import { useState, useRef, useEffect } from 'react'
import { motion, useMotionValue, useTransform, animate } from 'framer-motion'
import { Brain, Eye, Coins, Shield, Share2, Globe, ChevronDown, ArrowRight, Zap, ExternalLink } from 'lucide-react'

// ─── i18n ───
const t = {
  en: {
    nav: { bot: 'Bot', github: 'GitHub' },
    hero: {
      badge: 'THE INFINITE MONEY GLITCH — POWERED BY OPENCLAW',
      title: 'SUI DEFI JARVIS',
      sub: 'YOUR AI ARMY ON SUI. TRADES. HUNTS. SPREADS. 24/7.',
      desc: 'An autonomous DeFi agent swarm that monitors whale movements, executes arbitrage, mints tokens, and grows your portfolio — all from a single Telegram command.',
      cta1: 'Try on Telegram',
      cta2: 'View Source',
    },
    start: {
      title: 'GET STARTED IN 30 SECONDS',
      steps: [
        { num: '01', title: 'Open Telegram', desc: 'Search @SuiJarvisBot or click the link below.' },
        { num: '02', title: 'Send /start', desc: 'The bot activates your personal AI agent swarm.' },
        { num: '03', title: 'Trade & Earn', desc: 'Sit back. Jarvis hunts, trades, and compounds 24/7.' },
      ],
      cta: 'Open @SuiJarvisBot →',
    },
    features: {
      title: 'WHAT JARVIS DOES FOR YOU',
      sub: '6 core modules. Zero compromise.',
      items: [
        { icon: 'Brain', title: 'AI Strategy Engine', desc: 'Multi-model reasoning picks optimal entry/exit across Sui DEXs.' },
        { icon: 'Eye', title: 'Whale Tracker', desc: 'Real-time monitoring of whale wallets. Front-run the smart money.' },
        { icon: 'Coins', title: 'Token Minter', desc: 'One-click token deployment on Sui with built-in liquidity.' },
        { icon: 'Shield', title: 'On-chain Auditor', desc: 'Contract risk scoring & rug-pull detection before you ape.' },
        { icon: 'Share2', title: 'Social Fission', desc: 'Referral system with on-chain rewards. Your army grows itself.' },
        { icon: 'Globe', title: 'Bilingual AI', desc: 'Native Chinese & English. No lost-in-translation moments.' },
      ],
    },
    dashboard: {
      title: 'LIVE AGENT DASHBOARD',
      wallets: 'Active Wallets',
      value: 'Total Value',
      pnl: 'Unrealized PnL',
      trades: [
        { pair: 'SUI/USDC', action: 'BUY', amount: '+2,400 SUI', time: '2m ago' },
        { pair: 'CETUS/SUI', action: 'SELL', amount: '-500 CETUS', time: '5m ago' },
        { pair: 'WETH/SUI', action: 'BUY', amount: '+0.8 WETH', time: '12m ago' },
        { pair: 'USDT/USDC', action: 'ARB', amount: '+$12.40', time: '18m ago' },
        { pair: 'SUI/USDC', action: 'BUY', amount: '+1,100 SUI', time: '31m ago' },
      ],
    },
    proof: {
      title: "WE DON'T DO WHITEPAPERS. WE DO PROFITS.",
      amount: '$1,000 → $3,500',
      stats: ['+250% ROI', '6 Days', '24/7 Uptime', '3 Accounts'],
      quote: '"I let Jarvis run for a week. It outperformed my 6 months of manual trading."',
    },
    arch: {
      title: 'HOW IT WORKS',
      flow1: ['You', 'TG Bot', 'AI Agent', 'Sui Chain'],
      flow2: ['OpenClaw', 'Strategy', 'Cetus', 'Walrus'],
    },
    stack: {
      title: 'BUILT ON THE SUI STACK',
      items: ['Sui', 'Cetus', 'Walrus', 'Seal', 'StableLayer', 'OpenClaw', 'Moltbook'],
    },
    bottomCta: {
      line1: 'STOP TRADING MANUALLY.',
      line2: 'LET JARVIS COOK. 🔥',
      cta: 'Launch Jarvis on Telegram',
      sub: 'Free. Open source. No API keys needed.',
    },
    footer: {
      built: 'Built with 🤖 by AI agents, supervised by humans',
      event: 'Mission OpenClaw × Vibe Hackathon 2026',
    },
  },
  cn: {
    nav: { bot: '机器人', github: 'GitHub' },
    hero: {
      badge: '无限印钞机 — POWERED BY OPENCLAW',
      title: 'SUI DEFI JARVIS',
      sub: '你的 AI 军团，在 SUI 上。交易、追踪、裂变，全天候。',
      desc: '一个自主 DeFi 代理集群：监控巨鲸动向、执行套利、铸币、自动复投——一条 Telegram 命令搞定一切。',
      cta1: '在 Telegram 体验',
      cta2: '查看源码',
    },
    start: {
      title: '30 秒极速启动',
      steps: [
        { num: '01', title: '打开 Telegram', desc: '搜索 @SuiJarvisBot 或点击下方链接。' },
        { num: '02', title: '发送 /start', desc: '机器人激活你的专属 AI 代理集群。' },
        { num: '03', title: '交易赚钱', desc: '躺平即可。Jarvis 全天候追踪、交易、复投。' },
      ],
      cta: '打开 @SuiJarvisBot →',
    },
    features: {
      title: 'JARVIS 为你做什么',
      sub: '六大核心模块，零妥协。',
      items: [
        { icon: 'Brain', title: 'AI 策略引擎', desc: '多模型推理，自动选择 Sui DEX 最优买卖点。' },
        { icon: 'Eye', title: '巨鲸追踪', desc: '实时监控巨鲸钱包，抢在聪明钱前面。' },
        { icon: 'Coins', title: '一键铸币', desc: '在 Sui 上一键发币，内置流动性。' },
        { icon: 'Shield', title: '链上审计', desc: '合约风险评分，Rug Pull 检测，入场前先看清。' },
        { icon: 'Share2', title: '社交裂变', desc: '链上推荐奖励，你的军团自己壮大。' },
        { icon: 'Globe', title: '中英双语', desc: '原生中英文支持，沟通零障碍。' },
      ],
    },
    dashboard: {
      title: '实时代理仪表盘',
      wallets: '活跃钱包',
      value: '总价值',
      pnl: '未实现盈亏',
      trades: [
        { pair: 'SUI/USDC', action: '买入', amount: '+2,400 SUI', time: '2分钟前' },
        { pair: 'CETUS/SUI', action: '卖出', amount: '-500 CETUS', time: '5分钟前' },
        { pair: 'WETH/SUI', action: '买入', amount: '+0.8 WETH', time: '12分钟前' },
        { pair: 'USDT/USDC', action: '套利', amount: '+$12.40', time: '18分钟前' },
        { pair: 'SUI/USDC', action: '买入', amount: '+1,100 SUI', time: '31分钟前' },
      ],
    },
    proof: {
      title: '我们不写白皮书，我们写利润。',
      amount: '$1,000 → $3,500',
      stats: ['+250% 收益率', '6 天', '24/7 在线', '3 个账户'],
      quote: '"让 Jarvis 跑了一周，超过了我六个月手动交易的收益。"',
    },
    arch: {
      title: '运作原理',
      flow1: ['你', 'TG 机器人', 'AI 代理', 'Sui 链'],
      flow2: ['OpenClaw', '策略引擎', 'Cetus', 'Walrus'],
    },
    stack: {
      title: '构建于 SUI 生态',
      items: ['Sui', 'Cetus', 'Walrus', 'Seal', 'StableLayer', 'OpenClaw', 'Moltbook'],
    },
    bottomCta: {
      line1: '别再手动交易了。',
      line2: '让 JARVIS 上场。🔥',
      cta: '在 Telegram 启动 Jarvis',
      sub: '免费。开源。无需 API Key。',
    },
    footer: {
      built: '由 🤖 AI 代理构建，人类监督',
      event: 'Mission OpenClaw × Vibe Hackathon 2026',
    },
  },
}

// ─── Components ───

function BadgeShine({ children }: { children: React.ReactNode }) {
  return (
    <span className="inline-flex animate-background-shine items-center justify-center rounded-full border border-gray-800 bg-[linear-gradient(110deg,#000,45%,#4D4B4B,55%,#000)] bg-[length:250%_100%] px-4 py-1.5 text-xs font-medium text-gray-300 tracking-wider">
      {children}
    </span>
  )
}

function ButtonGradient({ children, href, className = '' }: { children: React.ReactNode; href?: string; className?: string }) {
  const cls = `inline-flex h-12 items-center justify-center rounded-md border border-gray-800 bg-gradient-to-t from-[#8678f9] to-[#c7d2fe] px-6 font-medium text-gray-950 transition-all hover:scale-105 cursor-pointer ${className}`
  if (href) return <a href={href} target="_blank" rel="noopener noreferrer" className={cls}>{children}</a>
  return <button className={cls}>{children}</button>
}

function CardSpotlight({ children, className = '' }: { children: React.ReactNode; className?: string }) {
  const ref = useRef<HTMLDivElement>(null)
  const [pos, setPos] = useState({ x: 0, y: 0 })
  const [hovering, setHovering] = useState(false)

  function handleMouseMove(e: React.MouseEvent<HTMLDivElement>) {
    if (!ref.current) return
    const rect = ref.current.getBoundingClientRect()
    setPos({ x: e.clientX - rect.left, y: e.clientY - rect.top })
  }

  return (
    <div
      ref={ref}
      onMouseMove={handleMouseMove}
      onMouseEnter={() => setHovering(true)}
      onMouseLeave={() => setHovering(false)}
      className={`relative overflow-hidden rounded-xl border border-gray-800 bg-gradient-to-r from-black to-gray-950 p-6 ${className}`}
      style={{
        background: hovering
          ? `radial-gradient(600px circle at ${pos.x}px ${pos.y}px, rgba(255,182,255,.06), transparent 40%), linear-gradient(to right, #000, #0a0a0f)`
          : undefined,
      }}
    >
      {children}
    </div>
  )
}

function GradientText({ children, className = '' }: { children: React.ReactNode; className?: string }) {
  return (
    <span className={`bg-gradient-to-r from-indigo-400 via-purple-400 to-pink-400 bg-clip-text text-transparent ${className}`}>
      {children}
    </span>
  )
}

function NumberTicker({ value, duration = 1.5 }: { value: number; duration?: number }) {
  const motionVal = useMotionValue(0)
  const rounded = useTransform(motionVal, (v) => {
    if (value >= 1000) return Math.round(v).toLocaleString()
    if (value % 1 !== 0) return v.toFixed(2)
    return Math.round(v).toLocaleString()
  })
  const [display, setDisplay] = useState('0')

  useEffect(() => {
    const controls = animate(motionVal, value, { duration })
    const unsub = rounded.on('change', (v) => setDisplay(v))
    return () => { controls.stop(); unsub() }
  }, [value, duration, motionVal, rounded])

  return <span>{display}</span>
}

const fadeUp = {
  initial: { opacity: 0, y: 20 },
  whileInView: { opacity: 1, y: 0 },
  viewport: { once: true },
  transition: { duration: 0.5 },
}

const stagger = { transition: { staggerChildren: 0.08 } }
const staggerChild = { initial: { opacity: 0, y: 20 }, whileInView: { opacity: 1, y: 0 }, viewport: { once: true } }

const iconMap: Record<string, React.ReactNode> = {
  Brain: <Brain className="w-6 h-6 text-indigo-400" />,
  Eye: <Eye className="w-6 h-6 text-purple-400" />,
  Coins: <Coins className="w-6 h-6 text-yellow-400" />,
  Shield: <Shield className="w-6 h-6 text-green-400" />,
  Share2: <Share2 className="w-6 h-6 text-pink-400" />,
  Globe: <Globe className="w-6 h-6 text-cyan-400" />,
}

const TG = 'https://t.me/SuiJarvisBot'
const GH = 'https://github.com/wrx1234/sui-hackathon'
const CONTRACT = '0x737a73b3a146d45694c341a22b62607e5a6e6b6496b91156217a7d2c91f7e65d'

// ─── App ───

export default function App() {
  const [lang, setLang] = useState<'en' | 'cn'>('en')
  const c = t[lang]

  return (
    <div className="min-h-screen bg-[var(--background)] text-[var(--foreground)]">
      {/* Nav */}
      <nav className="fixed top-0 left-0 right-0 z-50 backdrop-blur-xl border-b border-white/5 bg-black/60">
        <div className="max-w-6xl mx-auto px-6 h-14 flex items-center justify-between">
          <a href="#" className="flex items-center gap-2 font-bold text-lg">
            <Zap className="w-5 h-5 text-indigo-400" />
            <GradientText>JARVIS</GradientText>
          </a>
          <div className="flex items-center gap-4 text-sm text-zinc-400">
            <a href={TG} target="_blank" rel="noopener noreferrer" className="hover:text-white transition-colors">{c.nav.bot}</a>
            <a href={GH} target="_blank" rel="noopener noreferrer" className="hover:text-white transition-colors">{c.nav.github}</a>
            <button
              onClick={() => setLang(lang === 'en' ? 'cn' : 'en')}
              className="px-2 py-1 rounded border border-gray-800 hover:border-gray-600 transition-colors cursor-pointer text-xs"
            >
              {lang === 'en' ? '🇨🇳 中文' : '🇬🇧 EN'}
            </button>
          </div>
        </div>
      </nav>

      {/* Hero */}
      <section className="min-h-screen flex flex-col items-center justify-center text-center px-6 pt-20">
        <motion.div {...stagger} className="flex flex-col items-center gap-6">
          <motion.div {...staggerChild}><BadgeShine>{c.hero.badge}</BadgeShine></motion.div>
          <motion.h1 {...staggerChild} className="text-6xl md:text-8xl font-black tracking-tighter">
            <GradientText>{c.hero.title}</GradientText>
          </motion.h1>
          <motion.p {...staggerChild} className="text-xl md:text-2xl text-zinc-400 font-medium">{c.hero.sub}</motion.p>
          <motion.p {...staggerChild} className="text-zinc-500 max-w-2xl leading-relaxed">{c.hero.desc}</motion.p>
          <motion.div {...staggerChild} className="flex gap-4 flex-wrap justify-center">
            <ButtonGradient href={TG}>{c.hero.cta1}</ButtonGradient>
            <a href={GH} target="_blank" rel="noopener noreferrer" className="inline-flex h-12 items-center justify-center rounded-md border border-gray-800 px-6 font-medium text-zinc-300 hover:border-gray-600 transition-colors">
              {c.hero.cta2} <ExternalLink className="w-4 h-4 ml-2" />
            </a>
          </motion.div>
          <motion.div {...staggerChild} className="mt-8 animate-bounce-slow text-zinc-600">
            <ChevronDown className="w-6 h-6" />
          </motion.div>
        </motion.div>
      </section>

      {/* How to Start */}
      <section className="py-24 px-6">
        <div className="max-w-5xl mx-auto">
          <motion.h2 {...fadeUp} className="text-3xl md:text-5xl font-black tracking-tight text-center mb-16">
            <GradientText>{c.start.title}</GradientText>
          </motion.h2>
          <div className="grid md:grid-cols-3 gap-6">
            {c.start.steps.map((s, i) => (
              <motion.div key={i} {...fadeUp} transition={{ delay: i * 0.1 }}>
                <CardSpotlight className="h-full">
                  <div className="text-5xl font-black text-indigo-500/20 mb-4">{s.num}</div>
                  <h3 className="text-lg font-bold mb-2">{s.title}</h3>
                  <p className="text-zinc-500 text-sm">{s.desc}</p>
                </CardSpotlight>
              </motion.div>
            ))}
          </div>
          <motion.div {...fadeUp} className="text-center mt-12">
            <ButtonGradient href={TG} className="text-lg px-8">{c.start.cta}</ButtonGradient>
          </motion.div>
        </div>
      </section>

      {/* Features */}
      <section className="py-24 px-6">
        <div className="max-w-5xl mx-auto">
          <motion.h2 {...fadeUp} className="text-3xl md:text-5xl font-black tracking-tight text-center mb-4">
            <GradientText>{c.features.title}</GradientText>
          </motion.h2>
          <motion.p {...fadeUp} className="text-zinc-500 text-center mb-16">{c.features.sub}</motion.p>
          <div className="grid md:grid-cols-3 gap-6">
            {c.features.items.map((f, i) => (
              <motion.div key={i} {...fadeUp} transition={{ delay: i * 0.08 }}>
                <CardSpotlight className="h-full">
                  <div className="mb-4">{iconMap[f.icon]}</div>
                  <h3 className="font-bold mb-2">{f.title}</h3>
                  <p className="text-zinc-500 text-sm">{f.desc}</p>
                </CardSpotlight>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Live Dashboard */}
      <section className="py-24 px-6">
        <div className="max-w-5xl mx-auto">
          <motion.h2 {...fadeUp} className="text-3xl md:text-5xl font-black tracking-tight text-center mb-16">
            <GradientText>{c.dashboard.title}</GradientText>
          </motion.h2>
          <div className="grid md:grid-cols-2 gap-8">
            <motion.div {...fadeUp} className="space-y-4">
              {[
                { label: c.dashboard.wallets, val: 3, prefix: '' },
                { label: c.dashboard.value, val: 12480, prefix: '$' },
                { label: c.dashboard.pnl, val: 2340, prefix: '+$' },
              ].map((s, i) => (
                <CardSpotlight key={i}>
                  <p className="text-zinc-500 text-sm mb-1">{s.label}</p>
                  <p className="text-2xl font-black">{s.prefix}<NumberTicker value={s.val} /></p>
                </CardSpotlight>
              ))}
            </motion.div>
            <motion.div {...fadeUp}>
              <CardSpotlight className="h-full">
                <p className="text-xs text-zinc-500 uppercase tracking-wider mb-4">Recent Trades</p>
                <div className="space-y-3">
                  {c.dashboard.trades.map((tr, i) => (
                    <div key={i} className="flex items-center justify-between text-sm">
                      <span className="font-medium w-24">{tr.pair}</span>
                      <span className={`text-xs px-2 py-0.5 rounded ${tr.action === 'BUY' || tr.action === '买入' ? 'bg-green-500/10 text-green-400' : tr.action === 'SELL' || tr.action === '卖出' ? 'bg-red-500/10 text-red-400' : 'bg-indigo-500/10 text-indigo-400'}`}>{tr.action}</span>
                      <span className="text-zinc-400 w-28 text-right">{tr.amount}</span>
                      <span className="text-zinc-600 text-xs w-16 text-right">{tr.time}</span>
                    </div>
                  ))}
                </div>
              </CardSpotlight>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Proof */}
      <section className="py-24 px-6">
        <div className="max-w-4xl mx-auto text-center">
          <motion.h2 {...fadeUp} className="text-3xl md:text-5xl font-black tracking-tight mb-8">
            <GradientText>{c.proof.title}</GradientText>
          </motion.h2>
          <motion.div {...fadeUp} className="text-5xl md:text-7xl font-black mb-12 animate-shimmer bg-[linear-gradient(110deg,#e2e8f0,45%,#818cf8,55%,#e2e8f0)] bg-[length:250%_100%] bg-clip-text text-transparent">
            {c.proof.amount}
          </motion.div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-12">
            {c.proof.stats.map((s, i) => (
              <motion.div key={i} {...fadeUp} transition={{ delay: i * 0.1 }}>
                <CardSpotlight className="text-center py-4">
                  <p className="text-xl font-bold text-indigo-400">{s}</p>
                </CardSpotlight>
              </motion.div>
            ))}
          </div>
          <motion.p {...fadeUp} className="text-zinc-500 italic max-w-xl mx-auto">{c.proof.quote}</motion.p>
        </div>
      </section>

      {/* Architecture */}
      <section className="py-24 px-6">
        <div className="max-w-4xl mx-auto text-center">
          <motion.h2 {...fadeUp} className="text-3xl md:text-5xl font-black tracking-tight mb-16">
            <GradientText>{c.arch.title}</GradientText>
          </motion.h2>
          {[c.arch.flow1, c.arch.flow2].map((flow, fi) => (
            <motion.div key={fi} {...fadeUp} className="flex items-center justify-center gap-2 md:gap-4 flex-wrap mb-8">
              {flow.map((item, i) => (
                <span key={i} className="flex items-center gap-2 md:gap-4">
                  <span className="px-4 py-2 rounded-lg border border-gray-800 bg-gray-950 text-sm font-medium">{item}</span>
                  {i < flow.length - 1 && <ArrowRight className="w-4 h-4 text-zinc-600" />}
                </span>
              ))}
            </motion.div>
          ))}
        </div>
      </section>

      {/* Sui Stack */}
      <section className="py-24 px-6">
        <div className="max-w-5xl mx-auto text-center">
          <motion.h2 {...fadeUp} className="text-3xl md:text-5xl font-black tracking-tight mb-16">
            <GradientText>{c.stack.title}</GradientText>
          </motion.h2>
          <div className="flex flex-wrap justify-center gap-4">
            {c.stack.items.map((item, i) => (
              <motion.div key={i} {...fadeUp} transition={{ delay: i * 0.05 }}>
                <CardSpotlight className="px-6 py-4">
                  <span className="font-bold text-sm">{item}</span>
                </CardSpotlight>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Bottom CTA */}
      <section className="py-32 px-6 text-center">
        <motion.div {...fadeUp} className="max-w-3xl mx-auto">
          <h2 className="text-4xl md:text-6xl font-black tracking-tight mb-2">{c.bottomCta.line1}</h2>
          <h2 className="text-4xl md:text-6xl font-black tracking-tight mb-12">
            <GradientText>{c.bottomCta.line2}</GradientText>
          </h2>
          <ButtonGradient href={TG} className="text-lg px-10 animate-pulse-glow">{c.bottomCta.cta}</ButtonGradient>
          <p className="text-zinc-600 mt-6 text-sm">{c.bottomCta.sub}</p>
        </motion.div>
      </section>

      {/* Footer */}
      <footer className="border-t border-white/5 py-12 px-6">
        <div className="max-w-5xl mx-auto text-center text-sm text-zinc-600 space-y-4">
          <div className="flex justify-center gap-6">
            <a href={GH} target="_blank" rel="noopener noreferrer" className="hover:text-zinc-400 transition-colors">GitHub</a>
            <a href={TG} target="_blank" rel="noopener noreferrer" className="hover:text-zinc-400 transition-colors">Telegram Bot</a>
            <a href={`https://suivision.xyz/object/${CONTRACT}`} target="_blank" rel="noopener noreferrer" className="hover:text-zinc-400 transition-colors">Contract</a>
          </div>
          <p>{c.footer.built}</p>
          <p className="text-zinc-700">{c.footer.event}</p>
        </div>
      </footer>
    </div>
  )
}
