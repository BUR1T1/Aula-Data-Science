# 10 - Gabarito Comentado

## 1

```python
df.head()
```

## 2

```python
df.shape
```

## 3

```python
df['valor'].mean()
df['valor'].median()
df['valor'].mode()[0]
df['valor'].std()
```

## 4

```python
df[df['Idade'] > 30]
```

## 5

```python
df.groupby('Regiao')['Gasto'].mean()
```

## 6

```python
df_seguro = df.drop(columns=['Email'])
```

## 7

A média é sensível a valores extremos. Um único valor muito alto pode puxá-la para cima.

## 8

```python
q1 = df['valor'].quantile(0.25)
q2 = df['valor'].quantile(0.50)
q3 = df['valor'].quantile(0.75)
```

## 9

```python
iqr = q3 - q1
```

## 10

```python
li = q1 - 1.5 * iqr
ls = q3 + 1.5 * iqr
```

## 11

```python
df_limpo = df[(df['valor'] >= li) & (df['valor'] <= ls)]
```

## 12-16

```python
sns.countplot(data=df, x='Regiao')
sns.barplot(data=df, x='Regiao', y='Gasto')
sns.boxplot(data=df, y='Gasto')
sns.scatterplot(data=df, x='Tempo', y='Gasto')
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()
```

## 17

```text
H0: não há diferença.
H1: há diferença.
```

## 18-19

```python
A = df[df['grupo'] == 'A']['valor']
B = df[df['grupo'] == 'B']['valor']

t, p = stats.ttest_ind(A, B)
```

## 20

p = 0,03 < 0,05 -> rejeita H0.

## 21

p = 0,42 >= 0,05 -> não rejeita H0.

## 22

A diferença observada pode ser ruído amostral. É necessário analisar a incerteza.

## 23

0,80 indica forte relação linear positiva.

## 24

-0,75 indica forte relação linear negativa.

## 25

0,04 indica relação linear praticamente inexistente.

## 26

Duas variáveis podem se mover juntas por coincidência ou por uma terceira variável.

## 27

Spearman é útil quando a relação é monotônica/rankeada e não necessariamente linear.

## 28-30

```python
X = df[['Tempo']]
y = df['Gasto']

modelo = LinearRegression()
modelo.fit(X, y)

pred = modelo.predict(X)
novo = modelo.predict([[45]])[0]
```

## 31

`coef_` é a inclinação/peso da reta.

## 32

`intercept_` é o valor base da reta quando x = 0.

## 33

R² representa a parcela da variabilidade de y explicada pelo modelo.

## 34

RMSE mede o tamanho típico do erro na unidade aproximada do alvo.

## 35

```python
previsao = modelo.predict([[45]])[0]
```

## 36

CIA = confidencialidade, integridade e disponibilidade.

## 37

Dado pessoal identifica ou pode identificar uma pessoa. Dado sensível exige proteção reforçada.

## 38-40

- Finalidade: propósito claro.
- Adequação: uso compatível com o propósito.
- Minimização: manter apenas o necessário.
