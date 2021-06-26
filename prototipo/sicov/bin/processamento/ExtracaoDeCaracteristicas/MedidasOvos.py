from util.modelo.ovulo import Ovulo
import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
#from skimage import metrics
#from ContaOvos import conta
#from skimage.measure import label, regionprops
#from processamento.ExtracaoDeCaracteristicas.mask import AplicarMascara as AM
#from util.ProcessadorTarefa import ProcessadorTarefa
#from imutils import perspective
#from imutils import contours
import imutils

'''class MedidasOvos:
    def __init__(self):
        self.mascara = AM()

    def PorScikit(self, img):
        return self.Scikit(img)

    def PorCV2(self, img):
        return self.CV2(img)

    class Scikit(ProcessadorTarefa):
        def __init__(self) -> None:
            pass

        def dimenssoesImagem(self, img):
            return img.shape[:2]

        def regioesImagem(self, img):
            label_img = label(img)
            return regionprops(label_img)

        def analiseReta(self, img):
            regions = self.regioesImagem(img)
            altura, largura = self.dimenssoesImagem(self, img)
            fig, ax = plt.subplots()
            for props in regions:
                y0, x0 = props.centroid
                orientation = props.orientation
                min_y, min_x, max_y, max_x = props.bbox
                ponto_c = np.array((x0, y0)).astype(int)
                ponto_a = np.array((x0, min_y)).astype(int)
                ponto_b = np.array((max_x, y0)).astype(int)
                forma = (largura, altura)

                imagem_a = np.zeros(forma, dtype=bool)
                imagem_b = np.zeros(forma, dtype=bool)
                imagem_c = np.zeros(forma, dtype=bool)

                coord_c = tuple(ponto_c.tolist())
                coord_a = tuple(ponto_a.tolist())
                coord_b = tuple(ponto_b.tolist())

                imagem_c[coord_c] = True
                imagem_a[coord_a] = True
                imagem_b[coord_b] = True

                semi_reta_eixo_y = metrics.hausdorff_distance(imagem_c, imagem_a)
                semi_reta_eixo_x = metrics.hausdorff_distance(imagem_c, imagem_b)
                semi_eixo_maior = semi_reta_eixo_x if semi_reta_eixo_x > semi_reta_eixo_y else semi_reta_eixo_y
                semi_eixo_menor = semi_reta_eixo_y if semi_reta_eixo_y < semi_reta_eixo_x else semi_reta_eixo_x

                xa = x0 - math.cos(orientation) * semi_eixo_menor
                ya = y0 - math.sin(orientation) * semi_eixo_menor
                xb = x0 + math.sin(orientation) * semi_eixo_maior
                yb = y0 + math.cos(orientation) * semi_eixo_maior

                ax.plot((x0, xa), (y0, ya), '-r', linewidth=2.5)
                ax.plot((x0, xb), (y0, yb), '-r', linewidth=2.5)
                ax.plot(x0, y0, '.g', markersize=15)

                bx = (min_x, max_x, max_x, min_x, min_x)
                by = (min_y, min_y, max_y, max_y, min_y)
                ax.plot(bx, by, '-b', linewidth=2.5)
            return ax

        def algo(self):
            pass

    class CV2(ProcessadorTarefa):
        def __init__(self) -> None:
            pass

        def midpoint(ptA, ptB):
            return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
    
        def obterContornos(self):
            # load the image, convert it to grayscale, and blur it slightly
            gray = cv2.GaussianBlur(self.__imagem, (7, 7), 0)
            # perform edge detection, then perform a dilation + erosion to
            # close gaps in between object edges
            edged = cv2.Canny(gray, 50, 100)
            edged = cv2.dilate(edged, None, iterations=1)
            edged = cv2.erode(edged, None, iterations=1)
            # find contours in the edge map
            cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            # sort the contours from left-to-right and initialize the
            # 'pixels per metric' calibration variable
            (cnts, _) = contours.sort_contours(cnts)
            pixelsPerMetric = None
            return cnts, pixelsPerMetric
            img = self.mascara.desenharMascara(img)    
            kernel = np.ones((2,2),np.uint8)
            dilation = cv2.erode(img,kernel,iterations = 1)
            contours,_ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            return contours

        def g(self, img, cnts, pixelsPerMetric):
            for c in cnts:
	            # if the contour is not sufficiently large, ignore it
                if cv2.contourArea(c) < 100:
                    continue
                # compute the rotated bounding box of the contour
                orig = img.copy()
                box = cv2.minAreaRect(c)
                box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
                box = np.array(box, dtype="int")
                # order the points in the contour such that they appear
                # in top-left, top-right, bottom-right, and bottom-left
                # order, then draw the outline of the rotated bounding
                # box
                #box = perspective.order_points(box)
                cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)
                # loop over the original points and draw them
                for (x, y) in box:
                    cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)
                # unpack the ordered bounding box, then compute the midpoint
                # between the top-left and top-right coordinates, followed by
                # the midpoint between bottom-left and bottom-right coordinates
                (tl, tr, br, bl) = box
                (tltrX, tltrY) = midpoint(tl, tr)
                (blbrX, blbrY) = midpoint(bl, br)
                # compute the midpoint between the top-left and top-right points,
                # followed by the midpoint between the top-righ and bottom-right
                (tlblX, tlblY) = midpoint(tl, bl)
                (trbrX, trbrY) = midpoint(tr, br)
                # draw the midpoints on the image
                cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
                cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
                cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
                cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
                # draw lines between the midpoints
                cv2.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
                    (255, 0, 255), 2)
                cv2.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
                    (255, 0, 255), 2)
                # compute the Euclidean distance between the midpoints
                dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
                dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
                # if the pixels per metric has not been initialized, then
                # compute it as the ratio of pixels to supplied metric
                # (in this case, inches)
                if pixelsPerMetric is None:
                    pixelsPerMetric = dB / args["width"]
                # compute the size of the object
                dimA = dA / pixelsPerMetric
                dimB = dB / pixelsPerMetric
                # draw the object sizes on the image
                cv2.putText(orig, "{:.1f}in".format(dimA),
                    (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                    0.65, (255, 255, 255), 2)
                cv2.putText(orig, "{:.1f}in".format(dimB),
                    (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
                    0.65, (255, 255, 255), 2)
                # show the output image
                cv2.imshow("Image", orig)
                cv2.waitKey(0)

        def dadosImagem(self, img):
            #modificar função
            dicionario = {}
            contours = self.tratarImagem(img)
            cont = 1
            for (i,c) in enumerate(contours):
                (x,y,w,h) = cv2.boundingRect(c)
                area = cv2.contourArea(c)
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
                cmY = (h*7)/100
                cmX = (w*7)/100
                cv2.putText(img, str(int(cmY)), (x, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0),1)
                cv2.putText(img, str(int(cmX)), (x+w+15, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0),1)
                dicionario[f'{cont}'] = [cmY, cmX]
                cont += 1
            dicionario['quantidade'] = int(cont/2)
            return dicionario'''

