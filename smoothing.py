import cv2 as cv

img = cv.imread('Fotos/anelideos.jpg')
cv.imshow('Minhoca', img)

#   Quando iremos usar o blur nós definimos um kernel(núcleo) que nada mais é
#que uma região da imagem que iremos modificar, esse kernel é basicamente
#numeros de linhas e colunas

#   PRIMEIRO MÉTODO - Averiging
# Ele implica que o pixel central do kernel seja o resultado de uma média
# das intensidades dos pixels ao redor dele, esse processo é aplciado para
# toda a imagem esse modelo de kernel irá ser repetido para a direita
# e depois para baixo

average = cv.blur(img, (7,7))
cv.imshow('average blur', average)

#   SEGUNDO MÉTODO - Blur Gaussiano
#Faz basicamente a mesma coisa que o Average porém ao invés de médias 
# cada pixel que está em volta do central é dado um peso

cv.waitKey(0)