import cv2 as cv
import numpy as np


class ElementoEstruturante:

    @staticmethod
    def retangular(quantidadeLinha, quantidadeColuna):
        matrix = ElementoEstruturante.__formarMatrix(
            quantidadeLinha, quantidadeColuna)
        return cv.getStructuringElement(cv.MORPH_RECT, matrix)

    @staticmethod
    def elipico(quantidadeLinha, quantidadeColuna):
        matrix = ElementoEstruturante.__formarMatrix(
            quantidadeLinha, quantidadeColuna)
        return cv.getStructuringElement(cv.MORPH_ELLIPSE, matrix)

    @staticmethod
    def cruzado(quantidadeLinha, quantidadeColuna):
        matrix = ElementoEstruturante.__formarMatrix(
            quantidadeLinha, quantidadeColuna)
        return cv.getStructuringElement(cv.MORPH_CROSS, matrix)

    @staticmethod
    def matrixBitOne(quantidadeLinha, quantidadeColuna):
        matrix = ElementoEstruturante.__formarMatrix(
            quantidadeLinha, quantidadeColuna)
        return np.ones(matrix, np.uint8)

    @staticmethod
    def __formarMatrix(quantidadeLinha, quantidadeColuna):
        return (quantidadeLinha, quantidadeColuna)
