import cv2 as cv
import numpy as np

img = cv.imread('Fotos/anelideos.jpg')

cv.imshow('Minhoca', img)

branco = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('Branco', branco)

cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Cinza', cinza)

#blur = cv.GaussianBlur(cinza, (5,5), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#canny = cv.Canny(blur, 125, 175)
#cv.imshow('canny edges', canny)

#OUTRA FORMA DE FAZER A IMAGEM EM CONTORNOS 'BINARIZANDO'
ret, thresh = cv.threshold(cinza, 125, 255, cv.THRESH_BINARY)
cv.imshow('Contorno 2.0', thresh)


contorno, hierarquia = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#Há um módulo em openúltimo lugar para especificar os contornos TREE, EXTERNAL, LIST
#BASICAMENTE SÃO OS CONTORNOS HIEÁRQUICOS, EXTERNOS E TODOS
#O módulo ao final significa para aproximar os contornos que pode ser com
#NONE que não faz nada, ou SIMPLE que comprime os contornos e simplifica por exemplo um reta em dois pontos

#Contando os contornos 
print(f'{len(contorno)} contorno(s) encontrado(s)')

#Desenhando contornos
cv.drawContours(branco, contorno, -1, (0,0,255), 2)
cv.imshow('Desenho', branco)

cv.waitKey(0)