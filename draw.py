import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')#dtype = datatype
cv.imshow("Em Branco", blank)

#   Pontuar a imagem com uma certa cor
#Verde
#blank[:] = 0, 255, 0

#Vermelho
#blank[:] = 0, 0, 255

#Tamanho dentro do display blank
#blank[200:300, 300:400] = 0, 0, 255
#cv.imshow('Red', blank)

#   Traçar um retângulo

#Retângulo sem preencimento
#cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)

#Retângulo com preechimento
#cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness = -1)

#Retângulo que tem dimensões com metade do valor da imagem
#cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 255), thickness = -1)

#   Traçar um círculo
#Círculo sem preenchimento
#cv.circle(blank, (250, 250), 50, (0, 0, 255), thickness = 3)

#Círculo com preenchimento
#cv.circle(blank, (250, 250), 50, (0, 0, 255), thickness = -1)

#   Traçar uma reta 
#cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness = 3)

#   Escrever um texto
#cv.putText(blank, 'Ola meu nome e Jose Augusto', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 255), 2)

cv.imshow('Text', blank)


cv.waitKey(0)