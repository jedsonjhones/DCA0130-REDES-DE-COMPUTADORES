# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# PROF: CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
# Aluno: Jedson Jhones Barbosa Alves
#
# Tarefa B: Servidor de sockets TCP modificado.
# Modificado por Jedson Jhones
# SCRIPT: Cliente de sockets TCP modificado.
#Tarefa B: Desenvolver um servidor de arquivos
#Faca as alteracoes necessarias nos codigos fonte para que o cliente envie uma solicitacao ao servidor e este responda com conteudo de um arquivo texto.
#a.	Implemente utilizando sockets TCP;
#b.	Crie um arquivo de texto simples (por exemplo: arquivo.txt) e escreva alguma informacao em 1 linha nesse arquivo;
#c.	Faca com que o servidor leia o arquivo (local) e retorne o seu conteudo para o cliente quando este digitar o comando: obter arquivo.txt. Outros comandos nao devem ser aceitos;
#d.	Use o metodo open(arquivo.txt) para abrir o arquivo solicitado e o metodo .read() para ler o seu conteudo.


# importacao das bibliotecas
from socket import * # sockets
# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  sentence = connectionSocket.recv(1024) # recebe dados do cliente
  sentence = sentence.decode('utf-8')
  if sentence == "obter arquivo.txt" :
    arquivo = "arquivo.txt"
    with open(arquivo) as ler: # abrir o arquivo
      conteudo = ler.read()
      capitalizedSentence = conteudo # texto dentro do arquivo 
      print ('Cliente %s enviou %s: %s' % (addr, sentence, capitalizedSentence))
      connectionSocket.send(capitalizedSentence.encode('utf-8')) # envia para o cliente o texto que esta dentro do arquivo txt
  else:
    modMessage = str('Esse comando nao e aceito') 
    print ('Cliente %s enviou: %s: %s' % (addr, sentence, modMessage))
    connectionSocket.send(modMessage.encode('utf-8')) # envia para o cliente o texto transformado
  connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor