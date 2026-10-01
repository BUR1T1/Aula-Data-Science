# 08 - Erros Comuns e Depuração

## NameError

```text
NameError: name 'pd' is not defined
```

Provável causa: import não executado.

```python
import pandas as pd
```

## KeyError

```text
KeyError: 'Gasto'
```

Cheque:

```python
print(df.columns)
```

## X em formato errado no sklearn

Pode acontecer se fizer:

```python
X = df['Tempo']
```

Use:

```python
X = df[['Tempo']]
```

## Filtro com and/or

Errado:

```python
df[df['x'] > 10 and df['x'] < 20]
```

Certo:

```python
df[(df['x'] > 10) & (df['x'] < 20)]
```

## Gráfico não aparece

```python
plt.show()
```

## Correlação com colunas de texto

Use:

```python
df.corr(numeric_only=True)
```

## Dados nulos

```python
df.isna().sum()
```

## Modelo treinado com outlier absurdo

Inspecione:

```python
sns.boxplot(data=df, y='Gasto')
plt.show()
```

Depois filtre apenas se o exercício justificar.
