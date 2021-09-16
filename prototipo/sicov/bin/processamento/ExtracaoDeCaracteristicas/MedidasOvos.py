from util.modelo.ovulo import Ovulo
import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image

from skimage.draw import ellipse
from util.GerenciadorRecurso import GerenciadorRecurso as gr
from processamento.SegmentadorDeImagem import SegmentadorDeImagem as sdi
from skimage.transform import rotate
from processamento.preparacao.util.ElementoEstruturante import\
    ElementoEstruturante
#from ContaOvos import conta
from skimage.measure import label, regionprops
from processamento.ExtracaoDeCaracteristicas.mask import AplicarMascara as AM
from processamento.util.ProcessadorTarefa import ProcessadorTarefa, processar
#from imutils import perspective
#from imutils import contours
#import imutils

class MedidasOvos:
    def __init__(self):
        self.mascara = AM()

    def PorScikitECv2(self, img):
        return self.ScikitECv2(img)

    class ScikitECv2(ProcessadorTarefa):
        def __init__(self, imagem):
            super().__init__()
            self.__imagem = imagem
            self.recurso = gr()
            self.ListaCoordenadas = []
            

        def executar(self):
            return processar(self._tarefas(), self.__imagem)

        def tamanho(self, x1, x2, y1, y2):
            # 0 = x; 1 = y; 2 = raio 
            catetoAdj = x2 - x1
            catetoOps = y2 - y1
            tang = math.sqrt((catetoAdj**2) + (catetoOps**2))
            return tang

        def dimenssoesImagem(self, img):
            return img.shape[:2]

            

        def regioesImagem(self, img):
            label_img = label(img)
            return regionprops(label_img)

        def analiseReta(self, img):
            cont = 0
            label_img = label(img)
            regions = regionprops(label_img)
            self.listaOvos = []
            largura, altura = img.shape[:2]

            fig, ax = plt.subplots()
            ax.imshow(img, cmap=plt.cm.gray)

            for props in regions:
                y0, x0 = props.centroid
                orientation = props.orientation
                x1 = x0 + math.cos(orientation) * 0.5 * props.minor_axis_length
                y1 = y0 - math.sin(orientation) * 0.5 * props.minor_axis_length
                x2 = x0 - math.sin(orientation) * 0.5 * props.major_axis_length
                y2 = y0 - math.cos(orientation) * 0.5 * props.major_axis_length
                raio1 = self.tamanho(x0, x1, y0, y1)
                raio2 = self.tamanho(x0, x2, y0, y2)
                if raio1 >= 5 and raio1 <= 25 and raio2 >= 5 and raio2 <= 25:
                    listaR = self.recurso.getObjetoPadrao()
                    alturaReal = listaR[1]
                    alturaPixel = self.ListaCoordenadas[2]*2
                    raio1 = (alturaReal * raio1) / alturaPixel
                    raio2 = (alturaReal * raio2) / alturaPixel
                    print(f'Raio1 = {raio1} | Raio2 = {raio2}')
                    egge = Ovulo(raio1, raio2)
                    self.listaOvos.append(egge)
                    ax.plot((x0, x1), (y0, y1), '-r', linewidth=2.5)
                    ax.plot((x0, x2), (y0, y2), '-r', linewidth=2.5)
                    ax.plot(x0, y0, '.g', markersize=15)
                    #cv2.line(self.__imagem,(int(x0),int(y0)), (int(x1), int(y1)), (255,255,255),2)


                    minr, minc, maxr, maxc = props.bbox
                    bx = (minc, maxc, maxc, minc, minc)
                    by = (minr, minr, maxr, maxr, minr)
                    ax.plot(bx, by, '-b', linewidth=2.5)
                    ax.plot(bx, by, '-b', linewidth=2.5)

            ax = 0    
            return self.__imagem, self.listaOvos
        
        def identificarCirculos(self, img):
            return np.uint16(np.around(cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,
                            param1=50,param2=12,minRadius=0,maxRadius=20)))


        def cobrirCirculos(self):
            img = self.__imagem 
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

            kernel = np.ones((5,5),np.uint8)

            erode = cv2.erode(threshold,kernel,iterations = 1)
            segmentar = sdi()
            
            erode = segmentar.porBinarizacao(erode)\
                .objetoInteresseBranco()\
                .metodoAdaptativoMedian()\
                .porAdaptacao(200, 3, 6)\
                .executar()
            circles = self.identificarCirculos(erode)
            cont = 0
            raio11 = 0
            raio22 = 0
            for i in circles[0,:]:
                if cont == 0:
                    self.ListaCoordenadas = i
                    
                cont = 1
                #circulo externo
                listaR = self.recurso.getObjetoPadrao()
                if i[2] >= 8:
                    cv2.circle(erode,(i[0],i[1]),i[2],(255,255,255),2)
                    cv2.circle(erode,(i[0],i[1]),2,(255, 0, 0, 255),12)
                    cv2.circle(self.__imagem,(i[0],i[1]),i[2],(255, 0, 0, 255),2)
                    cv2.circle(self.__imagem,(i[0],i[1]),2,(255, 0, 0, 255),2)
                    alturaReal = listaR[1]
                    
                    alturaPixel = self.ListaCoordenadas[2]*2
                    print(i[2])
                    raio11 = (alturaReal * raio11) / alturaPixel
                    raio22 = (alturaReal * raio22) / alturaPixel
                    #print(f'Raio1 = {raio11} | Raio2 = {raio22}')
            
            return self.analiseReta(erode)


        

