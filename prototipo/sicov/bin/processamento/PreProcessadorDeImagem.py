from .preparacao.Filtragem import Filtragem
from .preparacao.OperacaoMorfologica import OperacaoMorfologica
from .preparacao.RealcarBorda import RealcarBorda
from .preparacao.util.ElementoEstruturante import ElementoEstruturante
from processamento.excecao.ProcessamentoErro import ProcessamentoErro
from processamento.util.ProcessadorTarefa import ProcessadorTarefa, processar
from .preparacao.ConversorCor import ConversorCor


class PreProcessadorDeImagem:
    def __init__(self):
        pass

    def porRealce(self, imagem):
        return self.PorRealce(imagem)

    def porTonalidade(self, imagem):
        return self.PorTonalidade(imagem)

    def porOperacaoMorfologica(self, imagem):
        return self.PorOperacaoMorfologica(imagem)

    def porFiltagem(self, imagem):
        return self.PorFiltragem(imagem)

    class PorFiltragem(ProcessadorTarefa):
        INTENSIDADE_KEY = 'intensidade'
        SUAVIZACAO_KEY = 'suavizacao'
        MATRIX_KEY = 'matrix'
        TAMANHO_KEY = 'tamanho'
        SIGMA_COR_KEY = 'sigmaCor'
        SIGMA_ESPACO = 'sigmaEspaco'

        def __init__(self, imagem):
            super().__init__()
            self.__imagem = imagem
            self._adicionarRecurso(self.INTENSIDADE_KEY, 1)
            self._adicionarRecurso(self.MATRIX_KEY, (1, 1))
            self._adicionarRecurso(self.SUAVIZACAO_KEY, 1)

        def matrix(self, quantidadeLinha=1, quantidadeColuna=1):
            self._adicionarRecurso(
                self.MATRIX_KEY, (quantidadeLinha, quantidadeColuna))
            return self

        def filtroLinear(self):
            self._adicionarTarefa(self.__executarFiltragemLinear)
            return self

        def filtroLinearMedio(self, intensidade=1):
            self._adicionarRecurso(self.INTENSIDADE_KEY, intensidade)
            self._adicionarTarefa(self.__executarFiltragemLinearMedio)
            return self

        def filtroGaussian(self, suavizacao=1):
            self._adicionarRecurso(self.SUAVIZACAO_KEY, suavizacao)
            self._adicionarTarefa(self.__executarFiltragemGaussian)
            return self

        def filtroBilateral(self, tamanho, sigmaCor, sigmaEspaco):
            self._adicionarRecurso(self.TAMANHO_KEY, tamanho)
            self._adicionarRecurso(self.SIGMA_COR_KEY, sigmaCor)
            self._adicionarRecurso(self.SIGMA_ESPACO, sigmaEspaco)
            self._adicionarTarefa(self.__executarFiltragemBilateral)
            return self

        def executar(self):
            return processar(self._tarefas(), self.__imagem)

        def __executarFiltragemLinear(self, imagem):
            matrix = self._recurso(self.MATRIX_KEY)
            return Filtragem.linear(imagem, matrix)

        def __executarFiltragemLinearMedio(self, imagem):
            intensidade = self._recurso(self.INTENSIDADE_KEY)
            return Filtragem.linearMediano(imagem, intensidade)

        def __executarFiltragemGaussian(self, imagem):
            matrix = self._recurso(self.MATRIX_KEY)
            suavizacao = self._recurso(self.SUAVIZACAO_KEY)
            return Filtragem.porMetodoGaussian(imagem, suavizacao, matrix)

        def __executarFiltragemBilateral(self, imagem):
            tamanho = self._recurso(self.TAMANHO_KEY)
            sigmaCor = self._recurso(self.SIGMA_COR_KEY)
            sigmaEspaco = self._recurso(self.SIGMA_ESPACO)
            return Filtragem.bilateral(
                self.__imagem, tamanho, sigmaCor, sigmaEspaco)

    class PorOperacaoMorfologica(ProcessadorTarefa):
        Elemento_Estruturante_MENSAGEM_ERRO =\
            'É necessário configurar o elemento estruturante.'
        ELEMENTO_ESTRUTURANTE_KEY = 'elementoEstruturante'
        ITERACAO_KEY = 'iteracao'

        def __init__(self, imagem):
            super().__init__()
            self.__imagem = imagem
            self._adicionarRecurso(self.ITERACAO_KEY, 1)

        def elementoEstrutrante(self, elemento: ElementoEstruturante):
            self._adicionarRecurso(self.ELEMENTO_ESTRUTURANTE_KEY, elemento)
            return self

        def iteracao(self, numeroRepeticao):
            self._adicionarRecurso(self.ITERACAO_KEY, numeroRepeticao)
            return self

        def aplicarCorrosao(self):
            self.__foiConfiguradoElementoEstruturante()
            self._adicionarTarefa(self.__executarCorrosao)
            return self

        def aplicarDilatacao(self):
            self._adicionarTarefa(self.__executarDilatacao)
            return self

        def aplicarGradiente(self):
            self._adicionarTarefa(self.__executarGradiente)
            return self

        def aplicarAberturaCor(self):
            self._adicionarTarefa(self.__executarAberturaCor)
            return self

        def aplicarSubtracaoTomCinzaAberto(self):
            self._adicionarTarefa(self.__executarSubtracaoTomCinzaAberto)
            return self

        def aplicarSubtracaoTomCinzaFechado(self):
            self._adicionarTarefa(self.__executarSubtracaoTomCinzaFechado)
            return self

        def aplicarFechamentoCor(self):
            self._adicionarTarefa(self.__executarFechamento)
            return self

        def executar(self):
            return processar(self._tarefas(), self.__imagem)

        def __executarCorrosao(self, imagem):
            try:
                elemento = self._recurso(self.ELEMENTO_ESTRUTURANTE_KEY)
                iteracao = self._recurso(self.ITERACAO_KEY)
                return OperacaoMorfologica.erodir(imagem, elemento, iteracao)
            except KeyError:
                raise ProcessamentoErro(
                    'PreProcessadorDeImagem.porOperacaoMorfologica',
                    self.Elemento_Estruturante_MENSAGEM_ERRO)

        def __executarDilatacao(self, imagem):
            try:
                elemento = self._recurso(self.ELEMENTO_ESTRUTURANTE_KEY)
                iteracao = self._recurso(self.ITERACAO_KEY)
                return OperacaoMorfologica.dilatar(self.__imagem, elemento,
                                                   iteracao)
            except KeyError:
                raise ProcessamentoErro(
                    'PreProcessadorDeImagem.porOperacaoMorfologica',
                    self.Elemento_Estruturante_MENSAGEM_ERRO)

        def __executarGradiente(self, imagem):
            try:
                elemento = self._recurso(self.ELEMENTO_ESTRUTURANTE_KEY)
                return OperacaoMorfologica.aplicarGradiente(imagem, elemento)
            except KeyError:
                raise ProcessamentoErro(
                    'PreProcessadorDeImagem.porOperacaoMorfologica',
                    self.Elemento_Estruturante_MENSAGEM_ERRO)

        def __executarAberturaCor(self, imagem):
            try:
                elemento = self._recurso(self.ELEMENTO_ESTRUTURANTE_KEY)
                return OperacaoMorfologica.abrirCor(imagem, elemento)
            except KeyError:
                raise ProcessamentoErro(
                    'PreProcessadorDeImagem.porOperacaoMorfologica',
                    self.Elemento_Estruturante_MENSAGEM_ERRO)

        def __executarSubtracaoTomCinzaAberto(self, imagem):
            try:
                elemento = self._recurso(self.ELEMENTO_ESTRUTURANTE_KEY)
                return OperacaoMorfologica.subtrairTomCinzaAberto(imagem,
                                                                  elemento)
            except KeyError:
                raise ProcessamentoErro(
                    'PreProcessadorDeImagem.porOperacaoMorfologica',
                    self.Elemento_Estruturante_MENSAGEM_ERRO)

        def __executarSubtracaoTomCinzaFechado(self, imagem):
            try:
                elemento = self._recurso(self.ELEMENTO_ESTRUTURANTE_KEY)
                return OperacaoMorfologica.subtrairTomCinzaFechado(imagem,
                                                                   elemento)
            except KeyError:
                raise ProcessamentoErro(
                    'PreProcessadorDeImagem.porOperacaoMorfologica',
                    self.Elemento_Estruturante_MENSAGEM_ERRO)

        def __executarFechamento(self, imagem):
            try:
                elemento = self._recurso(self.ELEMENTO_ESTRUTURANTE_KEY)
                return OperacaoMorfologica.fecharCor(imagem, elemento)
            except KeyError:
                raise ProcessamentoErro(
                    'PreProcessadorDeImagem.porOperacaoMorfologica',
                    self.Elemento_Estruturante_MENSAGEM_ERRO)

    class PorTonalidade(ProcessadorTarefa):
        HSV_KEY = 'HSV'

        def __init__(self, imagem):
            super().__init__()
            self.__imagem = imagem

        def equalizarNivelTomCinza(self):
            self._adicionarTarefa(self.__executarEqualizadorNivelTomCinza)
            return self

        def gerarTomCinza(self):
            self._adicionarTarefa(self.__executarGeracaoTomCinza)
            return self

        def gerarTomCinzaPelaMatiz(self):
            self._adicionarRecurso(self.HSV_KEY, ConversorCor.HSV_MATIZ)
            self._adicionarTarefa(self.__executarTomCinzaPorCanal)
            return self

        def gerarTomCinzaPelaSaturacao(self):
            self._adicionarRecurso(self.HSV_KEY, ConversorCor.HSV_SATURACAO)
            self._adicionarTarefa(self.__executarTomCinzaPorCanal)
            return self

        def gerarTomCinzaPeloBrilho(self):
            self._adicionarRecurso(self.HSV_KEY, ConversorCor.HSV_BRILHO)
            self._adicionarTarefa(self.__executarTomCinzaPorCanal)
            return self

        def executar(self):
            return processar(self._tarefas(), self.__imagem)

        def __executarEqualizadorNivelTomCinza(self, imagem):
            return ConversorCor.equalizarNivelTomCinza(imagem)

        def __executarGeracaoTomCinza(self, imagem):
            return ConversorCor.paraTomCinza(imagem)

        def __executarTomCinzaPorCanal(self, imagem):
            canal = self._recurso(self.HSV_KEY)
            return ConversorCor.paraHSV(imagem, canal)

    class PorRealce(ProcessadorTarefa):
        LIMITE_MINIMO_KEY = 'limiteMinimo'
        LIMITE_MAXIMO_KEY = 'limiteMaximo'
        MATRIX_KEY = 'matrix'
        FATOR_REALCE_KEY = 'fatorRealce'
        SUAVIZACAO_KEY = 'suavizacao'
        TAMANHO_MASCARA_KEY = 'tamanhoMascara'
        TIPO_REALCE_SOBEL = 'tipoRealceSobel'

        def __init__(self, imagem):
            super().__init__()
            self.__imagem = imagem

        def realcarBordaPorCanny(self, limiteMinimo=1, limiteMaxima=1):
            self._adicionarRecurso(self.LIMITE_MINIMO_KEY, limiteMinimo)
            self._adicionarRecurso(self.LIMITE_MAXIMO_KEY, limiteMaxima)
            self._adicionarTarefa(self.__executarRealcePorCanny)
            return self

        def realcarBordaPorDestaqueBorda(self):
            self._adicionarTarefa(self.__executarRealcePorDestaqueBorda)
            return self

        def realcarBordaPorFiltroRealce(self, fatorRealce=1, suavizacao=1,
                                        matrix=1):
            self._adicionarRecurso(self.FATOR_REALCE_KEY, fatorRealce)
            self._adicionarRecurso(self.SUAVIZACAO_KEY, suavizacao)
            self._adicionarRecurso(self.MATRIX_KEY, matrix)
            self._adicionarTarefa(self.__executarRealcePorFiltroRealce)
            return self

        def realcarBordaPorLaplacian(self):
            self._adicionarTarefa(self.__executarRealcePorLaplacian)
            return self

        def realcarBordaPorSobelHorizontal(self, tamanhoMascara):
            self._adicionarRecurso(self.TAMANHO_MASCARA_KEY, tamanhoMascara)
            self._adicionarRecurso(self.TIPO_REALCE_SOBEL, RealcarBorda
                                   .REALCE_HORIZONTAL)
            self._adicionarTarefa(self.__realcarBordaPorSobel)
            return self

        def realcarBordaPorSobelVertical(self, tamanhoMascara):
            self._adicionarRecurso(self.TAMANHO_MASCARA_KEY, tamanhoMascara)
            self._adicionarRecurso(self.TIPO_REALCE_SOBEL, RealcarBorda
                                   .REALCE_VERTICAL)
            self._adicionarTarefa(self.__realcarBordaPorSobel)
            return self

        def executar(self):
            return processar(self._tarefas(), self.__imagem)

        def __executarRealcePorCanny(self, imagem):
            limiteMinimo = self._recurso(self.LIMITE_MINIMO_KEY)
            limiteMaxima = self._recurso(self.LIMITE_MAXIMO_KEY)
            return RealcarBorda.porCanny(imagem, limiteMinimo, limiteMaxima)

        def __executarRealcePorDestaqueBorda(self, imagem):
            return RealcarBorda.porDestaqueBorda(imagem)

        def __executarRealcePorFiltroRealce(self, imagem):
            fatorRealce = self._recurso(self.FATOR_REALCE_KEY)
            suavizacao = self._recurso(self.SUAVIZACAO_KEY)
            matrix = self._recurso(self.MATRIX_KEY)
            return RealcarBorda.porFiltroRealce(imagem,
                                                fatorRealce,
                                                suavizacao,
                                                matrix)

        def __executarRealcePorLaplacian(self, imagem):
            return RealcarBorda.porLaplacian(imagem)

        def __realcarBordaPorSobel(self, imagem):
            tamanhoMascara = self._recurso(self.TAMANHO_MASCARA_KEY)
            tipoRealce = self._recurso(self.TIPO_REALCE_SOBEL)
            return RealcarBorda.porSobel(imagem, tamanhoMascara, tipoRealce)
