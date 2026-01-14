#actions&moves 1.0,um motor de ia para ações,ataques e todo tipo de realização fisica
import DreamCore
import random
import time
import os
import json
import ProceduralValley

aliados = []
acoes_batalha = []
acoes_inimigo = []
turno_batalha = ""
tipos_acoes_contraditorias = {
    "ataque":"defesa",
    "defesa":["habilidade_perfurante", "buff", "debuff"],
    "habilidade_perfurante":"defesa",
    "buff":"debuff",
    "debuff":"buff",
    "habilidade":"defesa",
}
clientes_taverna = [
    "Afonso", "Alvaro", "Antão", "Baltasar", "Belchior", "Bento",
    "Brás", "Calisto", "Cristóvão", "Duarte", "Estêvão", "Eusébio",
    "Fernão", "Gaspar", "Gil", "Gonçalo", "Heitor", "Henrique",
    "Inácio", "Jacinto", "Jerônimo", "João", "Jorge", "Lopo",
    "Lourenço", "Martim", "Mateus", "Mendo", "Miguel", "Nicolau",
    "Nuno", "Pascoal", "Pedro", "Rui", "Salvador", "Sancho",
    "Simão", "Tomé", "Tristão", "Vasco", "Vicente", "Xavier",

    "Abel", "Adrião", "Ambrósio", "Anselmo", "Bartolomeu", "Bertoldo",
    "Clemente", "Cosme", "Damião", "Domingos", "Elias", "Elói",
    "Felipe", "Filipe", "Gregório", "Hilário", "Isidro", "Leandro",
    "Leôncio", "Macário", "Manuel", "Maurício", "Melchior",
    "Norberto", "Odilon", "Orlando", "Ponciano", "Prudêncio",
    "Quirino", "Romão", "Severino", "Teobaldo", "Valentim",
    "Vitorino", "Zacarias",

    "Alda", "Beata", "Brites", "Catarina", "Clara", "Constança",
    "Custódia", "Doroteia", "Efigênia", "Elvira", "Engrácia",
    "Eulália", "Felícia", "Genoveva", "Guiomar", "Inês",
    "Isabel", "Leonor", "Madalena", "Mariana", "Margarida",
    "Matilde", "Mência", "Oriana", "Quitéria", "Raimunda",
    "Sancha", "Serafina", "Teodora", "Violante"
]
requisitos = [
    "mesas nivel 1", "mesas nivel 2", "mesas nivel 3", "mesas nivel 4", "mesas nivel 5",
    "bancos nivel 1", "bancos nivel 2", "bancos nivel 3", "bancos nivel 4", "bancos nivel 5",
    "cozinha nivel 1", "cozinha nivel 2", "cozinha nivel 3", "cozinha nivel 4", "cozinha nivel 5",
    "aparencia nivel 1", "aparencia nivel 2", "aparencia nivel 3", "aparencia nivel 4", "aparencia nivel 5",
    "bebidas nivel 1", "bebidas nivel 2", "bebidas nivel 3", "bebidas nivel 4", "bebidas nivel 5",
    "iluminação nivel 1", "iluminação nivel 2", "iluminação nivel 3", "iluminação nivel 4", "iluminação nivel 5",
    "loja sombria nivel 1", "loja sombria nivel 2", "loja sombria nivel 3", "loja sombria nivel 4", "loja sombria nivel 5",
]
requisitos_clientes_taverna = []
#gera npcs para frenquetar e habitar locais
class gerar_npcs:
    def __init__(self, contexto_tloe, upgrades_taverna):
        self.nome = ""
        self.local = ""
        self.numero_requisitos_concluidos = 0
        self.tloe = contexto_tloe
    def npc_taverna(self):

        self.nome = random.choice(clientes_taverna)
        self.local = "taverna"

        requisitos_clientes_taverna.append({
            "nome": self.nome,
            "requisitos": [],
            "reputacao_minima": 0
        })

        for i in range(3):

            # Gera requisito corretamente
            tipo = random.choice(list(self.tloe["reputacao_por_upgrades_taverna"].keys()))
            nivel = random.randint(1, 5)
            requisito = f"{tipo} nivel {nivel}"

            # Segurança: se algo errado nascer, ignora
            partes = requisito.split()
            if len(partes) != 3 or partes[1] != "nivel" or not partes[2].isdigit():
                continue

            # Evita repetir requisito
            if requisito in requisitos_clientes_taverna[-1]["requisitos"]:
                continue

            requisitos_clientes_taverna[-1]["requisitos"].append(requisito)

            chave_nivel = f"nivel {nivel}"
            requisitos_clientes_taverna[-1]["reputacao_minima"] += \
                self.tloe["reputacao_por_upgrades_taverna"][tipo].get(chave_nivel, 0)



    def verificar_requisitos_clientes_taverna(self):
        npc = requisitos_clientes_taverna[-1]
        
        if npc["reputacao_minima"] <= self.tloe["dados_taverna"]["reputação taverna"]:
            self.numero_requisitos_concluidos += 1

        for requisito in npc["requisitos"]:
            partes = requisito.split()
            item = partes[0]
            nivel_necessario = int(partes[2])

            if item in self.tloe["dados_taverna"]["melhorias_taverna"]:
                nivel_atual = len(self.tloe["dados_taverna"]["melhorias_taverna"][item])

                if nivel_atual >= nivel_necessario:
                    self.numero_requisitos_concluidos += 1
    def adicionar_npc_a_taverna(self, upgrades_taverna, dados_taverna):
        pode_entrar_taverna = False
        requisitos_concluidos = 0
        for npcs in requisitos_clientes_taverna:
            for requisitos_npcs in npcs["requisitos"]:
                item_requisitos_npcs = requisitos_npcs.split()
                if upgrades_taverna[item_requisitos_npcs[0]] >0:
                    requisitos_concluidos += 1
        if requisitos_concluidos == 3:
            for npcs in requisitos_clientes_taverna:
                if npcs["reputacao_minima"] >= dados_taverna["reputação taverna"]:
                    pode_entrar_taverna = True
        if pode_entrar_taverna:
            for npcs in requisitos_clientes_taverna:
                dados_taverna["frequentadores"].append(npcs)


    def iniciar_npc(self, upgrades_taverna, dados_taverna):
        self.npc_taverna()
        self.verificar_requisitos_clientes_taverna()
        self.adicionar_npc_a_taverna(upgrades_taverna, dados_taverna)
