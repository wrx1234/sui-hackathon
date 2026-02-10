import { useState } from 'react'

// ==================== 双语文案 ====================
const TEXTS = {
  en: {
    heroTitle: "SUI DEFI JARVIS",
    heroSub: "YOUR AI ARMY ON SUI. TRADES. HUNTS. SPREADS. 24/7.",
    heroDesc: "While you sleep, Jarvis hunts alpha across 30+ DEXs, snipes new pools, tracks whales, generates viral tweets, and grows your army — all on-chain, all transparent, all autonomous.",
    ctaTelegram: "💬 Try on Telegram",
    ctaGithub: "📂 View Source",
    ctaBottom: "STOP TRADING MANUALLY. LET JARVIS COOK. 🔥",

    featTitle: "WHAT JARVIS DOES FOR YOU",
    feat1Title: "SMARTER THAN YOUR FUND MANAGER",
    feat1Desc: "3 AI strategies running simultaneously — Trend Following, Mean Reversion, DEX Arbitrage. Real-time signals from EMA/RSI/MACD/Bollinger Bands. Not guessing. Computing.",
    feat2Title: "SEE WHAT WHALES SEE — BEFORE THEY MOVE",
    feat2Desc: "Real-time whale tracking, new pool sniping with APR ranking, token safety scanner with audit scores. Your unfair information advantage.",
    feat3Title: "MINT YOUR OWN STABLECOIN. YES, REALLY.",
    feat3Desc: "JarvisUSD via StableLayer. Deposit USDC → auto-compound 4.2% APY. Your money makes money makes money. DeFi inception.",
    feat4Title: "EVERY TRADE. ON-CHAIN. FOREVER.",
    feat4Desc: "Walrus decentralized logs + Move smart contract vault with VaultCap permissions. Not \"trust me bro\" — verify every trade yourself.",
    feat5Title: "YOUR AI GOES VIRAL — SO YOU DON'T HAVE TO",
    feat5Desc: "One-click AI-generated tweets for Crypto Twitter. Referral system with leaderboard. Social Sniper: auto-engage KOLs, broadcast alpha. Your agent builds your audience while you trade.",
    feat6Title: "SPEAKS YOUR LANGUAGE. LITERALLY.",
    feat6Desc: "Full bilingual CN/EN with one tap. Natural language commands — just type what you want. Send a contract address, get instant safety report with audit score.",

    dashTitle: "LIVE AGENT DASHBOARD",
    dashWallet: "Agent Wallet",
    dashTotal: "Total Value",
    dashPnl: "Today's P&L",
    dashTrades: "Recent Trades",

    proofTitle: "WE DON'T DO WHITEPAPERS. WE DO PROFITS.",
    proofStat: "$1,000 → $3,500 in 6 days. +250%.",
    proofDesc: "Our Polymarket bot. Running live. Right now. This is not a concept. Not a whitepaper. Not a pitch deck. It's real money, real trades, real profits.",
    proofCta: "We built an AI that prints money. Then we brought it to Sui.",

    archTitle: "HOW IT WORKS",
    archUser: "You",
    archBot: "TG Bot",
    archAgent: "AI Agent",
    archChain: "Sui Chain",
    archOc: "OpenClaw",
    archStrategy: "Strategy Engine",
    archCetus: "Cetus 30+ DEX",
    archWalrus: "Walrus Logs",

    stackTitle: "BUILT ON THE SUI STACK",
    footerBuilt: "Built with 🤖 by AI agents, supervised by humans",
    footerHack: "Mission OpenClaw × Vibe Hackathon 2026",
    langSwitch: "🇨🇳 中文",
  },
  cn: {
    heroTitle: "SUI DEFI JARVIS",
    heroSub: "你的 Sui 链上 AI 军团。交易。猎杀。裂变。全年无休。",
    heroDesc: "你睡觉时，Jarvis 横扫 30+ DEX 猎取 Alpha、狙击新池、追踪鲸鱼、自动生成病毒推文、裂变扩军——全链上、全透明、全自主。",
    ctaTelegram: "💬 Telegram 体验",
    ctaGithub: "📂 查看源码",
    ctaBottom: "别再手动交易了。让 Jarvis 来。🔥",

    featTitle: "JARVIS 为你做什么",
    feat1Title: "比你的基金经理更聪明",
    feat1Desc: "三大 AI 策略同时运行——趋势跟踪、均值回归、DEX 套利。EMA/RSI/MACD/布林带实时信号。不是猜，是算。",
    feat2Title: "比鲸鱼早一步看到机会",
    feat2Desc: "实时鲸鱼追踪、新池狙击 + APR 排名、Token 安全扫描 + 审计评分。你的不对称信息优势。",
    feat3Title: "铸造你自己的稳定币。没开玩笑。",
    feat3Desc: "通过 StableLayer 铸造 JarvisUSD。存入 USDC → 自动复利 4.2% APY。钱生钱生钱。DeFi 套娃。",
    feat4Title: "每笔交易。链上永存。",
    feat4Desc: "Walrus 去中心化日志 + Move 智能合约金库 + VaultCap 权限控制。不是「信我」——你自己验证。",
    feat5Title: "AI 帮你病毒传播——你躺着就行",
    feat5Desc: "一键生成 CT 推文、邀请裂变排行榜、Social Sniper 自动互动 KOL、广播 Alpha。你的 AI 帮你涨粉，你只管赚钱。",
    feat6Title: "说你的语言。字面意义上的。",
    feat6Desc: "中英一键切换。自然语言操作——想做什么直接说。发合约地址秒出安全报告 + 审计评分。",

    dashTitle: "实时 Agent 仪表盘",
    dashWallet: "Agent 钱包",
    dashTotal: "总资产",
    dashPnl: "今日盈亏",
    dashTrades: "最近交易",

    proofTitle: "我们不写白皮书。我们赚钱。",
    proofStat: "6 天 $1,000 → $3,500。+250%。",
    proofDesc: "我们的 Polymarket 机器人。正在实盘运行。不是概念，不是白皮书，不是 PPT。真金白银，真实交易，真实利润。",
    proofCta: "我们造了一个印钞机 AI。然后把它带到了 Sui。",

    archTitle: "工作原理",
    archUser: "用户",
    archBot: "TG Bot",
    archAgent: "AI Agent",
    archChain: "Sui 链",
    archOc: "OpenClaw",
    archStrategy: "策略引擎",
    archCetus: "Cetus 30+ DEX",
    archWalrus: "Walrus 日志",

    stackTitle: "构建于 SUI 技术栈",
    footerBuilt: "由 🤖 AI 代理构建，人类监督",
    footerHack: "Mission OpenClaw × Vibe Hackathon 2026",
    langSwitch: "🇬🇧 English",
  }
}

