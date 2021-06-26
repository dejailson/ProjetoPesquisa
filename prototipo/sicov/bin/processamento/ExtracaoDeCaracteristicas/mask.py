import cv2
import numpy as np

class AplicarMascara:
    def __init__(self):
        pass


    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # detect circles
    def detectarCirculos(self, img):
        gray = cv2.medianBlur(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), 5)
        return np.uint16(np.around(cv2.HoughCircles(gray, \
             cv2.HOUGH_GRADIENT, 1, 60, param1=50, param2=50, \
             minRadius=0, maxRadius=0)))

    # draw mask
    def desenharMascara(self, img):
        mask = np.full((img.shape[0], img.shape[1]), 0, dtype=np.uint8)
        for i in self.detectarCirculos(img)[0, :]:
            cv2.circle(mask, (i[0], i[1]), i[2], (255, 0, 0), -1)
        return self.obtendoMascaras(img, mask)


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

    def tudo(self, img):
        mask = np.full((img.shape[0], img.shape[1]), 0, dtype=np.uint8)
        for i in  np.uint16(np.around(cv2.HoughCircles(img, \
             cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=50, \
             minRadius=0, maxRadius=0)))[0, :]:
            cv2.circle(mask, (i[0], i[1]), i[2], (255, 255, 255), -1)

        fg = cv2.bitwise_or(img, img, mask=mask)

        # get second masked value (background) mask must be inverted
        mask = cv2.bitwise_not(mask)
        background = np.full(img.shape, 255, dtype=np.uint8)
        bk = cv2.bitwise_or(background, background, mask=mask)

        # combine foreground+background
        img = cv2.bitwise_or(fg, bk)

        return img



