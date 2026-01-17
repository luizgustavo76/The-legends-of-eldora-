def main():
	from win10toast import ToastNotifier
	import asyncio
	import sys
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
	from datetime import datetime
	import requests
	import DreamCore
	import ActionsMoves
	import ProceduralValley
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
	#o tloe utiliza o motor de IA Dreamcore desenvolvido por luiz gustavo para auxiliar nas conversas com npc
	dados_monstro = {
		"hp":0,
		"resistencia":0,
		"dano":0,
	}  
	saida_chat = 1  
	horario = {
	"ano":1023,
	"dia":0,
	"mes":0,
	"horas":"0",
	"minutos":"00",
	}
	
			
	def definir_horario():
		agora = datetime.now()
		horario["dia"] = random.randint(1,30)
		horario["mes"] = random.randint(1,12)
		horario["horas"] = int(agora.hour // 2)
		horario["minutos"] = int(agora.minute // 2)
	def selecao_dificuldade():
		
		if diculdade_selecionada == "facil":
			taxa_evolucao = 0.5
		if dificuldade_selecionada == "medio":
			taxa_evolucao = 0.75
		if dificuldade_selecionada == "dificil":
			taxa_evolucao = 1
		if dificuldade_selecionada == "inferno":
			taxa_evolucao = 1.75
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
					
					digitar(f"que deus guie sua mão meu {dados_jogador['classe']}")
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
	#classes,sub-classes e habilidades
	def escolher_subclasse():
		if dados_jogador["classe"] == "bruxo":
			while True:
				limpar_terminal()
				digitar("chegar ao nivel 50 não é so uma conquista...é uma prova que tu sobreviveu mesmo no caos...")
				digitar("agora você pode escolher um caminho para seguir")
				print("você deseja se tornar um:")
				print("[1]bruxo das águas")
				print("[2]bruxo do fogo")
				print("[3]bruxo do vento")
				print("[4]bruxo da folha")
				escolha_subclasse_bruxo = input("qual sub-classe você escolhará?escolha sabiamente,para ter informação\ndecada sub-classe escreva [i]")
				if escolha_subclasse_bruxo == "i":
					print("qual sub-classe deseja se informar?")
					print("[1]bruxo das águas")
					print("[2]bruxo do fogo")
					print("[3]bruxo do vento")
					print("[4]bruxo da folha")
					escolha_informacao_bruxo = input("")
					if escolha_informacao_bruxo == "1":
						while True:
							digitar("bruxo das agua:tem poders áquaticos para seu bem...tem ataques como mandar uma onda para o inimigo,essa sub-classe é bastante\npoderosa contra inimigos do tipo fogo")
							continuar = input("pressione Enter para continuar")
							if continuar == "":
								break
					if escolha_subclasse_bruxo == "2":
						while True:
							digitar("bruxo do fogo,tem ataques de fogo como queimadura e tem mais vantagens contra inimigos do tipo folha")
							continuar = input("pressione Enter para continuar")
							if continuar == "":
								break
							
				
	def habilidades_especiais():
		
		print("=====suas habilidades=====")
		print("sua classe:",dados_jogador["classe"])
		print(f"sua mana {valor_habilidade['mana']}")
		if dados_jogador["subclasse"] == "bruxo da agua":
			if int(dados_jogador["nivel"]) >=50:
				print("corte de água")
			if int(dados_jogador["nivel"]) >=65:
				pass
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
		escolha_usar_habilidade = input("qual habilidade deseja usar?")
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
							digitar("você não tem moedas o suficiente")
					if escolha_oferta == "defesa":
						if int(dados_jogador["moedas"]) >=15:
							dados_jogador["moedas"] = int(dados_jogador["moedas"])
							dados_jogador["moedas"] -= 15
							dados_jogador["defesa"] += 5
							print("sua defesa aumentou em 5")
						else:
							digitar("voc~e não tem dinheiro suficiente...")
					
									
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
			
					
	#valores para forjar
	valores_forja = {
		"golem de cobre":{
			"moedas":300,
			"itens":{
				"barra de cobre":30,
				"amuleto das almas":1,
			},
		},
		"golem de madeira":{
			"moedas":50,
			"itens":{
				"madeira":30,
				"amuleto das almas":1,
			},
		},
		"golem de ferro":{
			"moedas":450,
			"itens":{
				"barra de ferro":30,
				"amuleto das almas":1,
			},
		},
		"golem de pedra":{
			"moedas":150,
			"itens":{
				"pedra":30,
				"amuleto das almas":1,
			},
		},
		"golem de obsidiana":{
			"moedas":515,
			"itens":{
				"obsidiana":30,
				"amuleto das almas":1,
			},
		},
		"golem de rubi":{
			"moedas":700,
			"itens":{
				"rubi":30,
				"amuleto das almas":1,
			},
		},
		"golem de esmeralda":{
			"moedas":600,
			"itens":{
				"esmeralda":30,
				"amuleto das almas":1,
			},
		},
		"golem de ouro":{
			"moedas":650,
			"itens":{
				"barra de ouro":30,
				"amuleto das almas":1,
			},
		},
		"golem de diamante":{
			"moedas":900,
			"itens":{
				"diamante":30,
				"amuleto das almas":1,
			},
		},
	}
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
			barra = "ˆ" * int((vida / vida_max) * 10)
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

		salvar_arquivo("tloe_save.json", dados_jogador)
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
					salvar_arquivo("tloe_save.json", dados_jogador)
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
			salvar_arquivo("tloe_save.json", dados_jogador)
	def limpar_terminal():
		# Verifica se o sistema é Windows ('nt') ou outro (Linux, Android, etc.)
		os.system('cls' if os.name == 'nt' else 'clear')
	#cabana da resistencia
	dados_resistencia = {
		"primeira_vez_resistencia":True,
		"primeira_vez_bau_cabana":True,
		"bau_cabana":[],
	}
	def bau_cabana():
		while True:
			
			print("limite itens báu é 30 itens")
			print("[1] deposistar itens")
			print("[2] retirar itens")
			print("[0] sair")
			escolha_bau_cabana = input("o que deseja fazer?")
			if escolha_bau_cabana == "1":
				if len(dados_resistencia["bau_cabana"]) >=29:
					print("o báu está cheio!")
				while True:
					print("escolha os itens que deseja depositar")
					mostrar_inventario()
					escolha_deposistar_item_bau_cabana = input("item:")
					for chave, valor in [salvamento_dados, salvamento_dados2]:
						if escolha_deposistar_item_bau_cabana in chave:
							if salvamento_dados[escolha_deposistar_item_bau_cabana] >=1:
								if salvamento_dados[escolha_deposistar_item_bau_cabana] == 1:
									dados_resistencia["bau_cabana"].append(escolha_deposistar_item_bau_cabana)
								else:
									escolha_qtd_item = input(f"quantas unidades do item {escolha_deposistar_item_bau_cabana} deseja adicionar?")
									if escolha_qtd_item <=0:
										print("não é possivel depoistar itens com valor de 0 ou menos")
									else:
										print("item depositado com sucesso!")
											
	def menu_cabana():
		while True:
			print("[1] fazer missões")
			print("[2] conversar com algum integrante")
			print("[3] checar báu")
			print("[4] abrir inventário")
			escolha_cabana = input("o que deseja fazer?")
			if escolha_cabana == "3":
				if dados_resistencia["primeira_vez_bau_cabana"]:
					digitar("[Maria] a...esse é o bau daqui, pode guardas seus itens aí a vontade")
					bau_cabana()
				else:
					bau_cabana()
	def cabana_resistencia():
		while True:
			if dados_resistencia["primeira_vez_resistencia"]:
				digitar("você aproxima-se daquela cabana, ela ainda parece ser habitada")
				limpar_terminal()
				digitarlento("...")
				time.sleep(0.5)
				digitar("[pessoa desconhecida 1] quem...quem é você???")
				time.sleep(0.25)
				digitar("vocÊ varias pessoas dentro dessa cabana, elas parecem inseguras após a sua chegada")
				time.sleep(0.25)
				digite("[pessoa desconhecida 2] o garoto, vai se apresentar não???")
				time.sleep(0.25)
				digitar(f"cla..claro meu nome é {dados_jogador['nome']}")
				time.sleep(0.25)
				digitar("[pessoa desconhecida 2] pelo visto você não é uma ameaça...meu nome é Josué")
				digitar("[pessoa desconhecida 1] a... meu nome é maria")
				dados_resistencia["primeira_vez_resistencia"] = False
				menu_cabana()
			else:
				menu_cabana()
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
	mapa_ruinas = [
	"1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",
	]
	primeira_vez_ruina = False
	#ruinas de eldora
	def ruinas_eldora():
		if primeira_vez_ruina:
			digitar("[Dorian]então era aqui que você queria me levar?")
			digitar(f"[{dados_jogador['nome']}]Meu Deus!.... o que aconteceu aqui???????????")
			digitar("por que tá tudo destruido?")
			digitar("[Dorian]eu estava conversando com uns habitantes locais daqui e eles disseram que era sobreviventes de algum incidente desse reino...mas qual seria esse incidente..")
			digitar(f"[{dados_jogador['nome']}]entendi...")
			digitar("[Dorian]eu estou voltando para meu aposento então..")
		else:
			digitar("você chegou as ruinas")
			while True:
				limpar_terminal()
				print("[1]andar para frente")
				print("[2]virar para direita")
				print("[3]virar para esquerda")
				print("[4]andar para trás")
				print("[5]limpar destroço")
				print("[6]abrir inventário")
				print("[7]ver mapa")
				print("[0]voltar para o centro de eldora")
				escolha_ruinas = input("o que irá fazer")
				if escolha_ruinas == "0":
					break
				if escolha_ruinas == "7":
					while True:
						print(mapa_ruinas)
						escolha_sair_mapa_ruina = input("aperte [0~] para voltar para o menu")
						if escolha_sair_mapa_ruina == "0":
							break
						
				

	def mercado():
		digitar(f"você entra no mercado local de {dados_vila['vila atual']} ")
	def vila_rimvark():
		
		while True:
			
			limpar_terminal()
			print("Vila de Rimvark:")
			print("[1]loja")
			print("[2]igreja")
			print("[3]mercado")
			print("[4]casa")
			print("[5]ver mapa")
			print("[6]menu jogador")
			escolha_rimvark = input("o queres fazer?")
			if escolha_rimvark == "1":
				item_comprado = False
				while True:
					digitar("bem vindo á minha loja de armamentos...")
					print("[1]ver estoque")
					print("[2]vender itens")
					print("[3]conversar")
					print("[0]sair")
					escolha_loja_rimvark = input("o que deseja fazer?")
					if escolha_loja_rimvark == "0":
						if item_comprado:
							digitar("ao sair você percebe que o comerciante ficou feliz pois você comprou algo...")
						else:
							
							digitar("ok....volte sempre!")
					if escolha_loja_rimvark == "3":
						digitar("modo livre...escreva qualquer coisa que ele te responderá...tecnologia DreamCore,fale palavras como tchau,adeus para sair do chat")
						DreamCore.npc_selecionado = "comerciante de rimvark"
						DreamCore.iniciar_conversa()
			if escolha_rimvark == "2":
				digitar("você entra na igreja mas percebe que ainda está em construção depois das destruições que ocorreram em Rimvark")
				while True:
					print("Igreja católica de Rimvark")
					print("[1]se sentar nos bancos")
					print("[2]ir para o altar")
					print("[3]ir conversar com o Padre")
					print("[0]sair")
					escolha_igreja_rimvark = inpunt("o que deseja fazer?")
					if escolha_igreja_rimvark == "0":
						digitar("você sai da igreja...")
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
			if escolha_vangurd == "1":
				
				
				item_comprado = False
				while True:
					digitar("[comerciante de Vangurd]:seja bem vindo a minha humilde loja")
					print("[1]ver estoque")
					print("[2]vender itens")
					print("[3]conversar")
					print("[0]sair")
					escolha_loja_vangurd = input("o que deseja fazer?")
					if escolha_loja_vangurd == "0":
						if item_comprado:
							digitar("ao sair você percebe que o comerciante ficou feliz pois você comprou algo...")
						else:
							digitar("ok....volte sempre!")
						break
					if escolha_loja_vangurd == "3":
						digitar("modo livre...escreva qualquer coisa que ele te responderá...tecnologia DreamCore,fale palavras como tchau,adeus para sair do chat")
						DreamCore.npc_selecionado = "comerciante de vangurd"
						DreamCore.iniciar_conversa()
					
						
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
			if escolha_nocten == "1":
				item_comprado = False
				while True:
					digitar("[comerciante de nocten]:bem vindo a minha loja de poções e itens almadiçoados")
					print("[1]ver estoque")
					print("[2]vender itens")
					print("[3]conversar")
					print("[0]sair")
					escolha_loja_nocten = input("o que deseja fazer?")
					if escolha_loja_nocten == "0":
						if item_comprado:
							digitar("ao sair você percebe que o comerciante ficou feliz pois você comprou algo...")
						else:
							digitar("ok....volte sempre!")
						break
					if escolha_loja_nocten == "3":
						digitar("modo livre...escreva qualquer coisa que ele te responderá...tecnologia DreamCore,fale palavras como tchau,adeus para sair do chat")
						DreamCore.npc_selecionado = "comerciante de nocten"
						DreamCore.iniciar_conversa()
			if escolha_nocten == "2":
				digitar("você entra na igreja mas percebe que ainda está em construção")
				



				


	dados_ferreiro = {
		"dinheiro":1000,
		"estoque":[],
	}
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
			if escolha_ebranthal == "1":
				item_comprado = False
				while True:
					digitar("[comerciante de Ebranthal]:bem vindo á minha loja")
					print("[1]ver estoque")
					print("[2]vender itens")
					print("[3]conversar")
					print("[0]sair")
					escolha_loja_ebranthal = input("o que deseja fazer?")
					if escolha_loja_ebranthal == "0":
						if item_comprado:
						
							digitar("ao sair você percebe que o comerciante ficou feliz pois você comprou algo...")
						else:
							digitar("ok....volte sempre!")
					if escolha_loja_ebranthal == "3":
						digitar("modo livre...escreva qualquer coisa que ele te responderá...tecnologia DreamCore,fale palavras como tchau,adeus para sair do chat")
						DreamCore.npc_selecionado = "comerciante de ebranthal"
						DreamCore.iniciar_conversa()
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
					
	def criar_conta():
		digitar(
			"olá!antes de começar o jogo poderiamos perguntar se queira criar uma conta pra conteudos online? "
			"é de graça e te permite \n desfrutar de modos interativos multiplayer!"
		)

		escolha_criar_conta = input(
			"[S]sim, eu gostaria.\n[N]não, obrigado"
		).lower()

		if escolha_criar_conta != "s":
			return

		servidor = "http://luizsgustavo76.pythonanywhere.com"
		gerar_id_url = servidor + "/create-id"

		while True:
			data = {
				"nickname": None,
				"email": None,
				"senha": None,
			}

			print(
				"escolha um nickname, ele é unico e inalterável, é usado essencialmente \n "
				"para chats,trades e recursos online!"
			)

			escolha_nickname = input("qual será seu nickname?seja criativo ^^")

			print(f"tem certeza que seu nickname será {escolha_nickname}?")
			confirmar_nickname = input("[S]sim [N]não").lower()

			if confirmar_nickname != "s":
				continue

			data["nickname"] = escolha_nickname

			print(
				"deseja colocar um email?em caso de esquecimento de senha poderemos \n "
				"enviar um email de redefinição de senha!e tambem terá noticias de \n "
				"primeira mão direto no seu email"
			)
			print("obs:enviaremos um email de confirmação na sua caixa de entrada")

			colocar_email = input("[S] sim, [N] não").lower()

			if colocar_email == "s":
				escolha_email = input("qual é seu email?")
				print(
					"você poderá mudar seu email de recuperação á qualquer momento "
					"nas configurações"
				)
				data["email"] = escolha_email

			print("agora...defina uma senha por favor")
			escolha_senha = input("sua senha:")

			if len(escolha_senha) <= 6:
				digitar(
					"sua senha é muito curta...mas você tem a opção de ficar mas encarar "
					"riscos de segurança:segundo a licença"
				)
				aceitar_senha = input(
					"[S] sim,tenho consimento do risco, "
					"[N] não,quero redefinir minha senha"
				).lower()

				if aceitar_senha != "s":
					continue

				digitar("o aviso foi dado...")

			confirmar_senha = input("confirme sua senha")

			if escolha_senha != confirmar_senha:
				print("suas senhas não se coicidem")
				continue

			data["senha"] = escolha_senha

			try:
				print("enviando dados pro servidor...:[andamento]")
				response = requests.post(gerar_id_url, json=data)
				time.sleep(3)
				limpar_terminal()
				print(
					"enviando dados pro servidor...:"
					+ VERDE + "[concluido]" + RESET
				)
			except Exception:
				limpar_terminal()
				print(
					"enviando dados pro servidor...:"
					+ VERMELHO + "[FALHA]" + RESET
				)
				time.sleep(3)
				print(
					" um erro aconteceu durante a comunicação com os servidores,"
					"por favor tente mais tarde,se o erro persistir contacte no "
					"email:luizsgustavo76@gmail.com"
				)
				return

			try:
				resposta = response.json()
			except Exception:
				while True:
					print("Resposta não é JSON:")
					print(response.status_code)
					print(response.text)
					time.sleep(60)

			print("gerando ID")
			time.sleep(2)

			if "id" in resposta:
				print("finalizando criação da conta")
				return
	
		



	from datetime import datetime

	SERVER = "https://luizsgustavo76.pythonanywhere.com"


	import time

	def receber_mensagens(stop_event):
		ultimo_total = 0

		while not stop_event.is_set():
			try:
				r = requests.get(f"{SERVER}/r-chat", timeout=5)
				mensagens = r.json()

				if len(mensagens) > ultimo_total:
					novas = mensagens[ultimo_total:]

					for msg in novas:
						print(f"\n[{msg['hora']}] {msg['nome']}: {msg['mensagem']}")

					ultimo_total = len(mensagens)

			except Exception as e:
				print("Erro ao receber mensagens:", e)

			time.sleep(2)




	def enviar_mensagens_chat(nome):
		stop_event = threading.Event()

		thread_receber = threading.Thread(
			target=receber_mensagens,
			args=(stop_event,),
			daemon=True
		)
		thread_receber.start()

		while True:
			mensagem = input("> ")

			if mensagem.lower() == "/sair":
				stop_event.set()
				print("Saindo do chat...")
				break

			

			try:
				requests.post(
					f"{SERVER}/chat",
					json={
						"nome": nome,
						"mensagem": mensagem,
						"hora": datetime.now().strftime("%H:%M:%S")
					},
					timeout=5
				)

				
			except Exception as e:
				print("Erro ao enviar mensagem:", e)





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
					
	#falas batalhas
	#barman
	falas_batalha_barman = ["que belo dia....bom PRA TACAR UMA GARRAFA NA TUA CABEÇA,garotos como você não deveria estar nesse bar especialmente seno derrotado por mim,Então é isso?irá me deixar para trás para morrer??,toda causa haja uma consequencia"]
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
				if chance_fala == 1:
					digitar(falas_batalha[fala_aleatoria])
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
	def criar_mesa_trade():
			data_mesa = {
				"criador_trade": None,
				"integrantes": [],
				"itens": [],
				"em_duracao": None,
				"limite_pessoas": None,
			}

			while True:
				print("Quantos participantes terão?\n*Limite 10 integrantes")
				try:
					num_participantes = int(input(""))
				except ValueError:
					print("Digite um número válido!")
					continue

				if num_participantes > 10:
					digitar("Não é possível criar a trade, limite ultrapassado. Integrantes máximos são 10")
				elif num_participantes < 2:
					digitar("Não é possível criar uma mesa de trades com menos de 2 pessoas")
				else:
					data_mesa["criador_trade"] = dados_jogador["nome"]
					data_mesa["limite_pessoas"] = str(num_participantes)  # enviar como string
					data_mesa["em_duracao"] = "True"  # enviar como string
					data_mesa["integrantes"] = [dados_jogador["nome"]]  # adiciona o criador

					try:
						SERVER = "https://luizsgustavo76.pythonanywhere.com"
						requests.post(
							f"{SERVER}/s-trade",
							json={
								"criador_trade": data_mesa["criador_trade"],
								"integrantes": json.dumps(data_mesa["integrantes"]),
								"itens": json.dumps(data_mesa["itens"]),
								"em_duracao": data_mesa["em_duracao"],
								"limite_pessoas": data_mesa["limite_pessoas"]
							}
						)
					except Exception as e:
						print(f"Um erro aconteceu: {e}")
					break
	def buscar_estandes(url_servidor):
		try:
			resposta = requests.get(f"{url_servidor}/r-stands", timeout=5)
			resposta.raise_for_status()
			return resposta.json()
		except Exception as e:
			print("Erro ao conectar ao servidor:", e)
			return []



	def ver_estandes(stands):
		print("\nCENTRO MERCANTIL DE ELDORA\n")
		if not stands:
			print("Nenhum estande disponível.\n")
			return

		for stand in stands:
			print("-" * 40)
			print(f"Título do estande: {stand['nome_stand']}")
			print(f"Dono: {stand['nome']}")
			print("-" * 40)

			try:
				itens = json.loads(stand["itens"])
			except Exception:
				print("Itens inválidos ou corrompidos.")
				continue
			if not itens:
				print("Sem itens à venda.")
			else:
				for item in itens:
					nome_item = item.get("item", "Desconhecido")
					preco = item.get("preco", "N/A")
					print(f"{nome_item} | Preço: {preco}")

			print("-" * 40 + "\n")

	def criar_estande():
		SERVER = "https://luizsgustavo76.pythonanywhere.com"
		dados = {
			"nome":dados_jogador["nome"],
			"itens":[],
			"valor_pago":0,
			"nome_stand":None,
		}
		while True:
			print("Qual será o titulo do estande?")
			escolha_nome_estande = input("Titulo:")
			dados["nome_stand"] = escolha_nome_estande
			print("pra você ter seu estande você o aluga por hora(horario real) ou minutos!,somente 1000 moedas por hora ou 16 moedas por minuto!")
			print("[1] por hora")
			print("[2] por minuto")
			estande_hora = 1000
			estande_minuto = 16
			escolha_modo_tempo_estande = input("qual opção deseja escolher?")
			if escolha_modo_tempo_estande == "1":
				print("quantas horas você deseja alugar?")
				escolha_hora_estande = int(input("tempo:"))
				valor_total = estande_hora * escolha_hora_estande
				print(f"deu no total {valor_total}")
				escolha_aceitar_estande = input("deseja continuar\n[S] sim\n[N] não").lower()
				if escolha_aceitar_estande == "n":
					break
				if escolha_aceitar_estande == "s":
					dados_jogador["moedas"] -= valor_total
					dados["valor_pago"] = valor_total
			if escolha_modo_tempo_estande == "2":
				print("quantos minutos você deseja alugar?")
				escolha_minutos_estande = int(input("tempo:"))
				valor_total = estande_minuto * escolha_minutos_estande
				print(f"deu no total {valor_total}")
				escolha_aceitar_estande = input("deseja continuar\n[S] sim\n[N] não").lower()
				if escolha_aceitar_estande == "n":
					break
				if escolha_aceitar_estande == "s":
					dados_jogador["moedas"] -= valor_total
					dados["valor_pago"] = valor_total
			while True:
				print("quais serão o itens a venda...digite /finalizar pra finalizar a seleção de itens")
				mostrar_inventario()
				escolha_vender_item = input("")
				if escolha_vender_item == "/finalizar":
					break
				if escolha_vender_item in salvamento_dados:
					if salvamento_dados[escolha_vender_item] >=1:
						quantidade = input(f"quantas unidade de {escolha_vender_item}")
						quantidade = int(quantidade)
						if salvamento_dados[escolha_vender_item] >=quantidade:
							print("item adicionado!")
							print("qual será o valor da unidade desse item?")
							while True:
								try:
									escolha_preco_unidade = int(input("Preço:"))
									dados["itens"].append({
										"item": escolha_vender_item,
										"preco": escolha_preco_unidade
									})
									break

								except ValueError:
									print("digite um numero NÃO UMA PALAVRA!!!")
						else:
							print(f"você não {escolha_vender_item} o suficiente!")
				else:
					print("item não encontrado no seu inventário")
			digitar("finalizando...")
			server_stands = SERVER + "/s-stands"
			try:
				requests.post(server_stands, json=dados)
			except Exception as e:
				print(f"um erro aconteceu!{e}")
			break
	def menu_trade(trade_escolhida):
		SERVER = "https://luizsgustavo76.pythonanywhere.com"
		while True:
			print("[1] trocar itens")
			print("[2] chat interno")
			print("[0] sair")
			escolha_menu_trade = input("o que opção deseja escolher?")
			if escolha_menu_trade == "0":
				break
			if escolha_menu_trade == "1":
				mostrar_inventario()
				escolha_item_trade = input("qual item deseja trocar?se quer trocar moedas digite 'moedas {valor}'")
				for inventario in salvamento_dados:
					if escolha_item_trade in inventario:
						if salvamento_dados[escolha_item_trade] >=1:
							server_adicionar_item = SERVER + "/adicionar-itens"
							requests.post(server_adicionar_item, json={"trade_id":idx,"item":escolha_item_trade,})
							salvamento_dados[escolha_item_trade] -=1
	def ver_mesas_trades():
		servidor_r_trade = "https://luizsgustavo76.pythonanywhere.com/r-trade"
		
		try:
			r = requests.get(servidor_r_trade, timeout=5)
			dados = r.json()  # lista de trades
		except Exception as e:
			print(f"Erro ao conectar com o servidor: {e}")
			return None

		if not dados:
			print("Nenhuma trade aberta no momento.")
			return None

		# Lista numerada de trades
		print("Trades abertas:")
		for idx, trade in enumerate(dados, start=1):
			integrantes = json.loads(trade.get("integrantes")) if trade.get("integrantes") else []
			itens = json.loads(trade.get("itens")) if trade.get("itens") else []
			print(f"{idx}. Dono: {trade.get('criador_trade')} - {len(integrantes)}/{trade.get('limite_pessoas')} integrantes - {len(itens)} itens")

		# Escolha da trade pelo número
		while True:
			escolha = input("\nDigite o número da trade que deseja entrar (ou 0 para cancelar): ")
			try:
				escolha = int(escolha)
				if escolha == 0:
					return None
				if 1 <= escolha <= len(dados):
					trade_escolhida = dados[escolha - 1]
					print(f"\nVocê escolheu a trade do dono {trade_escolhida.get('criador_trade')}")
					resposta = requests.post("https://luizsgustavo76.pythonanywhere.com/entrar-trade", json={
					"trade_id": trade_escolhida["id"],
					"nome": dados_jogador["nome"]
					})
					resposta_dados = resposta.json()
					if resposta_dados["status"] == "ok":
						print(f"Você entrou na trade! Integrantes agora: {resposta_dados['integrantes']}")
						menu_trade(trade_escolhida["id"])
					else:
						print(f"Erro: {dados['mensagem']}")

				else:
					print("Número inválido. Tente novamente.")
			except ValueError:
				print("Digite um número válido!")
				

	#centro mercantil de eldora
	def centro_mercantil_eldora():
		while True:
			print("=====CENTRO MERCANTÍL DE ELDORA=====")
			print("[1] trades")
			print("[2] ir nos estandes de vendas")
			print("[3] abrir o chat")
			print("[0]sair")
			escolha_centro_mercantil = input("o que deseja fazer?")
			if escolha_centro_mercantil == "0":
				digitar("você sai do centro...")
				break
			if escolha_centro_mercantil == "3":
				enviar_mensagens_chat(nome)
			if escolha_centro_mercantil == "1":
				while True:
					print("[1]criar uma mesa de trade")
					print("[2]ver mesas de trades abertas")
					print("[0] sair")
					escolha_centro_mercantil_trades = input("o que deseja fazer?")
					if escolha_centro_mercantil_trades == "1":
						criar_mesa_trade()
					if escolha_centro_mercantil_trades == "2":
						ver_mesas_trades()
						entrar_trade = input("em qual trade deseja")
					if escolha_centro_mercantil == "0":
						break
			if escolha_centro_mercantil == "2":
				while True:
					print("[1] Criar um Estande")
					print("[2] Ver Estandes")
					print("[0] sair")
					escolha_estande = input("qual opção deseja escolher?")
					if escolha_estande == "1":
						criar_estande()
					elif escolha_estande == "2":
						URL_SERVIDOR = "https://luizsgustavo76.pythonanywhere.com"
						stands = buscar_estandes(URL_SERVIDOR)
						ver_estandes(stands)
					elif escolha_estande == "0":
						break
					else:
						print("opção invalida")
			
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
	MARROM = "\033[33m"
	VERDE_CLARO = "\033[92m"
	CINZA = "\033[1;37m"
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
		"picareta de obsidiana":0,
		"picareta de cobre":0,
		"cobre bruto":0,
		"ferro bruto":0,
		"ouro bruto":0,
		"machado de madeira":0,
		"machado de ferro":0,
		"machado de pedra":0,
		"machado de ferro":0,
		"machado de cobre":0,
		"machado de obsidiana":0,
		"machado de diamante":0,
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
		"cobre":0,
		"ferro":0,
		"ouro":0,
		"diamante":0,
		"rubi":0,
		"esmeralda":0,
		"amuleto das almas":0,
		"espada de rubi":0,
		"espada de esmeralda":0,
		"espada de ferro":0,
		"espada de cobre":0,
		"espada de ouro":0,
		"espada de diamante":0,
		"espada de obsidiana":0,
		"capacete de madeira":0,
		"capacete de pedra":0,
		"capacete de cobre":0,
		"capacete de ferro":0,
		"capacete de ouro":0,
		"capacete de rubi":0,
		"capacete de esmeralda":0,
		"capacete de obsidiana":0,
		"picareta de madeira":0,
		"picareta de pedra":0,
		"picareta de cobre":0,
		"picareta de ferro":0,
		"picareta de ouro":0,
		"picareta de esmeralda":0,
		"picareta de rubi":0,
		"picareta de diamante":0,
		"picareta de obsidiana":0,
		"peitoral de madeira":0,
		"peitoral de pedra":0,
		"peitoral de cobre":0,
		"peitoral de ferro":0,
		"peitoral de ouro":0,
		"peitoral de esmeralda":0,
		"peitoral de rubi":0,
		"peitoral de diamante":0,
		"peitoral de obsidiana":0,
		"calça de madeira":0,
		"calça de pedra":0,
		"calça de cobre":0,
		"calça de ferro":0,
		"calça de ouro":0,
		"calça de rubi":0,
		"calça de esmeralda":0,
		"calça de diamante":0,
		"calça de obsidiana":0,
		"botas de madeira":0,
		"botas de pedra":0,
		"botas de cobre":0,
		"botas de ferro":0,
		"botas de ouro":0,
		"botas de rubi":0,
		"botas de esmeralda":0,
		"botas de diamante":0,
		"botas de obidiana":0,
		"enxada de madeira":0,
		"enxada de pedra":0,
		"enxada de cobre":0,
		"enxada de ferro":0,
		"enxada de ouro":0,
		"enxada de rubi":0,
		"enxada de esmeralda":0,
		"enxada de diamante":0,
		"enxada de obsidiana":0,
	}
	inventario_jogador = {
		"madeira": {
			"raridade"
			"preço revenda"
			"categoria"
		},
		"carvão":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"adaga":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"barra_cobre":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pipeta_cobre":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pocao_exp2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"espada2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pao2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"carne2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"batata2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pocao_de_stamina2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"cerveja2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pinga2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"artefato_luz2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"artefato_fogo2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"artefato_agua2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"artefato_lava2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"artefato_diamante2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"artefato_força2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"artefato_defesa2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"artefato_ouro2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"artefato_sorte2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"artefato_magia2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"moeda_do_submundo2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"contrato_das_almas2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"amuleto_da_necromancia2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"fumaca_da_ilusao2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"adaga_envenenada2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"armadura_sombria2":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"cerveja":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pinga_de_mel":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"cachaça_mineira":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"vodka":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"velho_barreiro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"balde":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"obsidiana":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"balde de água":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"balde de lava":{
				"raridade"
			"preço revenda"
			"categoria"
		},
		"picareta de obsidiana":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"picareta de cobre":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"cobre bruto":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"ferro bruto":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"ouro bruto":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"machado de madeira":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"machado de ferro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"machado de pedra":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"machado de ferro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"machado de cobre":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"machado de obsidiana":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"machado de diamante":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pedra":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pergaminho da forca I":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pergaminho da forca II":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pergaminho da forca III":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pergaminho da forca IV":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pergaminho da defesa I":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pergaminho da defesa II":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pergaminho da defesa III":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pergaminho da defesa IV":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pergaminho de remendo":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"pergaminho de mais moedas":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"cobre":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"ferro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"ouro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"diamante":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"rubi":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"esmeralda":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"amuleto das almas":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"espada de rubi":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"espada de esmeralda":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"espada de ferro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"espada de cobre":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"espada de ouro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"espada de diamante":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"espada de obsidiana":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"capacete de madeira":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"capacete de pedra":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"capacete de cobre":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"capacete de ferro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"capacete de ouro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"capacete de rubi":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"capacete de esmeralda":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"capacete de obsidiana":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"picareta de madeira":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"picareta de pedra":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"picareta de cobre":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"picareta de ferro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"picareta de ouro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"picareta de esmeralda":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"picareta de rubi":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"picareta de diamante":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"picareta de obsidiana":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"peitoral de madeira":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"peitoral de pedra":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"peitoral de cobre":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"peitoral de ferro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"peitoral de ouro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"peitoral de esmeralda":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"peitoral de rubi":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"peitoral de diamante":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"peitoral de obsidiana":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"calça de madeira":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"calça de pedra":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"calça de cobre":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"calça de ferro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"calça de ouro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"calça de rubi":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"calça de esmeralda":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"calça de diamante":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"calça de obsidiana":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"botas de madeira":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"botas de pedra":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"botas de cobre":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"botas de ferro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"botas de ouro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"botas de rubi":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"botas de esmeralda":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"botas de diamante":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"botas de obidiana":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"enxada de madeira":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"enxada de pedra":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"enxada de cobre":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"enxada de ferro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"enxada de ouro":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"enxada de rubi":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"enxada de esmeralda":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"enxada de diamante":{
			"raridade"
			"preço revenda"
			"categoria"
		},
		"enxada de obsidiana":{
			"raridade"
			"preço revenda"
			"categoria"
		},
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
			"estoque_vinho":0,
			"estoque_whiskey":0,
			"estoque_tequila":0,
			"estoque_hidromel":0,
			"estoque_rum":0,
			"reputação taverna":0,
			"frequentadores":["bebado"],
			"melhorias_taverna": {
				"bancos":[50,100,200,250,750],
				"mesas":[100,250,450,800,1200],
				"aparencia":[500,1000,1500,2000,2500],
				"bebidas":[100,200,300,400,500],
				"iluminação":[200,400,600,800,1000],
				"cozinha":[300,600,900,1200,1500],
			},
	}


	#preço das bebidas sim o nome é confuso mas não da pra mudar pq tem muita coisa utilizando ele
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
	#verificação da taverna pra setar informações como npcs que vão na taverna,reputação e upgrades na hora do loading
	def verificar_taverna():
		pass
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
	#quando de reputação tu ganhará quando você comprar algum upgrade
	reputacao_por_upgrades_taverna = {
		"mesas": {
			"nivel 1":20,
			"nivel 2":50,
			"nivel 3":100,
			"nivel 4":150,
			"nivel 5":215,
		},
		"bancos":{
			"nivel 1":10,
			"nivel 2":25,
			"nivel 3":50,
			"nivel 4":75,
			"nivel 5":105,
		},
		"aparencia": {
			"nivel 1":100,
			"nivel 2":350,
			"nivel 3":500,
			"nivel 4":750,
			"nivel 5":1000,
		},
		"cozinha": {
			"nivel 1":50,
			"nivel 2":250,
			"nivel 3":400,
			"nivel 4":750,
			"nivel 5":975,
		},
		"loja sombria":{
			"nivel 1":750,
			"nivel 2":1200,
			"nivel 3":1750,
			"nivel 4":3200,
			"nivel 5":5000,
		},
		"bebidas": {
			"nivel 1":250,
			"nivel 2":600,
			"nivel 3":820,
			"nivel 4":1200,
			"nivel 5":2100,
		},
		"iluminação": {
			"nivel 1":100,
			"nivel 2":300,
			"nivel 3":750,
			"nivel 4":1000,
			"nivel 5":3000,
		},
	}
	upgrades_taverna = {
		"mesas":0,
		"bancos":0,
		"aparencia":0,
		"cozinha":0,
		"loja sombria":0,
		"bebidas":0,
		"iluminação":0,
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
		"golem de rubi":0,
		"golem de esmeralda":0,
		"golem de diamante":0,
	}

	# Golem selecionado (você pode usar depois)
	golem_selecionado = 0

	# Verifica se cada slot está ocupado
	slots_cheio = {
		"slot1_cheio": False,
		"slot2_cheio": False,
		"slot3_cheio": False,
		"slot4_cheio": False,
	}

	# Mostra qual golem está em cada slot
	slots = {
		"slot1_golem": False,
		"slot2_golem": False,
		"slot3_golem": False,
		"slot4_golem": False,
	}
	def mostrar_golens():
		for golens in dados_jogador_golem:
			try:
				valor = int(golens)  
			except:
				valor = 0            
			
			if valor >= 1:
				print(golens)
			else:
				pass
	design_golens = {
		"golem de pedra":CINZA,
		"golem de madeira":MARROM,
		"golem de rubi":VERMELHO,
		"golem de esmeralda":VERDE_CLARO,
		"golem de obsidiana":ROXO,
		"golem de diamante":CIANO,
		"golem de ouro":AMARELO,
		"golem de ferro":BRANCO,
	}
	def menu_gerenciamento_golem(escolha_gerenciamento_golem):
		while True:
			limpar_terminal()
			print(f"gerecianmento do {escolha_gerenciamento_golem}")
			print(design_golens[escolha_gerenciamento_golem] + " ■\n■■■\n ■" + RESET)
			print("[1]equipar itens")
			print("[2]ver status do golem")
			print("[0]sair")
			escolha_menu_gereciamento_golem = input("qual opção você escolhe?")
			if escolha_menu_gereciamento_golem == "0":
				break
			
	# Função principal do menu dos golems
	def gerenciar_golem():
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
			for golens in slots.values():
				if not golens:
					pass
				else:
					golem_habilitado = True
			if escolha_menu_golem == '1':
				# Você vai completar depois essa parte de ativar/desativar
				print("qual golem deseja habilitar/desabilitar?")
				for nome, qtd in dados_jogador_golem.items():
					print(f"{nome} - Quantidade: {qtd}")
				habilitar_desativar_golem = input("")
				if habilitar_desativar_golem in dados_jogador_golem:
					print(f"Slot 1 ---- {slots['slot1_golem']}")
					print(f"Slot 2 ---- {slots['slot2_golem']}")
					print(f"Slot 3 ---- {slots['slot3_golem']}")
					print(f"Slot 4 ---- {slots['slot4_golem']}")
					print("em qual slot deseja adicionar/remover um golem?")
					escolha_habilitar_desabilitar_golem = input("")
					if "1" in escolha_habilitar_desabilitar_golem:
						if not slots["slot1_golem"]:
							mostrar_golens()
							adicionar_golem = input("qual golem deseja adicionar?")
							adicionar_golem = str(adicionar_golem)
							if dados_jogador_golem[adicionar_golem] >=1:
								print(f"o golem {adicionar_golem} foi adicionado!")
								dados_jogador_golem[adicionar_golem] -=1
								slots["slot1_golem"] = adicionar_golem
						else:
							print(f"deseja desabilitar o golem {slot['slot1']}?")
							escolha_desabilitar_golem("[S] OU [N]").lower()
							if escolha_desabilitar_golem == "s":
								print(f"o golem {slot['slot1']}foi desativado!")
								slot[slot1] = False
							else:
								pass
					if "2" in escolha_habilitar_desabilitar_golem:
						if not slots["slot2_golem"]:
							mostrar_golens()
							adicionar_golem = input("qual golem deseja adicionar?")
							adicionar_golem = str(adicionar_golem)
							if dados_jogador_golem[adicionar_golem] >=1:
								print(f"o golem {adicionar_golem} foi adicionado!")
								dados_jogador_golem[adicionar_golem] -=1
								slots["slot2_golem"] = adicionar_golem
						else:
							print(f"deseja desabilitar o golem {slot['slot1']}?")
							escolha_desabilitar_golem("[S] OU [N]").lower()
							if escolha_desabilitar_golem == "s":
								print(f"o golem {slot['slot2']}foi desativado!")
								slot[slot2_golem] = False
							else:
								pass
					if "3" in escolha_habilitar_desabilitar_golem:
						if not slots["slot3_golem"]:
							mostrar_golens()
							adicionar_golem = input("qual golem deseja adicionar?")
							adicionar_golem = str(adicionar_golem)
							if dados_jogador_golem[adicionar_golem] >=1:
								print(f"o golem {adicionar_golem} foi adicionado!")
								dados_jogador_golem[adicionar_golem] -=1
								slots["slot3_golem"] = adicionar_golem
						else:
							print(f"deseja desabilitar o golem {slot['slot3']}?")
							escolha_desabilitar_golem("[S] OU [N]").lower()
							if escolha_desabilitar_golem == "s":
								print(f"o golem {slot['slot3']}foi desativado!")
								slot[slot3_golem] = False
							else:
								pass
					if "4" in escolha_habilitar_desabilitar_golem:
						if not slots["slot4_golem"]:
							mostrar_golens()
							adicionar_golem = input("qual golem deseja adicionar?")
							adicionar_golem = str(adicionar_golem)
							if dados_jogador_golem[adicionar_golem] >=1:
								print(f"o golem {adicionar_golem} foi adicionado!")
								dados_jogador_golem[adicionar_golem] -=1
								slots["slot4_golem"] = adicionar_golem
						else:
							print(f"deseja desabilitar o golem {slot['slot4']}?")
							escolha_desabilitar_golem("[S] OU [N]").lower()
							if escolha_desabilitar_golem == "s":
								print(f"o golem {slot['slot4']}foi desativado!")
								slot[slot4_golem] = False
							else:
								pass
							
			elif escolha_menu_golem == '2':
				while True:
					print("\n--- Seus Golems ---")
					print(f"Slot 1 ---- {slots['slot1_golem']}")
					print(f"Slot 2 ---- {slots['slot2_golem']}")
					print(f"Slot 3 ---- {slots['slot3_golem']}")
					print(f"Slot 4 ---- {slots['slot4_golem']}")
					
					escolha_gerenciamento_golem = input("\nDigite o nome do golem que deseja gerenciar (ou 'voltar'): ").lower()
					if escolha_gerenciamento_golem == 'voltar':
						break

					golem_encontrado = False
					for nome_golem in dados_jogador_golem:
						if escolha_gerenciamento_golem == nome_golem.lower() and dados_jogador_golem[nome_golem] > 0:
							golem_encontrado = True
							print(f"\nGerenciando o {nome_golem}...")
							menu_gerenciamento_golem(escolha_gerenciamento_golem)

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
	diamante = [24, 25,26, 27]
	rubi = [28, 29, 30]
	esmeralda = [31, 32, 33, 34, 35, 36]
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
		
					

	ferro_nivel_y = 8
	pedra_nivel_y = 0
	cobre_nivel_y = 5
	ouro_nivel_y = 10
	carvao_nivel_y = 2
	rio_lava_nivel_y = 15
	rubi_nivel_y = 35
	esmeralda_nivel_y = 23
	diamante_nivel_y = 14
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
						if linha_minerios[nivel_x_superfice] in diamante:
							digitar("...\num...um diamante")
							salvamento_dados["diamante"] +=1
							nivel_x_superfice += 1
						if linha_minerios[nivel_x_superfice] in esmeralda:
							digitar("o meu deus....uma esmeralda!")
							salvamento_dados["esmeralda"] +=1
							nivel_x_superfice += 1
						if linha_minerios[nivel_x_superfice] in rubi:
							digitar("nossa..essa pedra tá muito brilante e vermelha..pera um pouco....é um rubi!")
							nivel_x_superfice += 1
							salvamento_dados["rubi"] += 1
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
							digitar(f"[{dados_jogador['nome']}]nossa...ja cheguei a um rio de lava..")
							digitar("será que eu pego um pouco?")
							print("[s]sim\n[n]não")
							escolha_rio_lava = input("o que deseja fazer?")
							if escolha_rio_lava == "s":
								if dados_itens_equipados["mao esquerda"] == "balde":
									digitar("você coletou um balde de lava...!")
									salvamento_dados["balde de lava"] += 1
									dados_itens_equipados["mao esquerda"] = ""
							if escolha_rio_lava == "n":
								pass
					
					
						
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
														escolha_comprar_item_mineiro = input("qual item deseja comprar?digite [0] para sair")
														if escolha_comprar_item_mineiro == "0":
															digitar(f"até mais {dados_jogador['nome']}")
															break
												
										
								
								
								
							
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

	#pessoas te acompanhando
	pessoas_acompanhando = []
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
	#para quando os golens tiverem equipados e prontos para situação de batlha ou mineração

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
			
		print("	cabeça ------",dados_itens_equipados["cabeca"])
		print("	tronco ------",dados_itens_equipados["tronco"])
		print("	pernas ------",dados_itens_equipados["pernas"])
		print("	pés	------",dados_itens_equipados["pes"])
					   

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
		digitar(f"olá {dados_jogador['nome']} como vai?")
		while True:
			print("[1]conversar")
			print("[2]trocar itens")
			print("[3]fazer missões")
			if "ruinas de eldora" in registro_acoes:
				print("[4]pedir para o acompanhar as ruinas")
			print("[0]sair")
			escolha_dorian = input("o que deseja fazer?")
			if escolha_dorian == "4":
				if "ruinas de eldora" in registro_acoes:
					digitar("ok..eu te acompanho até lá..")
					pessoas_acompanhando.append("dorian")
			if escolha_dorian == "0":
				digitar("adeus....")
				break
			if escolha_dorian == "1":
				DreamCore.npc_selecionado = "dorian"
				DreamCore.iniciar_conversa()
			if escolha_dorian == "3":
				limpar_terminal()
				print(f"oi {dados_jogador['nome']},como vai?")
				if dados_missoes["missoes dorian"] == 0:
					digitar("como estou ainda muito cansado eu queria pedir um favor para você,na verdade seria uma missão,o que me diz?")
					npc_missao_selecionada = "dorian"
					missoes(npc_missao_selecionada)
	#batalha usando actionmoves
	def batalha_ia():
		golem = ActionsMoves.golem()
		contador_golem = 1
		golem.entrar_batalha_golem(slots,contador_golem)
		monstro = ActionsMoves.monstro()
		while True:
			monstro.gerar_acao()
			limpar_terminal()
			print(f"Vida monstro:{monstro.atributos_monstro['vida']}")
			print(f"Sua vida:{dados_jogador['vida']}")
			print("[1]Atacar")
			print("[2]Defender")
			print("[3]Usar habilidade")
			print("[4]Trocar com aliados")
			print("[5]Usar o inventário")
			print("[6]Gerenciar golens")
			print("[7]Ver status")
			print("[0]Sair da batalha")
			escolha_batalha = input("Qual opção deseja usar?")
			if escolha_batalha == "0":
				digitar("você sai da batalha silenciosamente")
				break
			if escolha_batalha == "1":
				monstro.atributos_monstro['vida'] -= dados_jogador["dano"]
				digitar(f"você tirou {dados_jogador['dano']} de vida do monstro!")
				dados_jogador["vida"] -= monstro.atributos_monstro["dano"]
				digitar(f"o monstro te atacou tirando {monstro.atributos_monstro['dano']} de vida!")
				
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
			"primeira_vez_ruina":primeira_vez_ruina,
			"dados_jogador_golem":dados_jogador_golem,
			"slots":slots,

		}

		with open("tloe_save.json", "w") as arquivo:
			json.dump(dados_salvar, arquivo, indent=4)
		print(" Jogo salvo com sucesso!")
	def cena_inicial():
		digitar(f"você...você era um viajante que explorava vários lugares desconhecidos e inóspitos que a humanidade nunca mais pisou lá....quando você era pequeno gostava de lendas por isso que se dedica a exploração mas uma delas que você via era as lendas de eldora....um lugar feliz,vivo e prospero teve sua decadencia a ataques de diferentes monstros e inimigos,eles roubaram os 10 artefatos de eldora o que fez eldora que era um paraiso se transformar e um inferno de ruinas com poucos sobreviventes....mas era uma lenda....nada disso seria real....era o que eu achava até agora....")
		limpar_terminal()
		digitar(CIANO + "Picos Congelados de NorthHills" + RESET)
		limpar_terminal()
		digitar("em uma longa escalada para chegar ao topo dos picos congelados.....")
		limpar_terminal()
		digitar("você.....você finalmente chegou ao topo,foi gratificante ter realizado esse grande marco...mas eu olho pro outro lado do pico....")
		digitarlento(VERDE + "ELDORA???????" + RESET )
		digitar("era tudo verdade então....")
		digitar("você encontrou o reino de uma historia que tanto marcou sua infancia")
		digitar("você depois dessa longa expedição você decide ficar por lá")
		digitar("[Dorian]eu estou muito exausto....vou passar essa noite numa cabana")
	def gerenciar_guilda():
			for aliados_guildas in aliados:
				while True:
					print(aliados_guildas)
					gerenciar_escolha = input("deseja gerenciar a Guilda?[S]Sim ou [N]Não").lower()
					if gerenciar_escolha == "n":
						break
					if gerenciar_escolha == "s":
						while True:
							print("O que deseja fazer?")
							print("[1]Remover aliados")
							print("[2]Ver status dos aliados")
							print("[3]equipar itens em aliados")
							print("[0]sair do menu")
							escolha_gerenciar_aliados = input("") 
							if escolha_gerenciar_aliado == "0":
								break	
							if escolha_gerenciar_aliado == "1":
								print(aliados)
								remover_aliado = input("qual aliado deseja remover?")
								try:
									aliados.remove[remover_aliado]
									print(f"o aliado {remover_aliado} foi removido com sucesso!")
								except:
									print("esse aliado não existe na sua guilda")
									
							
									  
						
		
	def carregar_progresso():
		nonlocal dados_jogador, salvamento_dados, upgrades, aliados, valor_habilidade,salvamento_dados2,dados_jogador2,dados_jogador3,dados_jogador4,amigos_conectados,dados_itens_equipados,dados_taverna,dados_mineiro,memoria_ferreiro,dados_vilas,horario,dados_jogador_server,slots,dados_jogador_golem;
		if os.path.exists("tloe_save.json"):	
			
			with open("tloe_save.json", "r") as arquivo:
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
				slots = dados_carregados.get("slots",slots)
				dados_jogador_golem = dados_carregados.get("dados_jogador_golem",dados_jogador_golem)
			print("Progresso carregado com sucesso!")
		else:
			limpar_terminal()
			digitar("desculpe....mas você não tem nenhum save disponivel o que resultara no fechamento do jogo")
			time.sleep(3)
			exit()

	digitar("The Legends Of Eldora, todos os direitos reservados a Luiz Gustavo luizsgustavo76@gmail.com")
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
		
			
		async def verificar_exp():
			if dados_jogador["exp"] >= dados_jogador["exp para evoluir"]:
				dados_jogador["nivel"] += 1
				digitar(f"parabens você subiu para o nivel {dados_jogador['nivel']}!")
				dados_jogador["exp para evoluir"] += 100
				dados_jogador["exp"] -= dados_jogador["exp para evoluir"]
				if dados_jogador["exp"] <=0:
					dados_jogador["exp"] = 0
					
		
		asyncio.run(verificar_exp())
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
		contexto_tloe = {
			"dados_taverna": dados_taverna,
			"reputacao_por_upgrades_taverna": reputacao_por_upgrades_taverna,
			"registro_acoes": registro_acoes,
			"upgrades_taverna": upgrades_taverna,
		}

		gerador = ActionsMoves.gerar_npcs(contexto_tloe=contexto_tloe, upgrades_taverna=upgrades_taverna)
		gerador.iniciar_npc(upgrades_taverna, dados_taverna)

		print("[1] Ir à taverna")
		print("[2] Ver seus status")
		print("[3] Ir para sua casa")
		print("[4] Sair do jogo")
		print("[5] Ir à loja")
		print("[6] Ir no inventário")
		print("[7] Enciclopédia")
		print("[8] Ver conquistas")
		print("[9] Salvar jogo")
		print("[10] Carregar jogo")
		print("[11] upgrades")
		print("[12] guilda")
		print("[13] arena infinita")
		print("[14] centro mercantil de eldora")
		print("[15] abrir o mapa")
		print("[16] ferreiro")
		
		escolha_centro = input("O que vai fazer? ")
		if escolha_centro == "teste_novo_motor_actionsmoves_ia 1.0":
			contador_golem = 1
			batalha_ia()
			
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
			preco_itens_revenda = {
			"cobre":25,
			"carvão":10,
			"ferro":50,
			"ouro":200,
			"diamante":500,
			"obsidiana":750,
			"lava":50,
			"espada":50,
			"picareta":100,
			"enxada":25,
			"pa":75,
			"rubi":1000,
			"esmeralda":750,
			}
			async def espera_forja_golem(escolha_criar_golem):
				time.sleep(60)
				notificacao = ToastNotifier()
				notificacao.show_toast(
					"The Legends Of Eldora"
					f"\n{dados_jogador['nome']},seu {escolha_criar_golem} está pronto"
				)

			while True:
				limpar_terminal()
				print("=====ferreiro=====")
				print("[1]forjar equipamento")
				print("[2]encantar itens")
				print("[3]concertar itens")
				print("[4]forjar golem")
				print("[5]conversar")
				print("[6]vender itens")
				print("[7]fazer missões")
				print("[0]sair")
				escolha_ferreiro = input("qual opção tu queres")
				if escolha_ferreiro == "4":
					digitar("um golem para ter dar uma força..bela escolha meu jovem")
					golens_possiveis = []
					tempo_forjar = horario["horas"] + 1
					if salvamento_dados["cobre"] >= 30 and salvamento_dados["amuleto das almas"] >=1:
						golens_possiveis.append("golem de cobre")
					if salvamento_dados["ferro"] >= 30 and salvamento_dados["amuleto das almas"] >=1:
						golens_possiveis.append("golem de cobre")
					if salvamento_dados["pedra"] >= 30 and salvamento_dados["amuleto das almas"] >=1:
						golens_possiveis.append("golem de pedra")
					if salvamento_dados["obsidiana"] >= 30 and salvamento_dados["amuleto das almas"] >=1:
						golens_possiveis.append("golem de obsidiana")
					if salvamento_dados["madeira"] >= 30 and salvamento_dados["amuleto das almas"] >=1:
						golens_possiveis.append("golem de madeira")
					if salvamento_dados["rubi"] >= 30 and salvamento_dados["amuleto das almas"] >=1:
						golens_possiveis.append("golem de rubi")
					if salvamento_dados["esmeralda"] >= 30 and salvamento_dados["amuleto das almas"] >=1:
						golens_possiveis.append("golem de esmeralda")
					if salvamento_dados["diamante"] >= 30 and salvamento_dados["amuleto das almas"] >=1:
						golens_possiveis.append("golem de diamante")
					if salvamento_dados["ouro"] >= 30 and salvamento_dados["amuleto das almas"] >=1:
						golens_possiveis.append("golem de ouro")
					while True:
						print("com seus itens você consegue fazer os seguintes golens")
						for lista_golens_possiveis in golens_possiveis:
							print(lista_golens_possiveis)
						escolha_criar_golem = input("qual golem deseja criar?digite [0] para sair")
						if escolha_criar_golem == "0":
							break
						
						if escolha_criar_golem in golens_possiveis:
							# subtrai moedas
							custo = valores_forja[escolha_criar_golem]["moedas"]
							dados_jogador["moedas"] -= custo

							# pega o dicionário do golem
							material_golem = valores_forja[escolha_criar_golem]

							# subtrai o amuleto das almas
							amuleto = "amuleto das almas"
							salvamento_dados[amuleto] -= material_golem["itens"][amuleto]

							# subtrai o segundo item do dicionário de itens
							dicionario_itens = material_golem["itens"]
							materias_chave = list(dicionario_itens.keys())[1]
							materias_valor = dicionario_itens[materias_chave]
							salvamento_dados[materias_chave] -= materias_valor
							digitar(f"volte aqui as {tempo_forjar} horas para buscar seu golem")
							asyncio.run(espera_forja_golem(escolha_criar_golem))
							dados_jogador_golem[escolha_criar_golem] += 1
							
						else:
							digitar(f"[ferreiro]você não pode fazer o {escolha_criar_golem} porque você não tem os materiais necessarios")
				if escolha_ferreiro == "6":
					digitar("[ferreiro]vejamos que você quer vender seus itens,aqui é uma boa escolha!")
					limpar_terminal()
					print("itens suportados")
					print("====minerios====")
					print("Carvão")
					print("Cobre")
					print("Ferro")
					print("pedra")
					print("Ouro")
					print("Diamante")
					print("Obsidiana")
					print("Rubi")
					print("Esmeralda")
					print("equipamentos e ferramentas")
					print("armaduras de madeira,cobre,diamante,ferro,ouro e obsidiana\n espada de diamante,pedra,madeira,ouro,obsidiana,cobre,ferro\nmachado de diamante,pedra,madeira,ouro,obsidiana,cobre,ferro\nenxada de diamante,pedra,madeira,ouro,obsidiana,cobre,ferro,pá de diamante,pedra,madeira,ouro,obsidiana,cobre,ferro\npicareta de diamante,pedra,madeira,ouro,obsidiana,cobre,ferro\n")
					mostrar_inventario()
					preco_revenda = 0
					def reduzir_preco_revenda(escolha_item_vender_ferreiro):
						item_pra_vender = escolha_item_vender_ferreiro.slipt()
						if len(item_pra_vender) == 1:
							preco_revenda += preco_itens_revenda[escolha_item_vender_ferreiro]
						if len(item_pra_vender) == 2:
							preco_revenda = int(preco_itens_revenda[item_pra_vender][0] + preco_itens_revenda[item_pra_vender][1])
					escolha_item_vender_ferreiro = input("qual item deseja vender?")
					for lista_itens in salvamento_dados.keys():
						if escolha_item_vender_ferreiro == lista_itens:
							reduzir_preco_revenda(escolha_item_vender_ferreiro)
							print(f"você deseja mesmo vender o item {escolha_item_vender_ferreiro}?você ganhará {preco_revenda} de moedas")
							aceitar_revenda = input("[S] OU [N]").lower()
							if aceitar_revenda == "s":
								dados_ferreiro["dinheiro"] -= preco_revenda
								dados_jogador["moedas"] += preco_revenda
						else:
							digitar("[ferreiro]desculpe mas eu não compro esse tipo de item")

		
						
							
						
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
							
							
							
								
							
						
							
		


			
		
				
					
				
					
				
					
										 
					
				
					
				
				
			
		

	 #GUILDAS
		elif escolha_centro == "12":
			
			registro_acoes.append("guilda")
			limpar_terminal()
			
			print("====guilda====")
			for nomes_aliados in aliados_guilda:
				if nomes_aliados == "":
					print("VOCÊ NÃO TEM NENHUM ALIADO")
					time.sleep(0.5)
					break
				else:
					print(f"{nomes_aliados}\n")
						
					gerenciar_guilda()   					
							
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
				print("[7]Mina de Eldora")
				print("[8]Ruinas de Eldora")
				if mod_carregado:
					for i,(areas_mods) in enumerate(game["areas"],start=8):
						print("####AREAS ADICIONADAS POR MODS#####")
						print(f"[{i}] {areas_mods}")
				print("[0]sair")
				escolha_mapa = input("qual area deseja ir?")
				limpar_terminal()
				if escolha_mapa == "8":
					registro_acoes.append("ruinas de eldora")
					if primeira_vez_ruina:
						if "dorian" in pessoas_acompanhando:
							ruinas_eldora()
						else:
							digitar("esse lugar....é totalmente desconhecido e hostíl é melhor eu chamar meu companheiro Dorian pra tentar me ajudar...")
					else:
						ruinas_eldora()
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
			

		if escolha_centro == "6":
			registro_acoes.append("inventario")
			limpar_terminal()
			voltar_inventario = 1
			while voltar_inventario == 1:	
				
				print("[1]abrir o inventário")
				print("[2]usar equipamentos")
				print("[3]gerenciar golens")
				print("[0]sair")
				escolha_menu_inventario = input("qual função deseja usar")
				if escolha_menu_inventario == "3":
					gerenciar_golem()
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
			centro_mercantil_eldora()
			
				
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
			wave = 1
			wave_time = 0
			zombaria = 0
			ataque_selvagem = 0
			if escolha_dificuldade == "1":
				taxa_de_evolucao = 0.25
				vida_definida = 5
				defesa_monstro = 5
			if escolha_dificuldade == "2":
				taxa_de_evolucao = 0.5
				vida_defenida = 7
				defesa_monstro = 7
			if escolha_dificuldade == "3":
				taxa_de_evolucao = 1
				vida_defenida = 13
				defesa_monstro = 13
			if escolha_dificuldade == "4":
				taxa_de_evolucao = 2
				vida_defenida = 18
				defesa_monstro = 18
			golem_habilitado = False
			for golem_ativado in slots:
				if not golem_ativado:
					golem_habilitado = True
			while dados_jogador["vida"] >=0:
				valor_dialogo = 0
				salvar_progresso()
			
					
					
								
						
						
				
					
				
				if hp_monstro <=0:
					hp_monstro = vida_definida
				
				print(VERMELHO + "UM MONSTRO APARECEU")
				
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
				if escolha_arena == "3":
					habilidades_especiais()
				if escolha_arena == "5":
					print("você abre seu inventario")
					print("=======INVENTARIO=======")
					mostrar_inventario()
					escolha_item = input("escolha um item para usar:").strip()
					usar_item(escolha_item)
					
					
					
					
				
						
				if escolha_arena == "1":
					ActionsMoves.acoes_batalha.append(f"jogador ataque dano {dados_jogador['dano']}")
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
					if golem_habilitado:
						ActionsMoves.golem.entrar_batalha_golem()
					limpar_terminal()
					digitar(VERDE + "você atacou o monstro" + RESET)
					hp_monstro -= dados_jogador["dano"]
					digitar(VERMELHO + f"o monstro te atacou tirando {dano_monstro}" + RESET)
					dados_jogador["vida"] -= dano_monstro
					limpar_terminal()
					
					
					
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
					vida_defenida = vida_definida + taxa_de_evolucao
					hp_monstro = vida_defenida
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
			criar_npc_taverna = ActionsMoves.gerar_npcs(contexto_tloe, upgrades_taverna)
			criar_npc_taverna.iniciar_npc(upgrades_taverna, dados_taverna)
			verificar_taverna()
			
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
				print("[2]conversar com um comerciante sombrio")
				print("[3]checar o baú")
				print("[4]sentar-se numa mesa")
				canto_taverna = input("")
				if canto_taverna == "4":
					limpar_terminal()
					if len(dados_taverna["frequentadores"]) >= 1:
						digitar("você chega lentamente numa mesa...há muitas pessoas ali,vou chegar mais perto")
					else:
						digitar("você chega naquela mesa...mas o percebe que niguem está sentado nela")
					while True:
						print("[1] pedir alguma bebida")
						print("[2] pedir alguma comida")
						print("[3] abrir seu inventario")
						if len(dados_taverna["frequentadores"]) >=1:
							print("[4] puxar assunto com alguem do seu lado")
						print("[0] se levantar da mesa")
						escolha_mesa_taverna = input("o que deseja fazer?")
						if escolha_mesa_taverna == "0":
							digitar("você levanta lentamente da mesa")
							break
							
						
				if canto_taverna == "3":
					menu_bau()
				if canto_taverna == "2":
					digitar("olá meu caro aprendiz...eu tenho coisas que os outros não vendem...vem cá e se acomoda-se")
					digitar("lembrando que meus itens são vendidos por diamantes...")
					while True:
						print("[1]ver estoque")
						print("[2]vender itens")
						print("[3]liquidar itens")
						print("[4]negociar e trocar")
						print("[5]conversar")
						print("[0]sair")
						escolha_comerciante_sombrio = input("o que deseja fazer?")
						if escolha_comerciante_sombrio == "0":
							digitar("adeus....ande pelas sombras por que quem brilha muito atrai a escuridão...")
							break
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
						print("eu aceitaria essa proposta mas com um porem,de todos os ganhos que tiver na batalha, 20% sera meu.")
						proposta_heroi = input("voce aceita essa proposta?(s) ou (n)")
						if proposta_heroi == "s":
							aliados["antigo_guerreiro"] += 1
							digitar("então está bom")
							digitar("no menu tera a opção de guilda,la voce pode gerenciar seus aliados")

			elif escolha_taverna == "2":
				print("Barman: O que deseja fazer?")
				print("[1] Conversar")
				print("[2] Pedir para entrar na luta")
				print("[3] upgrades da taverna")
				print("[4] comprar bebidas")
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
						
			   
					
						
						
							
						
							
							
					
				if escolha_barman == "3":
						digitar("vejo que está querendo dar uma melhorada por aqui....")
						while True:
							for upgrade, nivel in upgrades_taverna.items():
								print(f"{upgrade} nivel:{nivel}")

							escolha_upgrade_taverna = input("qual upgrade deseja fazer?[0] para sair: ")

							if escolha_upgrade_taverna == "0":
								digitar("[barman] muito obrigado meu jovem...")
								break

							if escolha_upgrade_taverna in upgrades_taverna:
								try:
									nivel = upgrades_taverna[escolha_upgrade_taverna]
									preco = dados_taverna["melhorias_taverna"][escolha_upgrade_taverna]
									if dados_jogador["moedas"] >= preco[nivel]:
										upgrades_taverna[escolha_upgrade_taverna] += 1
										dados_jogador["moedas"] -= preco[nivel]
										digitar("a taverna ficou mais bonita... e mais cara.")
									else:
										digitar("moedas insuficientes, meu jovem...")
								except KeyError:
									digitar("esse upgrade ainda não existe nos pergaminhos...")
							else:
								digitar("não conheço esse tipo de melhoria...")

								
						
				if escolha_barman == "1":
					DreamCore.npc_selecionado = "barman"

					DreamCore.iniciar_conversa()

				
					
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
				print("[5]vender itens")
				print("[6]liquidar itens")
				print("[7]conversar")
				print("[0]sair da loja")
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
				if escolha_categoria == "7":
					DreamCore.npc_selecionado = "comerciante de eldora"
					DreamCore.iniciar_conversa()
				if escolha_categoria == "0":
					digitar("[comerciante de eldora] até mais meu viajante!")
					break
		
			
		
		
			
		
		
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
if __name__ == "__main__":
	main()

