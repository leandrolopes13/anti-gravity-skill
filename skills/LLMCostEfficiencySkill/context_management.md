# Gerenciamento de Contexto

O gerenciamento inteligente da janela de contexto evita que o custo escale rapidamente conforme a conversa progride.

## 1. Chunking e Carregamento Parcial
- **Leia apenas trechos**: Use ferramentas como `view_file` com `StartLine` e `EndLine` para ler apenas a parte do arquivo necessária.
- **Resumos de arquitetura**: Mantenha um documento de arquitetura leve (como um KI) para dar contexto global sem precisar ler toda a estrutura de pastas todas as vezes.

## 2. Redefinição de Contexto (Context Reset)
Se a tarefa mudar drasticamente (ex: de refatorar o backend para debugar o CSS), considere informar que os arquivos anteriores podem ser "esquecidos" do contexto ativo, ou resuma o progresso atual em um artefato e reinicie a lógica.

## 3. Evite Redundância de Arquivos
Não peça para a LLM ler o mesmo arquivo várias vezes em turnos seguidos se ele não mudou. A LLM "lembra" do conteúdo (dentro da janela de contexto), então referenciar o nome do arquivo e a mudança desejada é suficiente.

## 4. Compactação de Informação
Ao transferir dados entre conversas ou agentes:
- Use siglas ou abreviações documentadas.
- Remova espaços em branco extras em payloads JSON.
- Substitua caminhos absolutos longos por relativos ou aliases se o contexto permitir.
