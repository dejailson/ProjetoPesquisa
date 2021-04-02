import cv2 as cv


class Filtragem:

    def __init__(self):
        pass

    @staticmethod
    def linear(imagem, matrix=(1, 1)):
        return cv.blur(imagem, matrix)

    @staticmethod
    def linearMediano(imagem, intensidade):
        return cv.medianBlur(imagem, intensidade)

    @staticmethod
    def porMetodoGaussian(imagem, suavizacao, matrix=(1, 1)):
        return cv.GaussianBlur(imagem, matrix, suavizacao)

    @staticmethod
    def bilateral(imagem, tamanho, sigmarCor, sigmaEspaco):
        return cv.bilateralFilter(imagem, tamanho, sigmarCor,
                                  sigmaEspaco)
