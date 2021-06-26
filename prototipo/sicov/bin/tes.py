import cv2
from processamento.ProcessamentoDeImagem import ProcessamentoDeImagem as ProDI
from processamento.ContaOvos import conta
import numpy as np
class t:
    def __init__(self):
        self.img = cv2.imread('C:\\Users\\rhuan\\Desktop\\egges_2.png')
        #self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        #self.img = cv2.GaussianBlur(self.img, (7, 7), -1)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.pd = ProDI()
        i = conta(self.img)
        #ret,self.img  = cv2.threshold(self.img , 127, 255, cv2.THRESH_BINARY_INV)

      
        
        cv2.drawContours(self.img, i[0], -1, (255, 0, 0), 2)
        #o, img =self.pd.ExtrairCaracteristicas(imagem=self.img)
        cv2.imshow('teste'+str(len(i[0])), self.img)
        cv2.waitKey()
    
t()