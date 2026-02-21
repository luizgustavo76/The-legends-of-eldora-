import shutil
import os
import zipfile 
import time
class desenhar_tela:
    def __init__(self):
        self.cols, self.rows = shutil.get_terminal_size()
        self.resolucao = self.cols * self.rows 
        self.tela = []
        self.camada1 = []
        self.camada2 = []
        self.camada3 = []
        self.camada4 = []
        self.reset = "\033[0m"
        self.meio_tela = ((self.cols / 2), (self.rows /2))
        self.canto_superior_esquerdo_tela = (0, 0)
        self.canto_inferior_esquerdo_tela = (self.cols, 0)
        self.canto_superior_direito_tela = (0, self.rows)
        self.canto_inferior_direito_tela = (self.rows, 0)
        for i in range(self.resolucao):
            self.tela.append(" ")
            self.camada1.append(" ")
            self.camada2.append(" ")
            self.camada3.append(" ")
            self.camada4.append(" ")
    def mesclar_camadas(self):
        camadas = [self.camada1, self.camada2, self.camada3, self.camada4]
        self.tela = [" " for _ in range(self.resolucao)]
        for camada in camadas:
            for i in range(self.resolucao):
                if camada[i] != " ":
                    self.tela[i] = camada[i]
    #BAF e ABAF são extensões de assets propietarias do tloe sendo baf(background ascii file) é uma linguagem de hypertext para imagens ascii estatica e abaf(animated background ascii file) para animações ascii
    def carregar_baf(self, caminho, camada):
        namespace = {}
        with open(caminho, "r") as f:
            exec(f.read(), {}, namespace)
            imagem = namespace["img"]
            linhas = imagem.splitlines()
        for y, linha in enumerate(linhas):
                for x, char in enumerate(linha):
                    if char != " ":
                        if 0 <= x < self.cols and 0 <= y < self.rows:
                            camada[y * self.cols + x] = char

    def carregar_abaf(self, caminho, camada):
        frames = []
        meta = {}

        with zipfile.ZipFile(caminho, "r") as z:
            # lê meta.txt
            with z.open("meta.txt") as f:
                for linha in f.read().decode().splitlines():
                    if "=" in linha:
                        k, v = linha.split("=", 1)
                        meta[k.strip()] = v.strip()

            ordem = meta.get("ORDER", "").split(",")

            for nome in ordem:
                nome = nome.strip()
                if nome.endswith(".baf"):
                    with z.open(nome) as f:
                        frames.append(f.read().decode())

        return frames, meta
    def renderizar_frame(self, texto_baf, camada):
        linhas = texto_baf.splitlines()

        for y, linha in enumerate(linhas):
            for x, char in enumerate(linha):
                if char != " ":
                    idx = y * self.cols + x
                    if 0 <= idx < self.resolucao:
                        camada[idx] = char
    def renderizar_frame(self, texto_baf, camada):
        linhas = texto_baf.splitlines()

        for y, linha in enumerate(linhas):
            for x, char in enumerate(linha):
                if char != " ":
                    idx = y * self.cols + x
                    if 0 <= idx < self.resolucao:
                        camada[idx] = char
    def tocar_abaf(self, caminho, camada):
        frames, meta = self.carregar_abaf(caminho, camada)

        delay = float(meta.get("DELAY", 0.2))
        loop = meta.get("LOOP", "TRUE") == "TRUE"

        while True:
            for frame in frames:
                camada[:] = [" "] * self.resolucao  # limpa camada
                self.renderizar_frame(frame, camada)
                self.mesclar_camadas()
                self.mostrar_tela()
                time.sleep(delay)

            if not loop:
                break

    def _resolver_posicao(self, valor, maximo):
        if isinstance(valor, str) and valor.endswith("%"):
            try:
                porcentagem = float(valor[:-1])
                return int((porcentagem / 100) * maximo)
            except ValueError:
                return 0
        return int(valor)

    def desenhar(self, objeto, camada, x, y, cor, direcao, curvatura):
        lista_caracteres = list(objeto)
        tamanho = len(lista_caracteres)
        curva = curvatura / 100
        x = self._resolver_posicao(x, self.cols)
        y = self._resolver_posicao(y, self.rows)

        for i in range(tamanho):
            px, py = x, y

            if direcao == "horizontal":
                px = x + i
                py = y

            elif direcao == "vertical":
                px = x
                py = y + i

            elif direcao == "diag_dir_baixo":
                px = x + i
                py = int(y + i * curva)

            elif direcao == "diag_dir_cima":
                px = x + i
                py = int(y - i * curva)


            elif direcao == "diag_esq_baixo":   
                px = x - i
                py = y + i

            elif direcao == "diag_esq_cima":    
                px = x - i
                py = y - i

            if 0 <= px < self.cols and 0 <= py < self.rows:
                idx = py * self.cols + px
                camada[idx] = cor + lista_caracteres[i] + self.reset


    def mostrar_tela(self):
        ultima_linha_usada = 0

        for i, char in enumerate(self.tela):
            if char.strip():
                ultima_linha_usada = i // self.cols

        for y in range(ultima_linha_usada + 1):
            linha = self.tela[y * self.cols:(y + 1) * self.cols]
            print("".join(linha))
