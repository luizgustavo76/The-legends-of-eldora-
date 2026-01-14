import tokenize
from io import BytesIO
import os

def extrair_strings_de_arquivo(caminho_arquivo: str):
    """
    Lê um arquivo Python (.py) e retorna todas as strings encontradas.
    """
    if not os.path.isfile(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")
    if not caminho_arquivo.endswith(".py"):
        raise ValueError("O arquivo deve ter extensão .py")

    strings_encontradas = []
    try:
        with open(caminho_arquivo, "rb") as f:
            tokens = tokenize.tokenize(f.readline)
            for toknum, tokval, _, _, _ in tokens:
                if toknum == tokenize.STRING:
                    # Remove aspas externas
                    valor_limpo = tokval
                    if (valor_limpo.startswith(("'", '"')) or
                        valor_limpo.startswith(("'''", '"""'))):
                        valor_limpo = valor_limpo.strip("'\"")
                    strings_encontradas.append(valor_limpo)
    except tokenize.TokenError as e:
        print(f"Erro ao processar código: {e}")
    return strings_encontradas

if __name__ == "__main__":
    caminho = input("Digite o caminho do arquivo .py: ").strip()
    try:
        resultado = extrair_strings_de_arquivo(caminho)
        print("\nStrings encontradas:")
        if resultado:
            for s in resultado:
                print(f"- {s}")
        else:
            print("Nenhuma string encontrada.")
    except (FileNotFoundError, ValueError) as e:
        print(f"Erro: {e}")
