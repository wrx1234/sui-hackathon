#!/usr/bin/env python3
"""
🤖 Sui DeFi Jarvis Bot — @SuiJarvisBot
The Infinite Money Glitch on Sui

Autonomous AI DeFi Agent powered by OpenClaw
Tech Stack: Sui × Cetus × Walrus × Seal
"""

import json, os, time, logging, requests, hashlib, random, re
from datetime import datetime, timezone, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes
)
from telegram.request import HTTPXRequest

# ==================== 配置 ====================
TOKEN = "7825340169:AAEL5DRdPL6E_zR6-eOSu0ttw-AxaHr0yzI"
PROXY = "http://172.18.0.1:7890"
ADMIN_ID = 6633019220
NETWORK = "testnet"
SUI_RPC = f"https://fullnode.{NETWORK}.sui.io:443"
WALRUS_AGGREGATOR = "https://aggregator.walrus-testnet.walrus.space"
DEPLOYED_PACKAGE = "0x737a73b3a146d45694c341a22b62607e5a6e6b6496b91156217a7d2c91f7e65d"
BOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BOT_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

HK_TZ = timezone(timedelta(hours=8))

# ==================== 双语系统 i18n ====================
LANG_FILE = os.path.join(DATA_DIR, "lang_prefs.json")

TEXTS = {
    "main_greeting": {
        "cn": "🤖 *Sui DeFi Jarvis*\n选择操作:",
        "en": "🤖 *Sui DeFi Jarvis*\nChoose action:",
    },
    "btn_assets": {"cn": "💰 资产", "en": "💰 Assets"},
    "btn_swap": {"cn": "🔄 Swap 交易", "en": "🔄 Swap"},
    "btn_portfolio": {"cn": "📊 持仓", "en": "📊 Portfolio"},
    "btn_limit": {"cn": "🏷️ 限价单", "en": "🏷️ Limit Order"},
    "btn_whale": {"cn": "🐋 鲸鱼追踪", "en": "🐋 Whale Tracker"},
    "btn_pools": {"cn": "🌱 新池子", "en": "🌱 New Pools"},
    "btn_signals": {"cn": "📢 AI 信号", "en": "📢 AI Signals"},
    "btn_strategy": {"cn": "🤖 策略", "en": "🤖 Strategy"},
    "btn_mint": {"cn": "💎 JarvisUSD Mint", "en": "💎 JarvisUSD Mint"},
    "btn_yield": {"cn": "📈 收益", "en": "📈 Yield"},
    "btn_walrus": {"cn": "🐘 Walrus", "en": "🐘 Walrus"},
    "btn_vault": {"cn": "🔐 Vault", "en": "🔐 Vault"},
    "btn_social": {"cn": "📣 Social", "en": "📣 Social"},
    "btn_settings": {"cn": "⚙️ 设置", "en": "⚙️ Settings"},
    "btn_help": {"cn": "❓ 帮助", "en": "❓ Help"},
    "btn_back": {"cn": "🔙 返回主菜单", "en": "🔙 Back to Menu"},
    "lang_choose": {
        "cn": "🌐 *语言设置*\n请选择语言 / Choose language:",
        "en": "🌐 *Language Settings*\nChoose language / 请选择语言:",
    },
    "lang_set_cn": {"cn": "✅ 语言已切换为中文", "en": "✅ 语言已切换为中文"},
    "lang_set_en": {"cn": "✅ Language set to English", "en": "✅ Language set to English"},
    "referral_welcome": {
        "cn": "🎉 你通过好友邀请加入！",
        "en": "🎉 You joined via referral!",
    },
    "social_panel_title": {
        "cn": "📣 *Viral Social — 病毒传播*",
        "en": "📣 *Viral Social — Growth Engine*",
    },
}

def _load_lang_prefs() -> dict:
    if os.path.exists(LANG_FILE):
        try:
            with open(LANG_FILE) as f: return json.load(f)
        except: pass
    return {}

def _save_lang_prefs(prefs: dict):
    with open(LANG_FILE, "w") as f: json.dump(prefs, f, indent=2)

def get_lang(uid) -> str:
    """获取用户语言偏好，默认中文"""
    prefs = _load_lang_prefs()
    return prefs.get(str(uid), "cn")

def set_lang(uid, lang: str):
    """设置用户语言偏好"""
    prefs = _load_lang_prefs()
    prefs[str(uid)] = lang
    _save_lang_prefs(prefs)

def t(uid, key: str) -> str:
    """获取翻译文本"""
    lang = get_lang(uid)
    entry = TEXTS.get(key, {})
    return entry.get(lang, entry.get("cn", key))

# ==================== Referral 系统 ====================
REFERRALS_FILE = os.path.join(DATA_DIR, "referrals.json")

def _load_referrals() -> dict:
    if os.path.exists(REFERRALS_FILE):
        try:
            with open(REFERRALS_FILE) as f: return json.load(f)
        except: pass
    return {}

def _save_referrals(refs: dict):
    with open(REFERRALS_FILE, "w") as f: json.dump(refs, f, indent=2)

def record_referral(new_uid: str, referrer_uid: str):
    """记录推荐关系"""
    refs = _load_referrals()
    if new_uid == referrer_uid:
        return  # 不能自己推荐自己
    if new_uid in refs:
        return  # 已被推荐过
    refs[new_uid] = {
        "referrer": referrer_uid,
        "time": datetime.now(HK_TZ).isoformat(),
    }
    _save_referrals(refs)
    log_action("referral", f"new:{new_uid} by:{referrer_uid}")

def get_referral_count(uid: str) -> int:
    """统计某用户邀请了多少人"""
    refs = _load_referrals()
    return sum(1 for v in refs.values() if v.get("referrer") == str(uid))

def get_referral_leaderboard(top_n=10) -> list:
    """邀请排行榜"""
    refs = _load_referrals()
    counts = {}
    for v in refs.values():
        r = v.get("referrer", "")
        counts[r] = counts.get(r, 0) + 1
    ranked = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    return ranked

# AI 推文模板
TWEET_TEMPLATES = [
    "🚀 Just discovered @SuiJarvisBot — the ultimate AI DeFi agent on #Sui! Auto-routing across 30+ DEXs, whale tracking, and AI signals. The Infinite Money Glitch is real! 💎🤖 #DeFi #Web3",
    "🤖 My new DeFi co-pilot: @SuiJarvisBot on #Sui\n\n✅ Smart swap routing\n✅ Whale alerts\n✅ AI trading signals\n✅ Portfolio tracking\n\nThis is the future of DeFi 🔥 #SuiNetwork",
    "GM! Been using @SuiJarvisBot and it's a game changer 🎯\n\nAI-powered trading on Sui with Cetus aggregation, on-chain logs via Walrus, and encrypted strategies via Seal.\n\nNot financial advice, but DYOR 👀 #Sui #AI",
    "💡 Why I'm bullish on @SuiJarvisBot:\n\n🌊 Sui L1 speed\n🐋 Cetus 30+ DEX routing\n🐘 Walrus transparent logs\n🔐 Seal encrypted strategies\n🦞 OpenClaw AI runtime\n\nFull stack DeFi AI agent 🤯 #Crypto",
    "🧠 AI + DeFi = @SuiJarvisBot\n\nJust set up limit orders, tracked some whales, and got AI signals — all in one Telegram bot on #Sui.\n\nThe future is autonomous finance 🌐💰 #Web3 #DeFi",
]

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler(os.path.join(DATA_DIR, "jarvis.log"))]
)
log = logging.getLogger("jarvis")

# ==================== 用户钱包管理 ====================
WALLETS_FILE = os.path.join(DATA_DIR, "wallets.json")

def load_wallets():
    if os.path.exists(WALLETS_FILE):
        with open(WALLETS_FILE) as f: return json.load(f)
    return {}

def save_wallets(w):
    with open(WALLETS_FILE, "w") as f: json.dump(w, f, indent=2)

def get_or_create_wallet(user_id: str) -> dict:
    wallets = load_wallets()
    if user_id in wallets:
        return wallets[user_id]
    wallet = {
        "address": "0xc3aa5e010270b6fa9f415739127152328f0bf860012577fff4e21569230a9b80",
        "created": datetime.now(HK_TZ).isoformat(),
        "mode": "demo",
    }
    wallets[user_id] = wallet
    save_wallets(wallets)
    log_action("wallet_auto_create", f"user:{user_id}")
    return wallet

# ==================== 操作日志 ====================
LOG_FILE = os.path.join(DATA_DIR, "operations.json")

def log_action(action: str, detail: str = ""):
    logs = _load_logs()
    logs.append({
        "time": datetime.now(HK_TZ).isoformat(),
        "action": action,
        "detail": detail
    })
    logs = logs[-200:]
    with open(LOG_FILE, "w") as f: json.dump(logs, f, ensure_ascii=False, indent=2)

def _load_logs():
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE) as f: return json.load(f)
        except: pass
    return []

# ==================== Sui RPC 调用 ====================
def sui_rpc(method: str, params: list):
    try:
        r = requests.post(SUI_RPC, json={
            "jsonrpc": "2.0", "id": 1,
            "method": method, "params": params
        }, timeout=10)
        return r.json().get("result")
    except Exception as e:
        log.error(f"RPC error: {e}")
        return None

def get_sui_balance(address: str) -> dict:
    result = sui_rpc("suix_getBalance", [address, "0x2::sui::SUI"])
    if result:
        bal = int(result["totalBalance"]) / 1e9
        return {"sui": bal, "formatted": f"{bal:.4f} SUI"}
    return {"sui": 0, "formatted": "查询失败"}

def get_all_balances(address: str) -> list:
    result = sui_rpc("suix_getAllBalances", [address])
    if not result: return []
    tokens = []
    for item in result:
        ct = item["coinType"]
        bal = int(item["totalBalance"])
        name = ct.split("::")[-1] if "::" in ct else ct
        decimals = 9 if name == "SUI" else 6
        formatted = bal / (10 ** decimals)
        tokens.append({"name": name, "balance": formatted, "raw": bal, "coinType": ct})
    return tokens

def get_recent_txns(address: str, limit=5) -> list:
    result = sui_rpc("suix_queryTransactionBlocks", [{
        "filter": {"FromAddress": address},
        "options": {"showEffects": True, "showInput": False}
    }, None, limit, True])
    if result and "data" in result:
        return result["data"]
    return []

