# Tarefas Incrementais e Refatoração

Manter a janela de contexto "limpa" é a melhor forma de evitar alucinações e erros de custo alto.

## O Problema do Contexto Cumulativo
Em sessões longas, o histórico de mensagens cresce. Se você adicionar 5 arquivos grandes ao contexto e fizer 10 perguntas sobre eles, cada pergunta custará o peso de todos esses arquivos + o histórico.

## Metodologia de Incremento

### 1. "Atomic Commits" no Chat
Em vez de pedir "Faça todo o sistema de login", peça:
1. "Crie apenas a interface da Model de usuário."
2. "Agora implemente a função de hash de senha."
3. (Opcional) Peça ao assistente para esquecer os detalhes da etapa anterior se eles não forem mais necessários.

### 2. A Técnica do "Context Reset"
Se você percebeu que o contexto está muito grande (muitos arquivos abertos e logs), use a ferramenta `task_boundary` para resumir o que foi feito e comece uma nova fase com o "mínimo viável" de arquivos abertos.

### 3. Evite o Ciclo de Erro-Correção
Cada vez que você pede para "corrigir o erro" sem analisar a causa raiz, você gasta tokens.
- **Dica**: Use um comando de terminal para validar a sintaxe (`python -m py_compile` ou `eslint`) localmente antes de pedir a correção para a LLM.

### 4. Resumos de Progresso
Use artifacts (`task.md`) para rastrear o estado. Isso evita que você precise perguntar "O que está faltando?" (o que custaria tokens de processamento de todo o histórico).
