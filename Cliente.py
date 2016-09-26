import socket
import _thread
import time
import sys

Running = True

class Cliente():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conecta(self, ipserver, port):
        try:
            self.socket.connect((ipserver, port))
        except:
            print("Nao foi possivel conectar ao servidor")
            raise SystemExit

    def ouvir(self):
        while True:
            msg = self.socket.recv(1024)
            print(msg.decode('ascii'))

    def escrever(self):
        global Running
        while True:
            msg = input()
            if msg == "\q":
                self.socket.close()
                Running = False
                return
            try:
                self.socket.send(msg.encode('ascii'))
            except:
                print("[ERRO] Caracteres inválidos")
c = Cliente()

#porta = int(input("Porta: "))
c.conecta("localhost", 9999)
print("<<< [CHAT] >>>\n")

print("Para sair do programa, digite: \q")
print("\n\n")

_thread.start_new_thread(c.ouvir, ())
_thread.start_new_thread(c.escrever, ())

while Running:
    time.sleep(0.001)
