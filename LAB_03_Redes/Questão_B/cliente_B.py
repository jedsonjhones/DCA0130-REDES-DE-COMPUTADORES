# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# PROF: CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
# Aluno: Jedson Jhones Barbosa Alves
# Modificado por Jedson Jhones
# SCRIPT: Cliente de sockets TCP modificado.
#Tarefa B: Desenvolver um servidor de arquivos
#Faca as alteracoes necessarias nos codigos fonte para que o cliente envie uma solicitacao ao servidor e este responda com conteudo de um arquivo texto.
#a.	Implemente utilizando sockets TCP;
#b.	Crie um arquivo de texto simples (por exemplo: arquivo.txt) e escreva alguma informacao em 1 linha nesse arquivo;
#c.	Faca com que o servidor leia o arquivo (local) e retorne o seu conteudo para o cliente quando este digitar o comando: obter arquivo.txt. Outros comandos nao devem ser aceitos;
#d.	Use o metodo open(arquivo.txt) para abrir o arquivo solicitado e o metodo .read() para ler o seu conteudo.


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