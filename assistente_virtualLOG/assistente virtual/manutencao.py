from time import sleep
import random

def marcar_manutencao():
    return None

def atuar_sobre_manutencao(acao, objeto, _):
    if acao in ["marcar", "agendar"] and objeto in ["manutenção", "conserto"]:
        
        numero = random.randint(1, 3)
        
        if numero == 1:
            print("Manutenção com André marcada com sucesso!")
        elif numero == 2:
            print("Manutenção com Fábio marcada com sucesso!")
        elif numero == 3:
            print("Manutenção com Felipe marcada com sucesso!")
        else:
            print("Todos os nossos mecanicos estão indisponíveis no momento!")
            
        sleep(5)
        
        print("Atuação sobre marcar manutenção finalizada!")
        
    elif acao in ["Desmarcar", "cancelar"] and objeto in ["Manutenção"]:
        print("A manutenção do veículo foi cancelada!")
        
    sleep(5)
        
    print("Atuação sobre marcar manutenção finalizada!")
        