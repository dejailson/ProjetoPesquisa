import cv2
import tkinter as t
from PIL import Image, ImageTk


class Aquisicao:
    def __init__(self, url, validador=None):
        self.url = url
        if validador == None:
            self.img = cv2.imread(self.url)
            self.imagem_cv2 = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            self.imagem_cv_img = Image.fromarray(self.imagem_cv2)
            self.imge = self.imagem_cv_img
        else:
            self.imge = Image.open(self.url)
        self.basewidth = 400
        self.wpercent = (self.basewidth/float(self.imge.size[0]))
        self.hsize = int((float(self.imge.size[1])*float(self.wpercent)))
        self.imge = self.imge.resize((self.basewidth,self.hsize), Image.ANTIALIAS)
        #self.processarimg(self.imagem)#criar função
        self.imagem_tk = ImageTk.PhotoImage(self.imge)
        self.imge_label = t.Label(image=self.imagem_tk, height="350", width="350").place(x=12, y=0)
        

