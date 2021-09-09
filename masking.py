import cv2 as cv
import numpy as np

img = cv.imread('Fotos/anelideos.jpg')
cv.imshow('Minhoca', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('Blank', blank)

maskcirculo = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
#cv.imshow('Mask circulo', maskcirculo)

maskretangulo = cv.rectangle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2 + 100, img.shape[0]//2 + 100), 255, -1)
#cv.imshow('Mask retangulo', maskretangulo)

maskretangulo2 = cv.rectangle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2 - 100, img.shape[0]//2 - 100), 255, -1)
#cv.imshow('Mask reantgulo 2', maskretangulo2)

junta = cv.bitwise_or(maskretangulo2, maskretangulo)
#cv.imshow('JUNCAO', junta)

junta2 = cv.bitwise_xor(maskcirculo, maskretangulo)
cv.imshow('JUNCAO2', junta2)

estranha = cv.bitwise_and(maskcirculo, junta)
#cv.imshow('Forma final', estranha)

#   Aplicando o masking numa imagem
masked = cv.bitwise_and(img, img, mask = estranha)
cv.imshow('Masked image', masked)

cv.waitKey(0)