def npcs():
    locais_npcs = {
        "barman":"taverna",
        "bebado":"taverna",
        "antigo guerreiro":"taverna",
        "vendendor sombrio":"taverna",
        "vendedor de eldora":"loja de eldora",
        "vendendor de rimvark":"loja de rimvark",
        "vendedor de ebranthal":"loja de ebranthal",
        "vendedor de vangurd":"loja de vangurd",
        "vendedor de nocten":"loja de nocten",
        "ferreiro":"ferraria",
        "mineiro":"mina de eldora",
        "lenhador":"floresta das almas",
        "dorian":"casa",
        "padre":"igreja",
        "dono do mercado de rimvark":"mercado de rimvark",
        "dono do mercado de vangurd":"mercado de vangurd",
        "dono do mercado de ebranthal":"mercado de ebranthal",
        "dono do mercado de rimvark":"mercado de nocten",
    }
    if registro_acoes[-1] == "taverna":
        npc_puxar_assunto = "barman"
        DreamCore.npc_puxando_assunto = npc_puxar_assunto
    if registro_acoes[-1] == "loja de eldora":
        chance_puxar_assunto = random.randint(0,4)
        if chance_puxar_assunto == 4:
            DreamCore.npc_puxando_assunto = "vendedor de eldora"
    if registro_acoes[-1] == "loja de rimvark":
        chance_puxar_assunto = random.randint(0,4)
        if chance_puxar_assunto == 4:
            DreamCore.npc_puxando_assunto = "vendedor de rimvark"
    if registro_acoes[-1] == "loja de vangurd":
        chance_puxar_assunto = random.randint(0,4)
        if chance_puxar_assunto == 4:
            DreamCore.npc_puxando_assunto = "vendedor de vangurd"
    if registro_acoes[-1] == "loja de nocten":
        chance_puxar_assunto = random.randint(0,4)
        if chance_puxar_assunto == 4:
            DreamCore.npc_puxando_assunto = "vendedor de nocten"
    if registro_acoes[-1] == "loja de ebranthal":
        chance_puxar_assunto = random.randint(0,4)
        if chance_puxar_assunto == 4:
            DreamCore.npc_puxando_assunto = "vendedor de ebranthal"
    if registro_acoes[-1] == "ferraria":
        chance_puxar_assunto = random.randint(0,4)
        if chance_puxar_assunto == 4:
            DreamCore.npc_puxando_assunto = "ferreiro"
    if registro_acoes[-1] == "mina de eldora":
        chance_puxar_assunto = random.randint(0,4)
        if chance_puxar_assunto == 4:
            DreamCore.npc_puxando_assunto = "minerio"
    if registro_acoes[-1] == "igreja":
        chance_puxar_assunto = random.randint(0,4)
        if chance_puxar_assunto == 4:
            DreamCore.npc_puxando_assunto = "padre"
    if registro_acoes[-1] == "mercado de rimvark":
        chance_puxar_assunto = random.randint(0,4)
        if chance_puxar_assunto == 4:
            DreamCore.npc_puxando_assunto = "dono do mercado de rimvark"
    if registro_acoes[-1] == "mercado de vangurd":
        chance_puxar_assunto = random.randint(0,4)
        if chance_puxar_assunto == 4:
            DreamCore.npc_puxando_assunto = "dono do mercado de vangurd"
    if registro_acoes[-1] == "mercado de ebranthal":
        chance_puxar_assunto = random.randint(0,4)
        if chance_puxar_assunto == 4:
            DreamCore.npc_puxando_assunto = "dono do mercado de ebranthal"
    if registro_acoes[-1] == "mercado de nocten":
        chance_puxar_assunto = random.randint(0,4)
        if chance_puxar_assunto == 4:
            DreamCore.npc_puxando_assunto = "dono do mercado de nocten"
    
   
