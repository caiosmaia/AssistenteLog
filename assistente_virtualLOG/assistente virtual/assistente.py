import speech_recognition as sr
from nltk import word_tokenize, corpus
from threading import Thread
from rota import *
from manutencao import *
from localizacao import *
from relatorio import *
import json

IDIOMA_CORPUS = "portuguese"
IDIOMA_FALA = "pt-BR"
CAMINHO_CONFIGURACAO = "assistente virtual\config.json"

ATUADORES = [
    {
        "nome": "rota",
        "iniciar": verificar_rota,
        "parametro_de_atuacao": None,
        "atuar": atuar_sobre_rota,
    },
    {
        "nome": "manutencao",
        "iniciar": marcar_manutencao,
        "parametro_de_atuacao": None,
        "atuar": atuar_sobre_manutencao
    },
    {
        "nome": "localizacao",
        "iniciar": iniciar_localizacao,
        "parametro_de_atuacao": None,
        "atuar": atuar_sobre_localizacao,
    },
    {
        "nome": "relatorio",
        "iniciar": gerar_relatorio,
        "parametro_de_atuacao": None,
        "atuar": atuar_sobre_relatorio
    }
]

def iniciar():
    iniciado = False
    
    reconhecedor = sr.Recognizer()

    try:    
        palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))   
        with open(CAMINHO_CONFIGURACAO, "r") as arquivo_de_configuracao:
            configuracao = json.load(arquivo_de_configuracao)

            nome_do_assistente = configuracao["nome"]
            acoes = configuracao["acoes"]

            arquivo_de_configuracao.close()

        iniciado = True
    except:
        # processar os erros do assistente (log? recuperação de falha?)
        ...
    
    for atuador in ATUADORES:
        parametro_de_atuacao = atuador["iniciar"]()
        atuador["parametro_de_atuacao"] = parametro_de_atuacao

    return iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes

def escutar_fala(reconhecedor):
    tem_fala = False
    fala = None  # Inicializa com None
    
    with sr.Microphone() as fonte_de_audio:
        reconhecedor.adjust_for_ambient_noise(fonte_de_audio)

        print("fale alguma coisa")
        try:
            fala = reconhecedor.listen(fonte_de_audio, timeout = 4)
            tem_fala = True
        except:
            # processar os erros de captura de fala
            ...

    return tem_fala, fala


def processar_audio_de_teste(audio, reconhecedor):
    tem_transcricao = False

    with sr.AudioFile(audio) as fonte_de_audio:
        fala = reconhecedor.listen(fonte_de_audio)
        try:
            transcricao = reconhecedor.recognize_google(
                fala, language=IDIOMA_FALA)
            tem_transcricao = True
        except:
            # processar os erros de captura de fala
            ...

    return tem_transcricao, transcricao.lower()

def transcrever_fala(fala, reconhecedor):
    tem_transcricao = False
    transcricao = ""  # Inicializa com uma string vazia

    try:
        transcricao = reconhecedor.recognize_google(fala, language=IDIOMA_FALA)
        tem_transcricao = True
    except:
        # Processar os erros de transcricao
        ...

    return tem_transcricao, transcricao.lower()


def tokenizar_transcricao(transcricao):
    return word_tokenize(transcricao)

def eliminar_palavras_de_parada(tokens, palavras_de_parada):
    tokens_filtrados = []
    
    for token in tokens:
        if token not in palavras_de_parada:
            tokens_filtrados.append(token)

    return tokens_filtrados

def validar_comando(tokens, nome_do_assistente, acoes):
    valido, acao, objeto = False, None, None

    if len(tokens) >= 3:
        if nome_do_assistente.strip(",") == tokens[0].strip(","):
            acao = tokens[1]
            objeto = tokens[2]

        for acao_cadastrada in acoes:
            if acao == acao_cadastrada["nome"]:
                if objeto in acao_cadastrada["objetos"]:
                    valido = True

                    break

    return valido, acao, objeto



def executar_comando(acao, objeto):
    print(f"executando a ação {acao} sobre {objeto}")
    for atuador in ATUADORES:
        parametro_de_atuacao = atuador["parametro_de_atuacao"]

        processo_paralelo = Thread(target= atuador["atuar"], args=[acao, objeto, parametro_de_atuacao])
        processo_paralelo.start()


if __name__ == "__main__":
    iniciado, reconhecedor, palavras_de_parada, nome_do_assistente, acoes = iniciar()

    if iniciado:
        while True:
            tem_fala, fala = escutar_fala(reconhecedor)
            if tem_fala:
                tem_transcricao, transcricao = transcrever_fala(fala, reconhecedor)
                if tem_transcricao:
                    tokens = tokenizar_transcricao(transcricao)
                    tokens = eliminar_palavras_de_parada(tokens, palavras_de_parada)

                    valido, acao, objeto = validar_comando(tokens, nome_do_assistente, acoes)
                    if valido:
                        executar_comando(acao, objeto)
                    else:
                        print("comando inválido, por favor tente novamente")