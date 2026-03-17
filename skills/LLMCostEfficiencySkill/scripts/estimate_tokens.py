import sys
import os

def estimate_tokens(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"Erro: Arquivo {file_path} não encontrado.")
            return

        size = os.path.getsize(file_path)
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            char_count = len(content)
            word_count = len(content.split())
            
        # Heurística comum: 1 token ~= 4 caracteres para Inglês
        # Para código e Português, a proporção costuma ser menor (~3 caracteres por token)
        tokens_pt_code = char_count / 3
        tokens_en = char_count / 4

        print(f"--- Estimativa de Tokens para: {os.path.basename(file_path)} ---")
        print(f"Tamanho: {size} bytes")
        print(f"Caracteres: {char_count}")
        print(f"Palavras: {word_count}")
        print(f"Tokens Estimados (Código/PT): ~{int(tokens_pt_code)}")
        print(f"Tokens Estimados (EN): ~{int(tokens_en)}")
        print("--------------------------------------------------")
        
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python estimate_tokens.py <caminho_do_arquivo>")
    else:
        estimate_tokens(sys.argv[1])
