
# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# PROF: CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
# Aluno: Jedson Jhones Barbosa Alves
# Modificado por Jedson Jhones
# SCRIPT: Cliente de sockets UDP modificado
# Tarefa A: Desenvolver um servidor de data
# Faca as alteracoes necessarias nos codigos fonte para que o cliente 
# envie uma solicitacao ao servidor e este responda com a data e o horario do sistema.
#a.	Implemente utilizando sockets UDP;
#b.	Importe a biblioteca time e utilize o metodo time.ctime() para capturar a hora;
#c.	Atente que sera necessario converter o metodo time.ctime() em string por meio do metodo str(): str(time.ctime())
#d.	O cliente deve digitar o comando: data e aguardar o servidor responder com a data. Outros comandos nao devem ser aceitos.

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = 'localhost' # ip do servidor a se conectar
serverPort = 61000 # porta a se conectar
clientSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP

message = raw_input('Digite o comando: ')
clientSocket.sendto(message.encode('utf-8'),(serverName, serverPort)) # envia mensagem para o servidor
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # recebe do servidor a resposta
print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, modifiedMessage.decode('utf-8')))
clientSocket.close() # encerra o socket do cliente