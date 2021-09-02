import cv2 as cv
import matplotlib.pyplot as plt

#O OPENCV MOSTRA SÓ IMAGENS EM BGR PORÉM PODEMOS MUDAR OS ESPAÇOS DE COR

img = cv.imread('Fotos/anelideos.jpg')
cv.imshow('Minhoca', img)

#    Apresentar cores invertidas em um gráfico, estamos colocando numa 
#biblioteca matplot que não faz ideia o que é uma imagem BGR e então
#mostra a imagem em RGB (inversão)
#plt.imshow(img)
#plt.show()

#   ESPAÇOS DE COR sistemas de arrays que representam cores de pixels
#Ex: RGB, gray scale, HSV, ...

#   BGR para gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#   BGR para HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow('HSV', hsv)

#   BGR para LAB ou L + a + b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
#cv.imshow('Lab', lab)

#   BGR para RGB (no OpenCV)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#cv.imshow('RGB', rgb)

#plt.imshow(rgb)
#plt.show()

#   PODEMOS FAZER A CONVERSÃO DE ESCALAS DE CORES DIFERENTES PARA BGR
#TAMBÉM PORÉM NÃO ENTRE ESCALAS ANTES DE CONVERTER EM BGR, PORTANTO SEMPRE
#DEVERÁPASSAR PELA ESCALA BGR

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv para bgr', hsv_bgr)

lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('lab para bgr', lab_bgr)

rgb_bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow('RGB PARA BGR', rgb_bgr)



cv.waitKey(0)