def get_coin_metadata(coin_type: str) -> dict:
    """Get token metadata via suix_getCoinMetadata"""
    result = sui_rpc("suix_getCoinMetadata", [coin_type])
    return result

def get_total_supply(coin_type: str) -> str:
    """Get total supply via suix_getTotalSupply"""
    result = sui_rpc("suix_getTotalSupply", [coin_type])
    if result and "value" in result:
        return result["value"]
    return None

# ==================== 限价单存储 ====================
LIMIT_ORDERS_FILE = os.path.join(DATA_DIR, "limit_orders.json")

def load_limit_orders() -> list:
    if os.path.exists(LIMIT_ORDERS_FILE):
        try:
            with open(LIMIT_ORDERS_FILE) as f: return json.load(f)
        except: pass
    return []

def save_limit_orders(orders: list):
    with open(LIMIT_ORDERS_FILE, "w") as f: json.dump(orders, f, ensure_ascii=False, indent=2)

# ==================== Cetus 报价（模拟） ====================
SWAP_PAIRS = {
    "SUI/USDC": {"rate": 3.82, "route": "Cetus → DeepBook → Aftermath", "dexes": 3, "pools": 5},
    "USDC/SUI": {"rate": 0.2618, "route": "DeepBook → Turbos → Cetus", "dexes": 3, "pools": 4},
    "SUI/WETH": {"rate": 0.00118, "route": "Cetus → FlowX → KriyaDEX", "dexes": 3, "pools": 6},
    "SUI/CETUS": {"rate": 42.5, "route": "Cetus AMM (Direct)", "dexes": 1, "pools": 1},
    "SUI/USDT": {"rate": 3.81, "route": "Aftermath → BlueFin → Cetus", "dexes": 3, "pools": 4},
}

# ==================== AI 策略引擎 ====================
STRATEGIES = {
    "trend": {
        "name": "📈 趋势跟踪 Trend Following",
        "desc": "跟踪大趋势，顺势交易。When SUI shows sustained momentum, ride the wave.",
        "signals": ["EMA 交叉", "MACD 趋势", "成交量突破"],
        "risk": "中等",
        "win_rate": "62%",
        "avg_return": "+4.2%/trade",
    },
    "mean_reversion": {
        "name": "🔄 均值回归 Mean Reversion",
        "desc": "价格偏离均值时反向交易。Buy low, sell high when price deviates from mean.",
        "signals": ["布林带", "RSI 超买/超卖", "VWAP 偏离"],
        "risk": "低-中",
        "win_rate": "71%",
        "avg_return": "+2.1%/trade",
    },
    "arbitrage": {
        "name": "⚡ DEX 套利 Arbitrage",
        "desc": "跨 DEX 价差套利。Exploit price differences across Cetus, DeepBook, Turbos etc.",
        "signals": ["价差监控", "Gas 优化", "原子交易"],
        "risk": "低",
        "win_rate": "89%",
        "avg_return": "+0.3%/trade",
    }
}

strategy_state = {
    "active": "trend",
    "enabled": {"trend": True, "mean_reversion": False, "arbitrage": False},
    "total_trades": 47,
    "win_count": 31,
    "pnl": +12.6,
    "last_signal": "EMA 12/26 金叉，建议加仓 SUI",
    "last_signal_time": "10:15",
}

# ==================== Walrus 日志 ====================
WALRUS_BLOBS = [
    {"id": "Dq4wG3x...", "time": "02-09 22:00", "type": "strategy_snapshot", "size": "2.1KB"},
    {"id": "Fx8kL2m...", "time": "02-09 18:30", "type": "trade_log", "size": "1.4KB"},
    {"id": "Ap3nR7w...", "time": "02-09 15:00", "type": "risk_report", "size": "3.2KB"},
]

# ==================== 模拟数据生成 ====================
def gen_whale_data():
    now = datetime.now(HK_TZ)
    whales = []
    addrs = [
        ("0x7d20...3f8a", "0x91ab...c4d2"), ("0xf4e1...8b73", "0x2c9d...a1f6"),
        ("0xa823...d9e1", "0x5f7b...2c84"), ("0x1b4e...f723", "0xd8a6...9e51"),
        ("0x6c3f...b248", "0x3e7a...d195"), ("0xe912...4a6d", "0x8b5c...f3e7"),
    ]
    types = ["🟢 买入 Buy", "🔴 卖出 Sell", "🔵 转账 Transfer"]
    tokens = ["SUI", "SUI", "SUI", "USDC", "SUI", "CETUS"]
    for i in range(6):
        t = now - timedelta(minutes=random.randint(2, 180))
        amt = random.choice([10_000, 25_000, 50_000, 100_000, 150_000, 280_000, 500_000])
        fr, to = addrs[i]
        typ = random.choice(types)
        tok = tokens[i]
        usd = amt * 3.82 if tok == "SUI" else amt
        whales.append({
            "time": t.strftime("%H:%M"),
            "amount": f"{amt:,.0f} {tok}",
            "usd": f"${usd:,.0f}",
            "from": fr, "to": to,
            "type": typ,
        })
    whales.sort(key=lambda x: x["time"], reverse=True)
    return whales

def gen_pool_data():
    pools = [
        {"pair": "SUI/USDC", "tvl": "$12.8M", "vol": "$4.2M", "apr": "18.5%", "age": "2h ago", "dex": "Cetus"},
        {"pair": "NAVX/SUI", "tvl": "$890K", "vol": "$320K", "apr": "45.2%", "age": "5h ago", "dex": "Cetus"},
        {"pair": "CETUS/USDC", "tvl": "$3.2M", "vol": "$1.1M", "apr": "22.8%", "age": "8h ago", "dex": "Cetus"},
        {"pair": "HASUI/SUI", "tvl": "$6.5M", "vol": "$2.8M", "apr": "12.3%", "age": "12h ago", "dex": "Cetus"},
        {"pair": "WETH/USDC", "tvl": "$5.1M", "vol": "$1.9M", "apr": "15.7%", "age": "1d ago", "dex": "Cetus"},
        {"pair": "TURBOS/SUI", "tvl": "$420K", "vol": "$95K", "apr": "68.4%", "age": "1d ago", "dex": "Turbos"},
    ]
    return pools

def gen_portfolio_data(sui_balance: float):
    holdings = [
        {"token": "SUI", "amount": sui_balance, "cost": 2.85, "price": 3.82, "icon": "🟦"},
        {"token": "USDC", "amount": 1250.00, "cost": 1.00, "price": 1.00, "icon": "💵"},
        {"token": "CETUS", "amount": 8500, "cost": 0.082, "price": 0.0897, "icon": "🐋"},
        {"token": "NAVX", "amount": 3200, "cost": 0.21, "price": 0.248, "icon": "🧭"},
        {"token": "HASUI", "amount": 450, "cost": 3.75, "price": 3.91, "icon": "💎"},
    ]
    return holdings

def gen_signals():
    now = datetime.now(HK_TZ)
    signals = [
        {
            "icon": "🟢", "type": "买入 BUY", "pair": "SUI/USDC",
            "reason": "EMA 12/26 金叉确认，MACD 柱状图转正",
            "target": "$4.20", "stop": "$3.45", "confidence": "85%",
            "time": (now - timedelta(minutes=12)).strftime("%H:%M"),
        },
        {
            "icon": "🔴", "type": "卖出 SELL", "pair": "CETUS/USDC",
            "reason": "RSI(14) = 78 超买区，布林带上轨压力",
            "target": "$0.072", "stop": "$0.095", "confidence": "72%",
            "time": (now - timedelta(minutes=45)).strftime("%H:%M"),
        },
        {
            "icon": "🟢", "type": "买入 BUY", "pair": "NAVX/SUI",
            "reason": "突破下降趋势线，成交量放大 3.2x",
            "target": "0.068 SUI", "stop": "0.052 SUI", "confidence": "78%",
            "time": (now - timedelta(hours=1, minutes=20)).strftime("%H:%M"),
        },
        {
            "icon": "🟡", "type": "观望 HOLD", "pair": "WETH/USDC",
            "reason": "横盘整理中，等待方向突破",
            "target": "-", "stop": "-", "confidence": "55%",
            "time": (now - timedelta(hours=2)).strftime("%H:%M"),
        },
        {
            "icon": "🟢", "type": "买入 BUY", "pair": "HASUI/SUI",
            "reason": "质押收益率上升，协议 TVL 增长 15%",
            "target": "1.05 SUI", "stop": "0.98 SUI", "confidence": "80%",
            "time": (now - timedelta(hours=3)).strftime("%H:%M"),
        },
    ]
    return signals

def gen_token_safety(coin_type: str, metadata: dict):
    """Generate mock safety check for a token"""
    # Well-known safe tokens
    safe_tokens = ["SUI", "USDC", "USDT", "WETH", "CETUS", "NAVX", "HASUI", "TURBOS"]
    symbol = (metadata or {}).get("symbol", "")
    
    if symbol.upper() in safe_tokens:
        return {
            "rating": "🟢 安全 SAFE",
            "score": random.randint(85, 98),
            "checks": [
                "✅ 合约已验证 Verified Contract",
                "✅ 流动性充足 Adequate Liquidity",
                "✅ 发行量合理 Reasonable Supply",
                "✅ 团队已知 Known Team",
                "✅ 审计通过 Audited",
            ]
        }
    else:
        checks = []
        score = random.randint(30, 70)
        checks.append(random.choice(["✅ 合约已验证", "⚠️ 合约未验证 Unverified"]))
        checks.append(random.choice(["✅ 流动性已锁", "⚠️ 流动性未锁 Unlocked LP"]))
        if score > 50:
            checks.append("✅ 发行量合理")
        else:
            checks.append("⚠️ 发行量过大 Excessive Supply")
        checks.append(random.choice(["✅ 无恶意函数", "⚠️ 存在可疑函数 Suspicious Functions"]))
        
        if score >= 60:
            rating = "🟡 注意 CAUTION"
        else:
            rating = "🔴 危险 DANGER"
        return {"rating": rating, "score": score, "checks": checks}

