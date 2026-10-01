# TEMPLATE DE RESOLUÇÃO
# Troque os nomes das colunas conforme o enunciado.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score

# 1. INSPEÇÃO
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)

# 2. ESTATÍSTICA
print(df["valor"].mean())
print(df["valor"].median())
print(df["valor"].std())

# 3. GRÁFICO
sns.boxplot(data=df, y="valor")
plt.show()

# 4. TESTE A/B
A = df[df["grupo"] == "A"]["valor"]
B = df[df["grupo"] == "B"]["valor"]

t, p = stats.ttest_ind(A, B)

if p < 0.05:
    print("Rejeita H0")
else:
    print("Não rejeita H0")

# 5. CORRELAÇÃO
print(df["x"].corr(df["y"]))

# 6. REGRESSÃO
X = df[["x"]]
y = df["y"]

modelo = LinearRegression()
modelo.fit(X, y)

pred = modelo.predict(X)

print("R²:", r2_score(y, pred))
print("RMSE:", root_mean_squared_error(y, pred))
print("Novo caso:", modelo.predict([[45]])[0])
