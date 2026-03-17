# Recursos Avançados de Modelos

Diferentes provedores de LLM oferecem recursos específicos que podem reduzir dramaticamente os custos se utilizados corretamente.

## 1. Context Caching (Gemini / Anthropic)
Se você envia repetidamente o mesmo conjunto grande de dados (documentação, código base, livros), use Context Caching.
- **Como funciona**: Você "congela" uma parte do contexto no servidor do provedor.
- **Vantagem**: Paga-se uma taxa de armazenamento menor e as chamadas subsequentes que usam esse cache são muito mais baratas e rápidas do que reenviar os tokens.

## 2. Batch APIs (OpenAI / Gemini)
Se a sua tarefa não precisa de resposta imediata (ex: processar 10.000 linhas de log), use Batch APIs.
- **Vantagem**: Geralmente oferece 50% de desconto no custo dos tokens em troca de um tempo de processamento de até 24 horas.

## 3. Model Steering (Roteamento de Modelos)
Nem toda tarefa precisa de um modelo "Frontier" (modelo mais potente e caro).
- **Classificação simples**: Use modelos menores e mais baratos (ex: Gemini Flash, GPT-4o-mini).
- **Raciocínio complexo**: Reserve os modelos maiores (ex: Gemini Pro, GPT-4o) para tarefas de arquitetura ou depuração lógica profunda.

## 4. Prompt Caching Automático
Alguns provedores aplicam cache automaticamente em prefixos de prompt idênticos. Mantenha as instruções sistêmicas e o contexto estático no início do seu prompt para maximizar as chances de hit no cache.
