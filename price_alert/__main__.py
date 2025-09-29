#!/usr/bin/env python3
import argparse, sys, requests

SYMBOL_MAP = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana",
    "BNB": "binancecoin",
}

def normalize_symbol(s: str) -> str:
    s = (s or "").upper().strip()
    return SYMBOL_MAP.get(s, s.lower())

def fetch_price_usd(asset_id: str) -> float:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={asset_id}&vs_currencies=usd"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    data = r.json()
    return float(data.get(asset_id, {}).get("usd", 0))

def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Simple price alerts via CoinGecko")
    p.add_argument("--symbol", default="BTC", help="symbol, e.g. BTC/ETH/SOL")
    p.add_argument("--above", type=float, help="alert if price goes ABOVE this USD value")
    p.add_argument("--below", type=float, help="alert if price goes BELOW this USD value")
    args = p.parse_args(argv)

    asset_id = normalize_symbol(args.symbol)
    if not asset_id:
        print("❌ Invalid symbol", file=sys.stderr)
        return 2

    try:
        price = fetch_price_usd(asset_id)
    except Exception as e:
        print(f"❌ API error: {e}", file=sys.stderr)
        return 3

    print(f"{args.symbol.upper()}: ${price:.2f}")

    alert = None
    if args.above is not None and price > args.above:
        alert = f"🚀 {args.symbol} broke ABOVE ${args.above:.2f}"
    if args.below is not None and price < args.below:
        alert = f"📉 {args.symbol} fell BELOW ${args.below:.2f}"

    if alert:
        print(alert)
        return 10  # спец-код чтобы можно было ловить в крон/скриптах
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
