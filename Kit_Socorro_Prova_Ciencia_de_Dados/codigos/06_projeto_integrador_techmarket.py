import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score

sns.set_theme(style="whitegrid")
np.random.seed(42)

# =========================================================
# 1. BASE
# =========================================================
n_clientes = 1000

idades = np.random.randint(18, 65, n_clientes)
emails = [f"cliente_{i}@email.com" for i in range(n_clientes)]
regioes = np.random.choice(
    ["Sul", "Sudeste", "Nordeste"],
    n_clientes,
    p=[0.2, 0.5, 0.3]
)
versoes = np.random.choice(["A", "B"], n_clientes)

tempo_A = np.random.normal(15, 5, 500)
tempo_B = np.random.normal(17, 5, 500)
tempo_tela = np.concatenate([tempo_A, tempo_B])
np.random.shuffle(tempo_tela)

gasto = (tempo_tela * 25) + 150 + np.random.normal(0, 100, n_clientes)

# Anomalias didáticas
gasto[10] = 9500
gasto[50] = 8800

df = pd.DataFrame({
    "Idade": idades,
    "Email": emails,
    "Regiao": regioes,
    "Versao_Site": versoes,
    "Tempo_Tela_Min": np.abs(tempo_tela),
    "Gasto_Site_R$": np.abs(gasto)
})

# =========================================================
# 2. LGPD / MINIMIZAÇÃO
# =========================================================
df_seguro = df.drop(columns=["Email"])

# =========================================================
# 3. ESTATÍSTICA DESCRITIVA
# =========================================================
print("\nREGIÃO MAIS FREQUENTE")
print(df_seguro["Regiao"].mode()[0])

print("\nGASTO MÉDIO")
print(df_seguro["Gasto_Site_R$"].mean())

print("\nGASTO MEDIANO")
print(df_seguro["Gasto_Site_R$"].median())

# =========================================================
# 4. VISUALIZAÇÃO
# =========================================================
sns.barplot(data=df_seguro, x="Regiao", y="Gasto_Site_R$")
plt.title("Gasto médio por região")
plt.show()

sns.boxplot(data=df_seguro, y="Gasto_Site_R$")
plt.title("Boxplot do gasto")
plt.show()

# =========================================================
# 5. TESTE A/B
# =========================================================
tempo_A = df_seguro[
    df_seguro["Versao_Site"] == "A"
]["Tempo_Tela_Min"]

tempo_B = df_seguro[
    df_seguro["Versao_Site"] == "B"
]["Tempo_Tela_Min"]

t_stat, p_valor = stats.ttest_ind(tempo_A, tempo_B)

print("\nTESTE A/B")
print("p-valor:", p_valor)

if p_valor < 0.05:
    print("Rejeita H0.")
else:
    print("Não rejeita H0.")

# =========================================================
# 6. CORRELAÇÃO
# =========================================================
r = df_seguro["Tempo_Tela_Min"].corr(
    df_seguro["Gasto_Site_R$"]
)

print("\nCORRELAÇÃO")
print(r)

sns.scatterplot(
    data=df_seguro,
    x="Tempo_Tela_Min",
    y="Gasto_Site_R$",
    alpha=0.3
)
plt.title("Tempo de tela x gasto")
plt.show()

# =========================================================
# 7. LIMPEZA DE OUTLIERS PARA O MODELO
# =========================================================
df_limpo = df_seguro[
    df_seguro["Gasto_Site_R$"] < 8000
]

# =========================================================
# 8. REGRESSÃO
# =========================================================
X = df_limpo[["Tempo_Tela_Min"]]
y = df_limpo["Gasto_Site_R$"]

modelo = LinearRegression()
modelo.fit(X, y)

pred = modelo.predict(X)

r2 = r2_score(y, pred)
rmse = root_mean_squared_error(y, pred)

print("\nMODELO")
print("Coeficiente:", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)
print("R²:", r2)
print("RMSE:", rmse)

# =========================================================
# 9. PRODUÇÃO
# =========================================================
previsao = modelo.predict([[45]])[0]
piso = previsao - rmse
teto = previsao + rmse

print("\nPREVISÃO PARA 45 MIN")
print(f"Piso: R$ {piso:.2f}")
print(f"Previsão: R$ {previsao:.2f}")
print(f"Teto: R$ {teto:.2f}")
