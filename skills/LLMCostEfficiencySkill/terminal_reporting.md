# Relatórios de Economia no Terminal

Este módulo define o padrão visual para exibir a economia de tokens e recursos após cada execução de prompt.

## Padrão de Exibição

Sempre que a `LLMCostEfficiencySkill` for aplicada, o assistente deve incluir um bloco de "Economia de LLM" ao final da resposta (ou no terminal, se aplicável).

### Formato Sugerido:

```text
---
📊 LLM Savings Report:
- 📥 Entrada Otimizada: [X] tokens economizados (via context filter/conciseness)
- 💾 Cache Utilization: [Y] tokens recuperados de cache
- ⚡ Eficiência de Ferramentas: [Z] chamadas de ferramentas evitadas
- 💰 Economia Estimada: [Valor/Porcentagem]% em relação ao prompt padrão
---
```

## Diretrizes de Cálculo (Estimativa)

Como o assistente não tem acesso em tempo real ao custo monetário exato de cada API, as seguintes heurísticas devem ser usadas:

1. **Entrada Otimizada**: Diferença estimada entre enviar um arquivo inteiro vs. apenas o trecho necessário.
2. **Cache**: Uso de `Context Caching` ou repetição de blocos de contexto conhecidos.
3. **Eficiência de Ferramentas**: Quando um comando de terminal substitui uma pesquisa longa da LLM.

## Exemplo de Uso Real

*Usuário: "Analise este arquivo de 5000 linhas."*
*Assistente: (Lê apenas as 50 linhas relevantes usando `grep`)*

**Saída final:**
> 📊 **LLM Savings Report:**
> - 📥 **Entrada Otimizada**: ~4950 tokens economizados (leitura seletiva)
> - ⚡ **Eficiência de Ferramentas**: Uso de `grep` evitou processamento de texto massivo.
> - 💰 **Economia Estimada**: 98% de redução no payload inicial.
