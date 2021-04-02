from .SegmentacaoPorLimiar import SegmentacaoPorLimiar
from .SegmentacaoAdaptativa import SegmentacaoAdaptativa

import cv2 as cv


class ConfiguracaoSegmentacao:

    LIMIAR_BINARIO_BRANCO = 1
    LIMIAR_BINARIO_PRETO = 2
    METODO_SEGMENTACAO_GAUSSIAN = 3
    METODO_SEGMENTACAO_MEDIAN = 4

    def __init__(self,):
        pass

    @staticmethod
    def segmentarPorLimiar(limiar=None, intensidade=None,
                           tipoLimiarBinario=LIMIAR_BINARIO_BRANCO,
                           algoritmoOTSU=False):
        metodoBinario = ConfiguracaoSegmentacao.__metodoBinario(
            tipoLimiarBinario)
        configuracao = SegmentacaoPorLimiar(
            metodoBinario, limiar, intensidade,
            algoritmoOTSU)
        return configuracao

    @staticmethod
    def segmentarPorAdaptacao(intensidadeMaxima,
                              quantidadeVizinho, fatorSubtracao,
                              tipoBinarizacao,
                              metodoAdaptativo=METODO_SEGMENTACAO_GAUSSIAN):
        metodoBinario = ConfiguracaoSegmentacao.__metodoBinario(
            tipoBinarizacao)
        metodoAdaptativo = ConfiguracaoSegmentacao.__metodoBinario(
            metodoAdaptativo)
        return SegmentacaoAdaptativa(intensidadeMaxima, quantidadeVizinho,
                                     fatorSubtracao,
                                     metodoBinario, metodoAdaptativo)

    @staticmethod
    def __metodoBinario(tipoBinarizacao):
        if(tipoBinarizacao == ConfiguracaoSegmentacao.LIMIAR_BINARIO_BRANCO):
            return cv.THRESH_BINARY_INV
        return cv.THRESH_BINARY

    @staticmethod
    def __metodoAdaptativo(metodoAdaptativo):
        if(metodoAdaptativo == ConfiguracaoSegmentacao.
           METODO_SEGMENTACAO_GAUSSIAN):
            return cv.ADAPTIVE_THRESH_GAUSSIAN_C
        return cv.ADAPTIVE_THRESH_MEAN_C
