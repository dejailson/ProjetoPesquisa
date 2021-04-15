import cv2 as cv


class SegmentacaoPorLimiar:
    def __init__(self, tipoLimiarBinario, limiar=None,
                 intensidade=None, algoritmoOTSU=False):
        if (limiar is not None) and (intensidade is not None):
            self.__limiar = limiar
            self.__intensidade = intensidade
        self.__tipoLimiarBinario = tipoLimiarBinario
        self.__metodo = self.__aplicarOTSU(algoritmoOTSU)

    def __aplicarOTSU(self, aplicar):
        if (aplicar):
            self.__limiar = 0
            self.__intensidade = 255
            return self.__tipoLimiarBinario + cv.THRESH_OTSU
        return self.__tipoLimiarBinario

    def getLimiar(self):
        return self.__limiar

    def getIntensidade(self):
        return self.__intensidade

    def getMetodoBinario(self):
        return self.__metodo
