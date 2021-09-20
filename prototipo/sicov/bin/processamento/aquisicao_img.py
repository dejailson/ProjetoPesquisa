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