def azul(img):
    kernel = np.ones((5 ,5), np.uint8)
    imagem = img
    rangomax = np.array([255, 160, 130, 255]) # 119, 148, 195 B, G, R
    rangomin = np.array([80,   80,   70, 0])#61, 112,  
    mask = cv2.inRange(imagem, rangomin,  rangomax )
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(imagem, 100, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5,5),np.uint8)

    dilation = cv2.erode(threshold,kernel,iterations = 1)

    contours,_ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    listaOvulo = []
    cont = 1


    for (i,c) in enumerate(contours):
        (x,y,w,h) = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        cv2.rectangle(imagem,(x,y),(x+w,y+h),(0,255,0),2)
        cmY = (h*15)/120
        cmX = (w*10)/71
        ovulo = Ovulo(diametroMaior=cmY, diametroMenor=cmX)
        listaOvulo.append(ovulo)
        cv2.putText(imagem, str(int(cmY)), (x, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255),1)
        cv2.putText(imagem, str(int(cmX)), (x+w+15, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255),1)
        cont += 1
        #print(f'Largura = {w} e altura = {h}')
    #cv2.imwrite("novalampada.png", imagem)
    return listaOvulo
    


def teste():
    a = 'C:\\Users\\rhuan\\Documents\\GitHub\\ProjetoPesquisa\\prototipo\\sicov\\recurso\\imagem\\amostras\\egges_7.png'
    b = 'C:\\Users\\rhuan\\Desktop\\egges_2.png'
    url = b
    img = cv2.imread(b)
    #azul(img)
    
    azul(img)

