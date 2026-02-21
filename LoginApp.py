def main():
    import customtkinter as ctk
    import requests
    import json
    import time
    import sys
    # ===== CONFIG =====
    SERVER = "https://aetherforgerid.pythonanywhere.com"
    def login_json(nickname, senha):
        with open("binarios.dat", "wb") as f:
            nick_bytes = nickname.encode("utf-8")
            senha_bytes = senha.encode("utf-8")

            # tamanho do nickname (4 bytes)
            f.write(len(nick_bytes).to_bytes(4, "big"))
            f.write(nick_bytes)

            # tamanho da senha (4 bytes)
            f.write(len(senha_bytes).to_bytes(4, "big"))
            f.write(senha_bytes)
        sys.exit(0)

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("400x500")
    app.title("Aetherforger ID")

    # ===== FRAME PRINCIPAL =====
    frame = ctk.CTkFrame(app, corner_radius=18)
    frame.pack(expand=True, fill="both", padx=20, pady=20)

    # ===== UTIL =====
    def limpar_frame():
        for widget in frame.winfo_children():
            widget.destroy()

    # ===== MENU INICIAL =====
    def menu_inicial():
        limpar_frame()

        ctk.CTkLabel(
            frame,
            text="Aetherforger ID",
            font=("Arial", 26, "bold")
        ).pack(pady=20)

        ctk.CTkButton(
            frame,
            text="Fazer Login",
            command=tela_login
        ).pack(pady=10)

        ctk.CTkButton(
            frame,
            text="Criar Conta",
            command=tela_cadastro
        ).pack(pady=10)

    # ===== LOGIN=====
    def tela_login():
        limpar_frame()

        ctk.CTkLabel(frame, text="Login", font=("Arial", 22)).pack(pady=15)

        entrada_nick = ctk.CTkEntry(frame, placeholder_text="Nickname")
        entrada_nick.pack(pady=8)

        entrada_senha = ctk.CTkEntry(frame, placeholder_text="Senha", show="*")
        entrada_senha.pack(pady=8)

        status = ctk.CTkLabel(frame, text="")
        status.pack(pady=5)

        def confirmar_login():
            nickname = entrada_nick.get().strip()
            senha = entrada_senha.get().strip()
            server_login = SERVER + "/login"

            try:
                r = requests.post(
                    server_login,
                    json={
                        "nickname": nickname,
                        "senha": senha
                    },
                    timeout=5
                )

                if r.status_code == 200:
                    status.configure(
                        text=f"Bem Vindo de volta {nickname}!",
                        text_color="#00FF8C"
                    )
                    login_json(nickname, senha)
                    
                else:
                    status.configure(
                        text=f"Status {r.status_code}: {r.text}",
                        text_color="red"
                    )

            except Exception:
                status.configure(
                    text="Servidor indisponivel ou fora do ar",
                    text_color="red"
                )

        ctk.CTkButton(frame, text="Entrar", command=confirmar_login).pack(pady=10)

    ctk.CTkButton(
        frame,
        text="Voltar",
        fg_color="#444444",
        command=menu_inicial
    ).pack(pady=5)

    # ===== CADASTRO =====
    def tela_cadastro():
        limpar_frame()

        ctk.CTkLabel(
            frame,
            text="Criar Conta",
            font=("Arial", 22)
        ).pack(pady=15)

        entrada_nick = ctk.CTkEntry(frame, placeholder_text="Nickname")
        entrada_email = ctk.CTkEntry(frame, placeholder_text="Email")
        entrada_senha = ctk.CTkEntry(frame, placeholder_text="Senha", show="*")
        entrada_confirmar = ctk.CTkEntry(frame, placeholder_text="Confirmar senha", show="*")

        entrada_nick.pack(pady=5)
        entrada_email.pack(pady=5)
        entrada_senha.pack(pady=5)
        entrada_confirmar.pack(pady=5)

        status = ctk.CTkLabel(frame, text="")
        status.pack(pady=5)

        def confirmar_cadastro():
            nickname = entrada_nick.get().strip()
            email = entrada_email.get().strip()
            senha = entrada_senha.get()
            confirmar = entrada_confirmar.get()

            if not nickname or not email or not senha:
                status.configure(text="Preencha todos os campos", text_color="red")
                return

            if senha != confirmar:
                status.configure(text="As senhas não coincidem", text_color="red")
                return

            try:
                r = requests.post(
                    SERVER + "/criar-usuario",
                    json={
                        "nickname": nickname,
                        "email": email,
                        "senha": senha
                    },
                    timeout=5
                )

                if r.status_code == 200:
                    status.configure(
                        text="Conta criada com sucesso!",
                        text_color="green"
                    )
                else:
                    status.configure(
                        text=f"Status {r.status_code}: {r.text}",
                        text_color="red"
                    )


            except Exception as e:
                status.configure(
                    text="Servidor indisponível",
                    text_color="red"
                )

        ctk.CTkButton(
            frame,
            text="Confirmar Cadastro",
            command=confirmar_cadastro
        ).pack(pady=10)

        ctk.CTkButton(
            frame,
            text="Voltar",
            fg_color="#444444",
            command=menu_inicial
        ).pack(pady=5)

    # ===== START =====
    menu_inicial()
    app.mainloop()


if __name__ == "__main__":
    main()
