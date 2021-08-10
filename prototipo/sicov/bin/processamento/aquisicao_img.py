import cv2
import tkinter as t
from PIL import Image, ImageTk
from processamento.PreProcessadorDeImagem import PreProcessadorDeImagem as PDI
from processamento.SegmentadorDeImagem import SegmentadorDeImagem as SDI
from processamento.ProcessamentoDeImagem import ProcessamentoDeImagem as ProID
import numpy as np


class Aquisicao:
    def __init__(self, url, validador=1):
        self.url = url
        #self.l = SG().porAdaptacao(self.t)
        if validador == None:
            self.img = cv2.imread(self.url)
            self.imge = self.img
        if validador == 2:
            self.imge = Image.fromarray(url)
        else:
            self.imge = Image.open(self.url)
        self.basewidth = 400
        self.wpercent = (self.basewidth/float(self.imge.size[0]))
        self.hsize = int((float(self.imge.size[1])*float(self.wpercent)))
        self.imge = self.imge.resize((self.basewidth,self.hsize), Image.ANTIALIAS)
        self.imagem_tk = ImageTk.PhotoImage(self.imge)
        self.imge_label = t.Label(image=self.imagem_tk, height="350", width="350").place(x=12, y=0)
        '''kernel = np.array([[-1,-1,-1], 
                           [-1, 9,-1],
                           [-1,-1,-1]])
        sharpened = cv2.filter2D(self.np_array, -1, kernel) # applying the sharpening kernel to the input image & displaying it.
        cv2.imshow('Image Sharpening', sharpened)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        
        self.tt = PDI()
        _,self.tt.PorRealce.LIMITE_MAXIMO_KEY = cv2.threshold(self.np_array,0,127,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        _,self.tt.PorRealce.LIMITE_MINIMO_KEY = cv2.threshold(self.np_array,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        self.t = self.tt.porRealce(self.np_array).executar()
        self.s = SDI().porBinarizacao(self.t).executar()
        self.np_array = numpy.array(self.t)
        self.np_array = self.np_array[:, ::-1].copy()
        #self.img = cv2.imread(self.np_array)
        self.imagem_cv_img = Image.fromarray(self.np_array)#self.imagem_cv2
        self.imge = self.imagem_cv_img

        
        #self.processarimg(self.imagem)#criar função


        
      
        cv2.imshow('teste', self.np_array)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        cv2.imshow('teste', self.s)
        cv2.waitKey(0)
        cv2.destroyAllWindows()'''
        '''
        self.imagem_tk = ImageTk.PhotoImage(self.imge)
        self.imge_label = t.Label(image=self.imagem_tk, height="350", width="350").place(x=12, y=0)
        #PP(url_img=self.np_array)'''

