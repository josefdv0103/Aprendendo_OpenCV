import cv2 as cv
import numpy as np

img = cv.imread('Fotos/anelideos.jpg')

cv.imshow('imagem', img)

#   Transladar
def translate(img,  x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])# Matriz de transladação
    dimensions = (img.shape[1], img.shape[0])#[1]comprimentp, [0] altura    
    return  cv.warpAffine(img, transMat, dimensions)

# Se tivermos valores negativos de x a transladação moverá para a esquerda
# Se tivermos valores negativos de x a transladação moverá para cima
# Se tivermos valores negativos de x a transladação moverá para a direta
# Se tivermos valores negativos de x a transladação moverá para baixo

translated = translate(img, -100, 100)
#cv.imshow('translated', translated)


#   Rotação
def rodado (img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensoes = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensoes)

# A rotação ela adiciona espaços em braco em triangulos que ficam mesmo rotacionando-a novamente
rotada = rodado(img, -45)# Padrão antihorário
#cv.imshow('rodada', rotada)

rotada_rotada = rodado(rotada, -90)
#cv.imshow('rodada rodada', rotada_rotada)

#    Mudando o tamanho
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
#cv.imshow('Retamanho', resized)

#   Virar
flip = cv.flip(img, 1) #No segundo termo pode ser 0, 1, -1; 
#0 flip vertical, 1 flip horizontal, -1 flip horizontal e vertical
#cv.imshow('Flip', flip)

#   Recortar
recortar = img[200:400, 300:400]
#cv.imshow('Recortado', recortar)
cv.waitKey(0)