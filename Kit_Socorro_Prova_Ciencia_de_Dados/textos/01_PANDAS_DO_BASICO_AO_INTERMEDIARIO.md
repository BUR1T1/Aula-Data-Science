# 01 - Pandas do Básico ao Intermediário

## Criando um DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carla'],
    'Idade': [22, 30, 27],
    'Gasto': [150, 220, 190]
})
```

## Inspeção

```python
df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns
```

### Quando usar

- `head()`: primeiras linhas.
- `info()`: tipos, nulos e quantidade de registros.
- `describe()`: resumo estatístico.
- `shape`: quantidade de linhas e colunas.
- `columns`: nomes das colunas.

## Selecionando

```python
df['Gasto']
df[['Idade', 'Gasto']]
```

## Filtrando

```python
df[df['Idade'] >= 25]
```

Duas condições:

```python
df[(df['Idade'] >= 20) & (df['Gasto'] > 180)]
```

OU:

```python
df[(df['Idade'] < 25) | (df['Gasto'] > 200)]
```

## Ordenando

```python
df.sort_values('Gasto')
df.sort_values('Gasto', ascending=False)
```

## Removendo coluna

```python
df_seguro = df.drop(columns=['Email'])
```

## Valores nulos

```python
df.isna().sum()
df.dropna()
df.fillna(0)
```

## Agrupamento

```python
df.groupby('Regiao')['Gasto'].mean()
```

Resumo completo:

```python
df.groupby('Versao')['Ticket'].describe()
```

## Erros comuns

### KeyError

```python
print(df.columns)
```

Confira o nome exato.

### `and` / `or` em filtros

Errado:

```python
df[df['Idade'] > 18 and df['Idade'] < 30]
```

Certo:

```python
df[(df['Idade'] > 18) & (df['Idade'] < 30)]
```
