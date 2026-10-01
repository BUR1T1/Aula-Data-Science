import numpy as np
import pandas as pd
from scipy import stats

np.random.seed(42)

ticket_A = np.random.normal(loc=1200, scale=350, size=500)
ticket_B = np.random.normal(loc=1220, scale=40, size=500)

df = pd.DataFrame({
    "versao": ["A"] * 500 + ["B"] * 500,
    "ticket": np.concatenate([ticket_A, ticket_B])
})

grupo_A = df[df["versao"] == "A"]["ticket"]
grupo_B = df[df["versao"] == "B"]["ticket"]

estatistica, p_valor = stats.ttest_ind(grupo_A, grupo_B)

print("Média A:", grupo_A.mean())
print("Média B:", grupo_B.mean())
print("P-valor:", p_valor)

if p_valor < 0.05:
    print("Rejeita H0: há evidência de diferença.")
else:
    print("Não rejeita H0: a diferença pode ser ruído amostral.")
