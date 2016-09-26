import _thread
import time
import socket

class Servidor():
    def __init__(self):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientes = []

    def print_clientes(self):
        if not self.clientes:
            print("Nao ha usuarios online")
        print("Usuarios online:")
        for i in self.clientes:
            print(i[1])

    def inicia_servidor(self):
        self.serversocket.bind(('', 9999))
        print("host:", socket.gethostname())
        print("porta:", self.serversocket.getsockname()[1])
        self.serversocket.listen(5)
        print("O servidor esta funcionando\n")


    # Função para as threads
    def f(self, serversocket):
        while True:
            data = ""

            clientsocket, addr = serversocket.accept()
            print("Conectei com %s" %str(addr))

            msg = "[SERVIDOR] Digite seu nome:"
            clientsocket.send(msg.encode('ascii'))

            nome = clientsocket.recv(1024).decode('ascii')
            self.clientes.append([clientsocket, nome])
            self.print_clientes()
            print()

            msg = "[CHAT] Voce entrou no chat com o nome: " + nome
            clientsocket.send(msg.encode('ascii'))

            while True:
                msg = clientsocket.recv(1024).decode('ascii')
                #print(msg.decode('ascii'))

                if not msg:
                    count = 0
                    for i in self.clientes:
                        if i[1] == nome:
                            self.clientes.pop(count)
                            break
                        count += 1
                    break

                else:
                    for i in self.clientes:
                        if i[1] != nome:
                            i[0].send(("[" + nome + "]: " + msg).encode('ascii'))

            # Encerra a conexao com o cliente
            print("conexao com", addr, "nome", nome, "encerrada", "\n")
            self.print_clientes()
            print()
            clientsocket.close()


server = Servidor()
server.inicia_servidor()

try:
    _thread.start_new_thread(server.f, (server.serversocket, ))
    _thread.start_new_thread(server.f, (server.serversocket, ))
    _thread.start_new_thread(server.f, (server.serversocket, ))
    _thread.start_new_thread(server.f, (server.serversocket, ))
    _thread.start_new_thread(server.f, (server.serversocket, ))
except:
    print ("Erro: Nao foi possivel iniciar as threads")

while 1:
    time.sleep(0.001)
