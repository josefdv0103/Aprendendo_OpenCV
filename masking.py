import cv2 as cv
import numpy as np
img = cv.imread('Fotos/anelideos.jpg')
cv.imshow('Minhoca', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
#cv.imshow('Blanck', blank)

maskcirculo = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask circulo', maskcirculo)

maskretangulo = cv.rectangle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2 + 100, img.shape[0]//2 + 100), 255, -1)
cv.imshow('Mask retangulo', maskretangulo)

#   Aplicando o masking numa imagem
masked = cv.bitwise_and(img, img, maskretangulo = maskretangulo)
cv.imshow('Masked image', masked)

cv.waitKey(0)