# 03 - Visualização de Dados

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

## Countplot

Contagem de categorias:

```python
sns.countplot(data=df, x='Regiao')
plt.show()
```

## Barplot

Comparação de uma medida numérica entre categorias:

```python
sns.barplot(data=df, x='Regiao', y='Gasto')
plt.show()
```

## Boxplot

Distribuição, quartis e possíveis outliers:

```python
sns.boxplot(data=df, y='Gasto')
plt.show()
```

Por grupo:

```python
sns.boxplot(data=df, x='Versao', y='Ticket')
plt.show()
```

## Histplot

```python
sns.histplot(data=df, x='Gasto', kde=True)
plt.show()
```

## Scatterplot

Duas variáveis numéricas:

```python
sns.scatterplot(
    data=df,
    x='Tempo_Tela_Min',
    y='Gasto_Site_R$',
    alpha=0.3
)
plt.show()
```

## Lineplot

Série temporal:

```python
sns.lineplot(data=df, x='Data', y='Faturamento')
plt.show()
```

## Heatmap

```python
matriz = df.corr(numeric_only=True)

sns.heatmap(
    matriz,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)
plt.show()
```

## Regra mental

- categoria pura -> countplot
- categoria + número -> barplot
- distribuição/outlier -> boxplot
- tempo -> lineplot
- número x número -> scatterplot
- várias correlações -> heatmap
