# Eficiência de Ferramentas (Tool Efficiency)

Para economizar tokens, escolha a ferramenta com o menor "custo" de entrada e saída.

## 🟢 Ferramentas Baratas (Alta Eficiência)
Use estas ferramentas sempre que possível para filtrar informações antes de trazê-las para o contexto.

- **`grep_search`**: Ideal para encontrar ocorrências específicas sem ler arquivos inteiros.
- **`find_by_name`**: Ótima para localizar arquivos em estruturas complexas sem listar todos os diretórios.
- **`command_status`**: Permite monitorar tarefas longas sem que o output flua constantemente para o terminal.
- **`list_dir` (Nível 1)**: Listar apenas a raiz ou um nível específico é barato.

## 🟡 Ferramentas Moderadas
Use com cautela em arquivos ou diretórios grandes.

- **`view_file` (com StartLine/EndLine)**: É muito mais eficiente ler as linhas 100-200 do que o arquivo todo.
- **`run_command`**: O custo depende totalmente do output do comando. Use pipes (`| head -n 20`) se o output for grande.

## 🔴 Ferramentas Caras (Baixa Eficiência)
Evite usar estas ferramentas em grandes volumes de dados de uma só vez.

- **`list_dir` (Recursivo/MaxDepth alto)**: Listar milhares de arquivos consome muita janela de contexto.
- **`view_file` (Arquivos Inteiros > 500 linhas)**: Traz muito ruído se você só precisa de uma parte.
- **`read_url_content`**: Sites modernos podem ter milhares de linhas de HTML/Markdown escondendo pouca informação útil.

## Estratégia Recomendada
1. Use `find_by_name` para achar o arquivo.
2. Use `grep_search` para achar a linha ou função.
3. Use `view_file` com `StartLine` e `EndLine` para ler apenas o trecho necessário.
