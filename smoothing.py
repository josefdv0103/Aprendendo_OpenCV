import cv2 as cv

img = cv.imread('Fotos/anelideos.jpg')
#cv.imshow('Minhoca', img)

#   Quando iremos usar o blur nós definimos um kernel(núcleo) que nada mais é
#que uma região da imagem que iremos modificar, esse kernel é basicamente
#numeros de linhas e colunas

#   PRIMEIRO MÉTODO - Averiging
# Ele implica que o pixel central do kernel seja o resultado de uma média
# das intensidades dos pixels ao redor dele, esse processo é aplciado para
# toda a imagem esse modelo de kernel irá ser repetido para a direita
# e depois para baixo

average = cv.blur(img, (3, 3))
cv.imshow('average blur', average)

#   SEGUNDO MÉTODO - Blur Gaussiano
#Faz basicamente a mesma coisa que o Average porém ao invés de médias 
# cada pixel que está em volta do central é dado um peso e a média dos produtops
# Desses pesos da o lavor do centro(é mais natural que o averiging)

gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gauss)

#   TERCEIRO MÉTODO - MEDIAN BLUR
#  Faz basicamente a mesma coisa que o Average porém ao invés de médias 
# cada pixel que está em volta do central é feita a mediana dos pixels
# em volta do central

median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

#   QUARTO MÉTODO - BILATERAL BLUR
# É considerado o melhor, aplica o blur porém faz o que os outros não
#fazem retém os limites da imagem

bilateral = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)