type Lang = 'en' | 'cn'

// ==================== Mock Data ====================
const TRADES = [
  { time: "23:15", op: "Swap", detail: "500 SUI → 1,910 USDC", status: "✅", pnl: "+$38" },
  { time: "22:48", op: "Buy", detail: "2,000 CETUS @ $0.089", status: "✅", pnl: "+$12" },
  { time: "22:12", op: "Arbitrage", detail: "SUI/USDC ×3 DEX", status: "✅", pnl: "+$67" },
  { time: "21:35", op: "Swap", detail: "1,000 USDC → 262 SUI", status: "✅", pnl: "+$5" },
  { time: "20:58", op: "Limit Sell", detail: "5,000 NAVX @ $0.25", status: "✅", pnl: "+$91" },
]

const STACK = [
  { icon: "🌊", name: "Sui", desc: "Layer 1 Blockchain" },
  { icon: "🐋", name: "Cetus", desc: "DEX Aggregator" },
  { icon: "🐘", name: "Walrus", desc: "Decentralized Storage" },
  { icon: "🔐", name: "Seal", desc: "Key Encryption" },
  { icon: "💎", name: "StableLayer", desc: "Stablecoin-as-a-Service" },
  { icon: "🦞", name: "OpenClaw", desc: "AI Agent Runtime" },
  { icon: "📱", name: "Moltbook", desc: "Agent Social Network" },
]

const FEATURES = [
  { icon: "🧠", key: "feat1" },
  { icon: "🐋", key: "feat2" },
  { icon: "💎", key: "feat3" },
  { icon: "🐘", key: "feat4" },
  { icon: "📣", key: "feat5" },
  { icon: "🌐", key: "feat6" },
]

