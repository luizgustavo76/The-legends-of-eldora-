import random

matriz_terreno = []
itens_biomas = {
    "ruinas de eldora": ["grama morta", "ruinas", "monstros", "postos de saqueadores", "bau"],
    "mina de eldora": ["pedra", "rubi", "ouro", "ferro", "carvão", "diamante", "esmeralda", "rio de lava", "rio de agua", "monstros"],
}

class proceduralValley:
    def __init__(self):
        self.tamanho_terreno = 4
        self.bioma = "ruinas de eldora"
        self.objetos = []
        self.seed = []  # <-- antes era string, isso quebrava o append

    def gerador_matriz(self):
        while len(matriz_terreno) <= self.tamanho_terreno * self.tamanho_terreno:
            matriz_terreno.append(0)

    def gerar_seed(self):
        posicao_seed = 0
        numero_biomas = len(itens_biomas[self.bioma])
        item_aleatorio_bioma = random.randint(0, numero_biomas - 1)

        while posicao_seed <= numero_biomas * 2:
            numero = posicao_seed + item_aleatorio_bioma
            numero = numero * random.randint(1, 9)  
            numero = numero + random.randint(0, 99) 
            self.seed.append(str(numero))
            posicao_seed += 1


classe = proceduralValley()
classe.gerador_matriz()
print(matriz_terreno)
classe.gerar_seed()
print(classe.seed)
