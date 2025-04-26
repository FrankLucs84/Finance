import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

df = (
    yf.download(["NVDA", "AMD"], start="2020-01-01")
    .Close.pct_change(fill_method=None)
    .dropna()
)

def tail_ratio(returns):
    return abs(np.percentile(returns, 95)) / abs(np.percentile(returns, 5))


tail_ratio_a = tail_ratio(df.AMD)
tail_ratio_b = tail_ratio(df.NVDA)

print(f"Tail Ratio for AMD: {tail_ratio_a:.4f}")
print(f"Tail Ratio for NVDA: {tail_ratio_b:.4f}")

plt.figure(figsize=(10, 6))
plt.hist(df.AMD, bins=50, alpha=0.5, label='AMD')
plt.hist(df.NVDA, bins=50, alpha=0.5, label='NVDA')
plt.axvline(np.percentile(df.AMD, 5), color='r', linestyle='dashed', linewidth=2)
plt.axvline(np.percentile(df.AMD, 95), color='r', linestyle='dashed', linewidth=2)
plt.axvline(np.percentile(df.NVDA, 5), color='g', linestyle='dashed', linewidth=2)
plt.axvline(np.percentile(df.NVDA, 95), color='g', linestyle='dashed', linewidth=2)
plt.legend()
plt.title('Return Distributions with 5th and 95th Percentiles')
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.show()