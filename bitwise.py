import cv2 as cv
import numpy as np

#OPERADORES BITWISE

blank = np.zeros((400,400), dtype = 'uint8')

retangulo = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circulo = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Retangulo', retangulo)
cv.imshow('Circulo', circulo)

#   bitwise AND
# Pega duas imagens e mostra a intersecção entre ambas
bitwise_and = cv.bitwise_and(retangulo, circulo)
cv.imshow('Bitwise AND', bitwise_and)

#   bitwise OR
# Pega duas imagens e mostra a união entre ambas

bitwise_or = cv.bitwise_or(retangulo, circulo)
cv.imshow('Bitwise_OR', bitwise_or)

#   bitwise XOR
# Pega dus imagens e mostra as partes que não intersectam
bitwise_xor = cv.bitwise_xor(retangulo, circulo)
cv.imshow('Bitwise XOR', bitwise_xor)

#   bitwise NON
# Pega uma inmagem e inverte as cores nesse caso preto em branco e vice versa
bitwise_not = cv.bitwise_not(retangulo)
cv.imshow('bitwise Not', bitwise_not)


cv.waitKey(0)