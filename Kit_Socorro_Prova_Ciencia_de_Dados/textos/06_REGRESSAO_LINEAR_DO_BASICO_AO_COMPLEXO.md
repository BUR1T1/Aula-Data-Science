# 06 - Regressão Linear do Básico ao Complexo

## Ideia

Queremos prever `y` a partir de `x`.

Equação:

```text
ŷ = w1*x + w0
```

- `ŷ`: previsão.
- `x`: entrada.
- `w1`: coeficiente/inclinação.
- `w0`: intercepto/viés.

## Treinamento

```python
from sklearn.linear_model import LinearRegression

X = df[['Tempo_Tela_Min']]
y = df['Gasto_Site_R$']

modelo = LinearRegression()
modelo.fit(X, y)
```

## Por que dois colchetes em X?

```python
X = df[['Tempo_Tela_Min']]
```

O sklearn espera uma matriz 2D para as variáveis de entrada.

`y` pode continuar 1D:

```python
y = df['Gasto_Site_R$']
```

## Previsão

```python
pred = modelo.predict(X)
```

Novo caso:

```python
previsao = modelo.predict([[45]])[0]
```

## Coeficiente e intercepto

```python
print(modelo.coef_)
print(modelo.intercept_)
```

Se:

```text
coef = 25
intercepto = 150
```

então:

```text
ŷ = 25*x + 150
```

## R²

```python
from sklearn.metrics import r2_score

r2 = r2_score(y, pred)
```

R² indica quanto da variabilidade observada de `y` é explicada pelo modelo.

Não trate `R² = 0,80` como "80% de precisão".

## RMSE

```python
from sklearn.metrics import root_mean_squared_error

rmse = root_mean_squared_error(y, pred)
```

O RMSE fica aproximadamente na mesma unidade de `y`.

## Faixa operacional usada no exercício

```python
piso = previsao - rmse
teto = previsao + rmse
```

Essa faixa ±RMSE é uma aproximação operacional do exercício, não um intervalo de confiança formal.

## Fluxo completo

```python
df_limpo = df[df['Gasto_Site_R$'] < 8000]

X = df_limpo[['Tempo_Tela_Min']]
y = df_limpo['Gasto_Site_R$']

modelo = LinearRegression()
modelo.fit(X, y)

pred = modelo.predict(X)

r2 = r2_score(y, pred)
rmse = root_mean_squared_error(y, pred)

previsao = modelo.predict([[45]])[0]
```
