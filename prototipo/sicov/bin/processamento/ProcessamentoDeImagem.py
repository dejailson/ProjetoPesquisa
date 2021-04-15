from processamento.PreProcessadorDeImagem import PreProcessadorDeImagem as PDI 
from processamento.SegmentadorDeImagem import SegmentadorDeImagem as SDI 
import cv2
class ProcessamentoDeImagem:
    def __init__(self):
        self.PDI = PDI()
        self.SDI = SDI()
        pass

    def PreProcessamento(self, imagem):
        '''self.PDI.PorRealce.FATOR_REALCE_KEY = 
        self.PDI.PorRealce.LIMITE_MAXIMO_KEY = 
        self.PDI.PorRealce.LIMITE_MINIMO_KEY = 
        self.PDI.PorRealce.MATRIX_KEY = 
        self.PDI.PorRealce.SUAVIZACAO_KEY = 
        self.PDI.PorRealce.TAMANHO_MASCARA_KEY =
        self.PDI.PorRealce.TIPO_REALCE_SOBEL = '''

        self.SDI.OBJETO_INTERESSE_COR_KEY = 0.4
        self.SDI.LIMIAR_KEY = 0.4
        ret,thresh4 = cv2.threshold(imagem,127,200,cv2.THRESH_TOZERO)
       
        return self.SDI.PorBinarizacao(imagem=self.PDI.porTonalidade(imagem=imagem).equalizarNivelTomCinza().executar()).objetoInteresseBranco().executar() #(thresh4, 0.4).executar()
        #return self.PDI.porRealce(imagem=imagem).realcarBordaPorCanny(50, 100).realcarBordaPorFiltroRealce(3, 50, (3, 3)).executar()