import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Email for assignment tracking
# 23f1001792@ds.study.iitm.ac.in

# -------------------------------
# Generate synthetic monthly data
# -------------------------------
np.random.seed(42)

months = pd.date_range(start="2023-01-01", periods=12, freq='M')
segments = ["Premium", "Standard", "Budget"]

data = []

for segment in segments:
    base = np.random.uniform(50_000, 120_000)
    seasonal = 10_000 * np.sin(np.linspace(0, 2*np.pi, 12))   # seasonal pattern
    noise = np.random.normal(0, 5_000, 12)                    # realistic noise
    revenue = base + seasonal + noise
    for m, r in zip(months, revenue):
        data.append([m, segment, max(r, 0)])  # no negative revenue

df = pd.DataFrame(data, columns=["Month", "Segment", "Revenue"])

# -------------------------------
# Professional Seaborn styling
# -------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # larger labels for presentations

# -------------------------------
# Create the 512x512 figure
# -------------------------------
plt.figure(figsize=(8, 8))  # 8x8 inches * 64 dpi = 512x512 pixels

sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    hue="Segment",
    palette="Set2",
    linewidth=2.5
)

plt.title("Monthly Revenue Trends by Customer Segment", fontsize=18)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Revenue (USD)", fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

# -------------------------------
# Save as required
# -------------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