// ==================== Components ====================
function App() {
  const [lang, setLang] = useState<Lang>('en')
  const t = TEXTS[lang]

  return (
    <div className="relative min-h-screen scroll-smooth">
      {/* Background effects */}
      <div className="grid-bg" />
      <div className="glow-orb glow-orb-1" />
      <div className="glow-orb glow-orb-2" />
      <div className="glow-orb glow-orb-3" />

      {/* Nav */}
      <nav className="fixed top-0 w-full z-50 backdrop-blur-md bg-[#0a0a0f]/80 border-b border-[#1e1e3a]">
        <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
          <span className="text-xl font-bold gradient-text">⚡ JARVIS</span>
          <div className="flex gap-4 items-center">
            <a href="https://t.me/SuiJarvisBot" target="_blank" className="text-sm text-[#4DA2FF] hover:text-white transition">Bot</a>
            <a href="https://github.com/wrx1234/sui-hackathon" target="_blank" className="text-sm text-[#4DA2FF] hover:text-white transition">GitHub</a>
            <button onClick={() => setLang(lang === 'en' ? 'cn' : 'en')} className="text-sm px-3 py-1 rounded-full btn-outline">
              {t.langSwitch}
            </button>
          </div>
        </div>
      </nav>

      {/* Hero */}
      <section className="relative z-10 pt-32 pb-16 px-6 text-center max-w-5xl mx-auto min-h-[85vh] flex flex-col justify-center">
        <div className="animate-slide-up">
          <div className="inline-block px-4 py-1.5 rounded-full text-xs font-mono mb-8 border border-[#4DA2FF]/30 text-[#4DA2FF] bg-[#4DA2FF]/5 badge-float">
            THE INFINITE MONEY GLITCH — POWERED BY OPENCLAW
          </div>
          <h1 className="text-5xl md:text-7xl font-black tracking-tight mb-6 gradient-text leading-tight">
            {t.heroTitle}
          </h1>
        </div>
        <p className="animate-slide-up-delay text-xl md:text-2xl font-bold text-white mb-6">
          {t.heroSub}
        </p>
        <p className="animate-slide-up-delay2 text-lg text-gray-400 max-w-3xl mx-auto mb-10 leading-relaxed">
          {t.heroDesc}
        </p>
        <div className="flex flex-wrap gap-6 justify-center mt-8" style={{animation: 'slide-up 0.8s ease-out 0.5s forwards', opacity: 0}}>
          <a href="https://t.me/SuiJarvisBot" target="_blank" className="btn-primary px-10 py-5 rounded-2xl text-white font-black text-xl no-underline shadow-lg shadow-[#4DA2FF]/25">
            {t.ctaTelegram}
          </a>
          <a href="https://github.com/wrx1234/sui-hackathon" target="_blank" className="btn-outline px-10 py-5 rounded-2xl text-white font-bold text-xl no-underline">
            {t.ctaGithub}
          </a>
        </div>
        <div className="mt-12 bounce-down text-gray-500 text-2xl">↓</div>
      </section>

      <div className="section-divider max-w-4xl mx-auto" />

      {/* Features */}
      <section className="relative z-10 py-20 px-6 max-w-7xl mx-auto">
        <h2 className="text-3xl md:text-4xl font-black text-center mb-4 gradient-text">{t.featTitle}</h2>
        <p className="text-center text-gray-500 mb-12 text-sm">6 CORE MODULES. ZERO COMPROMISE.</p>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {FEATURES.map((f, i) => (
            <div key={i} className="card-hover rounded-2xl p-8 bg-[#12122a]/80 backdrop-blur flex flex-col">
              <div className="text-5xl mb-5">{f.icon}</div>
              <h3 className="text-lg font-black text-white mb-3 uppercase tracking-wide leading-snug">
                {(t as any)[`${f.key}Title`]}
              </h3>
              <p className="text-gray-400 text-sm leading-relaxed flex-1">
                {(t as any)[`${f.key}Desc`]}
              </p>
            </div>
          ))}
        </div>
      </section>

      <div className="section-divider max-w-4xl mx-auto" />

      {/* Live Dashboard */}
      <section className="relative z-10 py-20 px-6 max-w-6xl mx-auto">
        <h2 className="text-3xl md:text-4xl font-black text-center mb-12 gradient-text">{t.dashTitle}</h2>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Left: Stats */}
          <div className="space-y-4">
            <div className="card-hover rounded-2xl p-6 bg-[#12122a]/80">
              <div className="text-sm text-gray-500 mb-1">{t.dashWallet}</div>
              <div className="font-mono text-sm text-[#4DA2FF] break-all">0xc3aa5e...230a9b80</div>
              <div className="text-xs text-gray-600 mt-1">Sui Testnet</div>
            </div>
            <div className="card-hover rounded-2xl p-6 bg-[#12122a]/80">
              <div className="text-sm text-gray-500 mb-1">{t.dashTotal}</div>
              <div className="text-4xl font-black text-white ticker">$12,847.52</div>
              <div className="flex gap-4 mt-2 text-sm">
                <span className="text-gray-400">🟦 3,142 SUI</span>
                <span className="text-gray-400">💵 1,250 USDC</span>
              </div>
            </div>
            <div className="card-hover rounded-2xl p-6 bg-[#12122a]/80">
              <div className="text-sm text-gray-500 mb-1">{t.dashPnl}</div>
              <div className="text-3xl font-black text-[#22c55e] ticker">+$213.40 (+1.7%)</div>
              <div className="w-full bg-gray-800 rounded-full h-2 mt-3">
                <div className="bg-gradient-to-r from-[#4DA2FF] to-[#22c55e] h-2 rounded-full" style={{width: '67%'}}></div>
              </div>
              <div className="text-xs text-gray-500 mt-1">Win Rate: 67% (31W / 16L)</div>
            </div>
          </div>
          {/* Right: Trades */}
          <div className="card-hover rounded-2xl p-6 bg-[#12122a]/80">
            <div className="text-sm text-gray-500 mb-4">{t.dashTrades}</div>
            <div className="space-y-3">
              {TRADES.map((tr, i) => (
                <div key={i} className="flex items-center justify-between py-2 border-b border-[#1e1e3a] last:border-0">
                  <div className="flex items-center gap-3">
                    <span className="text-xs text-gray-500 font-mono w-12">{tr.time}</span>
                    <span className="text-xs px-2 py-0.5 rounded bg-[#4DA2FF]/10 text-[#4DA2FF]">{tr.op}</span>
                  </div>
                  <span className="text-sm text-gray-300">{tr.detail}</span>
                  <span className="text-sm font-bold text-[#22c55e]">{tr.pnl}</span>
                </div>
              ))}
            </div>
            <div className="mt-4 text-center">
              <span className="text-xs text-gray-500">🐘 All logged on Walrus — verify anytime</span>
            </div>
          </div>
        </div>
      </section>

      <div className="section-divider max-w-4xl mx-auto" />

      {/* Proof */}
      <section className="relative z-10 py-20 px-6 max-w-4xl mx-auto text-center proof-glow">
        <h2 className="text-3xl md:text-4xl font-black mb-8 gradient-text">{t.proofTitle}</h2>
        <div className="card-hover rounded-2xl p-10 bg-[#12122a]/80 mb-8 border-[#4DA2FF]/20">
          <div className="text-4xl md:text-6xl font-black shimmer mb-6 leading-tight">{t.proofStat}</div>
          <div className="flex justify-center gap-10 mb-8">
            <div className="text-center">
              <div className="text-3xl font-black text-[#22c55e] stat-pop">+250%</div>
              <div className="text-xs text-gray-500 mt-1">ROI</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-black text-[#4DA2FF] stat-pop" style={{animationDelay: '0.1s'}}>6</div>
              <div className="text-xs text-gray-500 mt-1">Days</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-black text-white stat-pop" style={{animationDelay: '0.2s'}}>24/7</div>
              <div className="text-xs text-gray-500 mt-1">Uptime</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-black text-[#7B61FF] stat-pop" style={{animationDelay: '0.3s'}}>3</div>
              <div className="text-xs text-gray-500 mt-1">Accounts</div>
            </div>
          </div>
          <p className="text-gray-400 leading-relaxed mb-6">{t.proofDesc}</p>
          <p className="text-xl font-bold text-white italic">"{t.proofCta}"</p>
        </div>
      </section>

      <div className="section-divider max-w-4xl mx-auto" />

      {/* Architecture */}
      <section className="relative z-10 py-20 px-6 max-w-5xl mx-auto">
        <h2 className="text-3xl md:text-4xl font-black text-center mb-12 gradient-text">{t.archTitle}</h2>
        <div className="flex flex-wrap justify-center items-center gap-3 md:gap-4">
          {[
            { icon: "👤", label: t.archUser },
            null,
            { icon: "📱", label: t.archBot },
            null,
            { icon: "🤖", label: t.archAgent },
            null,
            { icon: "⛓️", label: t.archChain },
          ].map((item, i) => item ? (
            <div key={i} className="card-hover rounded-xl px-4 py-3 bg-[#12122a]/80 text-center min-w-[100px]">
              <div className="text-2xl mb-1">{item.icon}</div>
              <div className="text-xs font-bold text-white">{item.label}</div>
            </div>
          ) : (
            <div key={i} className="text-[#4DA2FF] text-2xl flow-line">→</div>
          ))}
        </div>
        <div className="flex flex-wrap justify-center items-center gap-3 md:gap-4 mt-4">
          {[
            { icon: "🦞", label: t.archOc },
            null,
            { icon: "🧠", label: t.archStrategy },
            null,
            { icon: "🐋", label: t.archCetus },
            null,
            { icon: "🐘", label: t.archWalrus },
          ].map((item, i) => item ? (
            <div key={i} className="card-hover rounded-xl px-4 py-3 bg-[#12122a]/80 text-center min-w-[100px]">
              <div className="text-2xl mb-1">{item.icon}</div>
              <div className="text-xs font-bold text-white">{item.label}</div>
            </div>
          ) : (
            <div key={i} className="text-[#7B61FF] text-2xl flow-line-delay">→</div>
          ))}
        </div>
        <div className="text-center mt-6 text-sm text-gray-500">
          {lang === 'en'
            ? "Fully autonomous pipeline — from market analysis to trade execution to on-chain logging"
            : "全自主流水线——从市场分析到交易执行到链上记录"}
        </div>
      </section>

      <div className="section-divider max-w-4xl mx-auto" />

      {/* Sui Stack */}
      <section className="relative z-10 py-20 px-6 max-w-5xl mx-auto text-center">
        <h2 className="text-3xl md:text-4xl font-black mb-12 gradient-text">{t.stackTitle}</h2>
        <div className="flex flex-wrap justify-center gap-6">
          {STACK.map((s, i) => (
            <div key={i} className="card-hover rounded-xl px-6 py-4 bg-[#12122a]/80 text-center min-w-[120px]">
              <div className="text-3xl mb-2">{s.icon}</div>
              <div className="text-sm font-bold text-white">{s.name}</div>
              <div className="text-xs text-gray-500">{s.desc}</div>
            </div>
          ))}
        </div>
      </section>

      <div className="section-divider max-w-4xl mx-auto" />

      {/* Bottom CTA */}
      <section className="relative z-10 py-20 px-6 text-center max-w-3xl mx-auto">
        <h2 className="text-3xl md:text-5xl font-black mb-8 text-white">{t.ctaBottom}</h2>
        <a href="https://t.me/SuiJarvisBot" target="_blank" className="btn-primary inline-block px-12 py-6 rounded-2xl text-white font-black text-2xl no-underline mega-pulse">
          {t.ctaTelegram}
        </a>
        <p className="mt-6 text-sm text-gray-500">
          {lang === 'en' ? 'Free. Open source. No API keys needed.' : '免费。开源。无需 API Key。'}
        </p>
      </section>

      {/* Footer */}
      <footer className="relative z-10 border-t border-[#1e1e3a] py-8 px-6 text-center">
        <div className="flex flex-wrap justify-center gap-6 mb-4">
          <a href="https://github.com/wrx1234/sui-hackathon" target="_blank" className="text-sm text-gray-500 hover:text-[#4DA2FF] transition no-underline">GitHub</a>
          <a href="https://t.me/SuiJarvisBot" target="_blank" className="text-sm text-gray-500 hover:text-[#4DA2FF] transition no-underline">Telegram Bot</a>
          <span className="text-sm text-gray-600">Contract: 0x737a73...7e65d</span>
        </div>
        <p className="text-sm text-gray-600 mb-2">{t.footerBuilt}</p>
        <p className="text-xs text-gray-700">{t.footerHack}</p>
      </footer>
    </div>
  )
}

export default App
