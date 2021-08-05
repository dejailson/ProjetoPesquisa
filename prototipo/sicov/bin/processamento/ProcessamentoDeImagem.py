from processamento.PreProcessadorDeImagem import PreProcessadorDeImagem as PDI 
from processamento.SegmentadorDeImagem import SegmentadorDeImagem as SDI
from .ExtracaoDeCaracteristicas.MedidasOvos import azul
from .ExtracaoDeCaracteristicas.mask import AplicarMascara as AM
from processamento.ContaOvos import conta
import cv2
class ProcessamentoDeImagem:
    def __init__(self):
        self.PDI = PDI()
        self.SDI = SDI()
        self.AM = AM()
        #self.Medidas = MO()

    def PreProcessamento(self, imagem):
        imagem = self.AM.desenharMascara(imagem)
        imagem [:, :,0] = cv2.equalizeHist(imagem[:, :,0])
        imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2BGRA)
        return imagem
        #return self.PDI.porRealce(imagem=imagem).realcarBordaPorCanny(50, 100).realcarBordaPorFiltroRealce(3, 50, (3, 3)).executar()

    def ExtrairCaracteristicas(self, imagem):
        #self.img = self.Segmentacao(imagem=imagem) 
        return azul(self.PreProcessamento(imagem=imagem))