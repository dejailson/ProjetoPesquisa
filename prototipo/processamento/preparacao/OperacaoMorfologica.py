import cv2 as cv

from .util.ElementoEstruturante import ElementoEstruturante


class OperacaoMorfologica:
    def __init__(self):
        pass

    @staticmethod
    def abrirCor(imagem, elementoEstruturante: ElementoEstruturante):
        return OperacaoMorfologica.__modificarMorfologia(imagem, cv.MORPH_OPEN,
                                                         elementoEstruturante)

    @staticmethod
    def fecharCor(imagem, elementoEstruturante: ElementoEstruturante):
        return OperacaoMorfologica.__modificarMorfologia(imagem,
                                                         cv.MORPH_CLOSE,
                                                         elementoEstruturante)

    @staticmethod
    def subtrairTomCinzaAberto(imagem, elementoEstruturante:
                               ElementoEstruturante):
        return OperacaoMorfologica.__modificarMorfologia(imagem,
                                                         cv.MORPH_TOPHAT,
                                                         elementoEstruturante)

    @staticmethod
    def subtrairTomCinzaFechado(imagem, elementoEstruturante:
                                ElementoEstruturante):
        return OperacaoMorfologica.__modificarMorfologia(imagem,
                                                         cv.MORPH_BLACKHAT,
                                                         elementoEstruturante)

    @staticmethod
    def aplicarGradiente(imagem, elementoEstruturante: ElementoEstruturante):
        return OperacaoMorfologica.__modificarMorfologia(imagem,
                                                         cv.MORPH_GRADIENT,
                                                         elementoEstruturante)

    @staticmethod
    def __modificarMorfologia(imagem, tipo, elementoEstruturante:
                              ElementoEstruturante):
        return cv.morphologyEx(imagem, tipo, elementoEstruturante)

    @staticmethod
    def erodir(imagem, elementoEstruturante: ElementoEstruturante, iteracao=1):
        return cv.erode(imagem, elementoEstruturante, iteracao)

    @staticmethod
    def dilatar(imagem, elementoEstruturante: ElementoEstruturante,
                iteracao=1):
        return cv.dilate(imagem, elementoEstruturante, iteracao)
