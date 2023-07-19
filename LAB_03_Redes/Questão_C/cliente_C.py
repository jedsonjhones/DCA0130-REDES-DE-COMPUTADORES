
# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# PROF: CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
# Aluno: Jedson Jhones Barbosa Alves
# Modificado por Jedson Jhones
# SCRIPT: Cliente de sockets TCP modificado.
# Tarefa C: Desenvolver um acesso remoto
# Faca as alteracoes necessarias nos codigos fonte para que o cliente envie um comando para o servidor e este o execute localmente.
# a.	Implemente utilizando sockets TCP;
# b.	Importe a biblioteca subprocess e utilize o metodo subprocess.check_output(comando, shell=True, universal_newlines=True, stderr=subprocess.STDOUT)
# c.	O metodo subprocess.check_output(comando, ...) tem como parametro de entrada o comando que o cliente digitar, por exemplo: cliente digita ls ou dir e o servidor recebe e enviara o resultado para a tela do cliente;
# d.	O servidor devera aceitar qualquer comando valido no sistema, nao apenas o ls / dir.


# importacao das bibliotecas
from socket import *

# definicao das variaveis
serverName = 'localhost' # ip do servidor
serverPort = 61000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

sentence = raw_input('Digite o comando: ')
clientSocket.send(sentence.encode('utf-8')) # envia o texto para o servidor
modifiedSentence = clientSocket.recv(1024) # recebe do servidor a resposta
print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, modifiedSentence.decode('utf-8')))
clientSocket.close() # encerramento o socket do cliente