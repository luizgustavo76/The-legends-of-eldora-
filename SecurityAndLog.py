import tkinter as tk
from tkinter import messagebox
import os
import sys
import json
import datetime
import subprocess

# ---------------- LOG BASE ----------------

base_log = {
    "data": None,
    "arquivo": "tloe.exe",
    "arquivo_path": None,
    "local_no_jogo": None,
    "ultimo_stdin": None,
    "ultimo_stdout": None,
    "erro": None,
}

LOG_FILE = "error_log.json"

# ---------------- LOG ----------------

def salvar_log(log):
    try:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(log, f, indent=4, ensure_ascii=False)
    except Exception:
        pass

# ---------------- POPUP ----------------

def mostrar_popup_erro():
    root = tk.Tk()
    root.withdraw()

    resposta = messagebox.askyesno(
        "O TLOE caiu…",
        "Algo deu errado durante a execução do TLOE.\n\n"
        "Deseja tentar abrir o jogo novamente?"
    )

    root.destroy()
    return resposta

# ---------------- EXECUTAR TLOE ----------------

def executar_tloe():
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    tloe_exe = os.path.join(base_dir, "tloe.exe")

    if not os.path.exists(tloe_exe):
        raise FileNotFoundError("tloe.exe não encontrado")

    processo = subprocess.Popen(
        [tloe_exe],
        cwd=base_dir,
        shell=False
    )

    codigo_saida = processo.wait()  # ⬅️ A PEÇA QUE FALTAVA

    return codigo_saida

# ---------------- MAIN ----------------

while True:
    try:
        exit_code = executar_tloe()

        # 0 normalmente = fechou normal
        if exit_code == 0:
            break

        raise RuntimeError(f"TLOE encerrou com código {exit_code}")

    except Exception as e:
        base_log["data"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        base_log["arquivo_path"] = os.path.abspath("tloe.exe")
        base_log["erro"] = repr(e)

        salvar_log(base_log)

        if not mostrar_popup_erro():
            sys.exit(1)
