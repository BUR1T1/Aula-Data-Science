# 05 - Correlação, Covariância e Causalidade

## Scatterplot primeiro

```python
sns.scatterplot(data=df, x='X', y='Y')
plt.show()
```

Procure:

- nuvem ascendente -> tendência positiva;
- nuvem descendente -> tendência negativa;
- nuvem sem padrão -> relação linear fraca ou ausente.

## Pearson

```python
r = df['X'].corr(df['Y'], method='pearson')
```

Interpretação:

- próximo de +1 -> relação linear positiva forte;
- próximo de -1 -> relação linear negativa forte;
- próximo de 0 -> pouca relação linear.

## Fórmula conceitual

```text
r = Cov(X,Y) / (sx * sy)
```

## Spearman

```python
rho = df['X'].corr(df['Y'], method='spearman')
```

Spearman trabalha com ranking e é útil para relações monotônicas.

## Pearson x Spearman

```python
pearson = df['X'].corr(df['Y'], method='pearson')
spearman = df['X'].corr(df['Y'], method='spearman')
```

Nos materiais, uma curva `y = x³` é usada para mostrar que uma relação pode ser fortemente monotônica sem ser perfeitamente representada por uma reta.

## Matriz de correlação

```python
matriz = df.corr(numeric_only=True)
print(matriz['Preco'].sort_values(ascending=False))
```

## Regra de ouro

Correlação não implica causalidade.

Uma terceira variável pode explicar o movimento conjunto de duas outras variáveis.

Exemplo didático do material:

- vendas de sorvete sobem;
- incidentes com tubarões sobem;
- isso não significa que sorvete causa ataques;
- temperatura/verão pode ser uma variável oculta.