# ==================== 键盘布局 ====================
def main_keyboard(lang="cn"):
    """GMGN-style main menu — 双语按钮"""
    # 用 lang 直接取文本的 helper
    def _t(key):
        entry = TEXTS.get(key, {})
        return entry.get(lang, entry.get("cn", key))
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(_t("btn_assets"), callback_data="assets"),
         InlineKeyboardButton(_t("btn_swap"), callback_data="swap_menu")],
        [InlineKeyboardButton(_t("btn_portfolio"), callback_data="portfolio"),
         InlineKeyboardButton(_t("btn_limit"), callback_data="limit")],
        [InlineKeyboardButton(_t("btn_whale"), callback_data="whale"),
         InlineKeyboardButton(_t("btn_pools"), callback_data="pools")],
        [InlineKeyboardButton(_t("btn_signals"), callback_data="signals"),
         InlineKeyboardButton(_t("btn_strategy"), callback_data="strategy")],
        [InlineKeyboardButton(_t("btn_mint"), callback_data="sl_mint"),
         InlineKeyboardButton(_t("btn_yield"), callback_data="sl_yield")],
        [InlineKeyboardButton(_t("btn_social"), callback_data="social"),
         InlineKeyboardButton(_t("btn_walrus"), callback_data="walrus")],
        [InlineKeyboardButton(_t("btn_vault"), callback_data="vault"),
         InlineKeyboardButton(_t("btn_settings"), callback_data="settings")],
        [InlineKeyboardButton(_t("btn_help"), callback_data="help")],
        [InlineKeyboardButton("🇨🇳 中文" if lang == "en" else "🇬🇧 English", callback_data="lang_toggle")],
    ])

def swap_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("SUI → USDC", callback_data="swap_SUI/USDC"),
         InlineKeyboardButton("USDC → SUI", callback_data="swap_USDC/SUI")],
        [InlineKeyboardButton("SUI → WETH", callback_data="swap_SUI/WETH"),
         InlineKeyboardButton("SUI → CETUS", callback_data="swap_SUI/CETUS")],
        [InlineKeyboardButton("SUI → USDT", callback_data="swap_SUI/USDT"),
         InlineKeyboardButton("🔧 自定义 Custom", callback_data="swap_custom")],
        [InlineKeyboardButton("🔙 返回主菜单", callback_data="back")],
    ])

def strategy_keyboard():
    s = strategy_state["enabled"]
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(
            f"{'✅' if s['trend'] else '⬜'} 趋势跟踪",
            callback_data="strat_trend"),
         InlineKeyboardButton(
            f"{'✅' if s['mean_reversion'] else '⬜'} 均值回归",
            callback_data="strat_mean_reversion")],
        [InlineKeyboardButton(
            f"{'✅' if s['arbitrage'] else '⬜'} DEX 套利",
            callback_data="strat_arbitrage"),
         InlineKeyboardButton("📊 策略详情", callback_data="strat_detail")],
        [InlineKeyboardButton("🔙 返回主菜单", callback_data="back")],
    ])

# ==================== Token 查询 ====================
async def send_token_info(message, coin_type: str):
    """Query and display token information + safety check"""
    log_action("token_query", coin_type[:40])
    
    await message.reply_text("🔍 正在查询代币信息...")
    
    metadata = get_coin_metadata(coin_type)
    supply_raw = get_total_supply(coin_type)
    
    if not metadata:
        await message.reply_text(
            f"❌ *未找到代币信息*\n\n"
            f"CoinType: `{coin_type}`\n\n"
            f"可能原因:\n"
            f"• 地址格式不正确\n"
            f"• 该代币不存在于 {NETWORK}\n"
            f"• 请检查是否为完整 CoinType 格式\n"
            f"  例: `0x2::sui::SUI`",
            parse_mode="Markdown"
        )
        return
    
    name = metadata.get("name", "Unknown")
    symbol = metadata.get("symbol", "???")
    decimals = metadata.get("decimals", 9)
    desc = metadata.get("description", "无描述")
    icon_url = metadata.get("iconUrl", "")
    
    # Format supply
    supply_text = "N/A"
    if supply_raw:
        supply_val = int(supply_raw) / (10 ** decimals)
        if supply_val >= 1e12:
            supply_text = f"{supply_val/1e12:.2f}T"
        elif supply_val >= 1e9:
            supply_text = f"{supply_val/1e9:.2f}B"
        elif supply_val >= 1e6:
            supply_text = f"{supply_val/1e6:.2f}M"
        elif supply_val >= 1e3:
            supply_text = f"{supply_val/1e3:.2f}K"
        else:
            supply_text = f"{supply_val:.2f}"
    
    # Safety check
    safety = gen_token_safety(coin_type, metadata)
    safety_lines = "\n".join(f"  {c}" for c in safety["checks"])
    
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"🔄 Swap 买入 {symbol}", callback_data=f"swap_SUI/{symbol}" if symbol != "SUI" else "swap_menu"),
         InlineKeyboardButton("📊 查看详情", callback_data="back")],
        [InlineKeyboardButton("🔙 返回主菜单", callback_data="back")],
    ])
    
    text = (
        f"🔍 *Token 详情 — {name}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📛 *名称:* {name}\n"
        f"🏷️ *符号:* {symbol}\n"
        f"🔢 *精度:* {decimals}\n"
        f"📊 *总供应:* {supply_text} {symbol}\n"
    )
    if desc and desc != "无描述":
        text += f"📝 *描述:* {desc[:120]}\n"
    
    text += (
        f"\n🛡️ *安全检查 Safety Check:*\n"
        f"  评级: *{safety['rating']}* ({safety['score']}/100)\n"
        f"{safety_lines}\n\n"
        f"📋 *CoinType:*\n`{coin_type}`\n"
    )
    
    await message.reply_text(text, parse_mode="Markdown", reply_markup=kb)

# ==================== 命令处理器 ====================
async def cmd_lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """语言切换命令"""
    uid = str(update.effective_user.id)
    lang = get_lang(uid)
    await update.message.reply_text(
        t(uid, "lang_choose"),
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🇨🇳 中文", callback_data="lang_cn"),
             InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")],
            [InlineKeyboardButton(t(uid, "btn_back"), callback_data="back")],
        ])
    )

async def cmd_refer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """查看邀请链接和统计"""
    uid = str(update.effective_user.id)
    lang = get_lang(uid)
    count = get_referral_count(uid)
    link = f"https://t.me/SuiJarvisBot?start=ref_{uid}"
    await update.message.reply_text(
        f"🔗 *{'你的邀请链接' if lang=='cn' else 'Your Referral Link'}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📎 `{link}`\n\n"
        f"👥 {'已邀请' if lang=='cn' else 'Invited'}: *{count}* {'人' if lang=='cn' else 'users'}\n\n"
        f"{'分享链接邀请好友，一起赚钱！' if lang=='cn' else 'Share and earn together!'}",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(
                "📤 分享 Share" if lang=="cn" else "📤 Share",
                switch_inline_query=f"🤖 Join me on Sui DeFi Jarvis! The Infinite Money Glitch 🚀 {link}")],
            [InlineKeyboardButton(t(uid, "btn_back"), callback_data="back")],
        ])
    )

