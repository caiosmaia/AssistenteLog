import unittest
from assistente import *

CHAMANDO_JOANA = "/misc/ifba/workspaces/inteligencia artificial/assistente virtual/audios/chamando joana.wav"
CHAMANDO_MARIA = "/misc/ifba/workspaces/inteligencia artificial/assistente virtual/audios/chamando outro nome.wav"
LIGAR_LAMPADA = "/misc/ifba/workspaces/inteligencia artificial/assistente virtual/audios/ligar lampada.wav"
DESLIGAR_LAMPADA = "/misc/ifba/workspaces/inteligencia artificial/assistente virtual/audios/desligar lampada.wav"

class TesteNomeAssistente(unittest.TestCase):
    
    def setUp(self):
        self.iniciado, self.reconhecedor, _, self.nome_do_assistente, _ = iniciar()

    def testar_01_reconhecer_nome(self):
        tem_transcricao, transcricao = processar_audio_de_teste(CHAMANDO_JOANA, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)
        self.assertEqual(tokens[0], self.nome_do_assistente)

    def testar_02_nao_reconhecer_outro_nome(self):
        tem_transcricao, transcricao = processar_audio_de_teste(CHAMANDO_MARIA, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)
        self.assertNotEqual(tokens[0], self.nome_do_assistente)

class TesteLampada(unittest.TestCase):

    def setUp(self):
        self.iniciado, self.reconhecedor, self.palavras_de_parada, self.nome_do_assistente, self.acoes = iniciar()

    def testar_01_ligar_lampada(self):
        tem_transcricao, transcricao = processar_audio_de_teste(LIGAR_LAMPADA, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)

    def testar_02_desligar_lampada(self):
        tem_transcricao, transcricao = processar_audio_de_teste(DESLIGAR_LAMPADA, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteNomeAssistente))
    testes.addTest(carregador.loadTestsFromTestCase(TesteLampada))

    executor = unittest.TextTestRunner()
    executor.run(testes)
