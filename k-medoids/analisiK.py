import yfinance as yf
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn_extra.cluster import KMedoids
import matplotlib.pyplot as plt

# === Parametri iniziali ===
tickers = ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'TSLA']
start_date = '2020-01-01'
end_date = '2020-12-31'

# === Scarico i dati storici da Yahoo Finance con auto-adjust ===
data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)

# === Estrazione dei prezzi di chiusura ===
data_close = data['Close']

# === Standardizzazione: elimina le differenze di scala tra i titoli ===
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_close.T)  # .T per avere i titoli come osservazioni

# === PCA: riduzione dimensionale a 2 componenti per visualizzare ===
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

# === Clustering con K-Medoids (più robusto di KMeans) ===
kmedoids = KMedoids(n_clusters=2, random_state=0, method='alternate')
labels = kmedoids.fit_predict(data_pca)

# === Visualizzazione e salvataggio del grafico ===
plt.figure(figsize=(10, 6))
for i, ticker in enumerate(data_close.columns):
    plt.scatter(data_pca[i, 0], data_pca[i, 1], label=ticker, c=f"C{labels[i]}")
    plt.text(data_pca[i, 0]+0.02, data_pca[i, 1]+0.02, ticker, fontsize=9)

plt.title("Clustering K-Medoids dei titoli (PCA 2D)")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Salva il grafico nella cartella del progetto
plt.savefig("C:/Users/f.lucignano/Desktop/k-medoids/clustering_kmedoids.png")
plt.show()
