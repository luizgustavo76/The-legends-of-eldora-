import sys
import os
import LoginApp
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFrame,
    QScrollArea, QLineEdit
)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QObject
from PyQt6.QtWidgets import QSizePolicy
import requests
import threading
import time
from functools import partial
from PyQt6.QtGui import QPalette, QColor

class ChatSignals(QObject):
    nova_mensagem = pyqtSignal(str, bool)  # texto, eh_sua


class AetherforgerID(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aetherforger ID")
        self.setFixedSize(900, 500)
        
        self.informacoes_conta = {
            "nickname": "",
            "senha": "",
        }

        self.thread_ativa = False  # controle da thread do chat
        self.amigo_atual = None  # amigo selecionado no chat
        self.ultima_msg_id = 0  # 🆕 RASTREAR ÚLTIMA MENSAGEM
        
        # ✅ CRIAR SIGNAL PARA CHAT
        self.chat_signals = ChatSignals()
        self.chat_signals.nova_mensagem.connect(self.adicionar_mensagem_ui)

        def carregar_conta():
            if not os.path.isfile("binarios.dat"):
                return None, None

            with open("binarios.dat", "rb") as f:
                # tamanho do nickname
                tamanho_nick = int.from_bytes(f.read(4), "big")
                nickname = f.read(tamanho_nick).decode("utf-8")

                # tamanho da senha
                tamanho_senha = int.from_bytes(f.read(4), "big")
                senha = f.read(tamanho_senha).decode("utf-8")

            return nickname, senha
        nick, senha = carregar_conta()

        if nick:
            self.informacoes_conta["nickname"] = nick
            self.informacoes_conta["senha"] = senha
        else:
            LoginApp.main()

        self.init_ui()

    # ---------------- UI PRINCIPAL ----------------
    def init_ui(self):
        main_layout = QVBoxLayout(self)

        header = QLabel("Aetherforger ID")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("""
            font-size: 26px;
            font-weight: bold;
            padding: 15px;
        """)

        subtitle = QLabel("Pare, olhe e identifique-se")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("color: white;")

        main_layout.addWidget(header)
        main_layout.addWidget(subtitle)

        body_layout = QHBoxLayout()

        sidebar = QFrame()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet("""
            QFrame {
                background-color: #1e1e1e;
                border-radius: 8px;
            }
            QPushButton {
                color: white;
                background: none;
                border: none;
                padding: 12px;
                text-align: left;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #333333;
            }
        """)

        sidebar_layout = QVBoxLayout(sidebar)

        btn_amigos = QPushButton("Amigos")
        btn_conquistas = QPushButton("Conquistas")
        btn_chat = QPushButton("Chat")
        btn_conta = QPushButton("Minha Conta")
        btn_caixa_entrada = QPushButton("Caixa de entrada")
        sidebar_layout.addWidget(btn_amigos)
        sidebar_layout.addWidget(btn_conquistas)
        sidebar_layout.addWidget(btn_chat)
        sidebar_layout.addWidget(btn_conta)
        sidebar_layout.addWidget(btn_caixa_entrada)
        sidebar_layout.addStretch()

        self.content = QFrame()
        self.content.setStyleSheet("""
            QFrame {
                background-color: #f2f2f2;
                border-radius: 8px;
            }
        """)

        self.content_layout = QVBoxLayout(self.content)
        body_layout.addWidget(sidebar)
        body_layout.addWidget(self.content)
        main_layout.addLayout(body_layout)
        btn_caixa_entrada.clicked.connect(self.inbox)
        btn_chat.clicked.connect(self.selecionar_chat)
        btn_amigos.clicked.connect(self.amigos_ui)
        btn_conta.clicked.connect(self.minha_conta_ui)
    # ---------------- LIMPAR ----------------
    def limpar_content(self):
        self.thread_ativa = False
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    # ---------------- CRIAR CAIXAS ----------------
    def criar_caixa_pedido(self, nome, recado):
        caixa = QFrame()
        caixa.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 10px;
            }
        """)

        layout_caixa = QHBoxLayout(caixa)
        label_nome = QLabel(f"Pedido de amizade: {nome}, Recado: {recado}")
        label_nome.setStyleSheet("font-size: 14px; color: black;")
        layout_caixa.addWidget(label_nome)
        self.content_layout.addWidget(caixa)

    def criar_caixa(self, descrição):
        caixa = QFrame()
        caixa.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 10px;
            }
        """)

        layout_caixa = QHBoxLayout(caixa)
        label_nome = QLabel(f"{descrição}")
        label_nome.setStyleSheet("font-size: 14px; color: black;")
        layout_caixa.addWidget(label_nome)
        self.content_layout.addWidget(caixa)

    def criar_caixa_clickavel(self, descricao):
        caixa = QPushButton(descricao)
        caixa.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
                color: black;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)
        return caixa

    def criar_label(self, texto):
        label = QLabel(texto)
        label.setStyleSheet("font-size: 14px; color: black;")
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.content_layout.addWidget(label)
        return label

    def criar_entrada(self, texto):
        entrada = QLineEdit()
        entrada.setPlaceholderText(texto)
        entrada.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border-radius: 8px;
                padding: 6px;
                font-size: 14px;
                color: black;
            }
        """)
        return entrada
    def atualizar_status_amigo(self):
        if not self.amigo_atual:
            return

        SERVER = "https://aetherforgerid.pythonanywhere.com"

        try:
            r = requests.post(
                SERVER + "/status",
                json={"usuario": self.amigo_atual},
                timeout=3
            )

            if r.status_code == 200:
                status = r.json()["status"]
                self.atualizar_status_ui(status)

        except:
            self.label_status.setText("Status: offline")

    def avisar_online(self):
        SERVER = "https://aetherforgerid.pythonanywhere.com"
        requests.post(SERVER + "/ping", json={
            "usuario": self.informacoes_conta["nickname"],
            "status": "online"
        }, timeout=3)
    def iniciar_ping(self):
        def loop():
            while True:
                try:
                    SERVER = "https://aetherforgerid.pythonanywhere.com"
                    requests.post(SERVER + "/ping", json={
                        "usuario": self.informacoes_conta["nickname"],
                        "status": "online"
                    }, timeout=3)
                except:
                    pass
                time.sleep(25)

        threading.Thread(target=loop, daemon=True).start()
    def status(self):
        self.timer_status = QTimer()
        self.timer_status.timeout.connect(self.atualizar_status_amigo)
        self.timer_status.start(5000)  # a cada 5s
    def atualizar_status_ui(self, status):
        status_lower = status.lower()
        
        if status_lower == "online":
            self.label_status.setText("🟢 Online")
            self.label_status.setStyleSheet("color: #00ff7f; font-weight: bold; font-size: 12px;")
        
        elif status_lower == "jogando":
            self.label_status.setText("Jogando TLOE")
            self.label_status.setStyleSheet("color: #b266ff; font-weight: bold; font-size: 12px;")
        
        elif status_lower == "ausente":
            self.label_status.setText("🌙 Ausente")
            self.label_status.setStyleSheet("color: #FFD700; font-weight: bold; font-size: 12px;")
        
        else:  # offline
            self.label_status.setText("Offline")
            self.label_status.setStyleSheet("color: gray; font-weight: bold; font-size: 12px;")

    def minha_conta_ui(self):
        self.limpar_content()

        # ---------- Foto de perfil (opcional) ----------
        foto_label = QLabel()
        foto_label.setFixedSize(100, 100)
        foto_label.setStyleSheet("""
            background-color: #cccccc;
            border-radius: 50px;
            border: 2px solid #888888;
        """)
        foto_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        foto_label.setText("Foto")
        self.content_layout.addWidget(foto_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # ---------- Nickname ----------
        nickname_label = QLabel(f"Nickname: {self.informacoes_conta['nickname']}")
        nickname_label.setStyleSheet("font-size: 16px; color: black; font-weight: bold; margin-top: 20px;")
        nickname_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.addWidget(nickname_label)

        # ---------- Senha (mascarada) ----------
        senha_label = QLabel(f"Senha: {self.informacoes_conta['senha']}")
        senha_label.setStyleSheet("font-size: 14px; color: black; margin-bottom: 20px;")
        senha_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.addWidget(senha_label)

        # ---------- Botões ----------
        btn_alterar_senha = self.criar_botao("Alterar Senha")
        btn_logout = self.criar_botao("Logout")
        self.content_layout.addWidget(btn_alterar_senha)
        self.content_layout.addWidget(btn_logout)

        # ---------- Conexões ----------
        btn_logout.clicked.connect(lambda: self.logout())
        btn_alterar_senha.clicked.connect(lambda: self.criar_label("Funcionalidade ainda não implementada!"))

    # ---------- Função de logout ----------
    def logout(self):
        # Apaga binarios.dat e retorna pro login
        if os.path.isfile("binarios.dat"):
            os.remove("binarios.dat")
        LoginApp.main()
        self.close()

    # ---------------- SELECIONAR CHAT ----------------
    def selecionar_chat(self):
        print("CHAT CLICADO")
        self.limpar_content()
        SERVER = "https://aetherforgerid.pythonanywhere.com"
        server_login = SERVER + "/ver-amizades"
        try:
            r = requests.post(
                server_login,
                json={"nickname": self.informacoes_conta["nickname"]},
                timeout=5
            )

            if r.status_code == 200:
                dados_recebidos = r.json()
                for amigos in dados_recebidos:
                    botao_amigo = self.criar_caixa_clickavel(descricao=amigos["amigo"])
                    self.content_layout.addWidget(botao_amigo)
                    botao_amigo.clicked.connect(
                        lambda _, a=amigos["amigo"]: self.chat_menu(a)
                    )
                    self.content.repaint()
                    print("STATUS:", r.status_code)
                    print("RESPOSTA:", r.text)
        except Exception as e:
            print("Erro ao carregar chat:", e)

    # ---------------- CRIAR BOTÃO ----------------
    def criar_botao(self, texto):
        botao = QPushButton(texto)
        botao.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                color: black;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
            QPushButton:pressed {
                background-color: #e0e0e0;
            }
        """)
        return botao

    # ---------------- ENVIAR PEDIDOS ----------------
    def enviar_pedido_server(self, destinatario, recado):
        SERVER = "https://aetherforgerid.pythonanywhere.com"
        server_login = SERVER + "/enviar-pedidos-amizade"
        try:
            r = requests.post(
                server_login,
                json={
                    "remetente": self.informacoes_conta["nickname"],
                    "destinatario": destinatario,
                    "recado": recado
                },
                timeout=5
            )
            self.limpar_content()
            self.criar_label("Pedido enviado! Está preparado para serem amigos?")
        except Exception:
            pass

    def enviar_pedido_amizade(self):
        self.limpar_content()
        self.entrada_nickname = self.criar_entrada("Nickname do jogador")
        self.entrada_recado = self.criar_entrada("Coloque um recado (opcional)")
        botao = self.criar_botao("Enviar!")
        self.content_layout.addWidget(self.entrada_nickname)
        self.content_layout.addWidget(self.entrada_recado)
        self.content_layout.addWidget(botao)
        botao.clicked.connect(
            lambda: self.enviar_pedido_server(
                self.entrada_nickname.text(),
                self.entrada_recado.text()
            )
        )

    # ---------------- AMIGOS ----------------
    def amigos_ui(self):
        self.limpar_content()
        botao = self.criar_caixa_clickavel("Adicionar novo amigo!")
        self.content_layout.addWidget(botao)
        botao.clicked.connect(self.enviar_pedido_amizade)
        SERVER = "https://aetherforgerid.pythonanywhere.com"
        server_login = SERVER + "/ver-amizades"
        try:
            r = requests.post(
                server_login,
                json={"nickname": self.informacoes_conta["nickname"]},
                timeout=5
            )
            if r.status_code == 200:
                dados_recebidos = r.json()
                for amigos in dados_recebidos:
                    self.criar_caixa(amigos["amigo"])
        except Exception:
            pass

    def aceitar_amizade(self, remetente):
        SERVER = "https://aetherforgerid.pythonanywhere.com"
        server_login = SERVER + "/aceitar-amizade"
        try:
            r = requests.post(
                server_login,
                json={
                    "destinatario": self.informacoes_conta["nickname"],
                    "remetente": remetente
                },
                timeout=5
            )
            try:
                SERVER = "https://aetherforgerid.pythonanywhere.com"
                server_login = SERVER + "/remover-pedido"
                r = requests.post(
                    server_login,
                    json={
                        "destinatario": self.informacoes_conta["nickname"],
                        "remetente": remetente
                    },
                    timeout=5
                )
            except Exception:
                pass
        except Exception:
            pass

    def recusar_amigo(self):
        pass

    # ---------------- INBOX ----------------
    def inbox(self):
        self.limpar_content()
        SERVER = "https://aetherforgerid.pythonanywhere.com"
        server_login = SERVER + "/ver-inbox"
        try:
            r = requests.post(
                server_login,
                json={"nickname": self.informacoes_conta["nickname"]},
                timeout=5
            )
            if r.status_code == 200:
                dados_recebidos = r.json()
                for pedidos in dados_recebidos:
                    remetente = pedidos["remetente"]
                    recado = pedidos["recado"]
                    caixa = QFrame()
                    caixa.setStyleSheet("background-color: #000000; border-radius: 10px; padding: 10px;")
                    layout_caixa = QHBoxLayout(caixa)
                    label = QLabel(f"{remetente}: {recado}")
                    label.setStyleSheet("color: white; font-size: 14px;")
                    layout_caixa.addWidget(label)
                    botao_aceitar = QPushButton("Aceitar")
                    botao_aceitar.setStyleSheet("""
                        QPushButton {
                            background-color: #ffffff;
                            color: black;
                            border-radius: 6px;
                            padding: 6px;
                        }
                        QPushButton:hover { background-color: #3ea0ff; }
                    """)
                    botao_recusar = QPushButton("Recusar")
                    botao_recusar.setStyleSheet("""
                        QPushButton {
                            background-color: #ffffff;
                            color: black;
                            border-radius: 6px;
                            padding: 6px;
                        }
                        QPushButton:hover { background-color: #ff6666; }
                    """)
                    layout_caixa.addWidget(botao_aceitar)
                    layout_caixa.addWidget(botao_recusar)
                    self.content_layout.addWidget(caixa)

                    def remover_caixa(caixa_remover):
                        self.content_layout.removeWidget(caixa_remover)
                        caixa_remover.deleteLater()

                    def adicionar_amizade_completo(remetente, caixa_remover):
                        remover_caixa(caixa_remover)
                        self.aceitar_amizade(remetente)

                    botao_aceitar.clicked.connect(lambda _, r=remetente, c=caixa: adicionar_amizade_completo(r, c))
                    botao_recusar.clicked.connect(lambda _, c=caixa: remover_caixa(c))
        except Exception:
            pass

    # ============ CHAT - CORRIGIDO ============
    def criar_bolha(self, texto, enviada_por_voce=False):
        wrapper = QWidget()
        wrapper_layout = QHBoxLayout(wrapper)
        wrapper_layout.setContentsMargins(5, 5, 5, 5)

        bolha = QFrame()
        bolha_layout = QVBoxLayout(bolha)
        bolha_layout.setContentsMargins(12, 8, 12, 8)

        label = QLabel(texto)
        label.setWordWrap(True)
        label.setMaximumWidth(300)
        label.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)

        if enviada_por_voce:
            bolha.setStyleSheet("background-color: #DCF8C6; border-radius: 15px;")
            label.setStyleSheet("color: black;")
            wrapper_layout.addStretch()
            wrapper_layout.addWidget(bolha)
        else:
            bolha.setStyleSheet("background-color: #FFFFFF; border-radius: 15px;")
            label.setStyleSheet("color: black;")
            wrapper_layout.addWidget(bolha)
            wrapper_layout.addStretch()

        bolha_layout.addWidget(label)
        return wrapper

    def adicionar_mensagem_ui(self, texto, enviada_por_voce):
        bolha = self.criar_bolha(texto, enviada_por_voce)
        self.chat_layout.insertWidget(self.chat_layout.count() - 1, bolha)

    def ver_chat(self):
        if not self.amigo_atual:
            return
        SERVER = "https://aetherforgerid.pythonanywhere.com"
        try:
            r = requests.post(
                SERVER + "/ver-mensagens",
                json={
                    "nickname": self.informacoes_conta["nickname"],
                    "outro_usuario": self.amigo_atual,
                    "ultima_msg_id": self.ultima_msg_id
                },
                timeout=5
            )
            if r.status_code == 200:
                mensagens = r.json()
                if not mensagens:
                    return
                
                for msg in mensagens:
                    msg_id = msg.get("id", 0)
                    
                    if msg_id <= self.ultima_msg_id:
                        continue
                    
                    texto = msg["mensagem"]
                    remetente = msg.get("remetente", self.amigo_atual)
                    
                    self.ultima_msg_id = msg_id
                    
                    eh_sua = (remetente == self.informacoes_conta["nickname"])
                    
                    # ✅ USAR SIGNAL AO INVÉS DE QTimer.singleShot
                    self.chat_signals.nova_mensagem.emit(texto, eh_sua)
        except Exception as e:
            print("Erro ao buscar mensagens:", e)

    def atualizar_mensagens(self):
        while self.thread_ativa:
            self.ver_chat()
            time.sleep(3)

    def iniciar_thread_chat(self):
        if not self.thread_ativa:
            self.thread_ativa = True
            self.ultima_msg_id = 0
            thread = threading.Thread(target=self.atualizar_mensagens)
            thread.daemon = True
            thread.start()
    def pedir_status(self):
        """Requisita o status do amigo atual do servidor"""
        if not self.amigo_atual:
            return
        
        try:
            SERVER = "https://aetherforgerid.pythonanywhere.com"
            r = requests.get(SERVER + "/status/" + self.amigo_atual, timeout=3)
            
            if r.status_code == 200:
                status = r.json().get("status", "offline")
                # ✅ Usar QTimer.singleShot para atualizar na thread principal
                QTimer.singleShot(0, lambda: self.atualizar_status_ui(status))
        except:
            QTimer.singleShot(0, lambda: self.atualizar_status_ui("offline"))
    def iniciar_loop_status(self):
        """Atualiza o status do amigo a cada 8 segundos enquanto está no chat"""
        def loop():
            while self.thread_ativa and self.amigo_atual:
                try:
                    self.pedir_status()
                except:
                    pass
                time.sleep(8)  # Verificar a cada 8 segundos

        thread = threading.Thread(target=loop, daemon=True)
        thread.start()
    def chat_menu(self, amigo_selecionado):
        self.limpar_content()
        self.amigo_atual = amigo_selecionado
        
        # ----- CABEÇALHO DO CHAT -----
        header = QHBoxLayout()

        nome = QLabel(f"Conversando com {amigo_selecionado}")
        nome.setStyleSheet("font-size: 16px; font-weight: bold; color: black;")

        self.label_status = QLabel("Status: ...")
        self.label_status.setStyleSheet("color: gray;")

        header.addWidget(nome)
        header.addStretch()
        header.addWidget(self.label_status)

        self.content_layout.addLayout(header)

        # ----- ÁREA DE CHAT -----
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        self.chat_layout = QVBoxLayout(container)
        self.chat_layout.addStretch()
        scroll.setWidget(container)

        # ----- LINHA DE ENVIO -----
        linha_envio = QHBoxLayout()
        self.campo_msg = QLineEdit()
        self.campo_msg.setPlaceholderText("Digite uma mensagem...")
        btn_enviar = QPushButton("Enviar")
        btn_enviar.setStyleSheet("""
            QPushButton {
                background-color: #007AFF;
                color: white;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        linha_envio.addWidget(self.campo_msg)
        linha_envio.addWidget(btn_enviar)

        self.content_layout.addWidget(scroll)
        self.content_layout.addLayout(linha_envio)

        btn_enviar.clicked.connect(lambda: self.enviar_mensagem(self.amigo_atual))
        
        # Permite enviar com Enter
        self.campo_msg.returnPressed.connect(lambda: self.enviar_mensagem(self.amigo_atual))

        # ----- INICIAR ATUALIZAÇÕES -----
        self.iniciar_thread_chat()
        self.iniciar_loop_status()  # ✅ INICIA O LOOP DE STATUS
        
        # Atualizar status imediatamente
        self.pedir_status()

    def enviar_mensagem(self, destinatario):
        texto = self.campo_msg.text()
        if texto:
            # ❌ REMOVER ISSO:
            # self.adicionar_mensagem_ui(texto, True)
            
            self.campo_msg.clear()
            self.enviar_mensagem_server(
                self.informacoes_conta["nickname"],
                destinatario,
                texto,
                time.strftime("%Y-%m-%d %H:%M:%S")
            )

    def enviar_mensagem_server(self, remetente, destinatario, mensagem, horario):
        SERVER = "https://aetherforgerid.pythonanywhere.com"
        try:
            r = requests.post(
                SERVER + "/chat",
                json={
                    "nickname": remetente,
                    "destinatario": destinatario,
                    "mensagem": mensagem,
                    "data": horario
                },
                timeout=5
            )
            if r.status_code != 200:
                print("Erro ao enviar:", r.text)
                return False
            return True
        except Exception as e:
            print("Erro de rede:", e)
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # ===== TEMA ESCURO GLOBAL (resolve todos os fundos brancos) =====
    palette = QPalette()

    palette.setColor(QPalette.ColorRole.Window, QColor(18,18,18))
    palette.setColor(QPalette.ColorRole.Base, QColor(18,18,18))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(25,25,25))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(30,30,30))
    palette.setColor(QPalette.ColorRole.Text, QColor(220,220,220))
    palette.setColor(QPalette.ColorRole.Button, QColor(28,28,28))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(220,220,220))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(220,220,220))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(90,130,255))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255,255,255))
    palette.setColor(QPalette.ColorRole.PlaceholderText, QColor(150,150,150))

    app.setPalette(palette)

    # remove fundo branco herdado do Windows
    app.setStyle("Fusion")

    window = AetherforgerID()
    window.show()
    sys.exit(app.exec())