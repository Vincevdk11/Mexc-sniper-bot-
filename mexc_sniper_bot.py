
# MEXC Sniper Bot (v1.0)
# Werkt met MEXC API via ccxt
# Functie: Snipen bij listing, market buy, +200% TP, -15% SL

import ccxt
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('MEXC_API_KEY')
API_SECRET = os.getenv('MEXC_API_SECRET')

mexc = ccxt.mexc({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'enableRateLimit': True
})

def snipe_coin(symbol: str, usdt_amount: float = 107):
    print(f"Sniper gestart voor {symbol} met {usdt_amount} USDT...")

    # Poll de markt totdat het symbool beschikbaar is
    while True:
        try:
            ticker = mexc.fetch_ticker(symbol)
            if ticker:
                print(f"{symbol} is live! Start aankoop...")
                break
        except:
            print(f"{symbol} nog niet beschikbaar. Wachten...")
        time.sleep(1)  # elke seconde checken

    # Koop market order
    market_price = mexc.fetch_ticker(symbol)['last']
    amount_to_buy = usdt_amount / market_price
    order = mexc.create_market_buy_order(symbol, amount_to_buy)
    print("Market buy geplaatst:", order)

    # Stel TP en SL (simulatie - op MEXC handmatig of via andere logic)
    tp_price = market_price * 3  # 200% winst
    sl_price = market_price * 0.85  # 15% verlies
    print(f"TP: {tp_price:.4f} | SL: {sl_price:.4f} (prijs: {market_price:.4f})")

    # Hier kan uitgebreidere logica komen voor limit TP/SL via een loop of OCO
    print("Trade geplaatst. Volg trade in je MEXC dashboard.")

# Voorbeeld: snipe_coin('PAWS/USDT')
