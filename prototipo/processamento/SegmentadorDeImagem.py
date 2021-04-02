from .segmentacao.Segmentacao import Segmentacao
from .excecao.ProcessamentoErro import ProcessamentoErro
from .segmentacao.configuracao.ConfiguracaoSegmentacao import\
    ConfiguracaoSegmentacao as cs
from .util.ProcessadorTarefa import ProcessadorTarefa, processar


class SegmentadorDeImagem:

    def __init__(self):
        pass

    def porBinarizacao(self, imagem):
        return self.PorBinarizacao(imagem)

    class PorBinarizacao(ProcessadorTarefa):
        COR_OBJETO_MENSAGEM_ERRO = \
            'É necessário definir a cor do objeto de interesse da segmentação'
        METODO_ADAPTATIVO_MENSAGEM_ERRO = \
            'É necessário definir o método adaptativo de segmentação'

        OBJETO_INTERESSE_COR_KEY = 'objetoInteresseCor'
        LIMIAR_KEY = 'limiar'
        INTENSIDADE_KEY = 'intensidade'
        INTENSIDADE_MAXIMA_KEY = 'intensidadeMaxima'
        OTSU_KEY = 'OTSU'
        METODO_ADAPTATIVO_KEY = 'metodoAdaptativo'
        QUANTIDADE_VIZINHO_KEY = 'quantidadeVizinho'
        FATOR_SUBTRACAO_KEY = 'fatorSubtracao'

        def __init__(self, imagem):
            super().__init__()
            self.__imagem = imagem
            self._adicionarRecurso(self.OTSU_KEY, False)

        def objetoInteresseBranco(self):
            self._adicionarRecurso(
                self.OBJETO_INTERESSE_COR_KEY, cs.LIMIAR_BINARIO_BRANCO)
            return self

        def objetoInteressePreto(self):
            self._adicionarRecurso(
                self.OBJETO_INTERESSE_COR_KEY, cs.LIMIAR_BINARIO_PRETO)
            return self

        def metodoAdaptativoGaussian(self):
            self._adicionarRecurso(
                self.METODO_ADAPTATIVO_KEY, cs.METODO_SEGMENTACAO_GAUSSIAN)
            return self

        def metodoAdaptativoMedian(self):
            self._adicionarRecurso(
                self.METODO_ADAPTATIVO_KEY, cs.METODO_SEGMENTACAO_MEDIAN)
            return self

        def porLimiar(self, limiar=0, intensidade=0):
            self._adicionarRecurso(self.LIMIAR_KEY, limiar)
            self._adicionarRecurso(self.INTENSIDADE_KEY, intensidade)
            self._adicionarTarefa(self.__executarLimiarizacao)
            return self

        def porLimiarDeOTSU(self):
            self._adicionarRecurso(self.OTSU_KEY, True)
            return self.porLimiar()

        def porAdaptacao(self, intensidadeMaxima, quantidadeVizinho,
                         fatorSubtracao):
            self._adicionarRecurso(
                self.INTENSIDADE_MAXIMA_KEY, intensidadeMaxima)
            self._adicionarRecurso(
                self.QUANTIDADE_VIZINHO_KEY, quantidadeVizinho)
            self._adicionarRecurso(self.FATOR_SUBTRACAO_KEY, fatorSubtracao)
            self._adicionarTarefa(self.__executarAdaptacao)
            return self

        def executar(self):
            return processar(self._tarefas(), self.__imagem)

        def __executarLimiarizacao(self, imagem):
            self.__temCorDeInteresse()
            limiar = self._recurso(self.LIMIAR_KEY)
            intensidade = self._recurso(self.INTENSIDADE_KEY)
            objetoInteresse = self._recurso(self.OBJETO_INTERESSE_COR_KEY)
            OTSU = self._recurso(self.OTSU_KEY)

            config = cs.segmentarPorLimiar(
                limiar, intensidade, objetoInteresse, OTSU)

            return Segmentacao.porLimiar(imagem, config)

        def __executarAdaptacao(self, imagem):
            self.__temCorDeInteresse()
            self.__foiDefinidoMetodoAdaptativo()
            intensidadeMaxima = self._recurso(self.INTENSIDADE_MAXIMA_KEY)
            quantidadeVizinho = self._recurso(self.QUANTIDADE_VIZINHO_KEY)
            objetoInteresse = self._recurso(self.OBJETO_INTERESSE_COR_KEY)
            fatorSubtracao = self._recurso(self.FATOR_SUBTRACAO_KEY)
            metodoAdaptativo = self._recurso(self.METODO_ADAPTATIVO_KEY)

            config = cs.segmentarPorAdaptacao(intensidadeMaxima,
                                              quantidadeVizinho,
                                              fatorSubtracao,
                                              objetoInteresse,
                                              metodoAdaptativo)

            return Segmentacao.porAdaptacao(imagem, config)

        def __foiDefinidoMetodoAdaptativo(self):
            if (not self._existeRecurso(self.METODO_ADAPTATIVO_KEY)):
                raise ProcessamentoErro('SegmentadorDeImagem.metodoAdaptativo',
                                        self.METODO_ADAPTATIVO_MENSAGEM_ERRO)

        def __temCorDeInteresse(self):
            if (not self._existeRecurso(self.OBJETO_INTERESSE_COR_KEY)):
                raise ProcessamentoErro(
                    'SegmentadorDeImagem.corObjetoInteresse',
                    self.COR_OBJETO_MENSAGEM_ERRO)