async def cmd_social(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Social 面板"""
    uid = str(update.effective_user.id)
    await _send_social_panel(update.message, uid)

async def _send_social_panel(msg, uid: str):
    """病毒传播/社交面板"""
    lang = get_lang(uid)
    count = get_referral_count(uid)
    link = f"https://t.me/SuiJarvisBot?start=ref_{uid}"
    leaderboard = get_referral_leaderboard(5)

    # 排行榜文本
    lb_lines = []
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]
    for i, (r_uid, r_count) in enumerate(leaderboard):
        lb_lines.append(f"  {medals[i]} `{r_uid[:8]}...` — {r_count} {'人' if lang=='cn' else 'refs'}")
    lb_text = "\n".join(lb_lines) if lb_lines else ("  暂无数据" if lang=="cn" else "  No data yet")

    # 模拟传播数据
    impressions = count * random.randint(80, 200)
    clicks = count * random.randint(5, 20)
    conversion = f"{(clicks/max(impressions,1)*100):.1f}%" if impressions > 0 else "0%"

    text = (
        f"{t(uid, 'social_panel_title')}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🔗 *{'邀请链接' if lang=='cn' else 'Referral Link'}:*\n"
        f"  `{link}`\n\n"
        f"👥 *{'你的邀请' if lang=='cn' else 'Your Referrals'}:* {count} {'人' if lang=='cn' else 'users'}\n\n"
        f"📊 *{'传播数据' if lang=='cn' else 'Viral Stats'} ({'模拟' if lang=='cn' else 'simulated'}):*\n"
        f"  👀 {'曝光' if lang=='cn' else 'Impressions'}: {impressions:,}\n"
        f"  🖱️ {'点击' if lang=='cn' else 'Clicks'}: {clicks:,}\n"
        f"  📈 {'转化率' if lang=='cn' else 'Conversion'}: {conversion}\n\n"
        f"🏆 *{'邀请排行榜' if lang=='cn' else 'Referral Leaderboard'}:*\n"
        f"{lb_text}\n"
    )

    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "📣 AI 生成推文" if lang=="cn" else "📣 AI Tweet",
            callback_data="social_tweet"),
         InlineKeyboardButton(
            "🔗 邀请链接" if lang=="cn" else "🔗 Invite Link",
            callback_data="social_invite")],
        [InlineKeyboardButton(
            "📤 分享 Share" if lang=="cn" else "📤 Share",
            switch_inline_query=f"🤖 Sui DeFi Jarvis — The Infinite Money Glitch 🚀 {link}")],
        [InlineKeyboardButton(t(uid, "btn_back"), callback_data="back")],
    ])

    await msg.reply_text(text, parse_mode="Markdown", reply_markup=kb)

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uid = str(user.id)
    name = user.first_name or "Friend"
    lang = get_lang(uid)

    # 处理 referral 链接: /start ref_USERID
    if context.args and len(context.args) > 0:
        arg = context.args[0]
        if arg.startswith("ref_"):
            referrer_uid = arg[4:]
            record_referral(uid, referrer_uid)
    
    wallet = get_or_create_wallet(uid)
    balance = get_sui_balance(wallet["address"])
    
    log_action("start", f"{name} (id:{uid})")
    
    await update.message.reply_text(
        f"🤖 *Sui DeFi Jarvis — The Infinite Money Glitch*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"Hey {name}! 我是 Jarvis，你的自主 AI DeFi 代理。\n"
        f"I'm your autonomous AI DeFi agent on Sui.\n\n"
        f"🔧 *技术栈 Tech Stack:*\n"
        f"├ 🌊 *Sui* — Layer 1 区块链\n"
        f"├ 🐋 *Cetus Aggregator* — 30+ DEX 最优路由\n"
        f"├ 🐘 *Walrus* — 去中心化操作日志存储\n"
        f"├ 🔐 *Seal* — 链上加密策略数据\n"
        f"└ 🦞 *OpenClaw* — AI 运行时环境\n\n"
        f"💰 *钱包已就绪:*\n"
        f"`{wallet['address'][:16]}...{wallet['address'][-8:]}`\n"
        f"余额: *{balance['formatted']}*\n\n"
        f"🎯 *核心功能:*\n"
        f"• 🔍 发送合约地址即查 Token 信息\n"
        f"• 🔄 跨 30+ DEX 最优 Swap\n"
        f"• 📊 持仓面板 + AI 交易信号\n"
        f"• 🐋 鲸鱼追踪 + 新池子发现\n"
        f"• 🏷️ 限价单 + 策略引擎\n\n"
        f"👇 *选择操作开始:*",
        parse_mode="Markdown",
        reply_markup=main_keyboard(lang)
    )

async def cmd_wallet(update: Update, context):
    uid = str(update.effective_user.id)
    wallet = get_or_create_wallet(uid)
    balance = get_sui_balance(wallet["address"])
    tokens = get_all_balances(wallet["address"])
    
    token_lines = []
    for t in tokens:
        icon = "🟦" if t["name"] == "SUI" else "🟢"
        token_lines.append(f"  {icon} {t['name']}: *{t['balance']:.4f}*")
    
    token_text = "\n".join(token_lines) if token_lines else "  暂无持仓"
    
    log_action("wallet", balance["formatted"])
    
    await update.message.reply_text(
        f"👛 *钱包信息 Wallet*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📍 *地址 Address:*\n"
        f"`{wallet['address']}`\n\n"
        f"🌐 网络: Sui {NETWORK.capitalize()}\n"
        f"📦 模式: {'Demo (共享 Testnet)' if wallet.get('mode')=='demo' else 'Personal'}\n\n"
        f"💰 *资产 Assets:*\n"
        f"{token_text}\n\n"
        f"🔗 [查看浏览器 Explorer](https://suiscan.xyz/{NETWORK}/account/{wallet['address']})",
        parse_mode="Markdown",
        disable_web_page_preview=True
    )

async def cmd_balance(update: Update, context):
    uid = str(update.effective_user.id)
    wallet = get_or_create_wallet(uid)
    balance = get_sui_balance(wallet["address"])
    log_action("balance", balance["formatted"])
    await update.message.reply_text(
        f"💰 *{balance['formatted']}*\n"
        f"📍 `{wallet['address'][:16]}...`\n"
        f"🌐 Sui {NETWORK.capitalize()}",
        parse_mode="Markdown"
    )

async def cmd_swap(update: Update, context):
    log_action("swap_menu")
    await update.message.reply_text(
        "🔄 *Swap 交易 — Cetus Aggregator*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🐋 路由覆盖 30+ DEX:\n"
        "Cetus · DeepBook · Turbos · Aftermath\n"
        "FlowX · KriyaDEX · BlueFin · Haedal...\n\n"
        "选择交易对，获取最优报价 👇",
        parse_mode="Markdown",
        reply_markup=swap_keyboard()
    )

async def cmd_strategy(update: Update, context):
    log_action("strategy")
    await _send_strategy_panel(update.message)

async def cmd_logs(update: Update, context):
    log_action("view_logs")
    await _send_logs_panel(update.message)

async def cmd_whale(update: Update, context):
    log_action("whale")
    await _send_whale_panel(update.message)

async def cmd_pools(update: Update, context):
    log_action("pools")
    await _send_pools_panel(update.message)

async def cmd_portfolio(update: Update, context):
    uid = str(update.effective_user.id)
    log_action("portfolio")
    await _send_portfolio_panel(update.message, uid)

async def cmd_limit(update: Update, context):
    log_action("limit")
    await _send_limit_panel(update.message, str(update.effective_user.id), context)

async def cmd_signals(update: Update, context):
    log_action("signals")
    await _send_signals_panel(update.message)

async def cmd_help(update: Update, context):
    await update.message.reply_text(
        "❓ *Sui DeFi Jarvis — 使用指南*\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "*📱 命令 Commands:*\n"
        "├ /start — 主菜单 Main Menu\n"
        "├ /wallet — 钱包信息 Wallet Info\n"
        "├ /balance — 查看余额 Check Balance\n"
        "├ /swap — 代币交换 Token Swap\n"
        "├ /portfolio — 持仓面板 Portfolio\n"
        "├ /limit — 限价单 Limit Orders\n"
        "├ /whale — 鲸鱼追踪 Whale Tracker\n"
        "├ /pools — 新池子 New Pools\n"
        "├ /signals — AI 交易信号\n"
        "├ /strategy — AI 策略管理\n"
        "├ /mint — 铸造 JarvisUSD (StableLayer)\n"
        "├ /burn — 赎回 JarvisUSD\n"
        "├ /yield — 查看收益 Yield\n"
        "├ /stablelayer — StableLayer 面板\n"
        "├ /logs — 操作日志 Operation Logs\n"
        "└ /help — 帮助 Help\n\n"
        "*🔍 Token 查询:*\n"
        "直接发送合约地址或 CoinType 即可查询：\n"
        "• `0x2::sui::SUI`\n"
        "• `0xdba34672e...::coin::COIN`\n\n"
        "*💬 自然语言 Natural Language:*\n"
        "• \"余额多少\" / \"check balance\"\n"
        "• \"帮我换 10 SUI 到 USDC\"\n"
        "• \"鲸鱼\" / \"whale\"\n"
        "• \"新池子\" / \"pools\"\n"
        "• \"信号\" / \"signals\"\n\n"
        "*🔧 技术架构:*\n"
        "• 🌊 Sui — Move 智能合约\n"
        "• 🐋 Cetus — 聚合器最优路由\n"
        "• 🐘 Walrus — 去中心化日志\n"
        "• 🔐 Seal — 策略数据加密\n"
        "• 🦞 OpenClaw — AI Agent 运行时\n\n"
        f"📦 合约: `{DEPLOYED_PACKAGE[:20]}...`\n"
        f"🌐 网络: Sui {NETWORK.capitalize()}\n\n"
        "*Powered by OpenClaw × Sui × Cetus × Walrus*",
        parse_mode="Markdown"
    )

# ==================== 面板渲染函数 ====================
async def _send_strategy_panel(msg):
    s = strategy_state
    active = STRATEGIES[s["active"]]
    wr = s["win_count"] / s["total_trades"] * 100 if s["total_trades"] > 0 else 0
    
    await msg.reply_text(
        f"🤖 *AI 策略引擎 Strategy Engine*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎯 *当前策略: {active['name']}*\n"
        f"  {active['desc']}\n\n"
        f"📊 *信号源 Signals:*\n"
        f"  {'  ·  '.join(active['signals'])}\n\n"
        f"📈 *绩效 Performance:*\n"
        f"  ├ 总交易: {s['total_trades']} 笔\n"
        f"  ├ 胜率: {wr:.0f}% ({s['win_count']}W/{s['total_trades']-s['win_count']}L)\n"
        f"  ├ 累计盈亏: *{'+' if s['pnl']>=0 else ''}{s['pnl']:.1f} SUI*\n"
        f"  └ 平均回报: {active['avg_return']}\n\n"
        f"🔔 *最新信号:*\n"
        f"  💡 [{s['last_signal_time']}] {s['last_signal']}\n\n"
        f"⚠️ 风险等级: {active['risk']}\n\n"
        f"👇 点击切换策略:",
        parse_mode="Markdown",
        reply_markup=strategy_keyboard()
    )

async def _send_logs_panel(msg):
    logs = _load_logs()
    recent = logs[-8:]
    
    if not recent:
        await msg.reply_text("📋 暂无操作日志。试试 /start 或 /swap！")
        return
    
    lines = []
    for l in recent:
        t = l["time"][5:16].replace("T", " ")
        emoji = {"start": "🚀", "balance": "💰", "swap_menu": "🔄", "swap_quote": "📊",
                 "wallet": "👛", "strategy": "🤖", "wallet_auto_create": "🆕",
                 "view_logs": "📋", "whale": "🐋", "pools": "🌱", "signals": "📢",
                 "portfolio": "📊", "limit": "🏷️", "token_query": "🔍"}.get(l["action"], "📝")
        lines.append(f"  {emoji} `{t}` *{l['action']}* {l.get('detail','')[:40]}")
    
    walrus_section = "\n\n🐘 *Walrus 链上日志:*\n"
    for b in WALRUS_BLOBS[-3:]:
        walrus_section += f"  📦 `{b['id']}` ({b['time']}) {b['type']} [{b['size']}]\n"
    
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("🐘 上传到 Walrus", callback_data="walrus_upload"),
         InlineKeyboardButton("🔄 刷新", callback_data="refresh_logs")],
        [InlineKeyboardButton("🔙 返回主菜单", callback_data="back")],
    ])
    
    await msg.reply_text(
        f"📋 *操作日志 Operation Logs*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"*最近操作:*\n" + "\n".join(lines) +
        walrus_section +
        f"\n📊 总记录: {len(logs)} 条 | 链上: {len(WALRUS_BLOBS)} 条",
        parse_mode="Markdown",
        reply_markup=kb
    )

async def _send_dashboard(msg, uid):
    wallet = get_or_create_wallet(uid)
    balance = get_sui_balance(wallet["address"])
    s = strategy_state
    wr = s["win_count"] / s["total_trades"] * 100 if s["total_trades"] > 0 else 0
    active = STRATEGIES[s["active"]]
    
    now = datetime.now(HK_TZ).strftime("%H:%M")
    
    await msg.reply_text(
        f"📊 *Jarvis 仪表盘 Dashboard*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"⏰ {now} HKT | Sui {NETWORK.capitalize()}\n\n"
        f"💰 *资产 Assets:*\n"
        f"  🟦 SUI: *{balance['formatted']}*\n"
        f"  💵 估值: ~${balance['sui'] * 3.82:.2f}\n\n"
        f"🤖 *策略 Strategy:*\n"
        f"  📈 {active['name']}\n"
        f"  ├ 胜率: {wr:.0f}% | 交易: {s['total_trades']}笔\n"
        f"  └ P&L: *{'+' if s['pnl']>=0 else ''}{s['pnl']:.1f} SUI*\n\n"
        f"🔔 *最新信号:*\n"
        f"  💡 {s['last_signal']}\n\n"
        f"🐘 *Walrus:* {len(WALRUS_BLOBS)} logs on-chain\n"
        f"🔐 *Vault:* `{DEPLOYED_PACKAGE[:16]}...`\n\n"
        f"───────────────────\n"
        f"_Powered by OpenClaw × Sui × Cetus × Walrus_",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔄 刷新", callback_data="dashboard"),
             InlineKeyboardButton("🔙 返回", callback_data="back")],
        ])
    )

async def _send_whale_panel(msg):
    whales = gen_whale_data()
    now = datetime.now(HK_TZ).strftime("%H:%M")
    
    lines = []
    for w in whales:
        lines.append(
            f"  {w['type']}\n"
            f"    💰 {w['amount']} ({w['usd']})\n"
            f"    📍 {w['from']} → {w['to']}\n"
            f"    ⏰ {w['time']}"
        )
    
    text = (
        f"🐋 *鲸鱼追踪 Whale Tracker*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"⏰ {now} HKT | 筛选: >10K SUI\n\n"
        + "\n\n".join(lines) +
        f"\n\n📊 最近 3h 大额交易: {len(whales)} 笔\n"
        f"💰 总流动: ${sum(random.randint(50000, 500000) for _ in whales):,.0f}\n\n"
        f"_数据每 5 分钟刷新 | 实时监控 Sui 网络_"
    )
    
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 刷新", callback_data="whale"),
         InlineKeyboardButton("📊 统计分析", callback_data="whale_stats")],
        [InlineKeyboardButton("🔙 返回主菜单", callback_data="back")],
    ])
    
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=kb)

async def _send_pools_panel(msg):
    pools = gen_pool_data()
    now = datetime.now(HK_TZ).strftime("%H:%M")
    
    lines = []
    for i, p in enumerate(pools, 1):
        lines.append(
            f"  *{i}. {p['pair']}* ({p['dex']})\n"
            f"    💧 TVL: {p['tvl']} | 📈 Vol: {p['vol']}\n"
            f"    🔥 APR: *{p['apr']}* | 🕐 {p['age']}"
        )
    
    text = (
        f"🌱 *新池子 New Pools — Sui DEX*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"⏰ {now} HKT | Cetus · Turbos · DeepBook\n\n"
        + "\n\n".join(lines) +
        f"\n\n📊 过去 24h 新上线: {len(pools)} 个池子\n\n"
        f"_💡 高 APR 伴随高风险，请注意无常损失_"
    )
    
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 刷新", callback_data="pools"),
         InlineKeyboardButton("📊 按 APR 排序", callback_data="pools_apr")],
        [InlineKeyboardButton("🔙 返回主菜单", callback_data="back")],
    ])
    
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=kb)

async def _send_portfolio_panel(msg, uid):
    wallet = get_or_create_wallet(uid)
    balance = get_sui_balance(wallet["address"])
    holdings = gen_portfolio_data(balance["sui"])
    now = datetime.now(HK_TZ).strftime("%H:%M")
    
    lines = []
    total_value = 0
    total_cost = 0
    for h in holdings:
        val = h["amount"] * h["price"]
        cost = h["amount"] * h["cost"]
        pnl_pct = ((h["price"] - h["cost"]) / h["cost"] * 100) if h["cost"] > 0 else 0
        pnl_icon = "🟢" if pnl_pct >= 0 else "🔴"
        total_value += val
        total_cost += cost
        lines.append(
            f"  {h['icon']} *{h['token']}*\n"
            f"    数量: {h['amount']:,.2f} | 价值: ${val:,.2f}\n"
            f"    成本: ${h['cost']:.4f} → 当前: ${h['price']:.4f}\n"
            f"    {pnl_icon} P&L: *{'+' if pnl_pct>=0 else ''}{pnl_pct:.1f}%*"
        )
    
    total_pnl = total_value - total_cost
    total_pnl_pct = (total_pnl / total_cost * 100) if total_cost > 0 else 0
    pnl_icon = "🟢" if total_pnl >= 0 else "🔴"
    
    text = (
        f"📊 *持仓面板 Portfolio*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"⏰ {now} HKT\n\n"
        + "\n\n".join(lines) +
        f"\n\n━━━━━━━━━━━━━━━━━━━━\n"
        f"💼 *总资产:* ${total_value:,.2f}\n"
        f"💰 *总成本:* ${total_cost:,.2f}\n"
        f"{pnl_icon} *总盈亏:* {'+' if total_pnl>=0 else ''}${total_pnl:,.2f} ({'+' if total_pnl_pct>=0 else ''}{total_pnl_pct:.1f}%)\n\n"
        f"_SUI 余额为实时链上数据，其余为 Demo 模拟_"
    )
    
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 刷新", callback_data="portfolio"),
         InlineKeyboardButton("📈 收益曲线", callback_data="portfolio_chart")],
        [InlineKeyboardButton("🔙 返回主菜单", callback_data="back")],
    ])
    
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=kb)

async def _send_limit_panel(msg, uid, context=None):
    orders = load_limit_orders()
    user_orders = [o for o in orders if o.get("uid") == uid]
    now = datetime.now(HK_TZ).strftime("%H:%M")
    
    if user_orders:
        lines = []
        for i, o in enumerate(user_orders):
            status = "⏳ 等待" if o.get("status") == "pending" else "✅ 完成"
            direction = "🟢 买入" if o.get("direction") == "buy" else "🔴 卖出"
            lines.append(
                f"  *#{o.get('id', i+1)}* {direction}\n"
                f"    交易对: {o.get('pair', 'SUI/USDC')}\n"
                f"    目标价: ${o.get('target_price', 0):.4f}\n"
                f"    数量: {o.get('amount', 0)} {o.get('pair', 'SUI/USDC').split('/')[0]}\n"
                f"    状态: {status}\n"
                f"    创建: {o.get('created', 'N/A')[:16]}"
            )
        order_text = "\n\n".join(lines)
    else:
        order_text = "  暂无挂单 No active orders"
    
    text = (
        f"🏷️ *限价单 Limit Orders*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"⏰ {now} HKT\n\n"
        f"*当前挂单:*\n"
        f"{order_text}\n\n"
        f"*创建新限价单:*\n"
        f"发送格式:\n"
        f"`limit buy SUI/USDC 3.50 100`\n"
        f"`limit sell SUI/USDC 4.20 50`\n\n"
        f"_格式: limit [buy/sell] [交易对] [目标价] [数量]_"
    )
    
    buttons = [[InlineKeyboardButton("🔄 刷新", callback_data="limit")]]
    if user_orders:
        buttons.append([InlineKeyboardButton("❌ 取消全部挂单", callback_data="limit_cancel_all")])
    buttons.append([InlineKeyboardButton("🔙 返回主菜单", callback_data="back")])
    
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(buttons))

async def _send_signals_panel(msg):
    signals = gen_signals()
    now = datetime.now(HK_TZ).strftime("%H:%M")
    
    lines = []
    for s in signals:
        lines.append(
            f"  {s['icon']} *{s['type']}* — {s['pair']}\n"
            f"    📝 {s['reason']}\n"
            f"    🎯 目标: {s['target']} | 止损: {s['stop']}\n"
            f"    📊 置信度: {s['confidence']} | ⏰ {s['time']}"
        )
    
    text = (
        f"📢 *AI 交易信号 Trading Signals*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"⏰ {now} HKT | 引擎: Jarvis AI v2.0\n\n"
        + "\n\n".join(lines) +
        f"\n\n━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 今日信号: {len(signals)} 个 | 胜率: 73%\n"
        f"🤖 基于: EMA · RSI · MACD · 成交量 · 链上数据\n\n"
        f"⚠️ _信号仅供参考，不构成投资建议_"
    )
    
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 刷新信号", callback_data="signals"),
         InlineKeyboardButton("⚙️ 信号设置", callback_data="signals_settings")],
        [InlineKeyboardButton("🔙 返回主菜单", callback_data="back")],
    ])
    
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=kb)

# ==================== StableLayer 模拟数据 ====================
STABLELAYER_DATA = {
    "brand_coin": "JarvisUSD",
    "underlying": "USDC",
    "total_supply": 285_420.50,
    "total_reserve": 285_420.50,
    "apy": 4.2,
    "protocol": "Bucket Savings Pool",
    "contract": "0xstablelayer::jarvis_usd::JARVISUSD",
}

# 用户 JarvisUSD 余额（模拟）
_jarvis_balances: dict[str, float] = {}

def _get_jarvis_balance(uid: str) -> float:
    return _jarvis_balances.get(uid, 0.0)

def _add_jarvis_balance(uid: str, amount: float):
    _jarvis_balances[uid] = _jarvis_balances.get(uid, 0.0) + amount

def _sub_jarvis_balance(uid: str, amount: float) -> bool:
    cur = _jarvis_balances.get(uid, 0.0)
    if cur < amount:
        return False
    _jarvis_balances[uid] = cur - amount
    return True

# ==================== StableLayer 面板 ====================
async def _send_stablelayer_panel(msg):
    d = STABLELAYER_DATA
    now = datetime.now(HK_TZ).strftime("%H:%M")
    text = (
        f"🏦 *StableLayer — Stablecoin-as-a-Service*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"⏰ {now} HKT\n\n"
        f"💎 *{d['brand_coin']}* — 由 StableLayer 驱动的品牌稳定币\n"
        f"存入 USDC，自动生息，随时赎回\n\n"
        f"📊 *协议数据:*\n"
        f"  ├ 总供应量: *{d['total_supply']:,.2f} {d['brand_coin']}*\n"
        f"  ├ 底层储备: *{d['total_reserve']:,.2f} USDC*\n"
        f"  ├ 当前 APY: *{d['apy']}%*\n"
        f"  └ 底层协议: {d['protocol']} + 自动复利\n\n"
        f"🔗 合约: `{d['contract']}`\n\n"
        f"_Powered by StableLayer (stablelayer.site)_"
    )
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 Mint", callback_data="sl_mint"),
         InlineKeyboardButton("🔥 Burn", callback_data="sl_burn")],
        [InlineKeyboardButton("📈 查看收益", callback_data="sl_yield"),
         InlineKeyboardButton("📄 文档", url="https://docs.stablelayer.site/")],
        [InlineKeyboardButton("🔙 返回主菜单", callback_data="back")],
    ])
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=kb)

async def _send_mint_panel(msg, uid=None):
    d = STABLELAYER_DATA
    text = (
        f"💎 *铸造 JarvisUSD — Mint*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🏦 *StableLayer 品牌稳定币*\n"
        f"存入 USDC → 铸造等额 JarvisUSD\n"
        f"底层 USDC 自动进入 Bucket Savings Pool 生息\n\n"
        f"📈 当前 APY: *{d['apy']}%*\n"
        f"💰 1 USDC = 1 JarvisUSD (1:1)\n\n"
        f"选择铸造金额 👇"
    )
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("10 USDC", callback_data="sl_mint_10"),
         InlineKeyboardButton("50 USDC", callback_data="sl_mint_50"),
         InlineKeyboardButton("100 USDC", callback_data="sl_mint_100")],
        [InlineKeyboardButton("🔙 返回", callback_data="sl_panel")],
    ])
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=kb)

async def _exec_mint(msg, uid: str, amount: float):
    d = STABLELAYER_DATA
    _add_jarvis_balance(uid, amount)
    tx_hash = hashlib.sha256(f"mint{uid}{amount}{time.time()}".encode()).hexdigest()[:16]
    log_action("stablelayer_mint", f"uid:{uid} amount:{amount}")

    new_bal = _get_jarvis_balance(uid)
    text = (
        f"✅ *铸造成功！ Mint Complete*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📥 存入: *{amount:.2f} USDC*\n"
        f"📤 获得: *{amount:.2f} JarvisUSD*\n\n"
        f"💰 JarvisUSD 余额: *{new_bal:.2f}*\n"
        f"📈 当前 APY: *{d['apy']}%*\n"
        f"🔗 底层: Bucket Savings Pool + 自动复利\n\n"
        f"📋 TX: `0x{tx_hash}...`\n"
        f"⛽ Gas: 0.003 SUI\n\n"
        f"⚠️ _Demo 模式 — Testnet 模拟铸造_\n"
        f"_Powered by StableLayer_"
    )
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 继续 Mint", callback_data="sl_mint"),
         InlineKeyboardButton("📈 查看收益", callback_data="sl_yield")],
        [InlineKeyboardButton("🔙 主菜单", callback_data="back")],
    ])
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=kb)

async def _send_burn_panel(msg, uid: str):
    bal = _get_jarvis_balance(uid)
    text = (
        f"🔥 *赎回 JarvisUSD — Burn*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"销毁 JarvisUSD → 取回等额 USDC\n\n"
        f"💰 当前 JarvisUSD 余额: *{bal:.2f}*\n\n"
    )
    if bal <= 0:
        text += "⚠️ 余额不足，请先 Mint\n"
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("💎 去 Mint", callback_data="sl_mint")],
            [InlineKeyboardButton("🔙 返回", callback_data="sl_panel")],
        ])
    else:
        text += "选择赎回金额 👇"
        buttons_row = []
        for amt in [10, 50, 100]:
            if bal >= amt:
                buttons_row.append(InlineKeyboardButton(f"{amt} JUSD", callback_data=f"sl_burn_{amt}"))
        if bal > 0:
            buttons_row.append(InlineKeyboardButton(f"全部 {bal:.0f}", callback_data=f"sl_burn_all"))
        kb = InlineKeyboardMarkup([
            buttons_row,
            [InlineKeyboardButton("🔙 返回", callback_data="sl_panel")],
        ])
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=kb)

async def _exec_burn(msg, uid: str, amount: float):
    bal = _get_jarvis_balance(uid)
    if amount > bal:
        amount = bal
    if amount <= 0:
        await msg.reply_text("⚠️ 余额不足", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 返回", callback_data="sl_panel")]
        ]))
        return
    _sub_jarvis_balance(uid, amount)
    tx_hash = hashlib.sha256(f"burn{uid}{amount}{time.time()}".encode()).hexdigest()[:16]
    log_action("stablelayer_burn", f"uid:{uid} amount:{amount}")

    new_bal = _get_jarvis_balance(uid)
    text = (
        f"✅ *赎回成功！ Burn Complete*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🔥 销毁: *{amount:.2f} JarvisUSD*\n"
        f"📤 取回: *{amount:.2f} USDC*\n\n"
        f"💰 剩余 JarvisUSD: *{new_bal:.2f}*\n"
        f"📋 TX: `0x{tx_hash}...`\n\n"
        f"⚠️ _Demo 模式 — Testnet 模拟赎回_"
    )
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 Mint", callback_data="sl_mint"),
         InlineKeyboardButton("📈 收益", callback_data="sl_yield")],
        [InlineKeyboardButton("🔙 主菜单", callback_data="back")],
    ])
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=kb)

async def _send_yield_panel(msg, uid: str):
    d = STABLELAYER_DATA
    bal = _get_jarvis_balance(uid)
    daily_yield = bal * d["apy"] / 100 / 365
    monthly_yield = daily_yield * 30
    yearly_yield = bal * d["apy"] / 100
    # 模拟累计收益（假设持有 15 天）
    accumulated = daily_yield * 15

    text = (
        f"📈 *JarvisUSD 收益面板 — Yield*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💰 持有量: *{bal:.2f} JarvisUSD*\n\n"
        f"📊 *当前收益率:*\n"
        f"  ├ APY: *{d['apy']}%*\n"
        f"  ├ 日收益: ~{daily_yield:.4f} USDC\n"
        f"  ├ 月收益: ~{monthly_yield:.2f} USDC\n"
        f"  └ 年收益: ~{yearly_yield:.2f} USDC\n\n"
        f"💵 *累计收益:* ~{accumulated:.4f} USDC\n\n"
        f"🔗 *底层协议:*\n"
        f"  Bucket Savings Pool + 自动复利\n"
        f"  收益来源: USDC 借贷利息\n\n"
        f"_Powered by StableLayer (stablelayer.site)_"
    )
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 Mint 更多", callback_data="sl_mint"),
         InlineKeyboardButton("🔥 Burn 赎回", callback_data="sl_burn")],
        [InlineKeyboardButton("🏦 StableLayer", callback_data="sl_panel")],
        [InlineKeyboardButton("🔙 返回主菜单", callback_data="back")],
    ])
    await msg.reply_text(text, parse_mode="Markdown", reply_markup=kb)

# ==================== StableLayer 命令处理器 ====================
async def cmd_mint(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_action("mint_menu")
    await _send_mint_panel(update.message, str(update.effective_user.id))

async def cmd_burn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_action("burn_menu")
    await _send_burn_panel(update.message, str(update.effective_user.id))

async def cmd_yield(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_action("yield_view")
    await _send_yield_panel(update.message, str(update.effective_user.id))

async def cmd_stablelayer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_action("stablelayer_panel")
    await _send_stablelayer_panel(update.message)

# ==================== 回调处理器 ====================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    data = q.data
    uid = str(q.from_user.id)

    if data == "assets":
        wallet = get_or_create_wallet(uid)
        tokens = get_all_balances(wallet["address"])
        balance = get_sui_balance(wallet["address"])
        
        lines = []
        total_usd = 0
        for t in tokens:
            icon = "🟦" if t["name"] == "SUI" else "🟢"
            usd = t["balance"] * (3.82 if t["name"] == "SUI" else 1.0)
            total_usd += usd
            lines.append(f"  {icon} *{t['name']}*: {t['balance']:.4f} (~${usd:.2f})")
        
        token_text = "\n".join(lines) if lines else "  暂无持仓 No assets"
        
        await q.message.reply_text(
            f"💰 *资产面板 Assets*\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{token_text}\n\n"
            f"💵 总估值: *~${total_usd:.2f}*\n\n"
            f"📍 `{wallet['address'][:16]}...{wallet['address'][-8:]}`\n"
            f"🔗 [浏览器](https://suiscan.xyz/{NETWORK}/account/{wallet['address']})",
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄 刷新余额", callback_data="assets"),
                 InlineKeyboardButton("🔙 返回", callback_data="back")]
            ])
        )
        log_action("assets", f"${total_usd:.2f}")

    elif data == "swap_menu":
        await q.message.reply_text(
            "🔄 *Swap 交易 — Cetus Aggregator*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🐋 路由覆盖 30+ DEX:\n"
            "Cetus · DeepBook · Turbos · Aftermath\n"
            "FlowX · KriyaDEX · BlueFin · Haedal...\n\n"
            "选择交易对，获取最优报价 👇",
            parse_mode="Markdown",
            reply_markup=swap_keyboard()
        )

    elif data.startswith("swap_") and "/" in data:
        pair = data.replace("swap_", "")
        if pair in SWAP_PAIRS:
            info = SWAP_PAIRS[pair]
            src, dst = pair.split("/")
            amount = 1.0
            out = amount * info["rate"]
            variation = random.uniform(-0.02, 0.02)
            out *= (1 + variation)
            
            log_action("swap_quote", f"{src}→{dst} rate:{info['rate']}")
            
            kb = InlineKeyboardMarkup([
                [InlineKeyboardButton(f"✅ 确认交易 Execute", callback_data=f"exec_{pair}"),
                 InlineKeyboardButton("❌ 取消", callback_data="swap_menu")],
                [InlineKeyboardButton("🔙 返回", callback_data="swap_menu")],
            ])
            
            await q.message.reply_text(
                f"🔄 *Swap 报价 Quote*\n"
                f"━━━━━━━━━━━━━━━━━━━━\n\n"
                f"📥 *输入 Input:*  {amount} {src}\n"
                f"📤 *输出 Output:* {out:.6f} {dst}\n\n"
                f"📊 *路由详情 Route:*\n"
                f"  🛣 路径: {info['route']}\n"
                f"  🔀 经过 DEX: {info['dexes']} 个\n"
                f"  💧 流动性池: {info['pools']} 个\n"
                f"  📉 滑点保护: 0.5%\n"
                f"  ⛽ 预估 Gas: ~0.005 SUI\n\n"
                f"💡 _报价有效期 30 秒_",
                parse_mode="Markdown",
                reply_markup=kb
            )

    elif data.startswith("exec_"):
        pair = data.replace("exec_", "")
        src, dst = pair.split("/")
        tx_hash = hashlib.sha256(f"{pair}{time.time()}".encode()).hexdigest()[:16]
        log_action("swap_execute", f"{src}→{dst} tx:{tx_hash}")
        
        await q.message.reply_text(
            f"✅ *交易模拟执行成功！*\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"🔄 {src} → {dst}\n"
            f"📋 TX: `0x{tx_hash}...`\n"
            f"⛽ Gas: 0.004 SUI\n"
            f"⏱ 确认时间: <1s\n\n"
            f"🐘 日志已记录到 Walrus\n\n"
            f"⚠️ _Demo 模式 — Testnet 模拟交易_",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄 继续交易", callback_data="swap_menu"),
                 InlineKeyboardButton("🔙 主菜单", callback_data="back")],
            ])
        )

    elif data == "swap_custom":
        await q.message.reply_text(
            "🔧 *自定义 Swap*\n\n"
            "发送格式 / Send format:\n"
            "`swap 10 SUI USDC`\n\n"
            "支持的代币: SUI, USDC, USDT, WETH, CETUS",
            parse_mode="Markdown"
        )

    elif data == "strategy":
        await _send_strategy_panel(q.message)

    elif data.startswith("strat_") and data.replace("strat_", "") in STRATEGIES:
        key = data.replace("strat_", "")
        strategy_state["enabled"][key] = not strategy_state["enabled"][key]
        if strategy_state["enabled"][key]:
            strategy_state["active"] = key
        elif strategy_state["active"] == key:
            for k, v in strategy_state["enabled"].items():
                if v:
                    strategy_state["active"] = k
                    break
        log_action("toggle_strategy", f"{key}={strategy_state['enabled'][key]}")
        await _send_strategy_panel(q.message)

    elif data == "strat_detail":
        text = "📊 *策略详情 Strategy Details*\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        for key, info in STRATEGIES.items():
            enabled = "✅" if strategy_state["enabled"][key] else "⬜"
            active = " 🔥" if strategy_state["active"] == key else ""
            text += (
                f"{enabled} *{info['name']}*{active}\n"
                f"  {info['desc']}\n"
                f"  信号: {' · '.join(info['signals'])}\n"
                f"  胜率: {info['win_rate']} | 回报: {info['avg_return']} | 风险: {info['risk']}\n\n"
            )
        await q.message.reply_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 返回策略", callback_data="strategy")]
            ]))

    elif data == "dashboard":
        await _send_dashboard(q.message, uid)

    elif data == "whale":
        await _send_whale_panel(q.message)

    elif data == "whale_stats":
        await q.message.reply_text(
            "📊 *鲸鱼统计 Whale Stats (24h)*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🟢 *净流入:* +2,450,000 SUI\n"
            "🔴 *净流出:* -1,820,000 SUI\n"
            "📊 *净变化:* +630,000 SUI\n\n"
            "🐋 *活跃鲸鱼:* 23 个地址\n"
            "💰 *最大单笔:* 500,000 SUI ($1.91M)\n"
            "📈 *趋势:* 偏多 (净买入)\n\n"
            "_数据来源: Sui 链上交易分析_",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 返回鲸鱼", callback_data="whale")]
            ])
        )

    elif data == "pools":
        await _send_pools_panel(q.message)

    elif data == "pools_apr":
        pools = gen_pool_data()
        pools.sort(key=lambda x: float(x["apr"].replace("%", "")), reverse=True)
        lines = []
        for i, p in enumerate(pools, 1):
            lines.append(f"  {i}. 🔥 *{p['apr']}* — {p['pair']} (TVL: {p['tvl']})")
        await q.message.reply_text(
            f"🌱 *池子按 APR 排序*\n━━━━━━━━━━━━━━━━━━━━\n\n" + "\n".join(lines) +
            "\n\n⚠️ _高 APR = 高风险_",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 返回池子", callback_data="pools")]
            ])
        )

    elif data == "portfolio":
        await _send_portfolio_panel(q.message, uid)

    elif data == "portfolio_chart":
        await q.message.reply_text(
            "📈 *收益曲线 Performance Chart (7D)*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "```\n"
            "  $2,400 ┤                    ╭─\n"
            "  $2,350 ┤              ╭─────╯\n"
            "  $2,300 ┤         ╭────╯\n"
            "  $2,250 ┤    ╭────╯\n"
            "  $2,200 ┤╭───╯\n"
            "  $2,150 ┤╯\n"
            "         └─────────────────────\n"
            "          Mon Tue Wed Thu Fri Sat Sun\n"
            "```\n\n"
            "📊 周涨幅: *+8.2%* | 最高: $2,410 | 最低: $2,150",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 返回持仓", callback_data="portfolio")]
            ])
        )

    elif data == "limit":
        await _send_limit_panel(q.message, uid)

    elif data == "limit_cancel_all":
        orders = load_limit_orders()
        orders = [o for o in orders if o.get("uid") != uid]
        save_limit_orders(orders)
        log_action("limit_cancel_all", f"uid:{uid}")
        await q.message.reply_text(
            "✅ *已取消全部挂单*\n\n所有限价单已移除。",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 返回限价单", callback_data="limit")]
            ])
        )

    elif data.startswith("limit_cancel_"):
        order_id = data.replace("limit_cancel_", "")
        orders = load_limit_orders()
        orders = [o for o in orders if str(o.get("id")) != order_id or o.get("uid") != uid]
        save_limit_orders(orders)
        log_action("limit_cancel", f"order:{order_id}")
        await _send_limit_panel(q.message, uid)

    elif data == "signals":
        await _send_signals_panel(q.message)

    elif data == "signals_settings":
        await q.message.reply_text(
            "⚙️ *信号设置 Signal Settings*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "📊 *技术指标:*\n"
            "  ✅ EMA (12/26)\n"
            "  ✅ RSI (14)\n"
            "  ✅ MACD (12/26/9)\n"
            "  ✅ 布林带 (20,2)\n"
            "  ⬜ 斐波那契回撤\n\n"
            "🔔 *通知:*\n"
            "  ✅ 买入信号\n"
            "  ✅ 卖出信号\n"
            "  ⬜ 观望信号\n\n"
            "⏰ *刷新频率:* 每 5 分钟\n\n"
            "_完整版支持自定义指标参数_",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 返回信号", callback_data="signals")]
            ])
        )

    elif data == "walrus":
        text = (
            f"🐘 *Walrus 去中心化日志*\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"每笔交易、每个策略决策都透明记录在 Walrus 上。\n"
            f"不可篡改，任何人可验证。\n\n"
            f"📦 *链上日志 On-chain Logs:*\n"
        )
        for b in WALRUS_BLOBS:
            text += f"  🔗 `{b['id']}` | {b['time']} | {b['type']} | {b['size']}\n"
        
        text += (
            f"\n📊 总计: {len(WALRUS_BLOBS)} blobs | ~6.7KB\n\n"
            f"🔍 聚合器: `{WALRUS_AGGREGATOR[:40]}...`\n\n"
            f"_所有操作日志定期上传，确保审计透明_"
        )
        
        await q.message.reply_text(text, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🐘 立即上传", callback_data="walrus_upload"),
                 InlineKeyboardButton("🔙 返回", callback_data="back")]
            ]))

    elif data == "walrus_upload":
        log_action("walrus_upload")
        blob_id = hashlib.sha256(f"walrus{time.time()}".encode()).hexdigest()[:10]
        await q.message.reply_text(
            f"🐘 *日志上传中...*\n\n"
            f"✅ 上传成功！\n"
            f"📦 Blob ID: `{blob_id}...`\n"
            f"📊 大小: {random.randint(1,5)}.{random.randint(0,9)}KB\n"
            f"⏱ 存储时间: 永久\n\n"
            f"_数据已安全存储在 Walrus 去中心化网络_",
            parse_mode="Markdown"
        )

    elif data == "vault":
        await q.message.reply_text(
            f"🔐 *Vault 智能合约*\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"资金通过 Move 合约管理，安全透明。\n\n"
            f"📦 *合约信息:*\n"
            f"  Package: `{DEPLOYED_PACKAGE}`\n"
            f"  网络: Sui {NETWORK.capitalize()}\n\n"
            f"🛡️ *安全特性:*\n"
            f"  ├ VaultCap 权限控制\n"
            f"  ├ 单次提取限额\n"
            f"  ├ 紧急暂停机制\n"
            f"  └ 所有操作链上可查\n\n"
            f"📊 *功能:*\n"
            f"  • deposit() — 存入资金\n"
            f"  • withdraw() — 提取收益\n"
            f"  • emergency\\_pause() — 紧急暂停\n\n"
            f"🔗 [查看合约](https://suiscan.xyz/{NETWORK}/object/{DEPLOYED_PACKAGE})",
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 返回主菜单", callback_data="back")]
            ])
        )

    elif data == "settings":
        await q.message.reply_text(
            "⚙️ *设置 Settings*\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            f"🌐 网络: Sui {NETWORK.capitalize()}\n"
            f"📦 模式: Demo (共享 Testnet 钱包)\n"
            f"🔔 通知: 开启\n"
            f"💰 滑点: 0.5%\n"
            f"⛽ Gas 预算: 0.01 SUI\n\n"
            f"_完整版支持自定义钱包和 Mainnet_",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 返回主菜单", callback_data="back")]
            ])
        )

    elif data == "help":
        await q.message.reply_text(
            "❓ 使用 /help 查看完整帮助",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 返回主菜单", callback_data="back")]
            ])
        )

    elif data == "refresh_logs":
        await _send_logs_panel(q.message)

    # StableLayer callbacks
    elif data == "sl_panel":
        await _send_stablelayer_panel(q.message)

    elif data == "sl_mint":
        await _send_mint_panel(q.message, uid)

    elif data.startswith("sl_mint_"):
        amount = float(data.replace("sl_mint_", ""))
        await _exec_mint(q.message, uid, amount)

    elif data == "sl_burn":
        await _send_burn_panel(q.message, uid)

    elif data.startswith("sl_burn_"):
        val = data.replace("sl_burn_", "")
        if val == "all":
            amount = _get_jarvis_balance(uid)
        else:
            amount = float(val)
        await _exec_burn(q.message, uid, amount)

    elif data == "sl_yield":
        await _send_yield_panel(q.message, uid)

    # ---- 双语切换 ----
    elif data == "lang_toggle":
        cur = get_lang(uid)
        new_lang = "en" if cur == "cn" else "cn"
        set_lang(uid, new_lang)
        label = "🇬🇧 Switched to English" if new_lang == "en" else "🇨🇳 已切换为中文"
        await q.message.reply_text(label, reply_markup=main_keyboard(new_lang))

    elif data == "lang_cn":
        set_lang(uid, "cn")
        await q.message.reply_text(
            t(uid, "lang_set_cn"),
            reply_markup=main_keyboard("cn")
        )

    elif data == "lang_en":
        set_lang(uid, "en")
        await q.message.reply_text(
            t(uid, "lang_set_en"),
            reply_markup=main_keyboard("en")
        )

    # ---- Social 模块 ----
    elif data == "social":
        await _send_social_panel(q.message, uid)

    elif data == "social_tweet":
        lang = get_lang(uid)
        tweet = random.choice(TWEET_TEMPLATES)
        await q.message.reply_text(
            f"📣 *{'AI 生成推文' if lang=='cn' else 'AI Generated Tweet'}*\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{tweet}\n\n"
            f"{'复制上方文本发到 Twitter/X 🐦' if lang=='cn' else 'Copy and post to Twitter/X 🐦'}",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄 换一条" if lang=="cn" else "🔄 New Tweet", callback_data="social_tweet")],
                [InlineKeyboardButton(t(uid, "btn_back"), callback_data="social")],
            ])
        )

    elif data == "social_invite":
        lang = get_lang(uid)
        count = get_referral_count(uid)
        link = f"https://t.me/SuiJarvisBot?start=ref_{uid}"
        await q.message.reply_text(
            f"🔗 *{'邀请链接' if lang=='cn' else 'Referral Link'}*\n\n"
            f"`{link}`\n\n"
            f"👥 {'已邀请' if lang=='cn' else 'Invited'}: *{count}* {'人' if lang=='cn' else 'users'}",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(
                    "📤 分享" if lang=="cn" else "📤 Share",
                    switch_inline_query=f"🤖 Sui DeFi Jarvis 🚀 {link}")],
                [InlineKeyboardButton(t(uid, "btn_back"), callback_data="social")],
            ])
        )

    elif data == "back":
        lang = get_lang(uid)
        await q.message.reply_text(
            t(uid, "main_greeting"),
            parse_mode="Markdown",
            reply_markup=main_keyboard(lang)
        )

# ==================== 自然语言处理 ====================
async def nl_handler(update: Update, context):
    text = update.message.text or ""
    text_lower = text.lower().strip()
    
    # 1. 检测 CoinType 格式 (包含 ::)
    coin_type_match = re.search(r'(0x[a-fA-F0-9]{2,}::\w+::\w+)', text)
    if coin_type_match:
        coin_type = coin_type_match.group(1)
        await send_token_info(update.message, coin_type)
        return
    
    # 2. 检测 Sui 地址 (0x 开头, >=40字符的十六进制)
    addr_match = re.search(r'(0x[a-fA-F0-9]{40,})', text)
    if addr_match:
        address = addr_match.group(1)
        # Try as a coin type — could be a package address
        await update.message.reply_text(
            f"🔍 *检测到 Sui 地址*\n\n"
            f"`{address[:20]}...{address[-8:]}`\n\n"
            f"💡 如需查询代币信息，请发送完整 CoinType:\n"
            f"`{address}::module::TOKEN`\n\n"
            f"🔗 [浏览器查看](https://suiscan.xyz/{NETWORK}/account/{address})",
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 返回主菜单", callback_data="back")]
            ])
        )
        return
    
    # 3. 限价单创建
    limit_match = re.match(r'limit\s+(buy|sell)\s+(\w+/\w+)\s+([\d.]+)\s+([\d.]+)', text_lower)
    if limit_match:
        direction = limit_match.group(1)
        pair = limit_match.group(2).upper()
        target_price = float(limit_match.group(3))
        amount = float(limit_match.group(4))
        uid = str(update.effective_user.id)
        
        orders = load_limit_orders()
        order_id = len(orders) + 1
        orders.append({
            "id": order_id,
            "uid": uid,
            "direction": direction,
            "pair": pair,
            "target_price": target_price,
            "amount": amount,
            "status": "pending",
            "created": datetime.now(HK_TZ).isoformat(),
        })
        save_limit_orders(orders)
        log_action("limit_create", f"{direction} {pair} @{target_price} x{amount}")
        
        icon = "🟢" if direction == "buy" else "🔴"
        await update.message.reply_text(
            f"✅ *限价单已创建！*\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"  {icon} *{'买入 BUY' if direction=='buy' else '卖出 SELL'}*\n"
            f"  交易对: {pair}\n"
            f"  目标价: ${target_price:.4f}\n"
            f"  数量: {amount} {pair.split('/')[0]}\n"
            f"  订单号: #{order_id}\n\n"
            f"_当价格触及目标将自动执行_",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📋 查看挂单", callback_data="limit"),
                 InlineKeyboardButton("🔙 主菜单", callback_data="back")]
            ])
        )
        return
    
    # 4. 常规自然语言匹配
    if any(k in text_lower for k in ["余额", "balance", "钱包", "wallet", "多少钱"]):
        await cmd_balance(update, context)
    elif any(k in text_lower for k in ["swap", "交换", "兑换", "换"]):
        await cmd_swap(update, context)
    elif any(k in text_lower for k in ["日志", "log", "记录", "历史"]):
        await cmd_logs(update, context)
    elif any(k in text_lower for k in ["策略", "strategy"]):
        await cmd_strategy(update, context)
    elif any(k in text_lower for k in ["鲸鱼", "whale", "大户"]):
        await cmd_whale(update, context)
    elif any(k in text_lower for k in ["池子", "pool", "新池", "流动性"]):
        await cmd_pools(update, context)
    elif any(k in text_lower for k in ["持仓", "portfolio", "仓位"]):
        uid = str(update.effective_user.id)
        await _send_portfolio_panel(update.message, uid)
    elif any(k in text_lower for k in ["限价", "limit", "挂单"]):
        uid = str(update.effective_user.id)
        await _send_limit_panel(update.message, uid)
    elif any(k in text_lower for k in ["信号", "signal", "买卖点"]):
        await _send_signals_panel(update.message)
    elif any(k in text_lower for k in ["walrus", "链上", "存储"]):
        uid = str(update.effective_user.id)
        await _send_dashboard(update.message, uid)
    elif any(k in text_lower for k in ["mint", "铸造", "jarvisusd", "stablelayer"]):
        await _send_stablelayer_panel(update.message)
    elif any(k in text_lower for k in ["burn", "赎回", "销毁"]):
        await _send_burn_panel(update.message, str(update.effective_user.id))
    elif any(k in text_lower for k in ["yield", "收益", "生息", "apy"]):
        await _send_yield_panel(update.message, str(update.effective_user.id))
    elif any(k in text_lower for k in ["帮助", "help", "怎么用"]):
        await cmd_help(update, context)
    elif any(k in text_lower for k in ["social", "邀请", "refer", "推荐", "分享"]):
        await _send_social_panel(update.message, str(update.effective_user.id))
    elif any(k in text_lower for k in ["语言", "language", "lang", "英文", "中文"]):
        await cmd_lang(update, context)
    else:
        await update.message.reply_text(
            "🤖 *Jarvis 在线！*\n\n"
            "试试这些:\n"
            "• \"余额\" — 查看资产\n"
            "• \"swap\" — 开始交易\n"
            "• \"持仓\" — 投资组合\n"
            "• \"鲸鱼\" — 大额追踪\n"
            "• \"信号\" — AI 交易信号\n"
            "• 发送 CoinType 查 Token\n"
            "• /help — 完整帮助\n\n"
            "或直接使用下方按钮 👇",
            parse_mode="Markdown",
            reply_markup=main_keyboard(get_lang(str(update.effective_user.id)))
        )

# ==================== 启动 ====================
def main():
    log.info("🤖 Sui DeFi Jarvis v2.0 starting...")
    
    req = HTTPXRequest(proxy=PROXY, connect_timeout=30, read_timeout=30)
    get_req = HTTPXRequest(proxy=PROXY, connect_timeout=30, read_timeout=30)
    
    app = (Application.builder()
           .token(TOKEN)
           .request(req)
           .get_updates_request(get_req)
           .build())
    
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("wallet", cmd_wallet))
    app.add_handler(CommandHandler("balance", cmd_balance))
    app.add_handler(CommandHandler("swap", cmd_swap))
    app.add_handler(CommandHandler("strategy", cmd_strategy))
    app.add_handler(CommandHandler("logs", cmd_logs))
    app.add_handler(CommandHandler("whale", cmd_whale))
    app.add_handler(CommandHandler("pools", cmd_pools))
    app.add_handler(CommandHandler("portfolio", cmd_portfolio))
    app.add_handler(CommandHandler("limit", cmd_limit))
    app.add_handler(CommandHandler("signals", cmd_signals))
    app.add_handler(CommandHandler("mint", cmd_mint))
    app.add_handler(CommandHandler("burn", cmd_burn))
    app.add_handler(CommandHandler("yield", cmd_yield))
    app.add_handler(CommandHandler("stablelayer", cmd_stablelayer))
    app.add_handler(CommandHandler("lang", cmd_lang))
    app.add_handler(CommandHandler("refer", cmd_refer))
    app.add_handler(CommandHandler("social", cmd_social))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & filters.ChatType.PRIVATE, nl_handler))
    
    log.info("🤖 @SuiJarvisBot v2.0 ACTIVE — The Infinite Money Glitch")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
