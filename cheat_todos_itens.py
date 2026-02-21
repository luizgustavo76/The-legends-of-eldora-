import json
import os

CAMINHO_SAVE = "codigo tloe/tloe_save.json"

print("CAMINHO REAL DO SAVE:")
print(os.path.abspath(CAMINHO_SAVE))

with open(CAMINHO_SAVE, "r", encoding="utf-8") as f:
    dados = json.load(f)

for item in dados["salvamento_dados"]:
    dados["salvamento_dados"][item] = 9999

with open(CAMINHO_SAVE, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)

print("ESCRITO.")
