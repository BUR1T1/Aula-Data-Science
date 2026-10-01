import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "ticket": [100, 110, 115, 120, 122, 125, 130, 132, 140, 900]
})

q1 = df["ticket"].quantile(0.25)
q2 = df["ticket"].quantile(0.50)
q3 = df["ticket"].quantile(0.75)
iqr = q3 - q1

li = q1 - 1.5 * iqr
ls = q3 + 1.5 * iqr

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("IQR:", iqr)
print("Limite inferior:", li)
print("Limite superior:", ls)

df_limpo = df[(df["ticket"] >= li) & (df["ticket"] <= ls)]

print("\nBase original:")
print(df)

print("\nBase limpa:")
print(df_limpo)

sns.boxplot(data=df, y="ticket")
plt.title("Boxplot - base original")
plt.show()
