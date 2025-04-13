# ----------------------------
# 📊 PORTAFOGLIO OTTIMIZZATO CON RISKFOLIO-LIB
# ----------------------------

import warnings
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import riskfolio as rp
import os
import numpy as np

warnings.filterwarnings("ignore")

# ----------------------------
# FUNZIONE PER PERFORMANCE
# ----------------------------
def portfolio_performance(returns, weights, risk_free_rate=0, alpha=0.05):
    """
    Calcola rendimento atteso, volatilità e Sharpe Ratio del portafoglio.
    """
    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    port_return = np.dot(mean_returns.values, weights) * 252
    port_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix.values * 252, weights)))
    sharpe_ratio = (port_return - risk_free_rate) / port_volatility

    return port_return, port_volatility, sharpe_ratio

# ----------------------------
# 📁 PERCORSO DI OUTPUT
# ----------------------------
output_folder = r"C:\Users\f.lucignano\Desktop\CFO\grafici_portafoglio"
os.makedirs(output_folder, exist_ok=True)

# ----------------------------
# ⚙️ PARAMETRI BASE
# ----------------------------
start = "2023-01-01"
end = "2024-12-30"

tickers = [
    "JCI", "TGT", "CMCSA", "CPB", "MO", "APA", "MMC", "JPM", "ZION", "PSA",
    "BAX", "BMY", "LUV", "PCAR", "TXT", "TMO", "DE", "MSFT", "HPQ", "SEE"
]
tickers.sort()

# ----------------------------
# ⏳ DOWNLOAD E PULIZIA DATI
# ----------------------------
print("⏳ Download dati da Yahoo Finance...")
raw_data = yf.download(tickers, start=start, end=end).Close

min_valid_obs = int(0.7 * raw_data.shape[0])
filtered_data = raw_data.dropna(axis=1, thresh=min_valid_obs)
data = filtered_data.interpolate(method="linear").ffill().bfill()

Y = data.pct_change().dropna()
Y.to_csv(os.path.join(output_folder, "rendimenti_portafoglio.csv"))

if Y.empty:
    print("❌ Nessun dato valido dopo il calcolo dei rendimenti.")
    exit()
else:
    print(f"✅ Dati pronti. {Y.shape[1]} titoli su {len(tickers)} utilizzati.")

# ----------------------------
# 🧠 COSTRUZIONE PORTAFOGLIO
# ----------------------------
port = rp.Portfolio(returns=Y)
port.assets_stats(method_mu="hist", method_cov="ledoit")

# ----------------------------
# ⚖️ VINCOLI DI OTTIMIZZAZIONE
# ----------------------------
port.sht = True
port.uppersht = 1
port.upperlng = 1
port.budget = 0  # Neutralità di dollaro

# ----------------------------
# ⚙️ OTTIMIZZAZIONE
# ----------------------------
print("⚙️ Ottimizzazione in corso...")
w = port.optimization(model="Classic", rm="CVaR", obj="Sharpe", hist=True)

if w.empty or w.abs().sum().sum() == 0:
    print("❌ Ottimizzazione fallita.")
    exit()

# ----------------------------
# 📊 PESI E SALVATAGGI
# ----------------------------
print("\n🔍 Pesi del Portafoglio Ottimizzato:")
print(w[w > 0].dropna())
w.to_csv(os.path.join(output_folder, "pesi_portafoglio.csv"))

# Conversione dei pesi in array per il calcolo delle performance
weights_array = w.values.flatten()  # array 1D

# ----------------------------
# 📈 PERFORMANCE DEL PORTAFOGLIO
# ----------------------------
ret_ann, vol_ann, sharpe = portfolio_performance(Y, weights_array, risk_free_rate=0)

print("\n📊 Statistiche di Performance:")
print(f"Rendimento atteso annuo: {round(ret_ann * 100, 2)}%")
print(f"Volatilità annua: {round(vol_ann * 100, 2)}%")
print(f"Sharpe Ratio: {round(sharpe, 3)}")

# ----------------------------
# 📉 CVaR DEL PORTAFOGLIO
# ----------------------------
returns_portafoglio = Y @ w
alpha = 0.05
CVaR = returns_portafoglio[returns_portafoglio <= returns_portafoglio.quantile(alpha)].mean()
print(f"CVaR (5%): {round(CVaR.values[0] * 100, 2)}%")

# ----------------------------
# 📊 GRAFICI
# ----------------------------
title = "Max Return Dollar Neutral with CVaR Constraint"

# Pie chart
fig1 = rp.plot_pie(w=w, title=title, others=0.05, nrow=25, cmap="tab20", height=7, width=10)
fig1.figure.savefig(os.path.join(output_folder, "pie_chart_portfolio.png"))
print(f"✅ Grafico a torta salvato in: {os.path.join(output_folder, 'pie_chart_portfolio.png')}")

# Bar chart
fig2 = rp.plot_bar(w, title=title, kind="v", others=0.05)
fig2.figure.savefig(os.path.join(output_folder, "bar_chart_portfolio.png"))
print(f"✅ Grafico a barre salvato in: {os.path.join(output_folder, 'bar_chart_portfolio.png')}")

# ----------------------------
# 🧾 DASHBOARD FINALE
# ----------------------------
print("\n📈 DASHBOARD COMPLETA")
print("──────────────────────────────")
print(f"Periodo analizzato: {start} → {end}")
print(f"N. asset analizzati: {len(filtered_data.columns)}")
print(f"Asset selezionati nel portafoglio: {w[w > 0].dropna().shape[0]}")
print(f"Expected Return: {round(ret_ann * 100, 2)}%")
print(f"Volatility (Annuale): {round(vol_ann * 100, 2)}%")
print(f"Sharpe Ratio: {round(sharpe, 3)}")
print(f"CVaR (5%): {round(CVaR.values[0] * 100, 2)}%")
print("Grafici e file salvati nella cartella:")
print(output_folder)
print("──────────────────────────────")
