from time import sleep
import random

def gerar_relatorio():
    return None

def atuar_sobre_relatorio(acao, objeto, _):
    
    if acao in ["gerar", "fazer"] and objeto in ["relatorio"]:
            
        numero = random.randint(1, 3)
        
        if numero == 1:
            print("*Relatório do carro 01*")
            print("Veículo à caminho do destino")
            print("Motorista: Roberto Carneiro")
            print("Carro:Iveco Daily ")
        elif numero == 2:
            print("*Relatório do carro 02*")
            print("Veículo à caminho do destino")
            print("Motorista:Felix Gaspar")
            print("Carro:Renault Master ")
        elif numero == 3:
            print("*Relatório do carro 02*")
            print("Veículo à caminho do destino")
            print("Motorista:Jõao Victor")
            print("Carro:Ford Transit ")
        else:
            print("Não existe relatório no sistema! ")
            
        sleep(5)
        
        print("Atuação sobre gerar relatório finalizada!")
