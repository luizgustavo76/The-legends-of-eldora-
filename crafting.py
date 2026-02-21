import json
import tloe100 as tloe
class crafting:
    def __init__(self):
        self.dados = {}
        with open("craftings.json", "r", encoding="utf-8") as f:
            self.dados = json.load(f)

    def mostrar_receitas(self):
        receitas = self.dados["receitas"]["itens_necessarios"]

        for nome_item, info in receitas.items():
            print(f"\nItem: {nome_item}")

            print(" Ingredientes:")
            for ingrediente, qtd in info["itens_necessarios"].items():
                print(f"  - {ingrediente} x{qtd}")

            banca = info.get("banca_de_trabalho_necessario", False)
            print(f" Precisa de banca: {banca}")
    def crafting(self, nome_receita, quantidade):
        receitas = self.dados["receitas"]["itens_necessarios"]

        if nome_receita not in receitas:
            print("Essa receita não existe.")
            return

        receita = receitas[nome_receita]
        ingredientes = receita["itens_necessarios"]

        # verifica ingredientes
        for item, qtd in ingredientes.items():
            qtd_total = qtd * quantidade
            if tloe.salvamento_dados.get(item, 0) < qtd_total:
                print(f"Falta {item}. Precisa de {qtd_total}.")
                return

        # verifica banca
        if receita.get("banca_de_trabalho_necessario", False):
            if not tloe.salvamento_dados.get("banca_de_trabalho", False):
                print("Você precisa de uma banca de trabalho.")
                return

        # remove ingredientes
        for item, qtd in ingredientes.items():
            tloe.salvamento_dados[item] -= qtd * quantidade

        # adiciona item craftado
        if nome_receita not in tloe.salvamento_dados:
            tloe.salvamento_dados[nome_receita] = 0

        tloe.salvamento_dados[nome_receita] += quantidade

        print(f"Você craftou {quantidade}x {nome_receita}!")


