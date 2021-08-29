import cv2 as cv

img = cv.imread('Fotos/anelideos.jpg')

cv.imshow('Minhoca', img)

#   Convertendo para preto e branco(não é a única fora de se fazer isso)
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('PretoeBranco', gray)

#   Dando um Blur na imagem(Não é a única forma de se fazer isso)
#blur = cv.GaussianBlur(img, (7 ,7), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#   Cascate Edge(Não é a única forma de se fazer isso)
#canny = cv.Canny(blur, 125, 175)#**Para reduzir as linhas colocar blur
#cv.imshow('Canny', canny)

#   Dilatando Cascate Edge
#dilatado = cv.dilate(canny, (7, 7), iterations = 3)#Dilatou as linhas do canny
#cv.imshow('Dilatado', dilatado)

#   Contrair Cascate Edge(o inverso de dilatar)
#eroded = cv.erode(dilatado, (7, 7), iterations = 3)#Se colocarmos os mesmo parametros que colocamos para dilatar ele volta ao normal
#cv.imshow('eroded', eroded)

#   Redimensionar imagens(outra forma)
redimensio = cv.resize(img, (500, 500), interpolation = cv.INTER_AREA)
cv.imshow('AREA', redimensio)
redimensi = cv.resize(img, (500, 500), interpolation = cv.INTER_LINEAR)
cv.imshow('LINEAR', redimensi)
redimens = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
cv.imshow('CUBIC', redimens)


cv.waitKey(0)