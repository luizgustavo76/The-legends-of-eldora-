pt_file = "strings_tloe.txt"
<<<<<<< HEAD
en_file = "strings_tloe - English.txt"
=======
en_file = "strings_tloe.pt.en.txt"
>>>>>>> e19656e9f0b10e030925b7e7ba56be12c65a006f
saida = "traducao.txt"

with open(pt_file, "r", encoding="utf-8") as f:
    pt_linhas = [l.rstrip("\n") for l in f]

with open(en_file, "r", encoding="utf-8") as f:
    en_linhas = [l.rstrip("\n") for l in f]

if len(pt_linhas) != len(en_linhas):
    print("ERRO: arquivos têm tamanhos diferentes!")
    print(len(pt_linhas), "vs", len(en_linhas))
    exit()

with open(saida, "w", encoding="utf-8") as f:
    for pt, en in zip(pt_linhas, en_linhas):
        if pt and en:
            f.write(f"{pt}|||{en}\n")

print("Arquivo traducao.txt gerado com sucesso.")
