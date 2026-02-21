dono_trade = False
    def menu_trade(trade_escolhida):
        SERVER = "https://luizsgustavo76.pythonanywhere.com"
        while True:
            lista_propostas = []
            print("=== Propostas Disponiveis ===")
            for propostas in lista_propostas:
                print(propostas)
            print("[1] Trocar itens")
            print("[2] Chat interno")
            print("[3] Aceitar propostas")
            print("[0] Sair")
            escolha_menu_trade = input("o que opção deseja escolher?")
            if escolha_menu_trade == "0":
                break
            if escolha_menu_trade == "1":
                mostrar_inventario()
                escolha_item_trade = input("qual item deseja trocar?se quer trocar moedas digite /moedas")
                for inventario in salvamento_dados:
                    if escolha_item_trade in inventario:
                        escolha_quantidade_itens = input(f"quantas unidades do item {escolha_item_trade} ?")
                        if salvamento_dados[escolha_item_trade] >=escolha_quantidade_itens:
                            server_adicionar_item = SERVER + "/adicionar-itens"
                            requests.post(server_adicionar_item, json={"trade_id":trade_escolhida,"item":escolha_item_trade,"quantidade":escolha_quantidade_itens,})
                            salvamento_dados[escolha_item_trade] -= escolha_quantidade_itens
                if escolha_item_trade.startswith("/moedas"):
                    pass
                            
            if escolha_menu_trade == "2":
                trade_id = trade_escolhida
                enviar_mensagens_trades(trade_id)
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
                        dono_trade = True
                    except Exception as e:
                        print(f"Um erro aconteceu: {e}")
                    break
            
            menu_trade()
    def buscar_estandes(server):
        try:
            r = requests.get(f"{server}/r-stands", timeout=5)
            return r.json()
        except Exception as e:
            print("Erro:", e)
            return []


    def ver_estandes():
        stands = buscar_estandes(SERVER)

        print("\n🏪 CENTRO MERCANTIL DE ELDORA\n")

        if not stands:
            print("Nenhum estande ativo.\n")
            return

        for s in stands:
            print("-" * 40)
            print(f"Estande: {s['nome_stand']}")
            print(f"Dono: {s['nome']}")
            print(f"Aluguel pago: {s['valor_pago']} moedas")

            if not s["itens"]:
                print("Sem itens à venda.")
            else:
                for item in s["itens"]:
                    print(f"{item['item']} | {item['preco']} moedas")

            print("-" * 40)

    def criar_estande():
        dados = {
            "nome": dados_jogador["nome"],
            "nome_stand": input("Título do estande: "),
            "itens": [],
            "valor_pago": 0
        }

        minutos = int(input("Quantos minutos deseja alugar? "))
        dados["valor_pago"] = minutos * 16
        dados_jogador["moedas"] -= dados["valor_pago"]

        while True:
            item = input("Item (/finalizar): ")
            if item == "/finalizar":
                break

            preco = int(input("Preço: "))
            dados["itens"].append({"item": item, "preco": preco})

        r = requests.post(SERVER + "/criar-id-stand", json={
            "nome": dados["nome"],
            "nome_stand": dados["nome_stand"]
        })

        dados["id_stand"] = r.json()["id_stand"]

        requests.post(SERVER + "/s-stands", json=dados)

        print("🏪 Estante criada com sucesso.")

    
    def receber_mensagens_trades(stop_event):
        ultimo_total = 0

        while not stop_event.is_set():
            try:
                r = requests.get(f"{SERVER}/r-chat", timeout=5)
                mensagens = r.json()

                if len(mensagens) > ultimo_total:
                    novas = mensagens[ultimo_total:]

                    for msg in novas:
                        if msg["mensagem"].startswith("[trade"):
                            print(f"\n[{msg['hora']}] {msg['nome']}: {msg['mensagem']}")
                        else:
                            pass


                    ultimo_total = len(mensagens)

            except Exception as e:
                print("Erro ao receber mensagens:", e)

            time.sleep(2)
    def enviar_mensagens_trades(nome):
        stop_event = threading.Event()

        thread_receber = threading.Thread(
            target=receber_mensagens_trades,
            args=(stop_event,),
            daemon=True
        )
        thread_receber.start()

        while True:
            mensagem = input("> ")
            mensagem = mensagem + "[trade]"
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

    id_trade = 0
    def finalizar_trade():
        if id_trade is None:
            print("Nenhuma trade ativa.")
            return

        try:
            r = requests.post(
                SERVER + "/finalizar-trade",
                json={"trade_id": id_trade},
                timeout=5
            )
            dados = r.json()
        except Exception as e:
            print("Erro ao finalizar trade:", e)
            return

        if dados.get("status") != "ok":
            print("Erro:", dados.get("mensagem"))
            return

        resultado = dados.get("resultado", {})

        print("\n=== TRADE FINALIZADA ===")

        for jogador, itens in resultado.items():
            print(f"{jogador} entregou:")
            for item in itens:
                print(" -", item)

        print("=======================\n")

        

        id_trade = None

    def adicionar_item_trade(item):
        if id_trade is None:
            print("Nenhuma trade ativa.")
            return

        requests.post(
            SERVER + "/adicionar-itens",
            json={"trade_id": id_trade, "item": item}
        )
    def confirmar_trade(nome):
        requests.post(
            SERVER + "/confirmar-trade",
            json={"trade_id": id_trade, "player": nome}
        )
    
    def ver_propostas():
        if id_trade is None:
            print("Nenhuma trade ativa.")
            return

        try:
            r = requests.get(
                SERVER + "/ver-trade",
                params={"trade_id": id_trade},
                timeout=5
            )
            print(r.text)
            dados = r.json()
        except Exception as e:
            print("Erro ao buscar trade:", e)
            return

        if dados.get("status") != "ok":
            print("Erro:", dados.get("mensagem"))
            return

        ofertas = dados.get("ofertas", {})
        confirmacoes = dados.get("confirmacoes", [])
        status_trade = dados.get("trade_status")

        print("\n========== TRADE ==========")

        for jogador, itens in ofertas.items():
            print(f"\n{jogador} oferece:")
            if not itens:
                print("  (nada)")
            else:
                for item in itens:
                    print(" -", item)

            if jogador in confirmacoes:
                print("   ✔ confirmou")
            else:
                print("   ⏳ aguardando")

        print("\nStatus da trade:", status_trade)
        print("===========================\n")

    def menu_trade():
        global id_trade

        while True:
            print("[2] adicionar item")
            print("[3] ver proposta")
            print("[4] confirmar trade")
            print("[0] sair")

            escolha = input("> ")

            if escolha == "0":
                break

            

            if escolha == "2":
                mostrar_inventario()
                item = input("qual item deseja trocar? ")
                if item in salvamento_dados and salvamento_dados[item] > 0:
                    adicionar_item_trade(item)
                    salvamento_dados[item] -= 1
                else:
                    print("Item inválido.")

            if escolha == "3":
                ver_propostas()

            if escolha == "4":
                confirmar_trade(nome)

                            

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
                    id_trade = trade_escolhida
                    print(f"\nVocê escolheu a trade do dono {trade_escolhida.get('criador_trade')}")
                    resposta = requests.post("https://luizsgustavo76.pythonanywhere.com/entrar-trade", json={
                    "trade_id": trade_escolhida["id"],
                    "nome": dados_jogador["nome"]
                    })
                    resposta_dados = resposta.json()
                    if resposta_dados["status"] == "ok":
                        print(f"Você entrou na trade! Integrantes agora: {resposta_dados['integrantes']}")
                        menu_trade()
                    else:
                        print(f"Erro: {resposta_dados.get('mensagem', 'Erro desconhecido')}")


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
                    if dono_trade:
                        menu_trade()
                    print("[1]criar uma mesa de trade")
                    print("[2]ver mesas de trades abertas")
                    print("[0] sair")
                    escolha_centro_mercantil_trades = input("o que deseja fazer?")
                    if escolha_centro_mercantil_trades == "1":
                        criar_mesa_trade()
                    if escolha_centro_mercantil_trades == "2":
                        ver_mesas_trades()
                        entrar_trade = input("em qual trade deseja")
                    if escolha_centro_mercantil_trades == "0":
                        break
            if escolha_centro_mercantil == "2":
                while True:
                    print("[1] Criar um Estande")
                    print("[2] Ver Estandes")
                    print("[0] sair")
                    escolha_estande = input("qual opção deseja escolher?")
                    if escolha_estande == "1":
                        criar_estande()
                    if escolha_estande == "2":
                        URL_SERVIDOR = "https://luizsgustavo76.pythonanywhere.com"
                        stands = buscar_estandes(URL_SERVIDOR)
                        ver_estandes()
                    if escolha_estande == "0":
                        break