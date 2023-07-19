# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# PROF: CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
# Aluno: Jedson Jhones Barbosa Alves
#
# Tarefa B: Servidor de sockets TCP modificado.
# Modificado por Jedson Jhones
# SCRIPT: Cliente de sockets TCP modificado.
# Tarefa C: Desenvolver um acesso remoto
# Faca as alteracoes necessarias nos codigos fonte para que o cliente envie um comando para o servidor e este o execute localmente.
# a.	Implemente utilizando sockets TCP;
# b.	Importe a biblioteca subprocess e utilize o metodo subprocess.check_output(comando, shell=True, universal_newlines=True, stderr=subprocess.STDOUT)
# c.	O metodo subprocess.check_output(comando, ...) tem como parametro de entrada o comando que o cliente digitar, por exemplo: cliente digita ls ou dir e o servidor recebe e enviara o resultado para a tela do cliente;
# d.	O servidor devera aceitar qualquer comando valido no sistema, nao apenas o ls / dir.

# importacao das bibliotecas
from socket import * # sockets
from subprocess import *
import socket
import subprocess

def func(connectionSocket):
  comando = connectionSocket.recv(1024)
  process =  subprocess.check_output(comando.decode('utf-8'), shell=True, universal_newlines=True, stderr=subprocess.STDOUT)
  connectionSocket.sendall(process.encode('utf-8'))

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket.socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  sentence = connectionSocket.recv(1024) # recebe dados do cliente
  func(connectionSocket) #chama a funcao

connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor