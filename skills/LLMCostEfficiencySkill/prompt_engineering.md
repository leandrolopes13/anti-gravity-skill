# Prompt Engineering para Eficiência

Escrever prompts curtos e precisos é a forma mais direta de economizar tokens de entrada.

## 1. Elimine a Cortesia Desnecessária
Modelos de linguagem não precisam de "Por favor", "Olá" ou "Espero que esteja bem". Vá direto ao ponto.
- **Ruim**: "Olá, tudo bem? Você poderia por favor me ajudar a refatorar esta função para que ela fique mais limpa usando o padrão early return?"
- **Bom**: "Refatore a função usando early return."

## 2. Instruções de Formato Negativas
Use instruções para evitar que a LLM gere texto redundante.
- "Apenas o código."
- "Sem explicações."
- "Dê a resposta em uma única linha."

## 3. Delimitadores Claros
Use delimitadores (como triple backticks ` ``` ` ou tags XML) para separar instruções de dados. Isso ajuda o modelo a processar a informação mais rápido com menos necessidade de "atenção" em partes irrelevantes.

## 4. One-Shot ou Few-Shot vs Zero-Shot
Às vezes, dar um exemplo único (One-Shot) gasta mais tokens inicialmente, mas evita que a LLM erre e precise ser corrigida (o que gastaria muito mais tokens em múltiplas rodadas).

## 5. Token Pruning (Poda de Tokens)
Se você está colando logs ou erros, remova timestamps repetitivos, IDs de transação irrelevantes ou stack traces de bibliotecas externas se o erro estiver claramente no seu código.

## 6. Otimização de Idioma (Inglês vs Português)
Embora a skill seja documentada em Português, tenha em mente que a maioria dos tokenizers (como o do GPT-4 ou Gemini) são mais eficientes em Inglês.
- O mesmo comando em Inglês costuma gastar de 10% a 20% menos tokens que em Português devido à forma como as palavras são quebradas.
- **Dica**: Para tarefas puramente técnicas (ex: "Refactor this code"), use comandos em Inglês se o custo for crítico.
