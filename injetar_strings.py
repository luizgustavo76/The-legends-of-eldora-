import os

ARQUIVO_TRADUCAO = ""
PASTA_CODIGO = "."  # pasta onde está o TLOE
EXTENSOES = (".py",)
selecionar_arquivo = input("qual é o arquivo?")
ARQUIVO_TRADUCAO = selecionar_arquivo
# carrega mapa de tradução
mapa = {}
with open(ARQUIVO_TRADUCAO, "r", encoding="utf-8") as f:
    for linha in f:
        if "|||" in linha:
            pt, en = linha.rstrip().split("|||", 1)
            mapa[pt] = en

# percorre arquivos
for root, _, files in os.walk(PASTA_CODIGO):
    for nome in files:
        if nome.endswith(EXTENSOES):
            caminho = os.path.join(root, nome)

            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read()

            original = conteudo

            for pt, en in mapa.items():
                conteudo = conteudo.replace(f'"{pt}"', f'"{en}"')
                conteudo = conteudo.replace(f"'{pt}'", f"'{en}'")

            if conteudo != original:
                with open(caminho, "w", encoding="utf-8") as f:
                    f.write(conteudo)

                print(f"[OK] Traduzido:", caminho)
