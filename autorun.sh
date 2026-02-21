#!/bin/bash

APP="./SecurityAndLog"

# garante permissão
chmod +x "$APP"

# função para abrir terminal
abrir_terminal () {
    if command -v gnome-terminal >/dev/null 2>&1; then
        gnome-terminal -- bash -c "$APP; echo; echo 'Pressione ENTER para fechar'; read"
    elif command -v konsole >/dev/null 2>&1; then
        konsole -e bash -c "$APP; echo; echo 'Pressione ENTER para fechar'; read"
    elif command -v xfce4-terminal >/dev/null 2>&1; then
        xfce4-terminal -e "bash -c '$APP; echo; echo Pressione ENTER para fechar; read'"
    elif command -v xterm >/dev/null 2>&1; then
        xterm -hold -e "$APP"
    else
        echo "Nenhum terminal grafico encontrado."
        echo "Executando no terminal atual..."
        "$APP"
    fi
}

abrir_terminal