class monstro:
    def __init__(self):
        # ==========================
        # CLASSES
        # ==========================
        self.classe_monstro = [
            "fogo", "agua", "terra", "ar",
            "eletricidade", "gelo", "luz", "trevas"
        ]

        # ==========================
        # HABILIDADES POR CLASSE
        # ==========================
        self.habilidades_possiveis_fogo = [
            "bola de fogo", "cuspida flamejante",
            "queimadura", "ressecar", "bloqueio flamejante"
        ]
        self.habilidades_possiveis_agua = [
            "enchurrada", "bloqueio das aguas",
            "tiro d´agua", "desvio aquatico"
        ]
        self.habilidades_possiveis_terra = [
            "parede de terra", "golpe natural", "capangas da terra"
        ]
        self.habilidades_possiveis_ar = [
            "ventania", "furacão", "voo"
        ]
        self.habilidades_possiveis_eletricidade = [
            "choque rapido", "atordoação", "bloqueio eletrico"
        ]
        self.habilidades_possiveis_gelo = [
            "congelamento de inimigo", "parede congelada", "ataque gelado"
        ]
        self.habilidades_possiveis_luz = []
        self.habilidades_possiveis_trevas = []

        # Dicionário geral de habilidades
        self.habilidades_monstros = {
            "fogo": self.habilidades_possiveis_fogo,
            "agua": self.habilidades_possiveis_agua,
            "terra": self.habilidades_possiveis_terra,
            "ar": self.habilidades_possiveis_ar,
            "eletricidade": self.habilidades_possiveis_eletricidade,
            "gelo": self.habilidades_possiveis_gelo,
            "luz": self.habilidades_possiveis_luz,
            "trevas": self.habilidades_possiveis_trevas,
        }

        # ==========================
        # SORTEIO DA CLASSE E HABILIDADES
        # ==========================
        self.selecionar_classe = random.choice(self.classe_monstro)
        self.gerar_habilidade = self.habilidades_monstros[self.selecionar_classe]

        # ==========================
        # ATRIBUTOS DO MONSTRO
        # ==========================
        self.atributos_monstro = {
            "classe": self.selecionar_classe,
            "vida": 10,
            "dano":3,
            "defesa": 5,
            "itens": [],
            "habilidades": self.gerar_habilidade,
            "defesa": 5,
        }

        # ==========================
        # EMOÇÃO
        # ==========================
        self.emocao_atual = ""
        self.emocao_possiveis = ["raiva", "medo", "surpresa"]

        # ==========================
        # DADOS DE BATALHA
        # ==========================
        self.nivel_monstro = 1
        self.chance_usar_habilidade = random.randint(1, 10)

        self.acoes = ["atacar", "defender", "fugir", "tacar itens", "usar habilidade"]

    def atacar(self,dados_jogador):
        print("o monstro atacou!")
        dano_ataque = random.randint(1,5)
        if self.emocao_atual == "raiva":
            chance_dobrar_ataque = random.randint(1,10)
            if chance_dobrar_ataque == 1:
                dano_ataque *2
                dados_jogador["vida"] -= dano_ataque
        if self.emocao_atual == "medo":
            chance_atacar = random.randint(1,3)
            if chance_atacar == 1:
                dados_jogador["vida"] -= dano_ataque
        if self.emocao_atual == "surpresa":
            chance_usar_habilidade *2
    def usar_habilidade(self,dados_jogador):
        habilidade_escolhida = random.randint(0,len(habilidades_monstros["atributos_monstro"][classe]))
    def gerar_acao(self):
        if turno_batalha == "inimigo":
            if not acoes_inimigo[-1].startswith("inimigo"):
                ultima_acao = acoes_inimigo[-1].split()
                for chave_acao,valor_acao in tipos_acoes_contraditorias.items():
                    if chave_acao in ultima_acao[2]:
                        chance_acreditar = random.randint(0,2)
                        #não acredita na informação
                        if chance_acreditar != 2:
                            acoes_inimigo.append(f"inimigo {ultima_acao[0]} {valor_acao}")
                        else:
                            acoes_inimigo.append(f"inimigo {ultima_acao[0]} {ultima_acao[2]}")
                        turno_batalha = ultima_acao[0]
    def ler_acao(self):
        ultima_acao = acoes_inimigo[-1].split()
        if ultima_acao[0] == "golem":
            for chave_acao,valor_acao in tipos_acoes_contraditorias.items():
                if chave_acao in ultima_acao:
                    acao_inimigo = ultima_acao[2]

                    acao_contraria = tipos_acoes_contraditorias.get(acao_inimigo)
                    if isinstance(acao_contraria, list):
                        acao_contraria = random.choice(acao_contraria)
                        acoes_inimigo.append(f"{ultima_acao[0]} {acao_contraria}")

                    turno_batalha = ultima_acao[0]
                    
