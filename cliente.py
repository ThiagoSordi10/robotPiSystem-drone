import socket
import json
import threading
import time
from raspberryDB import get_raspberry, salvar_raspberry
from estacaoDB import salvar_estacoes
from comandoDB import salvar_comando
from alchemy_encoder import AlchemyEncoder
from estacao_scanner import procura_estacao

raspberry = get_raspberry()
if raspberry is None:
    estacaoId = procura_estacao(None, None)
#apagar estacoes salvas
s = socket.socket()
host = '192.168.1.11' #ip server
port = 9000

s.connect((host, port))
s.recv(1024)

def init():
    while True:
        leitura()

def worker(mensagem, comando):
    # executar comando - verificar a estação atual do raspberry, verificar o menor caminho
    raspberry = get_raspberry()
    if raspberry.estacaoId == comando.estacao_id:
        raspberryJson = json.dumps(raspberry, cls=AlchemyEncoder)
        raspberryJson = '{"raspberrySync": ' + raspberryJson + '}'
        escrita(raspberryJson)
    else:
        estacaoId = procura_estacao(comando.estacao_id, raspberry)
        raspberry.estacao_id = estacaoId
        raspberryJson = json.dumps(raspberry, cls=AlchemyEncoder)
        raspberryJson = '{"raspberrySync": ' + raspberryJson + '}'
        escrita(raspberryJson)

def leitura():
    print('Recebendo do server')
    while(True):
        mensagem = s.recv(4096)
        print(mensagem)
        mensagemJson = json.loads(mensagem)
        if('comandoSync' in mensagemJson):
            salvaComando(mensagemJson)
        if('raspberrySync' in mensagemJson): #Salva raspberry vindo do server
            salvarRaspberry(mensagemJson)
            escrita('{"getEstacoes": ' + 1 + '}') #Busca estações do server
        if('estacoesSync' in mensagemJson): #Salva estacoes
            salvarEstacoes(mensagemJson)


def escrita(mensagem):
    try:
        s.sendall(mensagem)
    except socket.error:
        print('Send failed')

def salvarRaspberry(mensagemJson):
    estacaoJson = mensagemJson['estacao']
    empresaJson = mensagemJson['empresa']
    salvar_raspberry(mensagemJson['id'], mensagemJson['nome'],
           empresaJson['id'], estacaoJson['id'])

def salvarEstacoes(mensagemJson):
    for elemento in mensagemJson:
        empresaJson = elemento['empresa']
        salvar_estacoes(elemento['id'], elemento['nome'], empresaJson['id'],
                        elemento['posicao'])

def salvaComando(mensagemJson):
    estacaoJson = mensagemJson['estacao']
    comando = salvar_comando(mensagemJson['id'], estacaoJson['id'])
    t = threading.Thread(target=worker, args=("comando sendo executado", comando,))
    t.start()



def main():
    if raspberry is None: #Raspberry primeira execução manda estação pra descobrir empresa e cadastrar ja salvar raspberry na estação
        estacaoJson = '{"estacaoId": '+estacaoId+'}'
        escrita(estacaoJson)
    else: #Vai mandar o raspberry salvo para buscar alterações no servidor
        raspberryJson = json.dumps(raspberry, cls=AlchemyEncoder)
        raspberryJson = '{"raspberrySync": '+raspberryJson+'}'
        escrita(raspberryJson)
    init()

main()