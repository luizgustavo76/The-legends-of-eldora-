from desenhar_tela import desenhar_tela
tela = desenhar_tela()
valor_x = 0
valor_y = 0
tela.desenhar(objeto="the legends of eldora", camada=tela.camada4, x="0%", y="0%", cor="\033[1;31m", direcao="diag_dir_baixo", curvatura=100)
tela.mesclar_camadas()
tela.mostrar_tela()

    