#dados e estatisticas sobre golens
dados_golem = {
    "golem de madeira": {
        "vida":15,
        "defesa":5,
        "dano":5,
    },
    "golem de pedra": {
        "vida":25,
        "defesa":13,
        "dano":10,
    },
    "golem de ferro": {
        "vida":45,
        "defesa":25,
        "dano":25,
    },
    "golem de esmeralda": {
        "vida":35,
        "defesa":20,
        "dano":15,
    },
    "golem de rubi": {
        "vida":50,
        "defesa":40,
        "dano":40,
    },
    "golem de ouro": {
        "vida":35,
        "defesa":12,
        "dano":20,
    },
    "golem de diamante": {
        "vida":70,
        "defesa":55,
        "dano":50,
    },
    "golem de obsidiana": {
        "vida":60,
        "defesa":45,
        "dano":80,
        
    },
}
class golem():
    def __init__(self):
        self.golem_atual = ""
        self.vida = 0
        self.dano = 0
        self.defesa = 0
        self.mana = 100
        self.equipamentos = {
            "cabeça":"",
            "tronco":"",
            "pernas":"",
            "pés":"",
        }
        self.inventario = []
        self.em_batalha = False
    def atacar(self):
        monstro.atributos_monstro["vida"] -= self.dano
        print(f"o {self.golem_atual} atacou tirando {self.dano} de dano!")
        time.sleep(0.5)
        acoes_batalha.append(f"golem ataque dano {self.dano}")
    def defender(self):
        monstro.atributos_monstro["vida"] -= monstro.atributos_monstro["dano"]
        self.mana -= 25
    def minerar(self):
        ProceduralValley.minerar()
    def analisar_estados(self,aliados):
        pass
    def gerar_acao(self):
        acoes_inimigo.append("inimigo inicio neutro")
        if acoes_inimigo[-1].startswith("inimigo"):
            ultima_acao = acoes_inimigo[-1].split()
            for chave_acao,valor_acao in tipos_acoes_contraditorias.items():
                if chave_acao in ultima_acao[2]:
                    chance_acreditar = random.randint(0,2)
                    #não acredita na informação
                    if chance_acreditar != 2:
                        acoes_inimigo.append(f"{self.golem_atual} monstro {valor_acao}")
                    else:
                        acoes_inimigo.append(f"{self.golem_atual} monstro {ultima_acao[2]}")
        if len(acoes_inimigo) == 0:
            acao_golem_escolhida = random.choice("atacar", "defender", "habilidade_perfurante", "buff", "debuff")
            acoes_inimigo.append("golem inimigo" +acao_golem_escolhida)
            turno_batalha = "golem"
    def ler_acao(self):
        ultima_acao = acoes_inimigo[-1].split()
        if ultima_acao[0] != "golem":
            for chave_acao,valor_acao in tipos_acoes_contraditorias.items():
                if chave_acao in ultima_acao:
                    acao_inimigo = ultima_acao[2]

                    acao_contraria = tipos_acoes_contraditorias.get(acao_inimigo)
                    if isinstance(acao_contraria, list):
                        acao_contraria = random.choice(acao_contraria)
                        acoes_inimigo.append(f"{ultima_acao[0]} {acao_contraria}")

                    turno_batalha = ultima_acao[0]
    def entrar_batalha_golem(self, slots, contador_golem):
        global monstro
        self.em_batalha = True
        contador_golem = 1
        self.golem_atual = None  # <- garante que começa vazio

        while contador_golem <= 4:
            slot = slots.get(f"slot{contador_golem}_golem")

            if slot:  # só substitui se for válido
                self.golem_atual = slot

            contador_golem += 1

        if not self.golem_atual:
            print("Nenhum golem encontrado!")
            return
        try:
            self.vida = dados_golem[self.golem_atual]["vida"]
            self.defesa = dados_golem[self.golem_atual]["defesa"]
            self.dano = dados_golem[self.golem_atual]["dano"]
        except Exception as e:
            print(f"erro ao ler slots {e}!")

        self.gerar_acao()
        turno_batalha = "inimigo"
        monstro.ler_acao()
        