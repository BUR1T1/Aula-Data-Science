import pandas as pd

df = pd.DataFrame({
    "Nome": ["Ana", "Bruno", "Carla", "Diego"],
    "Idade": [22, 31, 27, 40],
    "Regiao": ["Sul", "Sudeste", "Sul", "Nordeste"],
    "Gasto": [150.0, 220.0, 190.0, 310.0]
})

print("HEAD")
print(df.head())

print("\nDESCRIBE")
print(df.describe())

print("\nMEDIA")
print(df["Gasto"].mean())

print("\nMEDIANA")
print(df["Gasto"].median())

print("\nMODA DA REGIAO")
print(df["Regiao"].mode()[0])

print("\nFILTRO")
print(df[df["Idade"] > 30])

print("\nGROUPBY")
print(df.groupby("Regiao")["Gasto"].mean())
