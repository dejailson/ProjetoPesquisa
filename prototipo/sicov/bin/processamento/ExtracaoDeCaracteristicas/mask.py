import cv2
import numpy as np

class AplicarMascara:
    def __init__(self):
        pass


    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # detect circles
    def detectarCirculos(self, img, num=None):
        gray = cv2.medianBlur(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), 5)
        if num == None:
            img = np.uint16(np.around(cv2.HoughCircles(gray, \
                cv2.HOUGH_GRADIENT, 1.2, 100, param1=50, param2=50, \
                minRadius=0, maxRadius=0)))     
        else:
            img = np.uint16(np.around(cv2.HoughCircles(gray, \
                cv2.HOUGH_GRADIENT, 1, 100, param1=50, param2=50, \
                minRadius=0, maxRadius=0))) 
        return img


    # draw mask
    def desenharMascara(self, img):
        mask = np.full((img.shape[0], img.shape[1]), 0, dtype=np.uint8)
        try:
            for i in self.detectarCirculos(img)[0, :]:
                cv2.circle(mask, (i[0], i[1]), i[2], (255, 0, 0), -1)
        except:
            for i in self.detectarCirculos(img, 1)[0, :]:
                cv2.circle(mask, (i[0], i[1]), i[2], (255, 0, 0), -1)
        try:
            return self.obtendoMascaras(img, mask)
        except:
            return img


    # get first masked value (foreground)
    def obtendoMascaras(self, img, mask):
        fg = cv2.bitwise_or(img, img, mask=mask)

        # get second masked value (background) mask must be inverted
        mask = cv2.bitwise_not(mask)
        background = np.full(img.shape, 255, dtype=np.uint8)
        bk = cv2.bitwise_or(background, background, mask=mask)

        # combine foreground+background
        img = cv2.bitwise_or(fg, bk)

        return img