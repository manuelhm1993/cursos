import requests
import time
import sys

def get_bitcoin_price():
    # Cambiamos a la API pública de Binance (ultra estable)
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    
    # Engañamos a los firewalls simulando ser un navegador Chrome de Windows
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        price = float(data['price'])
        print(f"💰 Precio actual de Bitcoin: ${price:,.2f} USD")
        sys.stdout.flush() # Fuerza a que el log salga en Docker en tiempo real
    except Exception as e:
        print(f"❌ Error al consultar la API: {e}")
        sys.stdout.flush()

if __name__ == "__main__":
    print("🚀 Iniciando Bot Extractor de Criptomonedas (V2 - Binance)...")
    sys.stdout.flush()
    while True:
        get_bitcoin_price()
        time.sleep(10)