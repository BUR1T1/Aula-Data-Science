import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score

np.random.seed(42)

tempo = np.random.uniform(1, 60, 300)
gasto = 25 * tempo + 150 + np.random.normal(0, 100, 300)

df = pd.DataFrame({
    "Tempo_Tela_Min": tempo,
    "Gasto_Site_R$": gasto
})

X = df[["Tempo_Tela_Min"]]
y = df["Gasto_Site_R$"]

modelo = LinearRegression()
modelo.fit(X, y)

pred = modelo.predict(X)

r2 = r2_score(y, pred)
rmse = root_mean_squared_error(y, pred)

print("Coeficiente:", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)
print("R²:", r2)
print("RMSE:", rmse)

previsao = modelo.predict([[45]])[0]
piso = previsao - rmse
teto = previsao + rmse

print(f"\n45 minutos:")
print(f"Previsão: R$ {previsao:.2f}")
print(f"Piso operacional: R$ {piso:.2f}")
print(f"Teto operacional: R$ {teto:.2f}")
