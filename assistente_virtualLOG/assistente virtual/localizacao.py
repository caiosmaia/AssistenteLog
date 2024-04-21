from time import sleep
import random

def iniciar_localizacao():
    return None

def atuar_sobre_localizacao(acao, objeto, _):
    
    if acao in ["Mostrar", "Encontrar", "Localizar"] and objeto in ["carro", "veículo"]:
            
        numero = random.randint(1, 3)
        
        if numero == 1:
            print("O carro se encontra em Jequié, proximo ao destino!")
        elif numero == 2:
            print("O carro se encontra em Vitória da Conquista, na garagem.")
        elif numero == 3:
            print("O carro se encontra em Salvador, já chegou no destino!")
        else:
            print("O carro perdeu o sinal com a central e não podemos localiza-lo!")
            
        sleep(5)
        
        print("Atuação sobre mostrar localização finalizada!")