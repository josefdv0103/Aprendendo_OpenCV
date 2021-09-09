import cv2 as cv
import numpy as np

def rodado (img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensoes = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensoes)

img = cv.imread('Fotos/anelideos.jpg')

vazio = np.zeros((img.shape[:2]), dtype = 'uint8')

circulo1 = cv.circle(vazio.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
#cv.imshow('vazio', circulo1)

retangulo1 = cv.rectangle(vazio.copy(), (img.shape[1]//2 - 100, img.shape[0]//2 + 100), (img.shape[1]//2 + 100, img.shape[0]//2 - 100), 255, -1)
#cv.imshow('Retangulo', retangulo1)

junto1 = cv.bitwise_xor(retangulo1, circulo1)
cv.imshow('Junto', junto1)

junto2 = cv.bitwise_and(img, img, mask = junto1)
cv.imshow('Junto2', junto2)

retangulo2 = cv.rectangle(vazio.copy(), (img.shape[1]//2 - 100, img.shape[0]//2 - 100), (img.shape[1]//2, img.shape[0]//2), 255, -1)
retangulo2a = rodado(retangulo2, 45)
#cv.imshow('Retangulo2', retangulo2a)

retangulo3 = cv.rectangle(vazio.copy(), (img.shape[1]//2 + 100, img.shape[0]//2 - 100), (img.shape[1]//2, img.shape[0]//2), 255, -1)
retangulo3a = rodado(retangulo3, - 45)
#cv.imshow('Retangulo3', retangulo3a)

junto3 = cv.bitwise_or(retangulo2a, retangulo3a)
cv.imshow('Junto3', junto3)

junto4 = cv.bitwise_and(junto3, circulo1)
cv.imshow('Junto4', junto4)

junto5 = cv.bitwise_and(img, img, mask = junto4)
cv.imshow('Junto5', junto5)


cv.waitKey(0)