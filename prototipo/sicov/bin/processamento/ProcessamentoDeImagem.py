import numpy as np
from PIL import Image, ImageTk
from processamento.PreProcessadorDeImagem import PreProcessadorDeImagem as PDI 
from processamento.SegmentadorDeImagem import SegmentadorDeImagem as SDI
from .ExtracaoDeCaracteristicas.MedidasOvos import MedidasOvos as MO
from .ExtracaoDeCaracteristicas.mask import AplicarMascara as AM
from PIL import Image
import cv2
import time
class ProcessamentoDeImagem:
    def __init__(self):
        self.PDI = PDI()
        self.SDI = SDI()
        self.AM = AM()
        self.Medidas = MO()

    def PreProcessamento(self, imagem):
        #imagem = cv2.GaussianBlur(imagem, (5, 5))
        imagem = self.AM.desenharMascara(imagem)
        imagem [:, :,0] = cv2.equalizeHist(imagem[:, :,0])
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2BGRA)
        
        return imagem
        #return self.PDI.porRealce(imagem=imagem).realcarBordaPorCanny(50, 100).realcarBordaPorFiltroRealce(3, 50, (3, 3)).executar()

    def ExtrairCaracteristicas(self, imagem):
        tempo_inicial = time.time()
        self.imge = Image.fromarray(imagem)
        self.basewidth = 400
        self.wpercent = (self.basewidth/float(self.imge.size[0]))
        self.hsize = int((float(self.imge.size[1])*float(self.wpercent)))
        imagem = self.imge.resize((self.basewidth,self.hsize), Image.ANTIALIAS)
        imagem = np.array(imagem)
        i, lista = self.Medidas.PorScikitECv2(self.PreProcessamento(imagem=imagem)).cobrirCirculos() 
        tempo = time.time() - tempo_inicial
        return i, lista, tempo