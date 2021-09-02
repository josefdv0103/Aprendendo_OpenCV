import cv2 as cv
import numpy as np

img = cv.imread('Fotos/anelideos.jpg')
cv.imshow('Minhoca', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')


#   UMA IMAGEM DE COR É UMA IMAGEM DE MULTIPLOS CANAIS VERMELHO, VERDE E AZUL
#EM BGR E RGB AS CORES SÃO UMA MISTURA DESSAS TRÊS. NO  OPENCV PODEMOS 
#SEPARAR ESSAS CORES EM CANAIS DE CORES

b, g, r = cv.split(img)

#O blank representa na lista a altura e largura, e dizendo que os componentes 
# blue, green e red quando são mostrados individualmente as outras duas
# compoenentes serão representados por preto 

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Azul', blue)
cv.imshow('Verde', green)
cv.imshow('Vermelho', red)

#APARECE COMO GRAY SCALE MOSTRANDO A CONCENTRAÇÃO DESSAS CORES EM QUE
#QUANTO MAIS BRANCO MAIOR A CONCENTRAÇÃO

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#Unindo todas as cores

merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

cv.waitKey(0)