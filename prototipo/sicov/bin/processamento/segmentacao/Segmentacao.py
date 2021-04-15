import cv2 as cv

from .configuracao.SegmentacaoAdaptativa import SegmentacaoAdaptativa
from .configuracao.SegmentacaoPorLimiar import SegmentacaoPorLimiar


class Segmentacao:
    def __init__(self):
        pass

    @staticmethod
    def porAdaptacao(imagem, configuracaoAdaptativa:
                     SegmentacaoAdaptativa):
        imagemSegmentada = cv.adaptiveThreshold(imagem,
                                                configuracaoAdaptativa.
                                                getIntensidadeMaxima(),
                                                configuracaoAdaptativa
                                                .getMetodoAdaptativo(),
                                                configuracaoAdaptativa
                                                .getMetodoBinarizacao(),
                                                configuracaoAdaptativa
                                                .getQuantidadeVizinho(),
                                                configuracaoAdaptativa
                                                .getFatorSubtracao())
        return imagemSegmentada

    @staticmethod
    def porLimiar(imagem, configuracao: SegmentacaoPorLimiar):
        _, imagemSegmentada = cv.threshold(
            imagem, configuracao.getLimiar(), configuracao.getIntensidade(),
            configuracao.getMetodoBinario())
        return imagemSegmentada
