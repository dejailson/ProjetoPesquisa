import cv2
import numpy as np
def conta(img):
    limiar = 127
    maximo = 255 
    ret,T = cv2.threshold(img, limiar, maximo, cv2.THRESH_BINARY_INV)
    #(thresh, im_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = np.ones((5,5),np.uint8)
    #T = cv2.morphologyEx(T, cv2.MORPH_CLOSE, kernel)
    bin = img.copy()
    bin[bin > T] = 255
    bin[bin < 255] = 0
    bin = cv2.bitwise_not(bin)
    bordas = cv2.Canny(bin, 127, 255)
    #cv2.RETR_EXTERNAL = conta apenas os contornos externos
    (objetos, lx) = cv2.findContours(bordas.copy(),
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bordas = np.array(bordas)
    bordas = bordas[:, ::-1].copy()
    return [objetos, bordas] 