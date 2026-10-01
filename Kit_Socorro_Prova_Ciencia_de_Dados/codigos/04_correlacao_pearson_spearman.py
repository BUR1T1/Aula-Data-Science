import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = np.arange(1, 20)
y = x ** 3

df = pd.DataFrame({"X": x, "Y": y})

pearson = df["X"].corr(df["Y"], method="pearson")
spearman = df["X"].corr(df["Y"], method="spearman")

print(f"Pearson: {pearson:.4f}")
print(f"Spearman: {spearman:.4f}")

sns.scatterplot(data=df, x="X", y="Y")
plt.title("Relação monotônica não perfeitamente linear")
plt.show()
