import cv2 as cv

from .Filtragem import Filtragem


class RealcarBorda:
    REALCE_HORIZONTAL = 1
    REALCE_VERTICAL = 2

    def __init__(self):
        pass

    @staticmethod
    def porCanny(imagem, limiteMinimo, limiteMaximo):
        return cv.Canny(imagem,	limiteMinimo, limiteMinimo)

    @staticmethod
    def porFiltroRealce(imagem, fatorRealce,
                        suavizacao, dimensao=(1, 1)):
        imagemSuavizada = Filtragem.porMetodoGaussian(
            imagem, suavizacao, dimensao)
        detalhesImagem = fatorRealce * \
            cv.subtract(imagem, imagemSuavizada)
        return cv.add(imagem, detalhesImagem)

    @staticmethod
    def porDestaqueBorda(imagem):
        imagemComRealce = RealcarBorda.porLaplacian(imagem)
        return cv.subtract(imagem,	imagemComRealce)

    @staticmethod
    def porLaplacian(imagem):
        return cv.Laplacian(imagem, cv.CV_8U)

    @staticmethod
    def porSobel(imagem, tamanhoMascara,
                 tipoRealce=REALCE_HORIZONTAL):
        if (tipoRealce == RealcarBorda.REALCE_HORIZONTAL):
            return cv.Sobel(imagem,	cv.CV_8U,	1,	0, ksize=tamanhoMascara)
        return cv.Sobel(imagem,	cv.CV_8U,	0,	1, ksize=tamanhoMascara)
