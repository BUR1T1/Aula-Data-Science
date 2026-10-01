# 00 - Mapa de Estudo

## Nível 1 - Sobrevivência

Domine:

```python
df.head()
df.info()
df.describe()

df['coluna'].mean()
df['coluna'].median()
df['coluna'].mode()[0]
df['coluna'].std()

df[df['coluna'] > valor]
df.groupby('grupo')['valor'].mean()
```

Se você entende esses comandos, já consegue resolver boa parte das questões introdutórias.

## Nível 2 - Diagnóstico

Aprenda:

- quartis;
- IQR;
- identificação de outliers;
- boxplot;
- histogramas;
- comparação entre grupos.

## Nível 3 - Inferência

Aprenda:

- H0 e H1;
- Teste A/B;
- `stats.ttest_ind`;
- p-valor;
- alfa = 0,05;
- diferença observada x diferença estatisticamente significativa.

## Nível 4 - Relações

Aprenda:

- scatterplot;
- covariância;
- Pearson;
- Spearman;
- correlação positiva, negativa e próxima de zero;
- correlação não implica causalidade;
- variáveis ocultas.

## Nível 5 - Previsão

Aprenda:

- X e y;
- `LinearRegression`;
- `fit`;
- `predict`;
- coeficiente;
- intercepto;
- R²;
- RMSE.

## Nível 6 - Governança

Aprenda:

- confidencialidade;
- integridade;
- disponibilidade;
- dado pessoal;
- dado sensível;
- finalidade;
- adequação;
- minimização.

## Mapa rápido: pergunta -> ferramenta

| Pergunta | Ferramenta |
|---|---|
| Quantos existem por categoria? | countplot / value_counts |
| Qual a média por grupo? | groupby / barplot |
| Onde estão os valores extremos? | boxplot / IQR |
| Como os valores se distribuem? | histplot |
| Duas variáveis numéricas se relacionam? | scatterplot / corr |
| A e B são realmente diferentes? | t-test / p-valor |
| Quero prever um valor | regressão linear |
| Dados identificáveis são necessários? | LGPD / minimização |
