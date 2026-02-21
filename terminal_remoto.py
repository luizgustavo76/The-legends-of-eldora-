import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("127.0.0.1", 65432))

print("=== TERMINAL REMOTO ===")
print("Digite comandos Python que afetam o TLOE em tempo real.")
print("Ctrl+C para sair.\n")

while True:
    try:
        comando = input(">>> ")
        cliente.sendall(comando.encode())

        resposta = cliente.recv(4096).decode()
        print(resposta)

    except KeyboardInterrupt:
        break

cliente.close()
