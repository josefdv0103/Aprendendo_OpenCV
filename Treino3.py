import cv2 as cv
import numpy as np

def rescale_image(frame):
    largura = 800
    altura = 500
    dimensoes = (largura, altura) 
    return cv.resize(frame, dimensoes, interpolation = cv.INTER_AREA)

img = cv.imread('Fotos/anelideos.jpg')
#cv.imshow('Minhoca', img)

img2 = rescale_image(img)
#cv.imshow('Minhoca2', img2)

vazio = np.zeros(img2.shape[:2], dtype = 'uint8')
#cv.imshow('VAZIO', vazio)

largura = 800
altura = 500
d = 50
m = int((largura/d) / 2)
n = int(altura/d)
ret = cv.rectangle(vazio, (0, 0), (50, 50), 255, -1)
j = 0

for k in range(0, n):
    if k % 2 == 0:
        i = 0
    elif k % 2 != 0:
        i = 50
    for l in range(0, m):
        ret2 = cv.rectangle(vazio, (0 + i, 0 + j), (50 + i, 50 + j), 255, -1)
        junto = cv.bitwise_or(ret, ret2)
        i = i + 100
    j = j + 50

cv.imshow('Junto', junto)
cv.waitKey(0)