# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# PROF: CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
# Aluno: Jedson Jhones Barbosa Alves
# Modificado por Jedson Jhones
# Tarefa A: Desenvolver um servidor de data
# Faca as alteracoes necessarias nos codigos fonte para que o cliente 
# envie uma solicitacao ao servidor e este responda com a data e o horario do sistema.
# a. Implemente utilizando sockets UDP;
# b. Importe a biblioteca time e utilize o metodo time.ctime() para capturar a hora;
# c. Atente que sera necessario converter o metodo time.ctime() em string por meio do metodo str(): str(time.ctime())
# d. O cliente deve digitar o comando: data e aguardar o servidor responder com a data. Outros comandos nao devem ser aceitos.


# importacao das bibliotecas
from socket import * # sockets
from time import * 
# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
serverSocket.bind((serverName, serverPort)) # bind do ip do servidor com a porta
print ('Servidor UDP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    message, clientAddress = serverSocket.recvfrom(2048) # recebe do cliente
    message = message.decode('utf-8')
    if message == "data":
       modMessage = str(ctime()) #Converte hora e data
       print ('Cliente %s enviou: %s:  %s' % (clientAddress, message, modMessage))
       serverSocket.sendto(modMessage.encode('utf-8'), clientAddress)
    else:
       modMessage = str('Esse comando nao e aceito') 
       print ('Cliente %s enviou: %s: %s' % (clientAddress, message, modMessage))
       serverSocket.sendto(modMessage.encode('utf-8'), clientAddress) 
# envia a resposta para o cliente
serverSocket.close() # encerra o socket do servidor