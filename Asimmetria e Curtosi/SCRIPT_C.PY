import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 🔑 Inserisci la tua API Key gratuita FMP (registrazione gratuita su financialmodelingprep.com)
API_KEY = "vsZ9aM6FdD2t7ONUKRNNue6fq2EBNSHq"
symbol = "SPY"

# 📥 Scarica i dati storici da FMP in formato JSON
url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?serietype=line&apikey={API_KEY}"
response = requests.get(url)
data_json = response.json()

# 📄 Parsing dei dati in DataFrame
prices = data_json["historical"]
df = pd.DataFrame(prices)
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')
df.set_index('date', inplace=True)

# 📈 Calcolo dei rendimenti giornalieri
df['returns'] = df['close'].pct_change().dropna()

# 📊 Calcolo skewness e curtosi
skew = df['returns'].skew()
kurt = df['returns'].kurtosis()

print(f"Skewness: {skew:.4f}")
print(f"Kurtosis: {kurt:.4f}")

# 📉 Visualizzazione
plt.figure(figsize=(10,6))
df['returns'].hist(bins=50, density=True, alpha=0.6, color='darkcyan')

x = np.linspace(df['returns'].min(), df['returns'].max(), 100)
p = stats.norm.pdf(x, df['returns'].mean(), df['returns'].std())
plt.plot(x, p, 'k', linewidth=2, label="Distribuzione Normale")

plt.title("Distribuzione dei Rendimenti Giornalieri (SPY - FMP)")
plt.xlabel("Rendimenti")
plt.ylabel("Frequenza")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
