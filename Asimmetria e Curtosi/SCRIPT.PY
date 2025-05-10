# Importazione delle librerie necessarie
import yfinance as yf              # Per il download dei dati finanziari
import pandas as pd               # Per la manipolazione dei dati in DataFrame
import numpy as np                # Per operazioni numeriche
import matplotlib.pyplot as plt   # Per la visualizzazione grafica
from scipy import stats           # Per calcolare la distribuzione normale teorica

# Download dei dati storici di SPY (ETF S&P 500) degli ultimi 5 anni
spy = yf.Ticker("SPY")
data = spy.history(period="5y")

# Calcolo dei rendimenti giornalieri (percentuale di variazione del prezzo di chiusura)
returns = data['Close'].pct_change().dropna()  # Rimuove i NaN causati dal primo differenziale

# Calcolo delle statistiche di distribuzione
skewness = returns.skew()         # Asimmetria: misura la simmetria della distribuzione
kurtosis = returns.kurtosis()     # Curtosi: misura la "pesantezza" delle code

# Output delle metriche calcolate
print(f"Skewness: {skewness:.4f}")   # Valori positivi indicano code più lunghe a destra
print(f"Kurtosis: {kurtosis:.4f}")   # Valori > 3 indicano code più pesanti rispetto alla normale

# Visualizzazione della distribuzione dei rendimenti
plt.figure(figsize=(10, 6))

# Istogramma dei rendimenti normalizzato
returns.hist(bins=50, density=True, alpha=0.7, color='steelblue')

# Definizione del range per la curva normale teorica
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)

# Calcolo della distribuzione normale teorica con stessa media e std dei dati reali
p = stats.norm.pdf(x, returns.mean(), returns.std())

# Tracciamento della curva normale
plt.plot(x, p, 'k', linewidth=2, label='Distribuzione Normale')

# Personalizzazione del grafico
plt.title("Distribuzione dei Rendimenti Giornalieri di SPY")
plt.xlabel("Rendimenti")
plt.ylabel("Frequenza")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Mostra il grafico
plt.show()
