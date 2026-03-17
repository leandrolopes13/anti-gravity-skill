# Estratégias de Economia de Tokens

Para economizar no consumo de LLM, a regra de ouro é: **Pense antes de agir e transfira apenas o necessário.**

## 1. O Princípio da Necessidade
- **Leia apenas o que vai usar**: Evite ler arquivos inteiros se apenas uma função ou classe for relevante.
- **Seja seletivo no contexto**: Não envie o histórico completo da conversa se apenas as últimas mensagens forem suficientes.

## 2. Antecipação e Cache Mental
- **Valide localmente**: Antes de pedir para a LLM verificar um erro, tente rodar um comando de lint ou um teste local que possa identificar o problema mais rápido e "de graça".
- **Agrupe tarefas**: Em vez de fazer 10 perguntas pequenas, tente consolidar dúvidas relacionadas em uma única chamada estruturada.

## 3. Saída Concisa
- **Peça por brevidade**: Instrua a LLM a ser direta. Ex: "Resuma em 3 pontos", "Dê apenas o código, sem explicações".
- **Formatos leves**: Use Markdown simples ou JSON compacto em vez de textos explicativos longos quando o objetivo for apenas extração de dados.

## 4. Otimização de Ferramentas
- **Use `grep_search` e `find_by_name`**: Use ferramentas de busca no sistema de arquivos para encontrar arquivos específicos em vez de listar diretórios recursivamente (`list_dir`) em níveis muito profundos.
