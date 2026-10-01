# 07 - LGPD, Governança e Segurança

## Tríade CIA

### Confidencialidade

Dados só devem ser acessados por quem tem autorização.

### Integridade

Dados não devem ser alterados de forma indevida.

### Disponibilidade

Dados e sistemas devem estar acessíveis quando necessários.

## Princípios trabalhados

### Finalidade

A coleta precisa de propósito claro.

### Adequação

Os dados usados devem ser compatíveis com a finalidade informada.

### Minimização

Coletar/manter apenas o mínimo necessário.

## Exemplo prático

Se a análise não precisa de e-mail:

```python
df_seguro = df.drop(columns=['Email'])
```

## Dado pessoal

Informação que identifica ou pode identificar uma pessoa.

Exemplos trabalhados:
- nome;
- CPF;
- e-mail;
- telefone;
- IP/geolocalização.

## Dado sensível

Categoria que exige maior cuidado de proteção por envolver informações de maior risco de discriminação ou impacto.

## Pergunta provável

> O modelo precisa prever faturamento, mas a base contém e-mail.

Resposta esperada:
- retirar o e-mail da base analítica quando ele não é necessário;
- justificar pela minimização e pela finalidade.
