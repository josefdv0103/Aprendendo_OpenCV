import cv2 as cv

#Threshold É BINARIZAR A SUA IMAGEM

img = cv.imread('Fotos/anelideos.jpg')
#cv.imshow('Minhoca', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Cinza', gray)

#   Simple Thresholding
#ESTABELECE UM LIMITE PARA O VALORDE CADA PIXEL CASO O PIXEL ULTRAPASSE
#UM LIMITE DE 150 NESSE CASO IRÁ SER CONSIDERADO BRANCO(255) E O RESTO PRETO

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresh', thresh)

#Agora é o inverso o que estiver maior que 150 será preto
threshold, thresh_inverse = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresh Inverse', thresh_inverse)

# Adapted Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray.copy(), 255, 
cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive theshold', adaptive_thresh)

adaptive_thresh_inv = cv.adaptiveThreshold(gray.copy(), 255, 
cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive Threshold Inverse', adaptive_thresh_inv)

#Quanto maior o valor final que nesse caso é o 3 mais preciso e o
#threshhold
#SE USARMOS O THRESH 'GAUSSIAN' É MELHOR QUE O 'MEAN' MAIS PRECISO

cv.waitKey(0)