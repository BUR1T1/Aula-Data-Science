# 02 - Estatística Descritiva e Outliers

## Média

```python
media = df['Gasto'].mean()
```

A média é sensível a valores extremos.

Exemplo:

```text
100, 110, 120, 130, 5000
```

O 5000 puxa a média para cima.

## Mediana

```python
mediana = df['Gasto'].median()
```

É o valor central da base ordenada e tende a resistir melhor a outliers.

## Moda

```python
moda = df['Regiao'].mode()[0]
```

É o valor mais frequente.

## Variância

```python
variancia = df['Gasto'].var()
```

Mede dispersão em unidade ao quadrado.

## Desvio padrão

```python
desvio = df['Gasto'].std()
```

Quanto maior, mais espalhados estão os dados.

## Quartis

- Q1 = 25%
- Q2 = 50% = mediana
- Q3 = 75%

```python
q1 = df['Gasto'].quantile(0.25)
q2 = df['Gasto'].quantile(0.50)
q3 = df['Gasto'].quantile(0.75)
```

## IQR

```python
iqr = q3 - q1
```

Limites:

```python
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
```

Filtrando:

```python
df_limpo = df[
    (df['Gasto'] >= limite_inferior) &
    (df['Gasto'] <= limite_superior)
]
```

## Interpretação provável de prova

Se média e mediana são muito diferentes, suspeite de assimetria e/ou outliers.

Não remova outliers automaticamente em qualquer problema. Nos exercícios das aulas, a remoção é feita quando há justificativa de ruído/anomalia e isso faz parte da missão proposta.
