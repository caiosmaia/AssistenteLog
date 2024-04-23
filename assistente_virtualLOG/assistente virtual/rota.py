from time import sleep
import random

def verificar_rota():
    return None

def atuar_sobre_rota(acao, objeto, _):
    if acao in ["verificar", "analisar"] and objeto in ["rota"]:
        numero = random.randint(1, 3)
        
        if numero == 1:
            print("A rota desejada está livre e tranquila para viagem")
        elif numero == 2:
            print("A rota desejada está bloqueada para viagem")
        elif numero == 3:
            print("A rota desejada está congestionada para viagem")
        else:
            print("Ainda não foi gerada uma rota para essa entrega!")
            
        sleep(5)
        
        print("Atuação sobre verificar a rota finalizada!")
