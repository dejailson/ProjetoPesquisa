import cv2 as cv

from ..excecao.ProcessamentoErro import ProcessamentoErro


class ConversorCor:

    HSV_MATIZ = 1
    HSV_SATURACAO = 2
    HSV_BRILHO = 3
    MENSAGEM_ERROR_EQUALIZAR = \
        'É necessário converter a imagem para tom de cinza'

    def __init__(self):
        pass

    @staticmethod
    def paraHSV(imagem, canalHsv=HSV_MATIZ):
        im = cv.cvtColor(imagem, cv.COLOR_BGR2HSV)
        matiz, saturacao, brilho = cv.split(im)
        if (canalHsv == ConversorCor.HSV_MATIZ):
            return matiz
        if (canalHsv == ConversorCor.HSV_SATURACAO):
            return saturacao
        return brilho

    @staticmethod
    def paraTomCinza(imagem):
        return cv.cvtColor(imagem,	cv.COLOR_BGR2GRAY)

    @staticmethod
    def equalizarNivelTomCinza(imagemTomCinza):
        try:
            return cv.equalizeHist(imagemTomCinza)
        except cv.error:
            raise ProcessamentoErro('ConversorCor.equalizarNivelTomCinza',
                                    ConversorCor.MENSAGEM_ERROR_EQUALIZAR)
