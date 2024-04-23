import unittest
from assistente import *

CHAMANDO_LOG = "C:/Users/caiom/OneDrive/Área de Trabalho/assistente_virtualLOG/assistente virtual/audios/LogNome.wav"
VERIFICAR_ROTA = "C:/Users/caiom/OneDrive/Área de Trabalho/assistente_virtualLOG/assistente virtual/audios/VerificarRota.wav"
ANALISAR_ROTA = "C:/Users/caiom/OneDrive/Área de Trabalho/assistente_virtualLOG/assistente virtual/audios/AnalisarRotas.wav"
MARCAR_MANUTENCAO = "C:/Users/caiom/OneDrive/Área de Trabalho/assistente_virtualLOG/assistente virtual/audios/MarcarManutencao.wav"
AGENDAR_MANUTENCAO = "C:/Users/caiom/OneDrive/Área de Trabalho/assistente_virtualLOG/assistente virtual/audios/AgendarManutencao.wav"
ENCONTRAR_VEICULO = "C:/Users/caiom/OneDrive/Área de Trabalho/assistente_virtualLOG/assistente virtual/audios/EncontrarVeiculo.wav"
LOCALIZAR_VEICULO = "C:/Users/caiom/OneDrive/Área de Trabalho/assistente_virtualLOG/assistente virtual/audios/LocalizarVeiculo.wav"
FAZER_RELATORIO = "C:/Users/caiom/OneDrive/Área de Trabalho/assistente_virtualLOG/assistente virtual/audios/FazerRelatorio.wav"
GERAR_RELATORIO = "C:/Users/caiom/OneDrive/Área de Trabalho/assistente_virtualLOG/assistente virtual/audios/GerarRelatorio.wav"

class TesteNomeAssistente(unittest.TestCase):
    
    def setUp(self):
        self.iniciado, self.reconhecedor, _, self.nome_do_assistente, _ = iniciar()

    def testar_01_reconhecer_nome(self):
        tem_transcricao, transcricao = processar_audio_de_teste(CHAMANDO_LOG, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)
        self.assertEqual(tokens[0], self.nome_do_assistente)

class TesteRota(unittest.TestCase):

    def setUp(self):
        self.iniciado, self.reconhecedor, self.palavras_de_parada, self.nome_do_assistente, self.acoes = iniciar()

    def testar_01_verificar_rota(self):
        tem_transcricao, transcricao = processar_audio_de_teste(VERIFICAR_ROTA, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)

    def testar_02_analisar_rota(self):
        tem_transcricao, transcricao = processar_audio_de_teste(ANALISAR_ROTA, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)

class TesteLocalizacao(unittest.TestCase):
    
    def setUp(self):
        self.iniciado, self.reconhecedor, self.palavras_de_parada, self.nome_do_assistente, self.acoes = iniciar()

    def testar_01_localizar_veiculo(self):
        tem_transcricao, transcricao = processar_audio_de_teste(LOCALIZAR_VEICULO, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)

    def testar_02_encontrar_veiculo(self):
        tem_transcricao, transcricao = processar_audio_de_teste(ENCONTRAR_VEICULO, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)
        
class TesteRelatorio(unittest.TestCase):
    
    def setUp(self):
        self.iniciado, self.reconhecedor, self.palavras_de_parada, self.nome_do_assistente, self.acoes = iniciar()

    def testar_01_gerar_relatorio(self):
        tem_transcricao, transcricao = processar_audio_de_teste(GERAR_RELATORIO, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)

    def testar_02_fazer_relatorio(self):
        tem_transcricao, transcricao = processar_audio_de_teste(FAZER_RELATORIO, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)
        
class TesteManutencao(unittest.TestCase):
    
    def setUp(self):
        self.iniciado, self.reconhecedor, self.palavras_de_parada, self.nome_do_assistente, self.acoes = iniciar()

    def testar_01_agendar_manutencao(self):
        tem_transcricao, transcricao = processar_audio_de_teste(AGENDAR_MANUTENCAO, self.reconhecedor)

        self.assertTrue(tem_transcricao)

        tokens = tokenizar_transcricao(transcricao)
        self.assertIsNotNone(tokens)

        tokens = eliminar_palavras_de_parada(tokens, self.palavras_de_parada)
        valido, _, _ = validar_comando(tokens, self.nome_do_assistente, self.acoes)
        self.assertTrue(valido)

    def testar_02_marcar_manutencao(self):
        tem_transcricao, transcricao = processar_audio_de_teste(MARCAR_MANUTENCAO, self.reconhecedor)

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
    testes.addTest(carregador.loadTestsFromTestCase(TesteLocalizacao))
    testes.addTest(carregador.loadTestsFromTestCase(TesteRelatorio))
    testes.addTest(carregador.loadTestsFromTestCase(TesteRota))
    testes.addTest(carregador.loadTestsFromTestCase(TesteManutencao))

    executor = unittest.TextTestRunner()
    executor.run(testes)
