import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from datetime import datetime, timedelta
import os
from PIL import Image

# === Parametri principali ===
SYMBOL = "BTC-USD"
TIMEFRAME = "1h"
START = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
LAST_N_BARS = 66
PRED_N_BARS = 12
GIF_N_BARS = 72
GIF_FPS = 4
GIF_FNAME = "projections.gif"
GIF_PAD = 0.01
FRAME_DIR = "frames"

# === Step 1: Scarica i dati ===
data = yf.download(SYMBOL, interval=TIMEFRAME, start=START)
data.dropna(inplace=True)
data["hlc3"] = (data["High"] + data["Low"] + data["Close"]) / 3

# === Step 2: Pattern matching ===
def find_patterns(price_series, pattern_length):
    if len(price_series) < pattern_length + PRED_N_BARS:
        return []
    target = price_series[-pattern_length:].values
    matches = []
    for i in range(len(price_series) - pattern_length - PRED_N_BARS):
        window = price_series[i:i + pattern_length].values
        if len(window) == pattern_length:
            dist = euclidean(target, window)
            matches.append((i, dist))
    matches.sort(key=lambda x: x[1])
    return [i for i, _ in matches[:5]]

# === Step 3: Crea un frame PNG ===
def plot_projections(df, pattern_indices, frame_number):
    base = df["hlc3"].values
    if len(base) < LAST_N_BARS + PRED_N_BARS:
        return None

    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(base))
    ax.plot(x, base, label='HLC3', color='gray', alpha=0.5)

    for idx in pattern_indices:
        if idx + LAST_N_BARS + PRED_N_BARS > len(base):
            continue
        pattern = base[idx:idx + LAST_N_BARS]
        projection = base[idx + LAST_N_BARS: idx + LAST_N_BARS + PRED_N_BARS]

        x_pattern = np.arange(idx, idx + LAST_N_BARS)
        x_proj = np.arange(idx + LAST_N_BARS, idx + LAST_N_BARS + PRED_N_BARS)

        ax.plot(x_pattern, pattern, color='blue', linewidth=1)
        ax.plot(x_proj, projection, color='green', linestyle='--', linewidth=2)

    current = base[-LAST_N_BARS:]
    x_current = np.arange(len(base) - LAST_N_BARS, len(base))
    if len(current) == len(x_current):
        ax.plot(x_current, current, color='black', linewidth=2, label='Current pattern')

    ax.set_title(f"Frame {frame_number} — Pattern Matching")
    ax.legend()
    fig.tight_layout()

    # Salva frame
    os.makedirs(FRAME_DIR, exist_ok=True)
    fname = os.path.join(FRAME_DIR, f"frame_{frame_number:03d}.png")
    fig.savefig(fname)
    plt.close(fig)
    return fname

# === Step 4: Genera i frame ===
frame_files = []
for i in range(GIF_N_BARS):
    sub_df = data.iloc[:-(GIF_N_BARS - i)]
    if len(sub_df) < LAST_N_BARS + PRED_N_BARS:
        continue
    indices = find_patterns(sub_df["hlc3"], LAST_N_BARS)
    if not indices:
        continue
    path = plot_projections(sub_df, indices, i)
    if path:
        frame_files.append(path)

# === Step 5: Crea GIF animata da PNG ===
if frame_files:
    images = [Image.open(f) for f in frame_files]
    images[0].save(
        GIF_FNAME,
        save_all=True,
        append_images=images[1:],
        duration=int(1000 // GIF_FPS),
        loop=0
    )
    print(f"✅ GIF salvata come {GIF_FNAME} con {len(images)} frame.")
else:
    print("⚠️ Nessun frame valido trovato per generare la GIF.")
