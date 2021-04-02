class SegmentacaoAdaptativa:
    def __init__(self, intensidadeMaxima, quantidadeVizinho, fatorSubtracao,
                 tipoBinarizacao, metodoAdaptativo):
        self.__intensidadeMaxima = intensidadeMaxima
        self.__quantidadeVizinho = quantidadeVizinho
        self.__fatorSubtracao = fatorSubtracao
        self.__metodoAdaptativo = metodoAdaptativo
        self.__tipoBinarizacao = tipoBinarizacao

    def getIntensidadeMaxima(self):
        return self.__intensidadeMaxima

    def getQuantidadeVizinho(self):
        return self.__quantidadeVizinho

    def getFatorSubtracao(self):
        return self.__fatorSubtracao

    def getMetodoAdaptativo(self):
        return self.__metodoAdaptativo

    def getMetodoBinarizacao(self):
        return self.__tipoBinarizacao
