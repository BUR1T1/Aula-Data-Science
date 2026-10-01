# 04 - Inferência, Teste A/B e P-Valor

## Estatística descritiva x inferência

Descritiva:
- resume o que aconteceu na amostra.

Inferência:
- usa a amostra para avaliar evidências e generalizar com incerteza.

## Teste A/B

Exemplo:

- Versão A = interface atual.
- Versão B = nova interface.

Hipóteses:

```text
H0: não existe diferença entre A e B.
H1: existe diferença entre A e B.
```

## Código

```python
from scipy import stats

grupo_A = df[df['versao'] == 'A']['ticket']
grupo_B = df[df['versao'] == 'B']['ticket']

estatistica, p_valor = stats.ttest_ind(grupo_A, grupo_B)

if p_valor < 0.05:
    print('Rejeita H0: há evidência de diferença')
else:
    print('Não rejeita H0: não há evidência suficiente de diferença')
```

## A regra de 5%

```text
p < 0,05  -> rejeita H0
p >= 0,05 -> não rejeita H0
```

## Cuidado de interpretação

Não diga:

> H0 foi provada.

Prefira:

> Não encontramos evidência estatística suficiente para rejeitar H0.

## Média maior não é suficiente

Mesmo que B tenha média maior que A, a diferença pode ser explicada pelo acaso ou pela variabilidade.

Por isso usamos um teste estatístico.

## Limpeza e novo teste

Nos materiais, uma missão aplica IQR para remover anomalias e refaz o teste T.

Isso serve para observar como ruído e outliers podem alterar a análise.
