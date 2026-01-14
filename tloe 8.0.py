import importlib.util
import random
import time
import json
import os
import socket
import threading
import sqlite3
import platform
from collections import Counter
import pyfiglet
import datetime
import requests
try:
    from plyer import notification
    plyer_disponivel = True
except:
    plyer_disponivel = False


def digitar(texto, delay=0.05):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(delay)
    print()
def digitarlento(texto, delay=0.30):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(delay)
    print()
saida_chat = 1  
horario = {
"ano":1023,
"dia":0,
"mes":0,
"horas":"0",
"minutos":"00",
}
def definir_horario():
	agora = datetime.datetime.now()
	horario["dia"] = random.randint(1,30)
	horario["mes"] = random.randint(1,12)
	horario["horas"] = int(agora.hour // 2)
	horario["minutos"] = int(agora.minute // 2)

aliados_guilda = [""]			
dados_jogador = {
    "nome": "",
    "classe": "",
    "nivel": 1,
    "vida": 20,
    "habilidade espadas": 1,
    "habilidade magia": 1,
    "patente nivel": 0,
    "exp": 0,
    "moedas": 500,
    "diamantes": 10,
    "defesa": 10,
    "dano": 5,
    "exp para evoluir":100,
    "esquivar":0,
    "chat":[""],
    "area":"",
}
dados_jogador_server = {
"nome":"",
"classe":"",
"nivel":0,
"xp":0,
"local":"",
"amigos":[""],
"id online":"000000000",
}
def ferreiro_juntar_guilda():
	digitar("...poderei me juntar a sua guilda?")
	escolha_chamar_ferreiro_guilda = input("[1]sim\n[2]não")
	if escolha_chamar_ferreiro_guilda == "1":
		digitar("muito obrigado...juro que não irei te decepcionar companheiro!")
		aliados_guilda.append("ferreiro")
	else:
		digitar("então isso é um não,eu te entendo")
temas_perguntas_ferreiro = {

    				"saudacao":["oi", "ola", "eai", "eae", "como vai", "você", "vosmecê", "vossa mecê"],
    				"batalha":["batalhar", "confronto","arena infinita", "masmorra","monstro"],
    				
    				"guilda":["guilda", "grupo" ,"bando", "juntar"],
    				"xingamento":["filho da puta", "filho da mãe", "porra", "caralho", "vai se fuder", "corno", "viado", "puta que pariu"],
    				"ferreiro":["espada", "capacete", "peitoral", "calça", "bota", "adaga", "golem", "reparar", "concertar", "equipamento", "preço alto", "preço baixo"],
    				"loja":["vendendor", "concorrencia", "amigos", "loja"],
    				"taverna":["barman", "bêbado", "taverna", "alcool", "cerveja", "pinga de mel", "cachaça mineira", "vodka", "velho barreiro"],
    				"vilas":["rimvark", "ebrenthal", "vangurd", "nocten","vila"],
    				"clima":["chuva", "frio", "calor", "ensolarado", "nublado", "tempestade"],
    				"ajuda":["ajuda, duvida"],
    				"classes":["classe", "bruxo", "goblin", "cavaleiro", "monstro", "mercador"],
    				"economia":["dinheiro", "economia"],
    				"npcs":["ferreiro", "vendendor", "barman", "bebado", "antigo guerreiro", "golem"],
    				"elogios":["bom", "execelente", "otimo", "muito bom", "perfeito"],
    				"pergunta estado":["chato"," triste", "raiva", "feliz", "medo", "ansioso"],
    				"despedida":["adeus", "tchau"," até mais", "até a proxima"],
}
def ferreiro_responder(pergunta_ferreiro,saida_chat):
    
    # Função interna para checar se já sabemos o nome do jogador
    def nome_desconhecido_chat():
        if memoria_ferreiro["nome_player"] == "":
            digitar(f"olá, qual seria seu nome meu caro {dados_jogador['classe']} viajante?")
            time.sleep(0.5)
            digitar(f"meu nome.....é {dados_jogador['nome']}")
            memoria_ferreiro["nome_player"] = dados_jogador["nome"]
        else:
            digitar(f"olá de novo, {memoria_ferreiro['nome_player']}")

    # Dicionário de respostas
    respostas_ferreiro = {
    
        "saudacao": nome_desconhecido_chat,
        "batalha": [
            "vejamos que você gosta de batalhar....bom saber disso",
            "você gosta de batalhar então...eu me sinto sozinho às vezes depois disso tudo...poderia me juntar a sua guilda?",
            "opa...vamos batalhar?"
        ],
        "guilda":ferreiro_juntar_guilda,
        "xingamento": ["pra que isso......????"],
        "ferreiro": [f"vejamos que você gosta da minha mercadoria, {dados_jogador['nome']} gostaria de comprar algum item ou forja-lo?"],
        "ferreiro_preço": [
            "que bom saber que meus preços estão acessíveis para você",
            "eh....me desculpa se os preços são altos..minha vida não está nas melhores condições ainda mais na questão de dinheiro"
        ],
        "loja": ["não me incomodo por que nós dois somos essências para esse reino, pois somos os únicos"],
        "taverna": [
            "coisa boa que era ir na taverna nos tempos antigos, a alegria reinando e bebendo sem preocupação",
            "poderia ir lá na taverna, fazem anos que não vou lá"
        ],
        "vilas": [
            "só ouvi falar dessa e das outras vilas... eu não sei o que eu sinto.. uma obrigação de ficar nessa ferraria... como se todos os dias fossem iguais",
            "não conheço mas um dia irei lá"
        ],
        "ajuda": ["opa... em que posso ajudá-lo?", "está interessado na mercadoria mas precisa de ajuda, certo?"],
        "classes": "não vai a mal, mas nesse reino existiram poucos da sua classe, você eu que foi o mais destemido deles",
        "economia": "coisa difícil de conseguir facilmente em Eldora",
        "npcs": "meu amigo..... alias muito gente boa",
        "elogios": "fico feliz que tenha gostado do meu serviço, pois senão gostasse não teria outro lugar para comprar...",
        "despedida": ["até mais", "adeus", "que Deus guia a sua mão"],
    }
    if "adeus" in pergunta_ferreiro.lower():
            	
            	digitar(f"que deus guie sua mão meuv{dados_jogador['classe']}")
            	saida_chat = 0
    encontrou_tema = False
    for tema, palavras_chave in temas_perguntas_ferreiro.items():
        for palavra in palavras_chave:
            
            if palavra in pergunta_ferreiro.lower():
                resposta_chat = respostas_ferreiro[tema]
                # Se a resposta for função (como saudacao), chama a função
                
                if callable(resposta_chat):
                    resposta_chat()
                else:
                    digitar(f"[ferreiro]: {random.choice(resposta_chat) if isinstance(resposta_chat, list) else resposta_chat}")
                encontrou_tema = True
                break
              
        if encontrou_tema:
            break

    # Caso nenhuma palavra chave seja encontrada
    if not encontrou_tema:
        resposta_indefinida = random.choice([
            "vai falar direito ou não?",
            "desculpa mas não entendi o que você falou",
            "acho que estou ficando surdo! poderia repetir?",
            f"um {dados_jogador['classe']} gaguejando desse jeito! toma juízo rapaz"
        ])
        digitar(f"[ferreiro]: {resposta_indefinida}")
npcs_vivos = {
"barman":True,
"bebado":True,
"ferreiro":True,
"mineiro":True,
"mercador":True,
"mercador nocten":True,
"mercador vangurd":True,
"mercador ebranthal":True,
"mercador rimvark":True,
"vendedor sombrio":True,
"antigo guerreiro":True,
}
finais_completados = [""]
def finais_alternativos():
    for npcs_finais in npcs_vivos:
    	if not npcs_finais:
    		digitar(VERMELHO + "você...você veio aqui com a promessa de salvar aqueles que sofreram tanto só de estarem ali...mas você os matou....matou aqueles em que a esperança de um reino feliz como antes...você tinha esse poder...e por isso que eles estavam ali...." + RESET)
    		digitarlento(VERMELHO + "se a esperança é a ultima que morre...você já deveria estar morto. . . "+ RESET)
    		digitarlento(VERMELHO + "final genocidia..." + RESET)
    		finais_completados.append("final genocidia")
    
    		
    
    # Verifica o tema da pergunta e responde
    
#servidor global
dados_server = {}
def carregar_dados_servidor():
	# Puxar dados
	try:
		res = requests.get('https://luizsgustavo76.pythonanywhere.com/get')
		dados_server = res.json()
	except:
		digitar("atualmente você está sem internet ou o servidor está fora do ar...por favor retorne mais tarde se o problema persistir...")

def atualizar_dados_servidor(novo_dados):
	
	# Atualizar dados
	novo_dados = dados_server # aqui você altera 	conforme ações do jogador
	requests.post('https://luizsgustavo76.pythonanywhere.com/update', json=novo_dados)
def chat_server():
	while True:
		print(dados_server["chat"])
		mensagem_chat_server = input("sua mensagem\nou digite reload para recarregar o chat")
		if mensagem_chat_server == "reload":
			carregar_dados_servidor()
		else:
			atualizar_dados_servidor(novo_dados=mensagem_chat_server)
import socket
import threading
import json
import time
import os

# ---------------- Funções para salvar e carregar JSON ----------------
def carregar_arquivo(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)

# ---------------- Dados do jogador e do amigo ----------------


dados_amigo = {
    "nome": "Amigo",
    "vida": 100,
    "vida_max": 100,
    "area": "desconhecida",
    "itens": [],
    "ouro": 0,
    "chat": []
}

# ---------------- Funções para multiplayer ----------------

def iniciar_servidor():
    def thread_servidor():
        host = obter_ip_local()
        porta = 5000
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind((host, porta))
        servidor.listen()
        print(f"[SERVIDOR] IP: {host} - aguardando conexão do amigo...")

        cliente, endereco = servidor.accept()
        print(f"[SERVIDOR] Amigo conectado: {endereco}")

        def receber_amigo():
            while True:
                try:
                    dados = cliente.recv(8192).decode()
                    if dados:
                        recebido = json.loads(dados)
                        dados_amigo.update(recebido)
                        salvar_arquivo("amigo_mundo.json", dados_amigo)
                except:
                    print("[SERVIDOR] Amigo desconectou")
                    break

        threading.Thread(target=receber_amigo, daemon=True).start()

        while True:
            try:
                cliente.send(json.dumps(dados_jogador).encode())
                time.sleep(1)
            except:
                print("[SERVIDOR] Conexão encerrada")
                break

    threading.Thread(target=thread_servidor, daemon=True).start()

def conectar_ao_host(ip):
    def thread_cliente():
        porta = 5000
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            cliente.connect((ip, porta))
            print(f"[CLIENTE] Conectado ao host {ip}")
        except:
            print("[CLIENTE] Não foi possível conectar ao host")
            return

        def receber_host():
            while True:
                try:
                    dados = cliente.recv(8192).decode()
                    if dados:
                        recebido = json.loads(dados)
                        dados_amigo.update(recebido)
                        salvar_arquivo("amigo_mundo.json", dados_amigo)
                except:
                    print("[CLIENTE] Conexão perdida com host")
                    break

        threading.Thread(target=receber_host, daemon=True).start()

        while True:
            try:
                cliente.send(json.dumps(dados_jogador).encode())
                time.sleep(1)
            except:
                print("[CLIENTE] Conexão encerrada")
                break

    threading.Thread(target=thread_cliente, daemon=True).start()

def obter_ip_local():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

# ---------------- Mostrar barra do amigo ----------------

def mostrar_status_amigo():
    try:
        nome = dados_amigo.get("nome", "Amigo")
        vida = dados_amigo.get("vida", 0)
        vida_max = dados_amigo.get("vida_max", 100)
        area = dados_amigo.get("area", "desconhecida")
        barra = "█" * int((vida / vida_max) * 10)
        barra = f"[{barra:<10}]"
        print(f"Amigo: {nome} | Área: {area} | Vida: {vida}/{vida_max} {barra}")
    except:
        print("Não foi possível mostrar status do amigo")

# ---------------- Troca de itens e ouro (mesma área) ----------------

def trocar_com_amigo():
    

    mostrar_inventario()
    print(f"Itens do amigo: {dados_amigo.get('itens', [])} | Ouro: {dados_amigo.get('ouro', 0)}")

    escolha = input("[1] Enviar item\n[2] Enviar ouro\nEscolha: ")
    if escolha == "1":
        item = input("Qual item deseja enviar? ")
        if item in dados_jogador["itens"]:
            dados_jogador["itens"].remove(item)
            dados_amigo["itens"].append(item)
            print(f"Você enviou '{item}' para seu amigo.")
        else:
            print("Você não tem esse item.")
    elif escolha == "2":
        try:
            valor = int(input("Quanto ouro deseja enviar? "))
        except:
            print("Valor inválido.")
            return
        if valor <= dados_jogador.get("ouro", 0):
            dados_jogador["ouro"] -= valor
            dados_amigo["ouro"] += valor
            print(f"Você enviou {valor} de ouro para seu amigo.")
        else:
            print("Você não tem ouro suficiente.")
    else:
        print("Escolha inválida.")

    salvar_arquivo("savegame.json", dados_jogador)
    salvar_arquivo("amigo_mundo.json", dados_amigo)

# ---------------- Chat multiplayer ----------------

def abrir_chat():
    while True:
        print("\n=== CHAT MULTIPLAYER ===")
        chat = dados_jogador.get("chat", [])
        
        print("[1] abrir chat")
        print("[2] Sair do chat")
        escolha = input("Escolha: ")
        if escolha == "1":
            while True:
            	for msg in chat[-5:]:
            		print(msg)
            	print("[0] para sair")
            	msg = input(">>>Digite sua mensagem: ")
            	nome = dados_jogador.get("nome", "Você")
            	nova_msg = f"{nome}: {msg}"
            	dados_jogador.setdefault("chat", []).append(nova_msg)
            	salvar_arquivo("savegame.json", dados_jogador)
            	if msg == "0":
            		break
        elif escolha == "2":
            print("Saindo do chat.")
            break
        else:
            print("Comando inválido.")

# ---------------- Menu multiplayer ----------------

def multiplayer():
    while True:
        print("\n=== MENU MULTIPLAYER ===")
        print("[1] Abrir mundo (servidor)")
        print("[2] Entrar no mundo do amigo (cliente)")
        escolha = input("Escolha: ")

        if escolha == "1":
            iniciar_servidor()
            print("Servidor iniciado! Você pode continuar jogando normalmente.")
            break
        elif escolha == "2":
            ip = input("Digite o IP do seu amigo (servidor): ")
            conectar_ao_host(ip)
            print("Conectado ao mundo do amigo! Você pode continuar jogando normalmente.")
            break
        else:
            print("Escolha inválida.")

# ---------------- Exemplo básico de uso ----------------




        # Salvar estado do jogador sempre que muda
        salvar_arquivo("savegame.json", dados_jogador)
def limpar_terminal():
    # Verifica se o sistema é Windows ('nt') ou outro (Linux, Android, etc.)
    os.system('cls' if os.name == 'nt' else 'clear')

cabeca_equipado = 0
tronco_equipado = 0
pernas_equipado = 0
pes_equipado = 0
mao_esquerda_equipado = 0
mao_direita_equipado = 0
#boss da arena infinita
boss_arena = {
"Gortak o tirano da pedra":{
	"nivel":10,
	"dificuldade":"facil",
	"ataques":"apredejamento",
	"dano":5,
},
"colosso das sombras":{
	"nivel":10,
	"dificuldade":"medio",
	"ataques especiais":["escuridao", "envenenamento sombrio"],
	"dano":10,
},
"shadow dead":{
	"nivel":10,
	"dificuldade":"dificil",
	"ataques":["alma vazia", "ataque duplo"],
	"dano":12,
},
"dragão do inferno":{
	"dificuldade":"inferno",
	"ataques":["ardencia do inferno", "duplicada", "escudo de chamas"],
	"dano":20,

},
}
#valores
valor_habilidade = {
    "mana":50,
}
dados_evolucao_nivel = {
"valor_evolucao_nivel":100,
"pontos_upgrades":0,
}
lucro_maximo = 0
dados_jogador2 =  {
"nome":"antigo guerreiro",
"vida":25,
"defesa":10,
"dano":15,
"nivel":1,
}
dados_jogador4 = {
"nome":"bebado",
"vida":10,
"defesa":5,
"dano":7,
"nivel":1,
}
dados_jogador3 = {
"nome":dados_jogador["nome"],
"vida": 20,
"defesa": 10,
"dano": 5,
"nivel":dados_jogador["nivel"],
}
dados_itens_equipados = {
    "cabeca":"",
    "tronco":"",
    "pernas":"",
    "pes":"",
    "mao direita":"",
    "mao esquerda":"",
    
    }
memoria_ferreiro = {
    
"nome_player":"",
"objetivo_eldora":"",
"vezes_perguntas":0,
"memoria_adicional":[""],
"afinidade":10,
}
dados_vilas = {
"vila atual":"",
"reputação em Vangurd":0,
"reputação em Nocten":0,
"reputação em Ebranthal":0,
"reputação em Rimvark":0,
}
def mercado():
	digitar(f"você entra no mercado local de {dados_vila['vila atual']} ")
def vila_rimvark():
	
	while True:
		dados_vila["vila atual"] == "rimvark"
		limpar_terminal()
		print("Vila de Rimvark:")
		print("[1]loja")
		print("[2]igreja")
		print("[3]mercado")
		print("[4]casa")
		print("[5]ver mapa")
		print("[6]menu jogador")
		escolha_rimvark = input("o queres fazer?")
		if escolha_rimvark == "2":
			digitar("você entra na igreja mas percebe que ainda está em construção")
			
		if escolha_rimvark == "5":
			digitar("você esta viajando de volta para o centro de eldora")
			digitarlento("...")
			break

def vila_vangurd():
	
	while True:
		limpar_terminal()
		print("Vila de Vangurd:")
		print("[1]loja")
		print("[2]igreja")
		print("[3]mercado")
		print("[4]casa")
		print("[5]voltar para eldora")
		print("[6]abrir inventario")
		print("[7]abrir status")
		escolha_vangurd = input("o queres fazer?")
		if escolha_vangurd == "5":
			digitar("você esta viajando de volta para o centro de eldora")
			digitarlento("...")
			break
		if escolha_vangurd == "2":
			digitar("você entra na igreja mas percebe que ainda está em construção...\nlogo á frente o padre celebrando uma missa.....")
			
def vila_nocten():
	
	while True:
		limpar_terminal()
		print("Vila de Nocten:")
		print("[1]loja")
		print("[2]igreja")
		print("[3]mercado")
		print("[4]casa")
		print("[5]ver mapa")
		print("[6]menu jogador")
		escolha_nocten = input("o queres fazer?")
		if escolha_nocten == "5":
			digitar("você esta viajando de volta para o centro de eldora")
			digitarlento("...")
			break
		if escolha_nocten == "2":
			digitar("você entra na igreja mas percebe que ainda está em construção")
			
			


			


	
def vila_ebranthal():
	
	while True:
		limpar_terminal()
		print("vila de Ebranthal:")
		print("[1]loja")
		print("[2]igreja")
		print("[3]mercado")
		print("[4]casa")
		print("[5]ver mapa")
		print("[6]menu jogador")
		escolha_ebranthal = input("o queres fazer?")
		if escolha_ebranthal== "5":
			digitar("você esta viajando de volta para o centro de eldora")
			digitarlento("...")
			break	
		if escolha_ebranthal == "2":
			digitar("você entra na igreja mas percebe que ainda está em construção")
			
	
#efeito de enbriagues
bebida_ingerida = ""
estar_bebado = False
def efeito_bebado():
		chance_ficar_bebado = random.randint(0,100)
		if chance_ficar_bebado >= 75:
			estar_bebado = True
			digitar("você está bêbado...")
		
		
def floresta_negra():
	limpar_terminal()
	digitar("você entra nessa floresta mas esse lugar definitivamente não te conforta")
	digitar("o ceu parece escurecer e ficar de noite")
	dados_floresta = {
	"arvores":60,
	"inimigos": {
		"cogumelo ambulante": {
			"vida":10,
			"ataque":2,
			"habilidade especial":"envenenamento",
		},
	    "goblin do mal": {
	    	"vida":15,
	    	"ataque":5,
	    	"habilidade especial":"lançamento de adaga",
	    },
	    "assasino das trevas": {
	    	"vida":20,
	    	"ataque":5,
	    	"habilidade especial":"nenhuma",
	    },
	    "demonio da noite": {
	    	"vida":30,
	    	"ataque":10,
	    	"habilidade especial":"envenamento demoniaco",
	    },
	},
	}


	while True:
		limpar_terminal()
		print(f"árvores restantes{dados_floresta['arvores']}:")
		print("[1]quebrar uma arvore")
		print("[2]caminhar pela floresta")
		print("[0]sair da floresta")
		escolha_floresta = input("o que deseha fazer?")
				
#AUTO SAVE


tempo_ultimo_save = time.time()
intervalo = 120


    
#evoluçao nivel
verificar_exp = False
dados_exp_evoluir = 100
def verificar_exp():
		global dados_exp_evoluir
		global dados_jogador
		if dados_jogador["exp"] >= dados_exp_evoluir:
			dados_jogador["exp"] = 0
			dados_jogador["nivel"] += 1
			dados_exp_evoluir += 100
			def verificar_pontos_upgrade():
				
				global dados_jogador
				calcular_pontos = int(dados_jogador["nivel"] // 4)
				pontos_padrao = 3
				calcular_pontos2 = int(calcular_pontos * pontos_padrao)
				dados_evolucao_nivel["pontos_upgrades"] += calcular_pontos2
				
			print("você subiu de nivel para o nivel",dados_jogador["nivel"])
#barra de vida
def barra_vida():
	barra_vida = ''
	numero_barras = 10
	for i in range(numero_barras):
	   barra_vida += '#'
	barra_vida = ("[" + barra_vida + "]")
	if numero_barras <=5:
		print(AMARELO + f"{barra_vida}" + RESET)
	if numero_barras <=3:
		print(VERMELHO + f"{barra_vida}" + RESET)
	else:
		print(VERDE + f"{barra_vida}" + RESET)
#vida defesa e ataque de adversarios
nivel_arena = 1
dano_boss = 0
ataque_especial_boss = []
vida_boss = 0
drop_boss = []
def boss_batalha(dificuldade_selecionada):
	boss_selecionado = ""
	for chefes_arena in boss_arena:
		if dificuldade_selecionada == "facil":
			if nivel_arena == 10:
				dano_boss = boss_arena['gorthak tirano da pedra["dano"]']
				ataque_especial_boss = boss_arena['gorthak tirano da pedra["ataques"]']
				vida_boss = boss_arena['gorthak tirano da pedra["vida"]']
				
					
	
dados_adversarios = {
"vida_barman"
"vida_bebado"
"vida_vendedor"
"vida_vendedor_sombrio"
"vida_cavaleiro_antigo"
"vida_dorian"
"ataque_barman"
"ataque_bebado"
"ataque_vendedor"
"ataque_vendedor_sombrio"
"ataque_cavaleiro_antigo"
"ataque_dorian"
}
#falas batalhas
#barman
falas_batalha_barman = ["que belo dia....bom PRA TACAR UMA GARRAFA NA TUA CABEÇA,garotos como você não deveria estar nesse bar especialmente sendo derrotado por mim,Então é isso?irá me deixar para trás para morrer??,toda causa haja uma consequencia"]
#modelo batalha padrão
#isso sera usado nas batalhas menos na arena infinita
def batalha_padrao():
		falas_batalha = [""]
		vida_adversario = int()
		ataque_adversario = int
		nome_adversario = "barman"
		fala_aleatoria = random.randint(1,4)
		if nome_adversario == "barman":
			falas_batalha = falas_batalha_barman
			
			
		while True:
			chance_fala = random.randint(1,5)
			if chance_fala == 1:				digitar(falas_batalha[fala_aleatoria])
			limpar_terminal()
			print(f"{nome_adversario}")
			barra_vida()
			print("[1]atacar")
			print("[2]defender")
			print("[3]habilidade")
			print("[4]trocar aliado")
			print("[5]inventario")
			print("[6]fugir da batalha")
			print(f"[7]falar com {nome_adversario}")
			opcao_batalha_padrao = input("escolha uma opção")
			if opcao_batalha_padrao == "1":
				pass
		
#funçao baú
def menu_bau():
    while True:
        limpar_terminal()
        print("====== BAÚ ======")
        print("[1] Ver itens no baú")
        print("[2] Guardar item no baú")
        print("[3] Retirar item do baú")
        print("[0] Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("Itens no baú:")
            vazio = True
            for item, qtd in sistema_bau.items():
                if isinstance(qtd, int) and qtd > 0:
                    print(f"{item.replace('_', ' ').title()}: {qtd}")
                    vazio = False
            if vazio:
                print("O baú está vazio.")
            input("Pressione Enter para continuar...")
        
        elif escolha == "2":
            item = input("Nome do item para guardar: ").lower().replace(" ", "_")
            if item in salvamento_dados and salvamento_dados[item] > 0:
                qtd = int(input("Quantidade para guardar: "))
                if qtd <= salvamento_dados[item]:
                    salvamento_dados[item] -= qtd
                    sistema_bau[item] = sistema_bau.get(item, 0) + qtd
                    print(f"{qtd} {item.replace('_',' ')} guardado(s) no baú.")
                else:
                    print("Você não tem essa quantidade.")
            else:
                print("Item não encontrado no inventário.")
            input("Pressione Enter para continuar...")

        elif escolha == "3":
            item = input("Nome do item para retirar: ").lower().replace(" ", "_")
            if item in sistema_bau and sistema_bau[item] > 0:
                qtd = int(input("Quantidade para retirar: "))
                if qtd <= sistema_bau[item]:
                    sistema_bau[item] -= qtd
                    salvamento_dados[item] = salvamento_dados.get(item, 0) + qtd
                    print(f"{qtd} {item.replace('_',' ')} retirado(s) do baú.")
                else:
                    print("Você não tem essa quantidade no baú.")
            else:
                print("Item não encontrado no baú.")
            input("Pressione Enter para continuar...")

        elif escolha == "0":
            break

        else:
            print("Opção inválida.")    
#bau
sistema_bau = {
    
    
    "pocao_exp2":0,
    "espada2":0,
    "pao2":0,
    "carne2":0,
    "batata2":0,
    "pocao_de_stamina2":0,
    "artefato_luz2":0,
    "artefato_fogo2":0,
    "artefato_agua2":0,
    "artefato_lava2":0,
    "artefato_diamante2":0,
    "artefato_força2":0,
    "artefato_defesa2":0,
    "artefato_ouro2":0,
    "artefato_sorte2":0,
    "artefato_magia2":0,
    
    "moeda_do_submundo2":0,
    "contrato_das_almas2":0,
    "amuleto_da_necromancia2":0,
    "fumaca_da_ilusao2":0,
    "adaga_envenenada2":0,
    "armadura_sombria2":0,
    
}
#USAR INVENTARIO
def mostrar_inventario():
    vazio = True
    for dicionario in [salvamento_dados, salvamento_dados2,inventario_equipamentos]:
        for chave, valor in dicionario.items():
            if isinstance(valor, int) and valor > 0:
                nome = chave.replace("_", " ")
                nome_formatado = ''.join(c for c in nome if c.isalpha() or c == ' ').title()
                print(f"{nome_formatado}: {valor}")
                vazio = False
    if vazio:
        print("Seu inventário está vazio.")
def usar_item(nome_item):
    nome_digitado = nome_item.lower().replace(" ", "")  
    item_usado = False

    for dicionario in [salvamento_dados, salvamento_dados2]:
        for chave, valor in dicionario.items():
            if isinstance(valor, int) and valor > 0:
                nome_formatado = ''.join(c for c in chave if c.isalpha() or c == ' ').replace("_", "").lower()
                if nome_digitado == nome_formatado:
                    print(f"Você usou {nome_item.title()}!")
                    
                    # Efeitos dos itens
                    if chave in ["pao2", "batata2"]:
                        print("Você recuperou 10 de vida.")
                    elif chave == "carne2":
                        print("Você recuperou 20 de vida.")
                    elif chave == "pocao_de_stamina2":
                        print("Você recuperou toda sua energia.")
                    elif chave == "pocao_exp2":
                        print("Você ganhou 100 de exp!")
                        dados_jogador["exp"] += 100
                        verificar_exp()
                        
                    elif chave == "cerveja":
                        print("Você bebeu uma cerveja.")
                        bebida_ingerida = "cerveja"
                        efeito_bebado()
                    elif chave == "pinga de mel":
                        print("Você bebeu uma pinga de mel.")
                        bebida_ingerida = "pinga de mel"
                        efeito_bebado()
                    elif chave == "cachaça mineira":
                        print("você bebeu uma cachaça mineira")
                        bebida_ingerida = "cachaça mineira"
                        efeito_bebado()
                    elif chave == "vodka":
                        print("Você bebeu uma vodka")
                        bebida_ingerida = "vodka"
                        efeito_bebado()
                    elif chave == "velho barreiro":
                        print("você bebeu um velho barreiro.")
                        bebida_ingerida = "velho barreiro"
                        efeito_bebado()
                    
                    elif chave.endswith("1"):
                        print("Você examinou o item. Pode ser útil em crafting.")
                    elif chave == "moeda_do_submundo2":
                        print("Você ouviu sussurros do além...")
                    elif chave == "contrato_das_almas2":
                        print("Você fez um pacto obscuro.")
                    elif chave == "amuleto_da_necromancia2":
                        print("Mortos agora te reconhecem como um dos deles.")
                    elif chave == "fumaca_da_ilusao2":
                        print("Você ficou invisível por alguns segundos.")
                    elif chave == "adaga_envenenada2":
                        print("Sua próxima lâmina será mortal.")
                    elif chave == "armadura_sombria2":
                        print("Uma armadura sombria envolve seu corpo.")
                    elif chave in ["espada2", "armadura2"]:
                        print("Você equipou um novo equipamento de batalha.")
                    else:
                        print("Você usou o item, mas nada aconteceu.")

                    dicionario[chave] -= 1
                    item_usado = True
                    return

    if not item_usado:
        print("Item não encontrado no inventário.")


#configuração de nivel
valor_upgrade = {
"valor_nivel":100,
}

		
	
#patente
patente = { 
    "bronze I":0,
    "bronze II":0,
    "bronze III":0,
    "prata I":0,
    "prata II":0,
    "prata III":0,
    "ouro I":0,
    "ouro II":0,
    "ouro III":0,
    "platina I":0,
    "platina II":0,
    "platina III":0,
    "diamante I":0,
    "diamante II":0,
    "diamante III":0,
    "mestre I":0,
    "mestre II":0,
    "mestre III":0,
    "mestre da honrra I":0,
    "mestre da honrra II":0,
    "mestre da honrra III":0,
    "elite I":0,
    "elite II":0,
    "elite III":0,
}
#tutorial inicial 
def tutorial():
	print("bem vindo ",dados_jogador["nome"],dados_jogador["classe"])
	digitar("bem vindo ao tutorial")
	pular_tutorial = input("você deseja fazer o tutorial? (s/n)")
	if pular_tutorial == "n":
		digitar("então que a aventura começe")
		digitarlento("The Legends Of Eldora")
	if pular_tutorial == "s":
		print("bem vindo ao mundo de eldora")
		print("pra começar vamos comprar uma espada")
		def centro_tutorial():
			while True:
				seta1 = ("<--------")
				seta2 = (" <-------")
				seta3 = ("  <------")
				seta4 = ("   <-----")
				limpar_terminal() 
				print("(1)ir a taverna")
				print("(2)loja",seta1)
				print("(3)inventario")
				limpar_terminal()
				print("(1)ir a taverna")
				print("(2)loja",seta2)
				print("(3)inventario")
				limpar_terminal()
				print("(1)ir a taverna")
				print("(2)loja",seta3)
				print("(3)inventario")
				limpar_terminal()
				print("(1)ir a taverna")
				print("(2)loja",seta4)
				print("(3)inventario")
				limpar_terminal()
				print("(1)ir a taverna")
				print("(2)loja",seta3)
				print("(3)inventario")
				limpar_terminal()
				print("(1)ir a taverna")
				print("(2)loja",seta2)
				print("(3)inventario")
				limpar_terminal()
				print("(1)ir a taverna")
				print("(2)loja",seta1)
				print("(3)inventario")
		centro_tutorial()
		time.sleep(0,5)
			
			
			
			
			
			
			
		
		
	
#telas de morte
tela_morte = {
"facil":0,
"medio":0,
"dificil":0,
"inferno":0,
"morte_facil":"ok cara você tem que treinar mais um pouco",
"morte_medio":"não desista você ainda consegue",
"morte_dificil":"isso que foi uma batalha boa",
"morte_inferno":"você tentou,isso que foi o mais dificil",
}
#corzinha ^^
VERMELHO = "\033[1;31m"
VERDE = "\033[1;32m"
AZUL = "\033[1;34m"
AMARELO = "\033[1;33m"
RESET = "\033[0m"
ROXO = "\033[1;35m"
CIANO = "\033[1;36m"
BRANCO = "\033[1;37m"
#niveis
level0 = "descarted: aw000"
level1 = "caracol maligno"
level2 = "aranha"
level3 = "slime"
level4 = "goblin"
level5 = "gorthak o tirano da pedra"
#descartado
aventureiro = {
    "taverna":0,
    "loja":0,
    "guilda":0,
    "masmorra":0,
}

aliados = {
    "antigo_guerreiro":0,
    "bebado":0,
}
valor_vida_interno = {
"vida_max":1500,
}

upgrades = {
    "vida":1,
    "defesa":1,
    "mana":1,
    "exp":1,
    "maestria com espadas":1,
    "magia":1,
    "habilidade":0,
    "exp_valor":100,
    "pontos upgrades":0,
    "habilidade_cavaleiro":"golpe divino",
    "habilidade_bruxo":"bola de fogo",
    "habilidade_goblin":"lançar adaga",
    "habilidade_monstro":"rugido aterrorizante",
    "habilidade_mercador":"suborno",
    "habilidade_cavaleiro2":"escudo sagrado",
    "habilidade_cavaleiro3":"investida brutal",
    "habilidade_cavaleiro4":"voto de honra",
    "habilidade_bruxo2":"explosão arcana",
    "habilidade_bruxo3":"maldição sombria",
    "habilidade_bruxo4":"drenar alma",
    "habilidade_goblin2":"fuga agil",
    "habilidade_goblin3":"zombaria",
    "habilidade_goblin4":"bomba improvisada",
    "habilidade_mercador2":"oferta relampago",
    "habilidade_mercador3":"persuação",
    "habilidade_mercador4":"lucro maxímo",
    "habilidade_monstro2":"mordida voraz",
    "habilidade_monstro3":"raiva selvagem",
    "habilidade_monstro4":"regeneraçao natural",
}

    
#status secundarios
status_secundarios = {
"resfriado":0,
}
#climas
#valores sobre clima
valor_clima = {
"exposto_clima":0,
}
#função do clima
def clima():
	chance_clima = random.randint(1,9)
	clima_atual = 0
	if chance_clima <=3:
		clima_atual = 1
		print("o dia está com um pouco de sol")
		
	if chance_clima == 4:
		clima_atual = 2
		digitar("o dia está chuvoso")
		valor_clima["exposto_clima"] = 1
	if chance_clima == 5:
			clima_atual = 3
			digitar("está com uma chuva forte,até parece que vai dar uma tempestade")
			valor_clima["exposto_clima"] = 1
	if chance_clima == 6:
			clima_atual = 4
			digitar("está uma tempestade intensa com raios e ventos fortes,e melhor eu me abrigar")
			valor_clima["exposto_clima"] = 1
	if chance_clima == 7:
			clima_atual = 5
			digitar("o dia está nublado,está até bom ficar aqui!")
	if chance_clima == 8:
			clima_atual = 6
			digitar("o dia tá ensolarado,aproveite para fazer suas tarefas")
	if chance_clima == 9:
			clima_atual = 7
			digitar("está tendo uma nevasca,e melhor eu me abrigar")
			valor_clima["exposto_clima"] = 1
	def verificar_exposto():
		if valor_clima["exposto_clima"] <=1:
			digitar("você está esposto ao clima arrume um abrigo! ")
		if valor_clima["exposto_clima"] ==2:
			digitar("você está muito exposto ao clima arrume um abrigo urgentemente")
	
	
			
		
	
			
		
			



salvamento_dados = {
    "madeira":0,
    "pontos de upgrade": 0,
    "conquistas":0,
    "item espada bau":0,
    "bebado":0,
    "antigo_heroi":0,
    "picareta de pedra":0,
    "picareta de madeira":0,
    "picareta de ferro":0,
    "carvão":0,
    "adaga":0,
    "barra_cobre":0,
    "pipeta_cobre":0,
    "capacete":0,
    "peitoral":0,
    "calças":0,
    "botas":0,
    "pocao_exp2":0,
    "espada2":0,
    "pao2":0,
    "carne2":0,
    "batata2":0,
    "pocao_de_stamina2":0,
    "cerveja2":0,
    "pinga2":0,
    "choro_dragao2":0,
    "skull_soul2":0,
    "dead_soul2":0,
    "alma_negra2":0,
    "artefato_luz2":0,
    "artefato_fogo2":0,
    "artefato_agua2":0,
    "artefato_lava2":0,
    "artefato_diamante2":0,
    "artefato_força2":0,
    "artefato_defesa2":0,
    "artefato_ouro2":0,
    "artefato_sorte2":0,
    "artefato_magia2":0,
    "dente_goblin1":0,
    "olho_aranha1":0,
    "bola_slime1":0,
    "casca_caracol1":0,
    "moeda_do_submundo2":0,
    "contrato_das_almas2":0,
    "amuleto_da_necromancia2":0,
    "fumaca_da_ilusao2":0,
    "adaga_envenenada2":0,
    "armadura_sombria2":0,
    "cerveja":0,
    "pinga_de_mel":0,
    "cachaça_mineira":0,
    "vodka":0,
    "velho_barreiro":0,
    "balde":0,
    "obsidiana":0,
    "balde de água":0,
    "balde de lava":0,
    "espada de obsidiana":0,
    "picareta de obsidiana":0,
    "picareta de cobre":0,
    "espada de cobre":0,
    "cobre bruto":0,
    "ferro bruto":0,
    "ouro bruto":0,
    "machado de madeira":0,
    "machado de ferro":0,
    "machado de pedra":0,
    "machado de ferro":0,
    "machado de cobre":0,
    "machado de obsidiana":0,
    "pedra":0,
    "pergaminho da forca I":0,
    "pergaminho da forca II":0,
    "pergaminho da forca III":0,
    "pergaminho da forca IV":0,
    "pergaminho da defesa I":0,
    "pergaminho da defesa II":0,
    "pergaminho da defesa III":0,
    "pergaminho da defesa IV":0,
    "pergaminho de remendo":0,
    "pergaminho de mais moedas":0,
    
}

def bau_pergaminho():
	bau_pergaminho_aleatorio = random.randint(0,2)
	if bau_pergaminho_aleatorio == 0:
		digitar("você encontra um báu de madeira\ndurante sua jornada\nsua curiosidade foi mais forte e você decide abrir ele")
		
		if bau_pergaminho_aleatorio == 1:
			
			bau_pergaminho_madeira = random.randint(0,1)
			if bau_pergaminho_pedra == 0:
				digitar("você conseguiu um pergaminho da força nivel I.....!")
				salvamento_dados["pergaminho da forca I"] += 1
			if bau_pergaminho_madeira == 1:
				digitar("você conseguiu um pergaminho da defesa nivel I....!")
				salvamento_dados["pergaminho da defesa I"]
		if bau_pergaminho_aleatorio == "1":
			digitar("você encontra um báu de pedra\ndurante sua jornada\nsua curiosidade foi mais forte e você decide abrir ele")
			bau_pergaminho_pedra = random.randint(0,1)
			if bau_pergaminho_pedra == 0:
				digitar("você conseguiu um pergaminho da força nivel II....!")
				salvamento_dados["pergaminho da forca II"]
			if bau_pergaminho_pedra == 1:
				digitar("você conseguiu um pergaminho da defesa nivel II....!")
				salvamento_dados["pergaminho da defesa II"]
				
		if bau_pergaminho_aleatorio == 2:
			digitar("você encontra um báu de ouro\ndurante sua jornada\nsua curiosidade foi mais forte e você decide abrir ele")	
			bau_pergaminho_ouro = random.randint(0,5)
			if bau_pergaminho_ouro == 0:
				digitar("você conseguiu um pergaminho de força nivel iii")
				salvamento_dados["pergaminho da forca iii"]
			
			if bau_pergaminho_ouro == 1:
					digitar("você conseguiu um pergaminho de força nivel IV")
					salvamento_dados["pergaminho da forca iv"] += 1
			if bau_pergaminho_ouro == 2:
					digitar("você conseguiu um pergaminho de defesa iii")
					salvamento_dados["pergaminho da defesa iii"] += 1
			if bau_pergaminho_ouro == 3:
					
					digitar("você conseguiu um pergaminho da defesa nivel IV")
					salvamento_dados["pergaminho da defesa iv"] += 1
			if bau_pergaminho_ouro == 4:
				
				digitar("você conseguiu um pergaminho de remendo")
				salvamento_dados["pergaminho de remendo"] += 1
			if bau_pergaminho_ouro == 5:
				digitar("você ganhou um pergaminho de ganho de mais moedas")
				salvamento_dados["pergaminho de mais moedas"] += 1
				
			
					
					
					
					
salvamento_dados2 = {

    "espada_madeira":0,
    "escudo_madeira":0,
    "capacete_madeira":0,
    "placa_madeira":0,
    "placa_ferro":0,
    "espada_ferro":0,
    "escudo_ferro":0,
    "capacete_ferro":0,
    "barra_ouro":0,
    "barra_ferro":0,
    "barra_prata":0,
    "pipeta_ouro":0,
    "pipeta prata":0,
    "cerveja":0,
    "pinga de mel":0,
    "cachaça mineira":0,
    "vodka":0,
    "velho barreiro":0,
    
}
#bebidas da taverna
dados_taverna = {
"dinheiro_barman":250,
"estoque_cerveja":6,
"estoque_pinga_de_mel":4,
"estoque_cachaça_mineira":5,
"estoque_vodka":3,
"estoque_velho_barreiro":8,
}
bebidas_taverna = {

"cerveja":5,
"cachaça mineira":15,
"pinga de mel":15,
"vodka":20,
"velho barreiro":5,
}

#funçao mostrar bebida
def mostrar_bebidas():
	for nome,valor in bebidas_taverna.items():
		estoque = dados_taverna.get("estoque_" + nome.replace(" ", "_"), 0)
		print(f"{nome} {valor} moedas,Estoque:{estoque}")
		
		
			
		
		
#loja sombria
moeda_do_submundo = 2
amuleto_da_necromancia = 58
contrato_das_almas = 10
fumaça_da_ilusao = 3
armadura_sombria = 10
adaga_envenenada = 3 
#durabilidade equipamentos 
def sistema_durabilidade():
    if cabeca_equipado == 1:
        if dados_itens_equipados == "capacete":
            taxa_durabilidade_capacete = 3
            
    

aliados = {
    "antigo_guerreiro":0,
    "bebado":0,
    "antigo_guerreiro_hp":25,
    "bebado_hp":10,
    "ataque_guerreiro":10,
    "bebado_ataque":5,
    "guerreiro_defesa":10,
    "bebado_defesa":5,
}

upgrades_taverna = {
    "mesas":1,
    "bancos":1,
    "aparencia":1,
    "cozinha":1,
    "loja_sombria":0,
}
#online config
amigos_conectados = {}
nome = dados_jogador["nome"]
#pvp online config
def pvp_online():
    import socket
    import threading

    print("=== Lista de amigos disponíveis para PvP ===")
    for i, (amigo, ip) in enumerate(amigos_conectados.items(), start=1):
        print(f"{i} - {amigo} (IP: {ip})")

    escolha = input("Escolha o número do amigo para iniciar o PvP: ")
    try:
        escolha = int(escolha)
        amigo_nome = list(amigos_conectados.keys())[escolha - 1]
        amigo_ip = amigos_conectados[amigo_nome]
    except:
        print("Escolha inválida.")
        return

    # Conecta com o amigo (cliente)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((amigo_ip, 12345))
        s.send(nome.encode())
    except:
        print("Não foi possível conectar ao amigo.")
        return

    vida = 100
    vida_inimigo = 100
    defendendo = False

    def receber_turno():
        nonlocal vida
        while True:
            msg = s.recv(1024).decode()
            if msg == "ATAQUE":
                dano = 20 if not defendendo else 10
                vida -= dano
                print(f"Você foi atacado! Perdeu {dano} de vida. Vida atual: {vida}")
            elif msg == "FUGA":
                print("O inimigo fugiu!")
                break

    threading.Thread(target=receber_turno, daemon=True).start()

    while vida > 0 and vida_inimigo > 0:
        print("\n=== Seu turno ===")
        print("1 - Atacar")
        print("2 - Defender")
        print("3 - Inventário")
        print("4 - Fugir")
        acao = input("Escolha sua ação: ")

        if acao == "1":
            s.send("ATAQUE".encode())
            print("Você atacou!")
            vida_inimigo -= 20
        elif acao == "2":
            defendendo = True
            print("Você está se defendendo no próximo turno.")
        elif acao == "3":
            print("Inventário:", inventario)
        elif acao == "4":
            s.send("FUGA".encode())
            print("Você fugiu da batalha.")
            break
        else:
            print("Ação inválida.")

        if vida_inimigo <= 0:
            print("Você venceu a batalha!")
            break
        if vida <= 0:
            print("Você foi derrotado.")
            break
#trades
def trade_online():
    

    PORT = 12345
    itens_disponiveis = {
        "poção": "Cura 20 HP",
        "espada": "Dano +10",
        "escudo": "Defesa +5"
    }

    def tratar_conexao(conn, addr, inventario):
        nome_amigo = conn.recv(1024).decode()
        amigos_conectados[nome_amigo] = addr[0]
        print(f"{nome_amigo} ({addr[0]}) virou seu amigo!")
        if plyer_disponivel:
            notification.notify(
            title="Notificação de Amigo",
            message=f"{nome_amigo} está online!!!",
            timeout=5
        )
        

    

    
    
    

    while True:
        try:
            dados = conn.recv(1024).decode()
            if dados.startswith("MSG:"):
                print(dados[4:])
            elif dados.startswith("TRADE:"):
                item = dados[6:]
                inventario.append(item)
                print(f"Você recebeu o item '{item}'!")
        except:
            print(f"{nome_amigo} se desconectou. Salvando como amigo...")
            amigos_conectados[nome_amigo] = addr[0]
            salvar_progresso()
            break

        while True:
            try:
                dados = conn.recv(1024).decode()
                if dados.startswith("MSG:"):
                    print(dados[4:])
                elif dados.startswith("TRADE:"):
                    item = dados[6:]
                    inventario.append(item)
                    print(f"Você recebeu o item '{item}'!")
            except:
                print("Amigo se desconectou.")
                salvar_progresso()
                break
                

    def enviar_mensagens(conn, nome, inventario):
        conn.send(nome.encode())
        while True:
            msg = input()
            if msg.startswith("/enviaritem"):
                partes = msg.split()
                if len(partes) == 2:
                    item = partes[1]
                    if item in inventario:
                        conn.send(f"TRADE:{item}".encode())
                        inventario.remove(item)
                        print(f"Você enviou '{item}'!")
                    else:
                        print("Você não tem esse item.")
                else:
                    print("Uso: /enviaritem nome_do_item")
            elif msg == "/itens":
                print("Seus itens:", ", ".join(inventario))
            else:
                conn.send(f"MSG:{nome}: {msg}".encode())

    print("=== Sistema de Trade Online ===")
    nome = input("Digite seu nome: ")
    print("1 - Criar host")
    print("2 - Conectar como cliente")
    escolha = input("Escolha: ")

    inventario = ["poção", "espada"]

    if escolha == "1":
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind(('', PORT))
        servidor.listen()

        hostname = socket.gethostname()
        ip_local = socket.gethostbyname(hostname)
        print(f"Host criado! Seu IP é: {ip_local}")
        print("Esperando amigo se conectar...")

        conn, addr = servidor.accept()
        print(f"Conectado com {addr[0]}")
        threading.Thread(target=tratar_conexao, args=(conn, addr, inventario)).start()
        enviar_mensagens(conn, nome, inventario)

    elif escolha == "2":
        ip = input("Digite o IP do host: ")
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((ip, PORT))
        print("Conectado ao host!")
        threading.Thread(target=tratar_conexao, args=(cliente, (ip, PORT), inventario)).start()
        enviar_mensagens(cliente, nome, inventario)

    else:
        print("Opção inválida.")





import socket
import select
import threading
import time
import json
import os

PORTA_PADRAO = 12345
dados_guilda = {
    "nome": None,
    "senha": None,
    "dono": None,
    "membros": {},
    "conexoes": [],
    "mensagens": [],
    "convidados": [],
    "guilda_ativa": True,
    "atividades": {},  
    "membros_detectados": set(),
    "patentes": {}
}

def guilda_online():
    def log_acao(acao):
        with open('historico_guilda.txt', 'a') as log:
            log.write(f"[{time.ctime()}] {acao}\n")

    def salvar_guilda_json():
        with open('guilda.json', 'w') as f:
            json.dump(dados_guilda, f)

    def carregar_guilda_json():
        if os.path.exists('guilda.json'):
            with open('guilda.json', 'r') as f:
                return json.load(f)
        return None

    def menu_principal():
        print("\nMenu da Guilda Online:")
        print("1. Criar guilda")
        print("2. Entrar na guilda existente")
        escolha = input("Escolha: ")
        return escolha

    def menu_dono():
        print(f"\n[Gerenciamento da Guilda {dados_guilda['nome']}]")
        print("1. Ver atividade dos membros")
        print("2. Adicionar membro (por IP)")
        print("3. Expulsar membro")
        print("4. Enviar broadcast")
        print("5. PvP")
        print("6. Trade")
        print("7. Chat")
        print("8. Enviar script para membros")
        print("9. Definir patente")
        print("10. Sair")

    def chat_menu():
        while True:
            print("\n[Chat da Guilda]")
            for ip, msg in dados_guilda["mensagens"]:
                print(f"{ip}: {msg}")
            msg = input("Digite a mensagem (ou 'exit()' para sair): ")
            if msg == 'exit()':
                break
            for m in dados_guilda["conexoes"]:
                m.send(f"[Chat] {msg}".encode())
            dados_guilda["mensagens"].append(("Host", msg))
            log_acao(f"Host enviou mensagem: {msg}")

    def enviar_script():
        nome_script = input("Nome do arquivo .py para enviar: ")
        if not os.path.exists(nome_script):
            print("Arquivo não encontrado.")
            return
        with open(nome_script, 'r') as f:
            conteudo = f.read()
        for membro in dados_guilda["conexoes"]:
            membro.send(f"[Script]{conteudo}".encode())
        print("Script enviado para todos os membros.")
        log_acao(f"Script {nome_script} enviado.")

    def pvp_duelo(conn1, conn2):
        def escolha(conn):
            conn.send(b"1. Atacar 2. Defender 3. Fugir: ")
            return conn.recv(1024).decode().strip()

        hp1, hp2 = 100, 100
        while hp1 > 0 and hp2 > 0:
            a1 = escolha(conn1)
            a2 = escolha(conn2)
            if a1 == '1' and a2 != '2':
                hp2 -= 20
            if a2 == '1' and a1 != '2':
                hp1 -= 20
            if a1 == '3' or a2 == '3':
                conn1.send(b"Um dos jogadores fugiu!\n")
                conn2.send(b"Um dos jogadores fugiu!\n")
                log_acao("Um jogador fugiu do PvP.")
                return
            conn1.send(f"Seu HP: {hp1} | HP inimigo: {hp2}\n".encode())
            conn2.send(f"Seu HP: {hp2} | HP inimigo: {hp1}\n".encode())
        log_acao("PvP finalizado.")

    def trade_jogadores(conn1, conn2):
        conn1.send(b"Digite item para enviar: ")
        item1 = conn1.recv(1024)
        conn2.send(b"Digite item para enviar: ")
        item2 = conn2.recv(1024)
        conn1.send(b"Recebeu: " + item2)
        conn2.send(b"Recebeu: " + item1)
        log_acao(f"Trade realizado: {item1.decode()} <-> {item2.decode()}")

    def definir_patente():
        membro = input("IP do membro: ")
        patente = input("Patente a atribuir: ")
        dados_guilda["patentes"][membro] = patente
        print(f"Patente '{patente}' atribuída a {membro}.")
        log_acao(f"Patente '{patente}' atribuída a {membro}.")

    def servidor_guilda(ip_host):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((ip_host, PORTA_PADRAO))
        server.listen()
        print(f"[GUILDA] Servidor iniciado em {ip_host}:{PORTA_PADRAO}")
        log_acao("Servidor iniciado.")
        sockets_list = [server]
        while dados_guilda["guilda_ativa"]:
            leitura, _, _ = select.select(sockets_list, [], [], 1)
            for s in leitura:
                if s == server:
                    conn, addr = server.accept()
                    ip = addr[0]
                    conn.send("Digite a senha da guilda: ")
                    senha = conn.recv(1024).decode().strip()
                    if senha != dados_guilda["senha"]:
                        conn.send("Senha incorreta. Conexão encerrada.")
                        conn.close()
                        log_acao(f"Tentativa de entrada falhou de {ip}.")
                        continue
                    sockets_list.append(conn)
                    dados_guilda["conexoes"].append(conn)
                    dados_guilda["membros"][ip] = conn
                    dados_guilda["atividades"][ip] = time.time()
                    print(f"[+] {ip} entrou na guilda.")
                    log_acao(f"{ip} entrou na guilda.")
                else:
                    try:
                        msg = s.recv(1024).decode()
                        if not msg:
                            continue
                        ip = s.getpeername()[0]
                        dados_guilda["mensagens"].append((ip, msg))
                        dados_guilda["atividades"][ip] = time.time()
                        for membro in dados_guilda["conexoes"]:
                            if membro != s:
                                membro.send(f"[{ip}] {msg}".encode())
                        log_acao(f"Mensagem de {ip}: {msg}")
                    except:
                        sockets_list.remove(s)
                        ip = s.getpeername()[0]
                        if ip in dados_guilda["membros"]:
                            del dados_guilda["membros"][ip]
                        print(f"[-] {ip} saiu da guilda.")
                        log_acao(f"{ip} saiu da guilda.")

    escolha = menu_principal()
    if escolha == "1":
        ip = input("Seu IP (ou 127.0.0.1 para local): ")
        nome_guilda = input("Nome da guilda: ")
        senha_guilda = input("Defina a senha da guilda: ")
        dados_guilda.update({"dono": ip, "nome": nome_guilda, "senha": senha_guilda})
        dados_salvos = carregar_guilda_json()
        if dados_salvos:
            print("Guilda existente carregada.")
            dados_guilda.update(dados_salvos)
        threading.Thread(target=servidor_guilda, args=(ip,), daemon=True).start()
        while True:
            menu_dono()
            escolha = input("Escolha: ")
            if escolha == "1":
                for m, t in dados_guilda["atividades"].items():
                    patente = dados_guilda["patentes"].get(m, "Sem patente")
                    print(f"Membro: {m} - Patente: {patente} - Última atividade: {round(time.time() - t)}s atrás")
            elif escolha == "2":
                novo = input("IP do novo membro: ")
                dados_guilda["convidados"].append(novo)
                print(f"{novo} convidado!")
                log_acao(f"Convite enviado para {novo}.")
            elif escolha == "3":
                remover = input("IP a remover: ")
                if remover in dados_guilda["membros"]:
                    conn = dados_guilda["membros"][remover]
                    conn.close()
                    print(f"{remover} removido.")
                    log_acao(f"{remover} removido da guilda.")
            elif escolha == "4":
                msg = input("Mensagem de broadcast: ")
                for m in dados_guilda["conexoes"]:
                    m.send(f"[Broadcast] {msg}".encode())
                log_acao(f"Broadcast enviado: {msg}")
            elif escolha == "5":
                ip1 = input("IP jogador 1: ")
                ip2 = input("IP jogador 2: ")
                conn1 = dados_guilda["membros"].get(ip1)
                conn2 = dados_guilda["membros"].get(ip2)
                if conn1 and conn2:
                    threading.Thread(target=pvp_duelo, args=(conn1, conn2), daemon=True).start()
            elif escolha == "6":
                ip1 = input("IP jogador 1: ")
                ip2 = input("IP jogador 2: ")
                conn1 = dados_guilda["membros"].get(ip1)
                conn2 = dados_guilda["membros"].get(ip2)
                if conn1 and conn2:
                    threading.Thread(target=trade_jogadores, args=(conn1, conn2), daemon=True).start()
            elif escolha == "7":
                chat_menu()
            elif escolha == "8":
                enviar_script()
            elif escolha == "9":
                definir_patente()
            elif escolha == "10":
                print("Fechando guilda.")
                dados_guilda["guilda_ativa"] = False
                salvar_guilda_json()
                log_acao("Guilda encerrada pelo dono.")
                break
    elif escolha == "2":
        ip = input("Digite o IP do host para entrar: ")
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((ip, PORTA_PADRAO))
        print("[*] Conectado à guilda.")
        senha = input("Digite a senha da guilda: ")
        cliente.send(senha.encode())

        def receber():
            while True:
                try:
                    dados = cliente.recv(1024)
                    print(dados.decode())
                except:
                    break
        threading.Thread(target=receber, daemon=True).start()

        while True:
            print("\n[Menu Membro]")
            print("1 - Chat")
            print("2 - PvP")
            print("3 - Trade")
            print("4 - Sair")
            opc = input("Escolha: ")
            if opc == "1":
                while True:
                    msg = input("Mensagem (ou 'exit()'): ")
                    if msg == 'exit()':
                        break
                    cliente.send(msg.encode())
            elif opc == "2":
                cliente.send("Solicito PvP com o host.")
            elif opc == "3":
                cliente.send("Solicito trade com o host.")
            elif opc == "4":
                break
#crafting
#atributos maximos
max_atributos = {
"hp_max":20,
"mana_max":50,
"dano_max":5,
}
#golem
#golens existentes
# Quantos golems o jogador tem
dados_jogador_golem = {
    "golem de ferro": 0,
    "golem de cobre": 0,
    "golem de ouro": 0,
    "golem de pedra": 0,
    "golem de obsidiana":0,
}

# Golem selecionado (você pode usar depois)
golem_selecionado = 0

# Verifica se cada slot está ocupado
slots_cheio = {
    "slot1_cheio": True,
    "slot2_cheio": False,
    "slot3_cheio": False,
    "slot4_cheio": False,
}

# Mostra qual golem está em cada slot
slots = {
    "slot1_golem": "golem de ferrl",
    "slot2_golem": "vazio",
    "slot3_golem": "vazio",
    "slot4_golem": "vazio",
}

# Função principal do menu dos golems
def golem():
    while True:
        print("\n--- Slots de Golem ---")
        print(f"Slot 1 ---- {slots['slot1_golem']}")
        print(f"Slot 2 ---- {slots['slot2_golem']}")
        print(f"Slot 3 ---- {slots['slot3_golem']}")
        print(f"Slot 4 ---- {slots['slot4_golem']}")
        print("\n[1] Habilitar/Desabilitar Golem")
        print("[2] Gerenciar Golems")
        print("[0] Sair")
        
        escolha_menu_golem = input("Escolha uma opção: ")

        if escolha_menu_golem == '1':
            # Você vai completar depois essa parte de ativar/desativar
            print("Sistema de habilitar/desabilitar ainda não implementado.\n")
            pass

        elif escolha_menu_golem == '2':
            while True:
                print("\n--- Seus Golems ---")
                for nome, qtd in dados_jogador_golem.items():
                    print(f"{nome} - Quantidade: {qtd}")
                
                escolha_gerenciamento_golem = input("\nDigite o nome do golem que deseja gerenciar (ou 'voltar'): ").lower()
                if escolha_gerenciamento_golem == 'voltar':
                    break

                golem_encontrado = False
                for nome_golem in dados_jogador_golem:
                    if escolha_gerenciamento_golem == nome_golem.lower() and dados_jogador_golem[nome_golem] > 0:
                        golem_encontrado = True
                        print(f"\nGerenciando o {nome_golem}...")
                        # Aqui você vai criar o menu específico do golem depois
                        print("[1] Ver itens")
                        print("[2] Equipar item")
                        print("[3] Voltar")
                        break

                if not golem_encontrado:
                    print("Esse Golem não foi encontrado")

        elif escolha_menu_golem == '0':
            break

# Exemplo de teste
#golem()  
	    			
	    	
#upgrades classes

















   

#estoque mineiro
preco_itens_mineiro = {
"picareta de pedra":250,
"picareta de ferro":315,
"picareta de madeira":200,
"pedra":10,
"carvão":30,
"cobre bruto":60,
}
missoes_mineiro_facil = {
"consiga carvão":"pegue seu primeiro carvão",
"consiga pedra":"minere sua primeira pedra",
"consiga ferro":"minere seu primeiro ferro",
}
missoes_mineiro_medio = {
"venda seu minerio":"venda um minerio para o mineiro",
"consiga ouro":"minere seu prineiro ouro",
"consiga lava":"pegue um balde de lava",
}
missoes_mineiro_dificil = {
"consiga diamante":"minere um diamante",
"consiga obsidiana":"vá no ferreiro e misture um balde de água com um balde de lava para fazer uma barra de obsidiana",
}
dados_mineiro = {
"dinheiro":0,
"missões concluidas":0,
"dificuldade das missoes":"facil",
"recrutado guilda":False,
"itens vendidos":0,
"afinidade":0,
}
def missoes_mineiro():
	chave_missao2 = ""
	valor_missao2 = ""
	if dados_mineiro["dificuldade das missoes"] == "facil":
		
		for chave_missao,valor_missao in missoes_mineiro_facil.items():
			chave_missao2 = chave_missao
			valor_missao2 = valor_missao
		while True:
			
			print("===missões===")
		
			print(f"dificuldade:{dados_mineiro['dificuldade das missoes']}")
			print(f"{chave_missao2} {valor_missao2}")
			sair_missao_mineiro = input("aperte 0 para sair")
			if sair_missao_mineiro == "0":
				break
dados_mina = {
}
pedra = [0, 1, 2, 3, 4, 5]
ferro = [6, 7, 8]
cobre = [9, 10, 11]
carvao = [12, 13, 14, 15]
ouro = [16, 17, 18]
rio_lava = [19, 20, 21, 22, 23]
#limite x usado no for pq nao quero que quebre ou refazer num while
limite_x = 100		
contador_x_atual = 0
linha_minerios = []	
def gerar_caverna():
	global pedra,ouro,ferro,carvao,cobre,rio_lava,limite_x,contador_x_atual,linha_minerios
	
	
	while contador_x_atual <= limite_x:
				
				contador_x_atual +=1
				gerar = random.randint(0,23)
				linha_minerios.append(gerar)
	
				

ferro_nivel_y = 13
pedra_nivel_y = 0
cobre_nivel_y = 5
carvao_nivel_y = 2
rio_lava_nivel_y = 15
nivel_y_superfice = 0
nivel_x_superfice = 0				
def minerar():
	global pedra,ouro,ferro,carvao,cobre,rio_lava,limite_x,contador_x_atual,linha_minerios,ferro_nivel_y,pedra_nivel_y,cobre_nivel_y,carvao_nivel_y,rio_lava_nivel_y,nivel_x_superfice,nivel_y_superfice
	
	while True:
		limpar_terminal()
		print("[1]minerar")
		print("[2]abrir inventario")
		print("[3]usar equipamento")
		print("[0]sair")
		escolha_funcao_minerar = input("o que vai fazer?")
		if escolha_funcao_minerar == "teste de procedural":
			gerar_caverna()
		if escolha_funcao_minerar == "1":
			gerar_caverna()
			while True:
				limpar_terminal()
				print("[1]minerar pra frente")
				print("[2]minerar pra baixo")
				print("[0]sair da mina")
				escolha_mina = input("o que deseja fazer?")
				
				if escolha_mina == "1":
					
					
					
					if linha_minerios[nivel_x_superfice] in pedra:
						limpar_terminal()
						digitar("você minerou uma pedra...!")
						
						nivel_x_superfice += 1
						
						salvamento_dados["pedra"] += 1
							
					if linha_minerios[nivel_x_superfice] in cobre:
						limpar_terminal()
						digitar("você minerou um cobre bruto...!")
						
						nivel_x_superfice += 1
						salvamento_dados["cobre bruto"] +=1
						
					if linha_minerios[nivel_x_superfice] in ouro:
						limpar_terminal()
						digitar("você minerou um ouro bruto...!")
						
						nivel_x_superfice += 1
						salvamento_dados["ouro bruto"] +=1
					if linha_minerios[nivel_x_superfice] in carvao:
						limpar_terminal()
						digitar("você minerou um carvão...!")
						
						nivel_x_superfice += 1
						salvamento_dados["carvão"] += 1
					if linha_minerios[nivel_x_superfice] in rio_lava:
						limpar_terminal()
						nivel_x_superfice += 1
						digitar("você encontrou um rio de lava!!!!")
						digitar("deseja pegar um pouco de lava?precisa de um balde...!")
						print("[s]sim\n[n]não")
						escolha_rio_lava = input("o que deseja fazer?")
						if escolha_rio_lava == "s":
							if dados_itens_equipados["mao esquerda"] == "balde":
								digitar("você coletou um balde de lava...!")
								salvamento_dados["balde de lava"] += 1
								dados_itens_equipados["mao esquerda"] = ""
				
					
				if escolha_mina == "0":
					salvar_progresso()
					nivel_y_superfice = 0
					nivel_x_superfice = 0
					digitar("saindo da mina...")
					break
		if escolha_funcao_minerar == "0":
			break
		if escolha_funcao_minerar == "2":
			mostrar_inventario()
			escolha_item = input("escolha um item para usar")
			usar_item(escolha_item)
			
   
			
#mina   
def mina_eldora():
	while True:
		print("mina de eldora")
		print("[1]entrar na mina(picareta requirida)")
		print("[2]falar com o mineiro")
		print("[0]sair da mina")
		escolha_mina = input("qual opção ira escolher")
		if escolha_mina == "1":
			if dados_itens_equipados["mao direita"].startswith("picareta"):
				minerar()
			else:
				minerar()
		if escolha_mina == "0":
			digitar("você sai da mina...")
			break
		if escolha_mina == "2":
			while True:
				print("o que tu queiras meu jovem?")
				print("[1]fazer missões")
				print("[2]comprar itens")
				print("[3]vender itens e minerios")
				print("[0]sair")
				escolha_mineiro = input("qual opção selecionara?")
				if escolha_mineiro == "0":
					digitar("adeus...boa sorte na sua mineiração!")
				if escolha_mineiro == "1":
					missoes_mineiro()
				if escolha_mineiro == "2":
					
					
						
							global dados_jogador,salvamento_dados
							
    						
							while True:
											
											for chave, valor in preco_itens_mineiro.items():
													
													
    									
    												print(f"itens a venda:\n{chave}------{valor} moedas")
											
    								
    						
    						
							
						
							if "picareta de pedra" in escolha_comprar_mineiro:
								qtd_itens_mineiro = input("quantos itens?")
								preco_xqtd = int(preco_itens_mineiro["picareta de pedra"] * qtd_itens_mineiro)
								digitar("tome aqui sua picareta!")
								dados_jogador["moedas"] -= preco_xqtd
								salvamento_dados["picareta de pedra"] += qtd_itens_mineiro
							if "0" in escolha_comprar_mineiro:
								digitar("volte sempre...")
								break
							if "picareta de ferro" in escolha_comprar_mineiro:
								qtd_itens_mineiro = input("quantos itens?")
								preco_xqtd = int(preco_itens_mineiro["picareta de ferro"] * qtd_itens_mineiro)
								digitar("tome aqui sua picareta!")
								dados_jogador["moedas"] -= preco_xqtd
								salvamento_dados["picareta de ferro"] += qtd_itens_mineiro
							if "picareta de madeira" in escolha_comprar_mineiro:
								qtd_itens_mineiro = input("quantos itens?")
								preco_xqtd = int(preco_itens_mineiro["picareta de madeira"] * qtd_itens_mineiro)
								digitar("tome aqui sua picareta!")
								dados_jogador["moedas"] -= preco_xqtd
								salvamento_dados["picareta de madeira"] += qtd_itens_mineiro
							if "cobre" in escolha_comprar_mineiro:
								qtd_itens_mineiro = input("quantos itens")
								preco_xqtd = int(preco_itens_mineiro["cobre"] * qtd_itens_mineiro)
								digitar("tome aqui seu cobre")
								dados_jogador["moedas"] -= preco_xqtd
								salvamento_dados["cobre"] += qtd_itens_mineiro
							if "carvão" in escolha_comprar_mineiro:
								qtd_itens_mineiro = input("quantos itens?")
								preco_xqtd = int(preco_itens_mineiro["carvão"] * qtd_itens_mineiro)
								digitar("tome aqui seu carvão!")
								dados_jogador["moedas"] -= preco_xqtd
								salvamento_dados["carvão"] += qtd_itens_mineiro
#monumento historico de tão antigo que essa parte do codigo é...NAO REMOVA!28/07/25
					
valor_dano = 5
valor_defesa = 5
valor_inicial_compra_defesa = valor_verdadeiro_defesa = 0
guilda_word = "guilda"
quantidade_aliados = 1
valor_nivel = 1
valor_upar_nivel = 100
valor_bau = 60

conquista_pao = 0
conquista_espada = 0
conquista_bebado = 0
conquista_ganhe_bebado = 0
bebida = 0



artefato_luz = "artefato da luz"
artefato_fogo = "artefato do fogo"
artefato_agua = "artefato da agua"
artefato_lava = "artefato da lava"
artefato_diamante = "artefato do diamante"
artefato_força = "artefato da força"
artefato_defesa = "artefato da defesa"
artefato_ouro = "artefato do ouro"
artefato_sorte = "artefato da sorte"
artefato_magia = "artefato da magia"

cerveja, pinga, choro_dragao = "cerveja", "pinga", "choro de dragao"
skull_soul, dead_soul, alma_negra = "skull soul", "dead soul", "alma negra"


#armaduras e equipamentos equipados
armaduras_equipamentos = {
"capacete":0,
"peitoral":0,
"calcas":0,
"botas":0,
"escudo":0,
"espadas":0,
"adaga":0,
"adaga envenenada":0,
"espada de cobre":0,
"espada de obsidiana":0,
"espada de madeira":0,
"espada de pedra":0,
"espada de obsidiana":0,
"picareta de ferro":0,
"picareta de madeira":0,
"picareta de pedra":0,
"picareta de cobre":0,
"picareta de obsidiana":0,
"balde":0,
"balde de agua":0,
"balde de lava":0,
}
inventario_equipamentos = {
    "capacete":0,
    "peitoral":0,
    "calcas":0,
    "botas":0,
    "adaga":0,
    "espada":0,
    "adaga_envenenada":0,
    "espada de cobre":0,
	"espada de obsidiana":0,
	"espada de madeira":0,
	"espada de pedra":0,
	"espada de obsidiana":0,
	"picareta de ferro":0,
	"picareta de madeira":0,
	"picareta de pedra":0,
	"picareta de cobre":0,
	"picareta de obsidiana":0,
	"balde":0,
	"balde de agua":0,
	"balde de lava":0,
}
durabildade = {
"taxa_durabilidade_comum":100,
"taxa_durabilidade_incomum":200,
"taxa_durabilidade_raro":500,
"taxa_durabilidade_legendario":1000,
}
valor_itens = {
"capacete":0,
"peitoral":0,
"calca":0,
"botas":0,
"espada":0,
"adaga":0,
"adaga_envenenada":0,
}
verificar_equipamento = {
"capacete":False,
"peitoral":False,
"calca":False,
"botas":False,
"espada de ferro":False,
"adaga":False,
"adaga_envenenada":False,
"espada de cobre":False,
"espada de obsidiana":False,
"espada de madeira":False,
"espada de pedra":False,
"espada de obsidiana":False,
"picareta de ferro":False,
"picareta de madeira":False,
"picareta de pedra":False,
"picareta de cobre":False,
"picareta de obsidiana":False,
"balde":False,
"balde de agua":False,
"balde de lava":False
}
def morte():
    	
    	if dados_jogador["vida"] <= 0:
    		dados_jogador["vida"] = 0
    	if dados_jogador["vida"] == 0:
    	   
    	   print(VERMELHO + "VOCÊ MORREU" + RESET)
    	   resultado_exp = (dados_jogador["exp"] / 4)
    	   print(AZUL + f"você perdeu {resultado_exp} de exp" + RESET)
    	   print(dados_jogador["nome"])
    	   print("não desista você ainda tem um caminho pela frente")
    	   dados_jogador["exp"] -= resultado_exp
    	   dados_jogador["vida"] = 20
    	   lucro_maximo = 0
    	   morte = input("deseja continuar? [S] ou [N]: ").lower()
    	   if morte == "n":
    	       print("salvando o progresso...")
    	       salvar_progresso()
    	       exit()
def verificacao_morte():
            time.sleep(10)
            if dados_jogador["vida"] <= 0:
            	morte()
            else:
            	pass
segundo_plano_morte = threading.Thread(target=verificacao_morte, daemon=True)
#durabilidade itens

#juntar as funçoes

	
#verificar o equipamento	    
def verificar_equipamento():
    #isso e provisorio
    if inventario_equipamentos["picareta de pedra"] >=1:
        armaduras_equipamentos["picareta de pedra"] -= 1
    if inventario_equipamentos["picareta de madeira"] >=1:
        armaduras_equipamentos["picareta de madeira"] -= 1
    if inventario_equipamentos["picareta de ferro"] >=1:
        armaduras_equipamentos["picareta de ferro"] -= 1
    if inventario_equipamentos["picareta de cobre"] >=1:
        armaduras_equipamentos["picareta de cobre"] -= 1
    if inventario_equipamentos["picareta de obsidiana"] >=1:
        armaduras_equipamentos["picareta de obsidiana"] -= 1
    if inventario_equipamentos["espada de madeira"] >=1:
        armaduras_equipamentos["espada de madeira"] -= 1
    if inventario_equipamentos["espada de pedra"] >=1:
        armaduras_equipamentos["espada de pedra"] -= 1
    if inventario_equipamentos["espada de ferro"] >=1:
        armaduras_equipamentos["espada de ferro"] -= 1
    if inventario_equipamentos["espada de cobre"] >=1:
        armaduras_equipamentos["espada de cobre"] -= 1
    if inventario_equipamentos["espada de obsidiana"] >=1:
        armaduras_equipamentos["espada de obsidiana"] -= 1
    if inventario_equipamentos["balde"] >=1:
        armaduras_equipamentos["balde"] -= 1
    if inventario_equipamentos["balde de lava"] >=1:
        armaduras_equipamentos["balde de lava"] -= 1
    if inventario_equipamentos["balde de agua"] >=1:
        armaduras_equipamentos["balde de agua"] -= 1
    if inventario_equipamentos["capacete"] >=1:
        armaduras_equipamentos["capacete"] -= 1
        armaduras_equipamentos["capacete"] += inventario_equipamentos["capacete"]
    if inventario_equipamentos["peitoral"] >=1:
        armaduras_equipamentos["peitoral"] -= 1
        armaduras_equipamentos["peitoral"] += inventario_equipamentos["peitoral"]
    if inventario_equipamentos["calcas"] >=1:
        armaduras_equipamentos["calcas"] -= 1
        armaduras_equipamentos["calcas"] += inventario_equipamentos["calcas"] 
    if inventario_equipamentos["botas"] >=1:
        armaduras_equipamentos["botas"] -= 1
        
        armaduras_equipamentos["botas"] += inventario_equipamentos["botas"]    
    if inventario_equipamentos["adaga"] >=1:
        armaduras_equipamentos["adaga"] -= 1
        armaduras_equipamentos["adaga"] += inventario_equipamentos["adaga"]
    if inventario_equipamentos["adaga_envenenada"] >=1:
        armaduras_equipamentos["adaga_envenenada"] -= 1
        
        armaduras_equipamentos["adaga envenenada"] += inventário_equipamentos["adaga_envenenada"]
	
                   
#sistema descartado(melhor não mexer para não crashar)	
hp_bebado = 10
inimigos = ["goblin", "aranha", "slime", "caracol maligno","gorthak o tirano da pedra"]
hp_caracol = 8
hp_aranha = 15
hp_goblin = 25
hp_slime = 20
hp_gorthak = 300
hp_descaterd_aw000_unknow = 99999999999999999999999999999999999
#sistema de equipamentos

#itens e categorias da loja

moedas_word = "moedas"

itens_ataque = {
    
    "espada de pedra": 250,
    "adaga":100,
    "picareta de madeira":100,
    "machado de madeira":115,
    
    
}

itens_defesa = {

    "capacete": 50,
    "peitoral":50,
    "calças":50,
    "botas":50,
}
itens_consumiveis = {
"poção exp": 100,
    
    "pão": 10,
    "carne":20,
    "batata":5,
    "poção de stamina":100,
}
itens_outros = {
"diamantes": 250,
}

classes = ["bruxo", "cavaleiro", "goblin", "monstro", "mercador"]
def menu_mostrar_equipados():
    print("======itens equipados======")
    if dados_itens_equipados["cabeca"] == "":
        dados_itens_equipados["cabeca"] = "Nenhum"
    if dados_itens_equipados["tronco"] == "":
        dados_itens_equipados["tronco"] = "Nenhum"    
    if dados_itens_equipados["pernas"] == "":
        dados_itens_equipados["pernas"] = "Nenhum" 
    if dados_itens_equipados["pes"] == "":
        dados_itens_equipados["pes"] = "Nenhum"
    if dados_itens_equipados["mao direita"] == "":
        dados_itens_equipados["mao direita"] = "Nenhum"
    if dados_itens_equipados["mao esquerda"] == "":
        dados_itens_equipados["mao esquerda"] = "Nenhum"
        
    print("    cabeça ------",dados_itens_equipados["cabeca"])
    print("    tronco ------",dados_itens_equipados["tronco"])
    print("    pernas ------",dados_itens_equipados["pernas"])
    print("    pés    ------",dados_itens_equipados["pes"])
                   

registro_acoes = []
mensagem_missao = ""
dados_missoes = {
"missao aceitada":False,
"missoes dorian":0,
"missoes ferreiro":0,
"missoes mineiro":0,
}
npc_missao_selecionada = ""
def missoes(npc_missao_selecionada):
	if npc_missao_selecionada == "dorian":
		if dados_missoes['missoes dorian'] == 0:
			digitar("compre uma espada de pedra para dorian\nRECOMPENSAS:\n515 moedas\n100 EXP")
			escolha_dorian1 = input("[S]sim\n[N]não").lower()
			if escolha_dorian1 == "s":
				digitar(f"muito obrigado {dados_jogador['nome']}!")
				dados_missoes["missao aceitada"] = True
				mensagem_missao = "vá para a loja comprar uma espada de pedra"
			else:
				digitar("ok...sem problema,tente voltar aqui depois por favor!....")
def npc_dorian():
	limpar_terminal()
	print(f"oi {dados_jogador['nome']},como vai?")
	if dados_missoes["missoes dorian"] == 0:
		digitar("como estou ainda muito cansado eu queria pedir um favor para você,na verdade seria uma missão,o que me diz?")
		npc_missao_selecionada = "dorian"
		missoes(npc_missao_selecionada)
		
	
#IA barman
#essa porra ta mais bugada que o congresso nacional!!!e do governo eldoriano
def ia_barman():
	
	#imposto
	
	imposto_barman = int(dados_taverna["dinheiro_barman"] / 4)
	dados_taverna["dinheiro_barman"] -= imposto_barman
	#reposição de estoque
	
     

#classe espécial
sans_esqueleto = False
def classe_especial():
	
	digitar(CIANO +"esse segredo doi até o osso..." + RESET)
	sans_esqueleto = True
nome_estudio = pyfiglet.figlet_format("neverland\nstudio",font="small")
print(CIANO + nome_estudio + RESET)
posicao_loading = 0
loading = [""]
for barra_loading in range(0, 19):
	posicao_loading += 1
	
	loading.append("_")
	for mostrar_loading in loading:
			
			print(VERDE + mostrar_loading + RESET)
while True:
    ascii_menu_tloe_arte = pyfiglet.figlet_format("the legends of eldora",font="small")
    print(ascii_menu_tloe_arte)
    escolha_menu_iniciar = input("pressione enter para continuar")
    if escolha_menu_iniciar == "":
    	limpar_terminal()
    	break
    else:
    	pass


game = {
    "areas": [],     
    "npcs": [],     
    "enemies": [],   
    "items": [],      
}
def load_mod(mod_file, game):
    """
    Carrega um mod de qualquer caminho (.py) e integra ao jogo.
    game: dicionário que representa o estado do jogo
    """
    if not os.path.exists(mod_file):
        print(f"Arquivo de mod não encontrado: {mod_file}")
        return

    spec = importlib.util.spec_from_file_location("mod_module", mod_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    # Mostrar info do mod
    if hasattr(mod, "get_mod_info"):
        info = mod.get_mod_info()
        print(f"Mod carregado: {info.get('name', 'Sem nome')} por {info.get('author', 'Desconhecido')}")

    # Integrar conteúdo do mod
    if hasattr(mod, "add_content"):
        mod.add_content(game)
        print(f"Conteúdo do mod '{info.get('name', 'Sem nome')}' integrado ao jogo!")
mod_carregado = False	
def carregar_mod():
	while True:
		print("escreva o nome do mod com a extensão .py no nome")
		caminho_mod = input("")
		try:
			# Caminho do mod no seu PC
			mod_path = caminho_mod

			# Carregar o mod
			load_mod(mod_path, game)

			# Verificar se o conteúdo foi adicionado
			mod_carregado = True
			break
		except:
			digitar("algum erro foi ocorrido...")	
#salvar progresso
def salvar_progresso():
    dados_salvar = {
        "dados_jogador": dados_jogador,
        "salvamento_dados": salvamento_dados,
        "upgrades": upgrades,
        "aliados": aliados,
        "valor_habilidade": valor_habilidade,
        "dados_evolucao_nivel":dados_evolucao_nivel,
        "amigos_conectados":amigos_conectados,
        "salvamento_dados2":salvamento_dados2,
        "dados_itens_equipados":dados_itens_equipados,
        "dados_taverna":dados_taverna,
        "memoria_ferreiro":memoria_ferreiro,
        "dados_mineiro":dados_mineiro,
        "horario":horario,
        "dados_vilas":dados_vilas,
       "dados_jogador_server":dados_jogador_server,
        

    }

    with open("savegame.json", "w") as arquivo:
        json.dump(dados_salvar, arquivo, indent=4)
    print("✅ Jogo salvo com sucesso!")
def cena_inicial():
	digitar(f"você...você era um viajante que explorava vários lugares desconhecidos e inóspitos que a humanidade nunca mais pisou lá....quando você era pequeno gostava de lendas por isso que se dedica a exploração mas uma delas que você via era as lendas de eldora....um lugar feliz,vivo e prospero teve sua decadencia a ataques de diferentes monstros e inimigos,eles roubaram os 10 artefatos de eldora o que fez eldora que era um paraiso se transformar e um inferno de ruinas com poucos sobreviventes....mas era uma lenda....nada disso seria real....era o que eu achava até agora....")
	limpar_terminal()
	digitar(CIANO + "Picos Congelados de NorthHills" + RESET)
	limpar_terminal()
	digitar("em uma longa escalada para chegar ao topo dos picos congelados.....")
	limpar_terminal()
	
def carregar_progresso():
    global dados_jogador, salvamento_dados, upgrades, aliados, valor_habilidade,salvamento_dados2,dados_jogador2,dados_jogador3,dados_jogador4,amigos_conectados,dados_itens_equipados,dados_taverna,dados_mineiro,memoria_ferreiro,dados_vilas,horario,dados_jogador_server;
    if os.path.exists("savegame.json"):    
        with open("savegame.json", "r") as arquivo:
            dados_carregados = json.load(arquivo)
            dados_jogador = dados_carregados.get("dados_jogador", dados_jogador)
            salvamento_dados = dados_carregados.get("salvamento_dados", salvamento_dados)
            upgrades = dados_carregados.get("upgrades", upgrades)
            aliados = dados_carregados.get("aliados", aliados)
            valor_habilidade = dados_carregados.get("valor_habilidade", valor_habilidade)
            salvamento_dados2 = dados_carregados.get("salvamento_dados2",salvamento_dados2)
            dados_jogador2 = dados_carregados.get("dados_jogador2",dados_jogador2)
            dados_jogador3 = dados_carregados.get("dados_jogador3",dados_jogador3)
            dados_jogador4 = dados_carregados.get("dados_jogador4",dados_jogador4)
            amigos_conectados = amigos_conectados.get("amigos_conectados",amigos_conectados)
            
            dados_itens_equipados = dados_carregados.get("dados_itens_equipados",dados_itens_equipados)
            dados_taverna = dados_carregados.get("dados_taverna",dados_taverna)
            memoria_ferreiro = dados_carregados.get("memoria_ferreiro",memoria_ferreiro)
            dados_mineiro = dados_carregados.get("dados_mineiro",dados_mineiro)
            dados_vilas = dados_carregados.get("dados_vilas",dados_vilas)
            horario = dados_carregados.get("horario",horario)
            dados_jogador_server = dados_carregados.get("dados_jogador_server",dados_jogador_server)
        print("✅ Progresso carregado com sucesso!")
    else:
        limpar_terminal()
        digitar("desculpe....mas você não tem nenhum save disponivel o que resultara no fechamento do jogo")
        time.sleep(3)
        exit()

digitar("The Legends Of Eldora, todos os direitos reservados a Luiz Gustavo™luizsgustavo76@gmail.com")
digitar("Bem-vindo ao reino de Eldora")
print("Seu objetivo em Eldora é pegar os 10 artefatos para reinstaurar a paz no reino.")

carregar = input("O que deseja fazer?\n[1]novo jogo\n[2]carregar um jogo salvo\n[3]carregar um mod\n[4]creditos\n[5]sair: ").lower()
if carregar == "2":
    carregar_progresso()
    digitar(f"bem vindo de volta a Eldora {dados_jogador['nome']}")
if carregar == "4":
	while True:
		limpar_terminal()
		print("jogo somente feito por Luiz Gustavo")
		
		print("começo do desenvolvimento do projeto em fevereiro de 2025")
		print("instagram:luizsgustavo75")
		print("Email:luizsgustavo76@gmail.com")
		print("site oficial:thelegendsofeldora.wordpress.com")
		sair_creditos = input("aperte enter ou 0 para sair")
		if sair_creditos == "0":
			exit()
		if sair_creditos == "":
			exit()
if carregar == "3":
	carregar_mod()
if carregar == "5":
	digitar("até mais...")
	exit()
if carregar == "1":
    dados_jogador['nome'] = input("Por favor, escolha seu nome: ")
    
   
    if dados_jogador["nome"].lower() == "motherfucker":
        
        print("Cheat ativado,menu de trapaças")
        trapaca1 = input("quantos de moedas?")
        trapaca2 = input("qual nivel?")
        trapaca3 = input("quantos diamantes?")
        dados_jogador["moedas"] = trapaca1
        dados_jogador["nivel"] = trapaca2
        dados_jogador["diamantes"] = trapaca3
      

    print("Bem-vindo ao reino de Eldora, por favor escolha sua classe:")
    
    		
    escolha = input("(1) Bruxo,\n(2) Cavaleiro,\n(3) Goblin,\n(4) Monstro\n(5) Mercador: ")

    if escolha in ["1", "2", "3", "4", "5"]:
        dados_jogador["classe"] = classes[int(escolha) - 1]
   
    else:
        print("Opção inválida")
        exit()
    cena_inicial()

    print(f"Bem-vindo a Eldora, {dados_jogador['nome']}, o {dados_jogador['classe']}!")
    definir_horario()
    


			
					
					
				
			
				
				
			
		


            
            
            
        
        
        
        
        
    	   
        	
        	
       
        	
        	
        
        
        
        
        
    
    	
    
   
       
          	
          	
              
          	
        	
        
        	
conectado_server = False       
while True:   
    chance_mudar_clima = random.randint(0,100)
    if chance_mudar_clima >= 60:
        clima()         
    tempo_atual = time.time()
    if tempo_atual - tempo_ultimo_save >= intervalo:
        salvar_progresso()
        tempo_ultimo_save = tempo_atual
    import time
    tempo_ultimo_ativamento = time.time()
    tempo_atual = time.time()
    if tempo_atual - tempo_ultimo_ativamento >= 20:
            		 
            		 	
            		 	tempo_ultimo_ativamento = tempo_atual
            		 	time.sleep(1)
            		 
            		 	
            		 	
            		
            		
    
    finais_alternativos()		
    ia_barman()
    limpar_terminal()
    print(f"{horario['horas']}:{horario['minutos']} horas")       
    print("Você chegou ao centro de Eldora. O que deseja fazer?")
    registro_acoes.append("centro")
    if mensagem_missao == "":
    	pass
    else:
    	print(mensagem_missao)
    print("[1] Ir à taverna")
    print("[2] Ver seus status")
    print("[3] Ir para sua casa")
    print("[4] Sair do jogo")
    print("[5] Ir à loja")
    print("[6] Ir no inventário")
    print("[7] Enciclopédia")
    print("[8] Ver conquistas")
    print("[9] Salvar jogo")
    print("[10]Carregar jogo")
    print("[11]upgrades")
    print("[12]guilda")
    print("[13]arena infinita")
    print("[14]menu online")
    print("[15]abrir o mapa")
    print("[16]ferreiro")
    if conectado_server:
   	 print("[17]chat geral")
   	 print("[18]amigos")
   	 print("[19]sair do servidor")

    escolha_centro = input("O que vai fazer? ")
    if escolha_centro == "19":
    	conectado_server = False
    if escolha_centro == "17":
    	pass
    if escolha_centro == "teste_server":
    	carregar_dados_servidor()
    	
    if escolha_centro == "teste_chat_multiplayer":
    	abrir_chat()
    if escolha_centro == "teste bau":
    	bau_pergaminho()
    #ferreiro
    if escolha_centro == "16":
    	registro_acoes.append("ferreiro")
    	print("=====ferreiro=====")
    	digitar("olá,bem vindo ao ferreiro,aqui você pode forjar seus equipamentos e golens")
    	while True:
    		limpar_terminal()
    		print("=====ferreiro=====")
    		print("[1]forjar equipamento")
    		print("[2]encantar itens")
    		print("[3]concertar itens")
    		print("[4]forjar golem")
    		print("[5]conversar")
    		print("[0]sair")
    		escolha_ferreiro = input("qual opção tu queres")
    		if escolha_ferreiro == "4":
    			digitar(f"bela escolha {dados_jogador['nome']} ")
    			if salvamento_dados["cobre"] >=1:
    				print(f"cobre:{salvamento_dados['cobre']}")
    			if salvamento_dados["barra_ferro"] >=1:
    				print(f"ferro:{salvamento_dados['barra_ferro']}")
    			if salvamento_dados["barra_ouro"] >=1:
    				print(f"ouro:{salvamento_dados['barra_ouro']}")
    			if salvamento_dados["obsidiana"] >=1:
    				print(f"obsidiana:{salvamento_dados['obsidiana']}")
    			if salvamento_dados["madeira"] >=1:
    				print(f"madeira:{salvamento_dados['madeira']}")
    			if salvamento_dados["amuleto_da_necromancia2"] >=1:
    				print(f"amuleto da necromancia:{salvamento_dados['amuleto_da_necromancia2']}")
    		if escolha_ferreiro == "2":
    			for pergaminho_lista in salvamento_dados.items():
    				pergaminho_lista = str(pergaminho_lista)
    				print(pergaminho_lista.startswith("pergaminho"))
    			time.sleep(10)
    		receitas_ferreiro = {
    		"picareta de pedra": {
    			"madeira":2,
    			"pedra":3,
    		},
    		"picareta de madeira": {
    			"madeira":5,
    		},
    		"picareta de ferro": {
    			"ferro":3,
    			"madeira":2,
    		},
    		"espada de pedra": {
    			"pedra":2,
    			"madeira":1,
    		},
    		"espada de ferro": {
    			"barra de ferro":2,
    			"madeira":1,
    		},
    		"espada de madeira": {
    			"madeira":4,
    		},
    		"balde de ferro": {
    			"barra de ferro":6,
    		},
    		"obsidiana": {
    			"balde de agua":1,
    			"balde de lava":1,
    		},
    		"picareta de cobre": {
    			"barra de cobre":3,
    			"madeira":2,
    		},
    		"espada de cobre": {
    			"barra de cobre":2,
    			"madeira":1,
    		},
    		"espada de obsidiana": {
    			"obsidiana":3,
    			"madeira":1,
    		},
    		"picareta de obsidiana": {
    			"obsidiana":3,
    			"madeira":2,
    		},
    		"machado de madeira": {
    			"madeira":5,
    		},
    		"machado de pedra": {
    			"madeira":2,
    			"pedra":3,
    		},
    		"machado de ferro": {
    			"madeira":2,
    			"barra de ferro":3,
    		},
    		"machado de cobre": {
    			"madeira":2,
    			"barra de cobre":3,
    		},
    		"machado de obsidiana": {
    			"madeira":2,
    			"obsidiana":3,
    		},
    		}
    		if escolha_ferreiro == "1":
    			while True:
    				limpar_terminal()
    				for item,materiais in receitas_ferreiro.items():
    					print(f"\n {item.upper()}:")
    					for material,quantidade in materiais.items():
    						print(f"     {quantidade}x---- {material}")
    				print("[0]sair")
    				escolha_forja = input("qual item deseja forjar")
    
    				
    					
    				
    				if escolha_forja == "0":
    					break
    		if escolha_ferreiro == "0":
    			limpar_terminal()
    			digitar(f"volte sempre meu {dados_jogador['classe']}")
    			break
    		if escolha_ferreiro == "5":
    			
    			print("Conversa com o ferreiro:")
    			print("tipos de conversa")
    			print("[1]modo livre")
    			print("[2]perguntas predefinidas")
    			print("*modo livre-escreva qualquer coisa")	
    			escolha_modo_falar_ferreiro = input("qual modo deseja conversar")
    			if escolha_modo_falar_ferreiro == "2":
    				while True:
    					print("=====FERREIRO=====")
    					print("qual assunto deseja conversar?")
    					print("[1]economia")
    					print("[2]ajuda")
    					print("[3]batalha")
    					print("[4]elogiar")
    					print("[5]locais")
    					print("[6]climas")
    					print("[0]sair")
    					escolha_assunto_chat = input("")
    					if escolha_assunto_chat == "0":
    						digitar(f"ate mais {dados_jogador['classe']}")
    						break
    					if escolha_assunto_chat == "1":
    							print("[1]seus preços são muito altos")
    							print("[2]seus preços são muito baixos")
    							print("[3]a economia de eldora é muito ruim")
    							print("[4]a economia de eldora é muito boa")
    							escolha_economia_chat = input("")
    							if escolha_economia_chat == "1":
    								digitar("olha...\ndesculpa,a economia de eldora não está muito boa hoje em dia")
    							if escolha_economia_chat == "2":
    								digitar("que bom saber disso por que hoje em dia em eldora está tudo mais dificil de comprar")
    							if escolha_economia_chat == "3":
    								digitar("isso é verdade pois a 5 anos atras aquele rei prometia voltar a epoca de ouro de eldora mas aconteceu o contrario agora passamos pela essa idade das trevas")
    							if escolha_economia_chat == "4":
    								digitar(".....\nvocê não sabe o que eu e as outras pessoas passamos,você chegou agora nesse reino ...")  
    					if escolha_assunto_chat == "2":
    							
    							
    						    digitar("o que eu poderia lhe ajudar?")
    																	
    			if escolha_modo_falar_ferreiro == "1":
    				
    				
    			    
    					   
    					   
    					    	
    				
    				
    									
    							
    					
    
    								    
                
                 
                 
    					
    				while saida_chat == 1:
    					pergunta_ferreiro = input("DIALOGO>>>")
    					memoria_ferreiro["vezes_perguntas"] += 1
    					ferreiro_responder(pergunta_ferreiro,saida_chat)
    					
    					
    					
    						
    					
    				
    					
    


        
    
            
                
            
                
            
                
    							     
                
            
                
            
            
        
    

    					
    					
    #mapa
    if escolha_centro == "15":
    	registro_acoes.append("mapa")
    	limpar_terminal()
    	print("=====MAPA=====")
    	time.sleep(1)
    	limpar_terminal()
    	while True:
    		print("====ELDORA====")
    		print("")
    		print("")
    		print("######VILAS#####")
    		print("[1]Rimvark")
    		print("[2]Ebrenthal")
    		print("[3]Vangurd")
    		print("[4]Nocten")
    		print("######AREAS ABERTAS#####")
    		print("[5]Floresta das almas")
    		print("[6]Deserto da morte")
    		print("[7]mina de eldora")
    		if mod_carregado:
    			for i,(areas_mods) in enumerate(game["areas"],start=8):
    				print("####AREAS ADICIONADAS POR MODS#####")
    				print(f"[{i}] {areas_mods}")
    		print("[0]sair")
    		escolha_mapa = input("qual area deseja ir?")
    		limpar_terminal()
    		if escolha_mapa >=8 and mod_carregado:
    			pass
    		if escolha_mapa == "1":
    			registro_acoes.append("rimvark")
    			vila_rimvark()
    		if escolha_mapa == "0":
    			break
    		if escolha_mapa == "2":
    			registro_acoes.append("ebranthal")
    			vila_ebranthal()
    		if escolha_mapa == "3":
    			registro_acoes.append("vangurd")
    			vila_vangurd()
    		if escolha_mapa == "4":
    			registro_acoes.append("nocten")
    			vila_nocten()
    		if escolha_mapa == "7":
    			registro_acoes.append("mina")
    			mina_eldora()
    			
    voltar_inventario = 1
    if escolha_centro == "6":
        registro_acoes.append("inventario")
        limpar_terminal()
        while voltar_inventario == 1:	
            
            print("[1]abrir o inventário")
            print("[2]usar equipamentos")
            print("[0]sair")
            escolha_menu_inventario = input("qual função deseja usar")
            if escolha_menu_inventario == "0":
            	 break
            
                
                
                
                
            if escolha_menu_inventario == "1":
                limpar_terminal()
                voltar_inventario = 1
                mostrar_inventario()
                escolha_item = input("Escolha um item para usar\nou aperte [0] para sair").strip()
                usar_item(escolha_item)
            if escolha_menu_inventario == "2":
                limpar_terminal()
                voltar_inventario = 0
                verificar_equipamento()
                durabilidade_equipamentos = {
                    "espada":100,
                    "capacete":100,
                    "peitoral":100,
                    "calcas":100,
                    "botas":100,
                    "adaga":100,
                    "adaga_envenenada":100,
                    "armadura_sombria":100,
                }    
                def mostrar_equipamento():
                    
                    vazio = True
                    for dicionario in [armaduras_equipamentos]:
                        
                    
                
                        for chave, valor in dicionario.items():
                            
                        
                    
                            if isinstance(valor, int) and valor > 0:
                                
                            
                        
                        
                                nome = chave.replace("_", " ")
                                nome_formatado = ''.join(c for c in nome if c.isalpha() or c == ' ').title()
                                print(f"{nome_formatado}: {valor}")
                                vazio = False
                menu_mostrar_equipados()                
                mostrar_equipamento()
                def status_equipamentos():
                    status_defesa = {
                        "capacete":5,
                        "peitoral":10,
                        "calcas":2.5,
                    }    
                    status_ataque = {
                        "espada":7,
                        "adaga":4,
                        "adaga_envenenada":9,
                    }
                    status_veneno = {
                        "adaga_envenenada":5,
                    }    
                    status_buff = {
                        "botas":5,
                    }
                    if dados_itens_equipados["cabeca"] == "capacete":
                        dados_jogador["defesa"] += status_defesa["capacete"]
                    if dados_itens_equipados["tronco"] == "peitoral":
                        dados_jogador["defesa"] += status_defesa["peitoral"] 
                    if dados_itens_equipados["pernas"] == "calças":
                        dados_jogador["defesa"] += status_defesa["calcas"] 
                    if dados_itens_equipados["pes"] == "botas":
                        dados_jogador["esquivar"] += status_defesa["botas"] 
                    if dados_itens_equipados["mao direita"] == "espada":
                        dados_jogador["dano"] += status_ataque["espada"]             
                            
                            
                status_equipamentos()       
                equipar = input("qual item deseja\nequipar?")
                if equipar == "picareta de pedra":
                    if inventario_equipamentos["picareta de pedra"] >= 1:
                        mao_direita_equipado = 0
                        inventario_equipamentos["picareta de pedra"] = 0
                        print("o item 'picareta de pedra' foi equipado")
                        dados_itens_equipados["mao direita"] = "botas"
                    else:
                        print("você não tem esse item no inventário ")
                if equipar == "picareta de madeira":
                    
                    if inventario_equipamentos["picareta de madeira"] >= 1:
                        mao_direita_equipado = 0
                        inventario_equipamentos["picareta de madeira"] = 0
                        print("o item 'picareta de madeira' foi equipado")
                        dados_itens_equipados["mao direita"] = "botas"
                    else:
                        print("você não tem esse item no inventário ")
                if equipar == "picareta de ferro":
                    if inventario_equipamentos["botas"] >= 1:
                        mao_direita_equipado = 0
                        inventario_equipamentos["picareta de ferro"] = 0
                        print("o item 'picareta de ferro' foi equipado")
                        dados_itens_equipados["mao direita"] = "picareta de ferro"
                    else:
                        print("você não tem esse item no inventário ")
                if equipar == "picareta de cobre":
                    if inventario_equipamentos["picareta de cobre"] >= 1:
                        mao_direita_equipado = 0
                        inventario_equipamentos["picareta de cobre"] = 0
                        print("o item 'picareta de cobre' foi equipado")
                        dados_itens_equipados["mao direita"] = "botas"
                    else:
                        print("você não tem esse item no inventário ")
                if equipar == "picareta de obsidiana":
                    if inventario_equipamentos["picareta de obsidiana"] >= 1:
                        mao_direita_equipado = 0
                        inventario_equipamentos["picareta de obsidiana"] = 0
                        print("o item 'picareta de obsidiana' foi equipado")
                        dados_itens_equipados["mao direita"] = "picareta de obsidiana"
                    else:
                        print("você não tem esse item no inventário ")
                if equipar == "espada de pedra":
                    if inventario_equipamentos["espada de pedro"] >= 1:
                        mao_direita_equipado = 0
                        inventario_equipamentos["picareta de obsidiana"] = 0
                        print("o item 'espada de pedra' foi equipado")
                        dados_itens_equipados["mao direita"] = "espada de pedra"
                    else:
                        print("você não tem esse item no inventário ")
                if equipar == "espada de madeira":
                    if inventario_equipamentos["espada de madeira"] >= 1:
                        mao_direita_equipado = 0
                        inventario_equipamentos["espada de madeira"] = 0
                        print("o item 'espada de madeira' foi equipado")
                        dados_itens_equipados["mao direita"] = "espada de madeira"
                    else:
                        print("você não tem esse item no inventário ")
                if equipar == "espada de ferro":
                    if inventario_equipamentos["espada de ferro"] >= 1:
                        mao_direita_equipado = 0
                        inventario_equipamentos["espada de ferrl"] = 0
                        print("o item 'espada de ferro' foi equipado")
                        dados_itens_equipados["mao direita"] = "espada de ferro"
                    else:
                        print("você não tem esse item no inventário ")
                if equipar == "espada de cobre":
                    if inventario_equipamentos["espada de cobrw"] >= 1:
                        mao_direita_equipado = 0
                        inventario_equipamentos["espada de cobre"] = 0
                        print("o item 'espada de cobre' foi equipado")
                        dados_itens_equipados["mao direita"] = "espada de cobre"
                    else:
                        print("você não tem esse item no inventário ")
                if equipar == "espada de obsidiana":
                    if inventario_equipamentos["espada de obsidiana"] >= 1:
                        mao_direita_equipado = 0
                        inventario_equipamentos["espada de obsidiana"] = 0
                        print("o item 'espada de obsidiana' foi equipado")
                        dados_itens_equipados["mao direita"] = "espada de obsidiana"
                    else:
                        print("você não tem esse item no inventário ")
                if equipar == "balde":
                    if inventario_equipamentos["balde"] >= 1:
                        mao_direita_equipado = 0
                        inventario_equipamentos["balde"] = 0
                        print("o item 'balde' foi equipado")
                        dados_itens_equipados["mao esquerda"] = "balde"
                    else:
                        print("você não tem esse item no inventário ")
                if equipar == "capacete":
                    if inventario_equipamentos["capacete"] >= 1:
                        cabeca_equipado = 1
                        inventario_equipamentos["capacete"] = 0
                        print("o item 'capacete' foi equipado")
                        dados_itens_equipados["cabeca"] = "capacete"
                        
                    else:
                        print("você não tem esse item no inventário ")   
                if equipar == "peitoral":
                    if inventario_equipamentos["peitoral"] >= 1:
                        tronco_equipado = 1
                        inventario_equipamentos["peitoral"] = 0
                        print("o item 'peitoral' foi equipado")
                        dados_itens_equipados["tronco"] = "peitoral"
                    else:
                        print("você não tem esse item no inventário ")
                if equipar == "calças" or "calcas":
                    if inventario_equipamentos["calcas"] >= 1:
                        pernas_equipado = 1
                        inventario_equipamentos["calcas"] = 0
                        print("o item 'calças' foi equipado")
                        dados_itens_equipados["pernas"] = "calças"
                    else:
                        print("você não tem esse item no inventário ")
                if equipar == "botas":
                    if inventario_equipamentos["botas"] >= 1:
                        pes_equipado = 0
                        inventario_equipamentos["botas"] = 0
                        print("o item 'botas' foi equipado")
                        dados_itens_equipados["pes"] = "botas"
                    else:
                        print("você não tem esse item no inventário ")
                      
    elif escolha_centro == "teste_barra_vida":
        barra_vida()
    elif escolha_centro == "teste_batalha":
        batalha_padrao()
        
        
        
        
    	
        
                                        
                        
                    
                
            
        
    	
            
        	
    	
    	
#online
    elif escolha_centro == "14":
        escolha_modo_online = input("você deseja jogar como?\n[1]localmente(via lan)\n[2]servidor global")
        if escolha_modo_online == "2":
        	print("[1]conectar ao servidor")
        	print("[2]mudar configurações de conexão")
        	print("[0]sair")
        	escolha_menu_servidor = input("o que deseja fazer?")
        	if escolha_menu_servidor == "0":
        		break
        	if escolha_menu_servidor == "1":
        		pass
        	if escolha_menu_servidor == "2":
        		print("[1]alterar servidor padrão")
        		print("[0]sair")
        		inp_configuracao_rede = input("qual opção tu queres?")
        		if inp_configuracao_rede == "1":
        			pass
        
    		
    if escolha_centro == "teste_golem":
    	print("aviso isso é um comando de testes internos!")
    	time.sleep(1)
    
    	golem()
    	
       
    	
    

    	


    	
    	
    	


   
    
    
    
    

    
    

        
    
    
    
    
    
    

    
    
    
   
    	
    	



        	
        
        
    

    

     
   
    	
    	
    
   
        	
     
#ARENA INFINTA
    if escolha_centro == "13":
        registro_acoes.append("arena infinita")
        print(VERMELHO + "BEM VINDO A ARENA INFINITA" + RESET)
        print("qual modo deseja jogar")
        print("[1]facil")
        print("[2]medio")
        print("[3]dificil")
        print("[4]INFERNO")
        escolha_dificuldade = input("")
        taxa_de_evolucao = 0
        defesa_monstro = 10
        hp_monstro = 10
        dano_monstro = 3
        vida_definida = 10
        time = 0
        time2 = 0
        wave = 1
        wave_time = 0
        zombaria = 0
        ataque_selvagem = 0
        #dificuldades de arena
        if escolha_dificuldade == "1":
            
            tela_morte["facil"] = 1
            dificuldade_selecionada = "facil"
            facil = 2
            resultado_dificuldade = int(taxa_de_evolucao + facil)
            taxa_de_evolucao = resultado_dificuldade
        elif escolha_dificuldade == "2":
            tela_morte["medio"] = 1
            dificuldade_selecionada = "facil"
            medio = 4
            resultado_dificuldade2 = int(taxa_de_evolucao + medio)
            taxa_de_evoluçao = resultado_dificuldade2
        elif escolha_dificuldade == "3":
            dificuldade_selecionada = "facil"
            tela_morte["dificil"] = 1
            calcular_dano = int(dados_jogador["dano"] * 1.25)
            calcular_defesa = int(dados_jogador["defesa"] * 1.25)
            calcular_vida = int(dados_jogador["vida"] * 1.25)
            dano_monstro = calcular_dano
            hp_monstro = calcular_vida
            defesa_monstro = calcular_defesa
        elif escolha_dificuldade == "4":
            dificuldade_selecionada = "facil"
            tela_morte["inferno"] = 1
            dano_monstro = dados_jogador["dano"]
            defesa_monstro = dados_jogador["defesa"]
            hp_monstro = dados_jogador["vida"]
            
        
        while dados_jogador["vida"] >=0:
            valor_dialogo = 0
            salvar_progresso()
           
            	
            	
            				
            		
            		
            
            	
            
            if hp_monstro <=0:
                hp_monstro = vida_definida
            boss_batalha(dificuldade_selecionada)
            print(VERMELHO + "UM MONSTRO APARECEU")
            barra_vida()
            print("VIDA:",dados_jogador["vida"])
            print("VIDA MONSTRO:",hp_monstro)
            print("onda:",nivel_arena)
            print("" + RESET)
            chance_bau_arena = random.randint(0,7)
            if chance_bau_arena == 7:
            	bau_pergaminho()
            else:
            	pass
            print("[1]atacar")
            print("[2]defender")
            print("[3]habilidade")
            print("[4]trocar aliado")
            print("[5]inventario")
            print("[6]fugir")
            escolha_arena = input("escolha uma opçao")
            if escolha_arena == "5":
            	print("você abre seu inventario")
            	print("=======INVENTARIO=======")
            	mostrar_inventario()
            	escolha_item = input("escolha um item para usar:").strip()
            	usar_item(escolha_item)
            	
            	
            	
            	
            if time >=1:
            	time -=1
            if time <=0:
            	zombaria = 0
            if time2 < 1:
            	chance_zombaria = random.randint(0,100)
            	if chance_zombaria >=45:
            		zombaria = 1
            	if chance_zombaria <=45:
            		zombaria = 0
            		
            if escolha_arena == "1":
                chance_critico = 5
                sortear_critico = random.randint(0,5)
                if dados_itens_equipados["mao esquerda"] or dados_itens_equipados["mao direita"] == "adaga":
                	chance_critico -= 2
                if chance_critico == sortear_critico:
                	limpar_terminal()
                	print(VERMELHO +"VOCÊ DEU ATAQUE CRITICO!!!!!" + RESET)
                	ataque_critico = int(dados_jogador["dano"] * 2)
                	
                	hp_monstro -= ataque_critico
                
                if ataque_selvagem >=1:
                	print("você esta com o efeito do ataque selvagem")
                	print(f"vida monstro: {hp_monstro}")
                	print("hp:",dados_jogador["vida"])
                	atq1 = input('[1]atacar')
                	if atq1 == "1":
                		
                			
             
                		hp_monstro -= dados_jogador["dano"]
                		print(f"vida monstro: {hp_monstro}")
                		
                	print("hp:",dados_jogador["vida"])
                	atq2 = input('[1]atacar')
                	
                	
                	
                
                
                			
                	
                limpar_terminal	
                print(VERDE + "você atacou o monstro" + RESET)
                
                limpar_terminal()
                print("você tirou",dados_jogador["dano"])
                
                limpar_terminal()
                print(f"você perdeu {dano_monstro} de hp")
                dados_jogador["vida"] -= dano_monstro
               
                hp_monstro -= dados_jogador['dano']
            elif escolha_arena == "4":
            	print("aliados de",dados_jogador["nome"])
            	print("[0]sair")
            	if aliados["antigo_guerreiro"] >=1:
            		print("[1]antigo guerreiro")
            	if aliados["bebado"] >=1:
            		print("[2]bebado")
            	escolha_trocar_aliado = input("qual aliado deseja trocar")
            	if escolha_trocar_aliado == "2":
            		if aliados["bebbado"] >= 1:
            			print("[1]trocar")
            			print("[2]ver status")
            			escolha_trocar_bebado = input("escolha uma opção")
            			if escolha_trocar_bebado == "1":
            				dados_iogador3["vida"] = dados_jogador["vida"]
            				dados_iogador3["nivel"] = dados_jogador["nivel"]
            				dados_iogador3["dano"] = dados_jogador["dano"]
            				dados_iogador3["defesa"] = dados_jogador["defesa"]
            				dados_jogador["vida"] = dados_jogador4["vida"]
            				dados_jogador["nivel"] = dados_jogador4["nivel"]
            				dados_jogador["dano"] = dados_jogador4["dano"]
            				dados_jogador["defesa"] = dados_jogador4["defesa"]
            				limpar_terminal()
            				print("você trocou com o bebado")
            			if escolha_trocar_bebado == "2":
            				while True:
            					limpar_terminal()
            					print("========STATUS=======")
            					print("vida",dados_jogador4["vida"])
            					print("dano",dafods_jogador4["dano"])
            					print("defesa",dados_jogador4["defesa"])
            					print("nivel",dafos_jogador4["nivel"])
            					sair_status_bebado = input("para sair aperte [0]")
            					if sair_status_bebado == "0":
            						break
            					else:
            						print("tente novamente")
            			
            		
            		
            	if escolha_trocar_aliado == "1":
            		limpar_terminal()
            		if aliados["antigo_guerreiro"] >=1:
            			print("[1]trocar")
            			print("[2]ver status")
            			escolha_trocar_guerreiro = input("escolha uma opção")
            			if escolha_trocar_guerreiro == "2":
            				while True:
            					
            					print("=========STATUS==========")
            					print("vida",dados_jogador2["vida"])
            					print("dano",dados_jogador2["dano"])
            					print("defesa",dados_jogador2["defesa"])
            					print("nivel",dados_jogador2["nivel"])
            					sair_status = input("para sair coloque [0]")
            					if sair_status == "0":
            						break
            					else:
            						print("resposta invalida")
            				
            					
            					
            				
            				
            					
            				
            				
            				
            			if escolha_trocar_guerreiro == "1":
            				print("você trocou com o antigo guerreiro")
            				dados_jogador3["vida"] = dados_jogador["vida"]
            		dados_jogador3["defesa"] = dados_jogador["defesa"]
            		dados_jogador3["dano"] = dados_jogador["dano"]
            		dados_jogador["vida"] = dados_jogador2["vida"]
            		dados_jogador["dano"] = dados_jogador2["dano"]
            		dados_jogador["defesa"] = dados_jogador2["defesa"]
            		
            		
            		
            	
            	
            	
            elif escolha_arena == "2":
                if valor_habilidade["mana"] >= 25:
                    defender = random.randint(0,100)
                    if defender >=50:
                    	print("voce consegue se defender")
                    	
                    	print("o ataque volta para o inimigo")
                    	dano_diminuido_monstro = int(dano_monstro // dados_jogador["defesa"])
                    	hp_monstro -= dano_diminuido_monstro
                    	valor_habilidade["mana"] -=25
                    else:
                    	print("você não tem mana o suficiente!")
                    	
                    	
                   
                    
                    
                    
                    
                    
                    
                
              
            elif escolha_arena == "3":
                print("=====suas habilidades=====")
                print("sua classe:",dados_jogador["classe"])
                
                if dados_jogador["classe"] == "cavaleiro":
                    if int(dados_jogador["nivel"]) >=1:
                        if dados_jogador["classe"] == "cavaleiro":
                            print(upgrades["habilidade_cavaleiro"])
                
                if int(dados_jogador["nivel"]) >=10:
                    if dados_jogador["classe"] == "cavaleiro":
                        print(upgrades["habilidade_cavaleiro2"])
                
                if int(dados_jogador["nivel"]) >=15:
                    if dados_jogador["classe"] == "cavaleiro":
                        print(upgrades["habilidade_cavaleiro3"])
                
                if int(dados_jogador["nivel"]) >=50:
                    if dados_jogador["classe"] == "cavaleiro":
                        print(upgrades["habilidade_cavaleiro4"])
                
                if dados_jogador["classe"] == "bruxo":
                    if int(dados_jogador["nivel"]) >=1:
                        print(upgrades["habilidade_bruxo"])
                    if int(dados_jogador["nivel"]) >=10:
                        print(upgrades["habilidade_bruxo2"])
                    if int(dados_jogador["nivel"]) >=15:
                        print(upgrades["habilidade_bruxo3"])
                    if int(dados_jogador["nivel"]) >=50:
                        print(upgrades["habilidade_bruxo4"])
                elif dados_jogador["classe"] == "goblin":
                    if int(dados_jogador["nivel"]) >=1:
                        print(upgrades["habilidade_goblin"])
                    if int(dados_jogador["nivel"]) >=10:
                        print(upgrades["habilidade_goblin2"])
                    if int(dados_jogador["nivel"]) >=5:
                        
                        print(upgrades["habilidade_goblin3"])
                    if int(dados_jogador["nivel"]) >=50:
                        print(upgrades["habilidade_goblin4"])
                elif dados_jogador["classe"] == "monstro":
                    if int(dados_jogador["nivel"]) >=1:
                        print(upgrades["habilidade_monstro"])
                    if int(dados_jogador["nivel"]) >=10:
                        print(upgrades["habilidade_monstro2"])
                    if int(dados_jogador["nivel"]) >=15:
                        print(upgrades["habilidade_monstro3"])
                    if int(dados_jogador["nivel"]) >=50:
                        print(upgrades["habilidade_monstro4"])
                elif dados_jogador["classe"] == "mercador":
                    if int(dados_jogador["nivel"]) >=1:
                        print(upgrades["habilidade_mercador"])
                    if int(dados_jogador["nivel"]) >=10:
                        print(upgrades["habilidade_mercador2"])
                    if int(dados_jogador["nivel"]) >=15:
                        print(upgrades["habilidade_mercador3"])
                    if int(dados_jogador["nivel"]) >=50:
                        print(upgrades["habilidade_mercador4"])
                
                escolha_usar_habilidade = input("Qual habilidade deseja usar? Se for nenhuma, escolha [0],se precisar de ajuda escolha [1]: ")
                if escolha_usar_habilidade == "1":
                	print('vejamos escolheu a ajuda',dados_jogador["nome"],dados_jogador["classe"])

                if dados_jogador["classe"] == "cavaleiro":
                    if escolha_usar_habilidade == upgrades["habilidade_cavaleiro"]:
                        if valor_habilidade["mana"] >= 10:
                            print("você usou", upgrades["habilidade_cavaleiro"])
                            valor_habilidade["mana"] -= 10
                            print("você tirou 10 de vida do monstro")
                            print(f"MONSTRO TE DEU {dano_monstro} DE DANO!!")
                            dados_jogador["vida"] -= dano_monstro
                        else:
                            print("Você não tem mana suficiente")

                    elif escolha_usar_habilidade == upgrades["habilidade_cavaleiro4"]:
                        if valor_habilidade["mana"] >=25:
                            print("você recebeu a benção do voto de honra")
                            print(VERDE + "seus ataques e defesas serão multiplicados por 3 mas não podera fugir e recebera o ataque critico duas vezes mais forte" + RESET)
                            dano_cav4 = (dados_jogador["dano"] * 3)
                            defesa_cav4 = (dados_jogador["defesa"] * 3)
                            dados_jogador["dano"] = dano_cav4
                            dados_jogador["defesa"] = defesa_cav4
                            valor_habilidade["mana"] -= 25
                        else:
                            print("você não tem mana o suficiente")
                    elif escolha_usar_habilidade == upgrades["habilidade_cavaleiro3"]:
                        print("você atacou o monstro usando investida brutal")
                        print("-15 mana")
                        dano_cav3 = int(dados_jogador["dano"] * 3)
                        print(f"você tirou {dano_cav3} de dano")
                        print(f"o monstro tirou {dano_monstro} de hp")
                        valor_habilidade["mana"] -=15
                        hp_monstro -= dano_cav3
                        dados_jogador["vida"] -= dano_monstro
                    elif escolha_usar_habilidade == upgrades["habilidade_cavaleiro2"]:
                        print("você usou escudo sagrado")
                        print("você recebeu a benção sagrada ")
                        print(f"monstro atacou dando {dano_monstro} de dano")
                        dano_escudo = (dano_monstro * 3)
                        dano_monstro2 = (dano_escudo - dano_monstro)
                        hp_monstro = dano_monstro2
                        print(f"o escudo reconchiteo ")

                elif dados_jogador["classe"] == "bruxo":
                    if escolha_usar_habilidade == upgrades["habilidade_bruxo"]:
                        if valor_habilidade["mana"] >=25:
                            print("você soltou uma bola de fogo")
                            hp_monstro -=25
                            dados_jogador["vida"] -= dano_monstro
                            valor_habilidade["mana"] -=25
                        else:
                            print("você não tem mana o suficiente")
                            
                    elif escolha_usar_habilidade == upgrades["habilidade_bruxo2"]:
                        if valor_habilidade["mana"] >= 20:
                            print("você solta uma explosão arcana")
                            chance_queimadura = random.randint(0,100)
                            if chance_queimadura >=75:
                                print("a explosão arcana causou queimadura no inimigo")
                                dano_bru2 = (10 + 3)
                                hp_monstro -= dano_bru2
                                dados_jogador["vida"] -= dano_monstro
                            else:
                                print("a explosão arcana causou dano mas não deu queimadura")
                            valor_habilidade["mana"] -=20
                        else:
                            print("Você não tem mana suficiente")
                            
                    elif escolha_usar_habilidade == upgrades["habilidade_bruxo3"]:
                        if valor_habilidade["mana"] >=15:
                            print("você usou maldição sombria no inimigo")
                            reducao_ataque = int(dano_monstro * 0.3)
                            reducao_defesa = int(defesa_monstro * 0.3)
                            dano_monstro -= reducao_ataque
                            defesa_monstro -= reducao_defesa
                            valor_habilidade["mana"] -=15
                        else:
                            print("Você não tem mana suficiente")
                            
                    elif escolha_usar_habilidade == upgrades["habilidade_bruxo4"]:
                        if valor_habilidade["mana"] >= 25:
                            valor_drenagem = 15
                            hp_monstro -= valor_drenagem
                            print(f"você drenou a alma do inimigo causando {valor_drenagem}")
                            print(f"O Monstro te atacou causando {dano_monstro} de dano")
                            dados_jogador["vida"] -= dano_monstro
                            valor_habilidade["mana"] -=25
                        else:
                            print("Você não tem mana suficiente")
                elif dados_jogador["classe"] == "monstro":
                	if escolha_usar_habilidade == upgrades["habilidade_monstro"]:
                		if valor_habilidade["mana"] >=5:
                			valor_habilidade["mana"] -= 5
                			print("você dá um rugido aterrorizante")
                			chance_monstro_fugir = random.randint(0,100)
                			if chance_monstro_fugir <=25:
                				print("o rugido fez o monstro fugir")
                				hp_monstro = 0
                			else:
                				print("o rugido fez nada")
                				print("monstro te atacou com furia")
                				monstro_ataque_furia = int(dano_monstro * 2)
                				dados_jogador["vida"] -= monstro_ataque_furia
                			
                				print(f"monstro atacou tirando {monstro_ataque_furia} de hp")
                	if escolha_usar_habilidade == upgrades["habilidade_monstro2"]:
                		if valor_habilidade["mana"] >=15:
                			valor_habilidade["mana"] -= 15
                			print("com a mordida seu dano duplicou nesse ataque especial")
                			mordida = int(dados_jogador["dano"] * 2)
                	if escolha_usar_habilidade == upgrades["habilidade_monstro3"]:
                			if valor_habilidade["mana"] >= 20:
                				valor_habilidade["mana"] -= 20
                				print("com a raiva selvagem pode dar dois ataques de uma vez só")
                				
                				ataque_selvagem = 1
                	if escolha_usar_habilidade == upgrades["habilidade_monstro4"]:
                			if valor_habilidade["mana"] >=25:
                				regeneracao = 10
                				print("você esta se regenerando de forma sobrenatural")
                				dados_jogador["vida"] += regeneracao
                				valor_habilidade["mana"] -= 25
                elif dados_jogador["classe"]  == "mercador":
                	if escolha_usar_habilidade == upgrades["habilidade_mercador4"]:
                		if valor_habilidade["mana"] >= 25:
                			print("você usa a habilidade lucro maximo")
                			
                			lucro_maximo = 1
                	if escolha_usar_habilidade == upgrades["habilidade_mercador3"]:
                		if valor_habilidade["mana"] >= 15:
                			print("você usa o ataque de persuação")
                			print("monstro tenta te atacar")
                			ataque_raro_monstro = random.randint(0,1)
                			if ataque_raro_monstro == 0:
                				print("monstro errou o ataque")
                			if ataque_raro_monstro == 1:
                				print("monstro acertou o ataque")
                				dados_jogador["vida"] -= dano_monstro
                				
                		
                			
                	if escolha_usar_habilidade == upgrades["habilidade_mercador2"]:
                		if valor_habilidade["mana"] >= 40:
                			valor_habilidade["mana"] -= 40
                			print("cura 20 moedas")
                			print("defesa 15 moedas")
                			print("dano 10 moedas")
                			escolha_oferta = input("selecione um item para comprar")
                			if escolha_oferta == "cura":
                				if int(dados_jogador["moedas"]) >=20:
                					print("você foi curado")
                					dados_jogador["moedas"] = int(dados_jogador["moedas"])
                					dados_jogador["moedas"] -= 20
                					dados_jogador["vida"] = 20
                				else:
                					print("você não tem moedas o suficiente")
                			if escolha_oferta == "defesa":
                				if int(dados_jogador["moedas"]) >=15:
                					dados_jogador["moedas"] = int(dados_jogador["moedas"])
                					dados_jogador["moedas"] -= 15
                					dados_jogador["defesa"] += 5
                					print("sua defesa aumentou em 5")
                			else:
                				print("item não encontrado")
                				
                			if escolha_oferta == "dano":
                				if int(dados_jogador["moedas"]) >= 10:
                					
                					print("seu dano aumentou em 5")
                					dados_jogador["moedas"] = int(dados_jogador["moedas"])
                					dados_jogador["moedas"] -= 10
                					dados_jogador["dano"] +=5
                				else:
                					print("você não tem moedas o suficiente")
                				
                		
                	
                	if escolha_usar_habilidade == upgrades["habilidade_mercador"]:
                		valor_suborno = 75
                		if valor_habilidade["mana"] >=5 and dados_jogador["moedas"] >= valor_suborno:
                			print("você esta fazendo suborno com o monstro")
                			valor_habilidade["mana"]
                			dados_jogador["moedas"] -= valor_suborno
                			cair_suborno = random.randint(0,100)
                			if cair_suborno >=75:
                				print("o monstro aceitou a proposta")
                				print("o monstro foi embora")
                				hp_monstro = 0
                			else:
                				print("o monstro não aceitou a proposta")
                				chance_roubar_monstro = random.randint(1,3)
                				if chance_roubar_monstro <=2:
                					print("o monstro devolveu o dinheiro")
                					
                				dados_jogador["moedas"] += valor_suborno
                				if chance_roubar_monstro == 3:
                								
                								print("o monstro roubou o seu dinheiro")
                								

                elif dados_jogador["classe"] == "goblin":
                    if escolha_usar_habilidade == upgrades["habilidade_goblin4"]:
                    	if valor_habilidade["mana"] >= 20:
                    		print("você ARMOU UMA BOMBA")
                    		print("BOMBA EXPLODINDO EM")
                    		print("3")
                    		seg = 1
                    		seg = int(seg)
                    		time.sleep(seg)
                    		print("2")
                    		time.sleep(seg)
                    		print("1")
                    		time.sleep(seg)
                    		print("a bomba explodiu causando 10 de dano")
                    		hp_monstro -= 10
                    		dados_jogador["vida"] -= dano_monstro
                    		
                    if escolha_usar_habilidade == upgrades["habilidade_goblin3"]:
                    	if valor_habilidade["mana"] >=10:
                    		print("você usou o ataque zombaria")
                    		time = 3
                    		time2 = 0
                    	
                    if escolha_usar_habilidade == upgrades["habilidade_goblin2"]:
                    	if valor_habilidade["mana"] >= 5:
                    		escolha_goblin = input("essa habilidade faz fuga instantanea,deseja usar essa habilidade? [s] ou [n]")
                    		if escolha_goblin == "s":
                    			print("você escapou da batalha")
                    			valor_habilidade["mana"] -= 5
                    		if escolha_goblin == "n":
                    			print("sua mana não será gastada")
                    		else:
                    			print("resposta invalida")
                    if escolha_usar_habilidade == upgrades["habilidade_goblin"]:
                        if valor_habilidade["mana"] >= 10:
                            dano_adaga = 4
                            print(f"você lança uma adaga de longe e causa {dano_adaga} de dano")
                            print("o monstro não consegue te atingir porque esta longe demais")
                            hp_monstro -= dano_adaga
                            valor_habilidade["mana"] -=10
           

            elif escolha_arena == "6":
                chance_escapar = random.randint(0,100)
                if chance_escapar >= 50:
                	print("você conseguiu escapar da batalha")
                	break
                if chance_escapar <=50:
                	print("você não conseguiu escapar da batalha")
             
             
                
                
           
            
            
            
            if dados_jogador["vida"] <= 0:
            	morte() 
           
            if hp_monstro <= 0:
                ataque_selvagem = 0
                if lucro_maximo == 1:
                	print("o lucro maximo está ativado")
                	moeda_generatorMAX = random.randint(500,1000)
                	dados_jogador["moedas"] == int(dados_jogador["moedas"])
                	dados_jogador["moedas"] += moeda_generatorMAX
                
                moeda_generator = random.randint(1,500)
                print(f"parabens você ganhou {moeda_generator} de moedas!")
                dados_jogador["moedas"] = int(dados_jogador["moedas"]) + moeda_generator
                raridade_itens = random.randint(1,4)
                if raridade_itens == 1:
                	raridade1 = random.randint(1,2)
                	if raridade1 == 1:
                		print("você ganhou placa de madeira")
                		salvamento_dados2["placa_madeira"] += 1
                	if raridade1 == 2:
                		print("você ganhou placa de ferro")
                		salvamento_dados2["placa_ferro"] += 1
                if raridade_itens == 2:
                	raridade2 = random.randint(1,4)
                	if raridade2 == 1:
                		print("você ganhou espada de madeira")
                		salvamento_dados2["espada_madeira"] += 1
                	if raridade2 == 2:
                		print("você ganhou escudo de madeira")
                		salvamento_dados2["escudo_madeira"] += 1
                	if raridade2 == 3:
                		print("você ganhou capacete de madeira")
                		salvamento_dados2["capacete_madeira"] += 1
                	if raridade2 == 4:
                		print("você ganhou uma barra de cobre")
                		salvamento_dados["barra_cobre"] += 1
                if raridade_itens == 3:
                	raridade3 = random.randint(1,6)
                	if raridade3 == 1:
                		print("você ganhou espada de ferro")
                		salvamento_dados2["espada_ferro"] += 1
                	if raridade3 == 2:
                		print("você ganhou escudo de ferro")
                		salvamento_dados2["escudo_ferro"] += 1
                	if raridade3 == 3:
                		print("você ganhou capacete de ferro")
                		salvamento_dados2["capacete_ferro"] += 1
                	if raridade3 == 6:
                		qtd_pipeta_cobre = random.randint(1,9)
                		print(f"você ganhou {qtd_pipeta_cobre} pipetas de cobre!")
                		salvamento_dados["pipeta_cobre"] += qtd_pipeta_cobre
                		print("você ganhou")
                	if raridade3 == 4:
                		print("")
                		
                	if raridade3 == 5:
                		print("você ganhou pepita de ouro")
                		salvamento_dados2["pipeta_ouro"] += 1
                if raridade_itens == 4:
                	raridade4 = random.randint(1,3)
                	if raridade4 == 1:
                		print("você ganhou uma barra de ferro")
                		salvamento_dados2["barra_ferro"] += 1
                	if raridade4 == 2:
                		print("você ganhou uma barra de prata")
                		salvamento_dados2["barra_prata"] += 1
                	if raridade4 == 3:
                		print("você ganhou barra de ouro")
                		salvamento_dados2["barra_ouro"] += 1
                	
                
               
                nivel_arena += 1
                wave += 1
                print(f"Você derrotou o monstro! Wave {wave}")
                hp_monstro = vida_definida + (wave * taxa_de_evolucao)
                configuracao_dano_monstro = int(dano_monstro * taxa_de_evolucao)
                dano_monstro = configuracao_dano_monstro
                dados_jogador["exp"] += 10 * wave
                print(f"Ganhou {10 * wave} de exp!")
               
         
               
#UPGRADES
    elif escolha_centro == "11":
      registro_acoes.append("upgrades")
      while True:
      	print("======upgrades======")
      	print(f"seus pontos de upgrades:{upgrades['pontos_upgrades']}")
      	print(f"maximo de vida:\n{max_atributos['hp_max']}")
      	print(f"maximo de mana:\n{max_atributos['mana_max']}")
      	print(f"maximo de dano:\n {max_atributos['dano_max']}")
      	escolha_upgrade = input("escolha o upgrade ou\n[0]pra sair")
      	if escolha_upgrade == "0":
      		break
      
        
        
            
#GUILDAS
    elif escolha_centro == "12":
        registro_acoes.append("guilda")
        limpar_terminal()
        while True:
        	print("====guilda====")
        	for nomes_aliados in aliados_guilda:
        		if nomes_aliados == "":
        			print("VOCÊ NÃO TEM NENHUM ALIADO")
        		else:
        			print(f"{nomes_aliados}\n")
        			sair_menu_guilda = input("[0]sair")
        			if sair_menu_guilda == "0":
        				break
        

    

    

    elif escolha_centro == "2":
        registro_acoes.append("status")
        while True:
            print("\n==== SEUS STATUS ====")
            for chave, valor in dados_jogador.items():
                print(f"{chave.capitalize()}: {valor}")

            voltar = input("\nDigite (0) para voltar ao menu principal: ")
            if voltar == "0":
                break

    elif escolha_centro == "7":
        print("Você abriu sua enciclopédia")
        print(inimigos)
        enciclopedia = input("Aperte 0 para sair")
        if enciclopedia == "0":
            print('Você saiu da enciclopédia')

    elif escolha_centro == "8":
        print('Suas conquistas')
        if conquista_espada >= 1:
            print("Conquista da espada: Obtenha a espada")
        if conquista_pao >= 1:
            print('Conquista do pão: Você comprou um pão')
        if conquista_bebado >= 1:
            print("Conquista do bêbado: Fale com o bêbado")
        conquista_menu = input("aperte 0 para sair")
#taverna
    elif escolha_centro == "1":
        registro_acoes.append("taverna")
        print("Barman: Bem-vindo à taverna! Aqui você pode conversar, beber e lutar por dinheiro.")
        print("[1] Conversar com um bêbado")
        print("[2] Conversar com o barman")
        print("[3] ir para o canto da taverna")
        escolha_taverna = input("O que deseja fazer? ")

        if escolha_taverna == "1":
            print("Você vai conversar com o bêbado.")
            print("Bêbado: O que tu quer?")
            print("[1]conversar")
            print("[2]sair")
            escolha_conversa_bebado = input("escolha uma das opçoes")
            if escolha_conversa_bebado == "1":
                print("você escolheu conversar com o bebado,o que queres falar?")
                print("[1].porque você sempre esta aqui?")
                print("[2].você não se cansa de sempre ficar aqui.porque não visitar a sua familia.")
                print("[3]porque você tem sempre uma cara de depressivo?")
                escolha_conversa_bebado2 = input("")
                if escolha_conversa_bebado2 == "1":
                    print("bebado:porque não tenho mais lugares para esconder minha depressão")
                    print("depois de ouvir isso vc fica comovido e vai embora")
                    conquista_bebado += 1
                elif escolha_conversa_bebado2 == "2":
                    print("depois dos eventos que destruiram o reino,perdi a minha razão de viver e agora estou aqui bebe do para esquecer do meu passado")
                    digitar(VERMELHO +"você reflete com a fala dele e vai embora questionando a sua propia vida" + RESET)  
                elif escolha_conversa_bebado2 == "3":
                    digitar(VERMELHO +"por que nesse mundo não adianta o que você faça  sempre tentarão te desanimar e desistir de seus sonhos,isso que a inveja faz com as pessoas,se elas ve que você tem uma vida bem prospera vão tentar tirar de ti em vez de correr atras." + RESET)
                    time.sleep(2)
                    digitar("você reflete com a fala dele e vai embora questionando a sua propria vida")
                    conquista_bebado += 1

        elif escolha_taverna == "3":
            print("você foi para o canto da taverna e vê um baú, uma mesa e um antigo cavaleiro")
            print("o que fazer?")
            print('[1]conversar com um antigo heroi')
            print("[2]ir para uma mesa")
            print("[3]checar o baú")
            canto_taverna = input("")
            if canto_taverna == "3":
                menu_bau()
            if canto_taverna == "2":
                print("você vai e senta numa mesa")
                print("você percebe que alguem esta no seu lado")
                print(f"cidadão sombrio:você quer se tornar {dados_jogador['classe']} de respeito,não é?" )
                print("você responde que sim")
                print("eu tenho uns itens para te vender")
                print("eu vendo itens sombrios e proibidos")
                print("você quer ver as mercadorias?")
                escolha_cidadao = input("(s) ou (n)")
                if escolha_cidadao == "s":
                    print("lembrando que meus itens são vendidos por diamantes")
                    print("seus diamantes:",dados_jogador["diamantes"])
                    print(f"moeda do submundo:  -   {moeda_do_submundo} diamantes")
                    print(f"amuleto da necromancia:    -   {amuleto_da_necromancia} diamantes")
                    print(f"contrato das almas:-   {contrato_das_almas} diamantes")
                    print(f"armadura sombria:    -  {armadura_sombria} diamantes")
                    print(f"adaga envenenada:  -  {adaga_envenenada} diamantes")
                    compra_sombria = input("escreva o nome do item ou 0 para sair")
                    if compra_sombria == "moeda do submundo":
                        dados_jogador["diamantes"] -=2
                        salvamento_dados["moeda_do_submundo2"] +=1
            elif canto_taverna == "1":
                print("voce chega no heroi e comprimenta ele")
                print("ele te comprimenta devolta e pergunta em que ele poderia ajudar")
                print("[1]o que aconteceu com esse reino?")
                print("[2]quem governava eldora antes?")
                print("[3]o que tem naquela masmorra")
                print("[4]quer se juntar ao meu bando?")
                pergunta_heroi = input("o que quer perguntar?")
                if pergunta_heroi == "1":
                    print("a 5 anos atrás,monstros,bestas e maldiçoes começaram a atacar o reino e ai só sobriviveu os cavaleiros,herois e destemidos")
                    print("(1)porque o bebado sobreviveu?")
                    print("(2)sabe se o porque todo mundo morreu?")
                    print("(3)sair")
                    pergunta2_heroi = input("")
                    if pergunta2_heroi == "1":
                        print("então né,nem sei como esse pinguço foi parar aqui")
                    elif pergunta2_heroi =="2":
                        print("sei sim depois de tudo que aconteceu os monstros pegaram os 10 artefatos,eles sustentavam tudo que existia em eldora")
                    elif pergunta2_heroi == "3":
                        print("muito obrigado por informar meu caro heroi")
                elif pergunta_heroi == "2":
                    print("era o rei Dargan,ele causao a queda do reino pois na ligava para a segurança do povo e fez um pacto com o diabo")
                elif pergunta_heroi == "3":
                    print("niguem se sabe pois o que entraram nunca mais voltaram")
                elif pergunta_heroi == "4":
                    print("eu aceitaria essa proposta mas com um porem,de todos os ganhas que tiver na batalha, 20% sera meu.")
                    proposta_heroi = input("voce aceita essa proposta?(s) ou (n)")
                    if proposta_heroi == "s":
                        aliados["antigo_guerreiro"] += 1
                        print("então esta bom")
                        print("no menu tera a opção de guilda,la voce pode gerenciar seus aliados")

        elif escolha_taverna == "2":
            print("Barman: O que deseja fazer?")
            print("(1) Conversar")
            print("(2) Pedir para entrar na luta")
            print("(3)upgrades da taverna")
            print("(4)comprar bebidas")
            escolha_barman = input("O que você quer fazer? ")
#bebidas taverna            
            if escolha_barman == "4":
            	limpar_terminal
            	digitar("então vejo que está\ninteressado na minha mercadoria,vejamos que só tenho um estoque\nhumilde e pequeno")
            	alguma_coisa_comprada = False
            	while True:
            		
            		
      
        
        
            		
   
    


    




            		limpar_terminal()
            		
            		salvar_progresso()
            		print("BARMAN:")
            		
            		print(f"dinheiro do barman:{dados_taverna['dinheiro_barman']}")
            		print("======BEBIDAS=======")
            		mostrar_bebidas()
            		print("[0]sair")
            		comprar_bebida = input(f"qual bebida deseja comprar meu caro {dados_jogador['classe']}\ndigite [0] para sair")
            		if comprar_bebida == "0":
            			limpar_terminal()
            			if alguma_coisa_comprada:
            				digitar("ao sair o barman fica contente que você comprou algo")
            				limpar_terminal()
            				alguma_coisa_comprada = False
            				break
            			if not alguma_coisa_comprada:
            				limpar_terminal()
            				digitar("-barman:eu entendo sei que meu estoque ainda não está atraente")
            				digitar("-barman:volte sempre")
            				limpar_terminal()
            				alguma_coisa_comprada = False
            				break
            		
            		if comprar_bebida == "velho barreiro":
            			
            			bebida_selecionada = "velho barreiro"
            			bebida_selecionada_plural = "velhos barreiros"
            			bebida_selecionada_unificacao = ""
            			
            			numero_bebidas = input("quantas velhos barreiros o senhor queiras comprar?")
            			numero_bebidas = int(numero_bebidas)
            			if numero_bebidas == 1:
            				bebida_selecionada_unificacao = bebida_selecionada
            			if numero_bebidas >= 2:
            				bebida_selecionada_unificacao = bebida_selecionada_plural
            			bebidas_taverna["velho barreiro"] = int(bebidas_taverna["velho barreiro"])
            			preco_bebida = int(numero_bebidas * bebidas_taverna["velho barreiro"])
            			preco_bebida = int(preco_bebida)
            			dados_jogador["moedas"] = int(dados_jogador["moedas"])
            			if numero_bebidas <= dados_taverna["estoque_velho_barreiro"]:
            				if dados_jogador["moedas"] >= preco_bebida:
            					print(f"BARMAN:deu {preco_bebida} moedas,deseja comprar?")
            					confirmacao_bebida = input("[S/N]")
            					if confirmacao_bebida.lower() in ["s", "sim"]:
            						digitar(f"você comprou {numero_bebidas} {bebida_selecionada_unificacao}")
            						salvamento_dados["velho_barreiro"] += numero_bebidas
            						dados_jogador["moedas"] -= preco_bebida
            						dados_taverna["dinheiro_barman"] += preco_bebida
            						dados_taverna["estoque_velho_barreiro"] -= numero_bebidas
            						alguma_coisa_comprada = True
            					else:
            						print("")
            					
            			else:
            				digitar(f"não temos estoque de {numero_bebidas} velho barreiro somente de {dados_taverna['estoque_velho_barreiro']}...")
            			
            		if comprar_bebida == "vodka":
            			bebida_selecionada = "vodka"
            			bebida_selecionada_plural = "vodkas"
            			bebida_selecionada_unificacao = ""
            			
            			numero_bebidas = input("quantas vodkas o senhor queiras comprar?")
            			numero_bebidas = int(numero_bebidas)
            			if numero_bebidas == 1:
            				bebida_selecionada_unificacao = bebida_selecionada
            			if numero_bebidas >= 2:
            				bebida_selecionada_unificacao = bebida_selecionada_plural
            			bebidas_taverna["vodka"] = int(bebidas_taverna["vodka"])
            			preco_bebida = int(numero_bebidas * bebidas_taverna["vodka"])
            			preco_bebida = int(preco_bebida)
            			dados_jogador["moedas"] = int(dados_jogador["moedas"])
            			if numero_bebidas <= dados_taverna["estoque_vodka"]:
            				if dados_jogador["moedas"] >= preco_bebida:
            					print(f"BARMAN:deu {preco_bebida} moedas,deseja comprar?")
            					confirmacao_bebida = input("[S/N]")
            					if confirmacao_bebida.lower() in ["s", "sim"]:
            						digitar(f"você comprou {numero_bebidas} {bebida_selecionada_unificacao}")
            						salvamento_dados["vodka"] += numero_bebidas
            						dados_jogador["moedas"] -= preco_bebida
            						dados_taverna["dinheiro_barman"] += preco_bebida
            						dados_taverna["estoque_vodka"] -= numero_bebidas
            						alguma_coisa_comprada = True
            					else:
            						print("")
            					
            			else:
            				digitar(f"não temos estoque de {numero_bebidas} {bebida_selecionada_unificacao} somente de {dados_taverna['estoque_vodka']}...")
            		if comprar_bebida == "cerveja":
            			bebida_selecionada = "cerveja"
            			bebida_selecionada_plural = "cervejas"
            			bebida_selecionada_unificacao = ""
            			
            			numero_bebidas = input("quantas cervejas o senhor queiras comprar?")
            			numero_bebidas = int(numero_bebidas)
            			if numero_bebidas == 1:
            				bebida_selecionada_unificacao = bebida_selecionada
            			if numero_bebidas >= 2:
            				bebida_selecionada_unificacao = bebida_selecionada_plural
            			bebidas_taverna["cerveja"] = int(bebidas_taverna["cerveja"])
            			preco_bebida = int(numero_bebidas * bebidas_taverna["cerveja"])
            			preco_bebida = int(preco_bebida)
            			dados_jogador["moedas"] = int(dados_jogador["moedas"])
            			if numero_bebidas <= dados_taverna["estoque_cerveja"]:
            				if dados_jogador["moedas"] >= preco_bebida:
            					print(f"BARMAN:deu {preco_bebida} moedas,deseja comprar?")
            					confirmacao_bebida = input("[S/N]")
            					if confirmacao_bebida.lower() in ["s", "sim"]:
            						digitar(f"você comprou {numero_bebidas} {bebida_selecionada_unificacao}")
            						salvamento_dados["cerveja"] += numero_bebidas
            						dados_jogador["moedas"] -= preco_bebida
            						dados_taverna["dinheiro_barman"] += preco_bebida
            						dados_taverna["estoque_cerveja"] -= numero_bebidas
            						alguma_coisa_comprada = True
            					else:
            						print("")
            					
            			else:
            				digitar(f"não temos estoque de {numero_bebidas} cerveja somente de {dados_taverna['estoque_cerveja']}...")
            		if comprar_bebida == "cachaça mineira":
            			bebida_selecionada = "cachaça mineira"
            			bebida_selecionada_plural = "cachaças mineiras"
            			bebida_selecionada_unificacao = ""
            			
            			numero_bebidas = input("quantas cachaças mineiras o senhor queiras comprar?")
            			numero_bebidas = int(numero_bebidas)
            			if numero_bebidas == 1:
            				bebida_selecionada_unificacao = bebida_selecionada
            			if numero_bebidas >= 2:
            				bebida_selecionada_unificacao = bebida_selecionada_plural
            			bebidas_taverna["cachaça mineira"] = int(bebidas_taverna["cachaça mineira"])
            			preco_bebida = int(numero_bebidas * bebidas_taverna["cachaça mineira"])
            			preco_bebida = int(preco_bebida)
            			dados_jogador["moedas"] = int(dados_jogador["moedas"])
            			if numero_bebidas <= dados_taverna["estoque_cachaça_mineira"]:
            				if dados_jogador["moedas"] >= preco_bebida:
            					print(f"BARMAN:deu {preco_bebida} moedas,deseja comprar?")
            					confirmacao_bebida = input("[S/N]")
            					if confirmacao_bebida.lower() in ["s", "sim"]:
            						digitar(f"você comprou {numero_bebidas} {bebida_selecionada_unificacao}")
            						salvamento_dados["cachaça_mineira"] += numero_bebidas
            						dados_jogador["moedas"] -= preco_bebida
            						dados_taverna["dinheiro_barman"] += preco_bebida
            						dados_taverna["estoque_cachaça_mineira"] -= numero_bebidas
            						alguma_coisa_comprada = True
            					else:
            						print("")
            					
            			else:
            				digitar(f"não temos estoque de {numero_bebidas} velho barreiro somente de {dados_taverna['estoque_cachaça_mineira']}...")
            		if comprar_bebida == "pinga de mel":
            			bebida_selecionada = "pinga de mel"
            			bebida_selecionada_plural = "pingas de mel"
            			bebida_selecionada_unificacao = ""
            			
            			numero_bebidas = input("quantas pingas de mel o senhor queiras comprar?")
            			numero_bebidas = int(numero_bebidas)
            			if numero_bebidas == 1:
            				bebida_selecionada_unificacao = bebida_selecionada
            			if numero_bebidas >= 2:
            				bebida_selecionada_unificacao = bebida_selecionada_plural
            			bebidas_taverna["pinga de mel"] = int(bebidas_taverna["pinga de mel"])
            			preco_bebida = int(numero_bebidas * bebidas_taverna["pinga de mel"])
            			preco_bebida = int(preco_bebida)
            			dados_jogador["moedas"] = int(dados_jogador["moedas"])
            			if numero_bebidas <= dados_taverna["estoque_pinga_de_mel"]:
            				if dados_jogador["moedas"] >= preco_bebida:
            					print(f"BARMAN:deu {preco_bebida} moedas,deseja comprar?")
            					confirmacao_bebida = input("[S/N]")
            					if confirmacao_bebida.lower() in ["s", "sim"]:
            						digitar(f"você comprou {numero_bebidas} {bebida_selecionada_unificacao}")
            						salvamento_dados["pinga_de_mel"] += numero_bebidas
            						dados_jogador["moedas"] -= preco_bebida
            						dados_taverna["dinheiro_barman"] += preco_bebida
            						dados_taverna["estoque_pinga_de_mel"] -= numero_bebidas
            						alguma_coisa_comprada = True
            					else:
            						print("")
            					
            			else:
            				digitar(f"não temos estoque de {numero_bebidas} somente de {dados_taverna['estoque_cachaça_mineira']}...")
            		
           
            	
            		
            		
            			
            		
            			
            			
            		

            if escolha_barman == "1":
                digitar("Barman: Desculpa, não estou afim de conversar. Depois a gente conversa.")

            elif escolha_barman == "3":
                print("barman:aqui nos upgrades da taverna voce pode investir na taverna e ganhar uma quantia por hora")
                escolha_taverna_upgrade = input("[s] ou [n]")
                
            elif escolha_barman == "2":
                print("Barman: Que bom que quer entrar na luta!")
                
                digitar("Bêbado: Quanto quer apostar?")
                digitar(f"Suas moedas: {dados_jogador['moedas']}")
                aposta = int(input("Digite a quantia: "))

                if aposta > dados_jogador["moedas"]:
                    print("Você não tem moedas suficientes para essa aposta!")
                else:
                    print("Aposta aceita! Vamos lutar!")
                    while hp_bebado > 0 and dados_jogador["vida"] > 0:
                        print(f"Bêbado HP: {hp_bebado} | Seu HP: {dados_jogador['vida']}")
                        print("(1) Atacar")
                        print("(2) Fugir")
                        escolha_batalha = input("O que vai fazer? ")

                        if escolha_batalha == "1":
                            hp_bebado -= 5
                            print("Você atacou! O bêbado perdeu 5 HP.")
                            if hp_bebado <= 0:
                                print(f"Você venceu e ganhou {aposta} {moedas_word}!")
                                hp_bebado = 10
                                conquista_bebado += 1
                                dados_jogador["moedas"] += aposta
                                break
                            dados_jogador["vida"] -= 2
                            print("O bêbado contra-atacou! Você perdeu 2 HP.")
                            if dados_jogador["vida"] <= 0:
                                print("Você perdeu a luta!")
                                dados_jogador["moedas"] -= aposta
                        elif escolha_batalha == "2":
                            print("Você fugiu da luta!")
                            break
#casa
    elif escolha_centro == "3":
        registro_acoes.append("casa")
        digitar("você entrou na sua casa")
        print("[1]descansar(recuperar hp)")
        print("[2]conversar com Dorian")
        print("[3]sair de casa")
        escolha_casa = input('o que queres fazer')
        if escolha_casa == "2":
        	npc_dorian()
        if escolha_casa == "1":
            descansar = random.randint(1,5)
            print(f"você recuperou {descansar} de hp")
            dados_jogador["vida"] += descansar
        
        if escolha_casa == "2":
            print("você saiu de casa")
        else:
        	print("escolha invalida")

    elif escolha_centro == "4":
        print("Obrigado por jogar! Até a próxima.")
        salvar_progresso()
        break  

    elif escolha_centro == "5":
        registro_acoes.append("loja")
        print("\nMercador: Você entra na loja e o vendedor te apresenta a mercadoria:")
        voltar_menu_categoria = 0
        while voltar_menu_categoria == 0:
            print(f"\nVocê tem {dados_jogador['moedas']} moedas.")
            print("selecione a categoria do item")
            print("[1]itens de ataque")
            print("[2]itens de defesa")
            print("[3]itens consumíveis")
            print("[4]outros itens...")
            print("[5]sair da loja")
            escolha_categoria = input("")
            if escolha_categoria == "4":
                voltar_menu_categoria = 1
                for item, preco in itens_outros.items():
                    print(f"{item.capitalize()} - {preco} moedas")
                print("[0] Retornar")
                escolha_itens_outros = input("Qual item deseja comprar? ")    
                if escolha_itens_outros == "0":
                    
                    voltar_menu_categoria = 0
                if escolha_itens_outros == "diamantes":
                    print("o item diamante foi adicionado")
                    dados_jogador["diamantes"] += 1
    
        
    
    
        
    
    
            elif escolha_categoria == "2":
                voltar_menu_categoria = 1
                for item, preco in itens_defesa.items():
                    print(f"{item.capitalize()} - {preco} moedas")
                print("[0] Retornar")
                escolha_itens_defesa = input("Qual item deseja comprar? ")
                if escolha_itens_defesa == "0":
                    
                    voltar_menu_categoria = 0
                if escolha_itens_defesa == "capacete":
                    
                    print("o item capacete de ferro foi adicionado ao inventário ")
                    inventario_equipamentos["capacete"] += 1
                if escolha_itens_defesa == "peitoral":
                    
                    print("o item peitoral de ferro foi adicionado ao inventário ")
                    inventario_equipamentos["peitoral"] += 1
                if escolha_itens_defesa == "calças":
                    
                    
                    print("o item calças de ferro foi adicionado ao inventário ")
                    inventario_equipamentos["calcas"] += 1   
                if escolha_itens_defesa == "botas":
                    
                    print("o item botas de ferro foi adicionado ao inventário ")
                    inventario_equipamentos["botas"] += 1     
                       
                    

                    
                        

                        
                    
    
    


    
        
    
            elif escolha_categoria == "5":
                break
            elif escolha_categoria == "1":
                voltar_menu_categoria = 1
                
                for item, preco in itens_ataque.items():
                
                
                    print(f"{item.capitalize()} - {preco} moedas")
                print("[0]retornar")    
                escolha_itens_ataque = input("escolha um item para comprar")    
                if escolha_itens_ataque == "0":
                        voltar_menu_categoria = 0
                if escolha_itens_ataque == "espada de pedra":
                      
                      inventario_equipamentos["espada"] +=1
                if escolha_itens_ataque == "adaga":
                      
                      inventario_equipamentos["adaga"] +=1
                 
                      
                       
                if escolha_itens_ataque in itens_ataque:
                    
                    
                    if dados_jogador["moedas"] >= itens_ataque[escolha_itens_ataque]:
                        
                        dados_jogador["moedas"] -= itens_ataque[escolha_itens_ataque]
            elif escolha_categoria == "3":
                
                voltar_menu_categoria = 1
                
                for item, preco in itens_consumiveis.items():
                    print(f"{item.capitalize()} - {preco} moedas")
                
                
                        
                print("[0]retornar")    
                escolha_itens_consumiveis = input("escolha um item para comprar")    
                if escolha_itens_consumiveis == "0":
                    voltar_menu_categoria = 0
                        
                if escolha_itens_consumiveis == "carne":
                    
                    print("o item carne foi adicionado ao inventário ")
                    salvamento_dados["carne2"] += 1
                if escolha_itens_consumiveis == "pão":
                    
                    print("o item pão foi adicionado ao inventário ")
                    salvamento_dados["pao2"] += 1
                if escolha_itens_consumiveis == "batata":
                    
                    print("o item carne foi adicionado ao inventário ")
                    salvamento_dados["carne2"] += 1
                if escolha_itens_consumiveis == "poção exp":
                    print("o item poção exp foi adicionado ao inventário ")
                    salvamento_dados["pocao_exp2"] += 1
                if escolha_itens_consumiveis in itens_consumiveis:
                    
                    
                        
                    
                    dados_jogador["moedas"] = int(dados_jogador["moedas"])
                    if dados_jogador["moedas"] >= itens_consumiveis[escolha_itens_consumiveis]:
                        dados_jogador["moedas"] -= itens_consumiveis[escolha_itens_consumiveis]
                            
                            
                        
                    
                    
                                    
                    
            
                    
                    
                    
                
            
                     
                        
                   

    elif escolha_centro == "9":
        salvar_progresso()

    elif escolha_centro == "10":
        carregar_progresso()

    