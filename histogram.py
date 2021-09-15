import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('Fotos/anelideos.jpg')
cv.imshow('Minhoca', img)

#HISTOGRAMAS PERMITE VER A DISTRINBUIÇÃO DE PIXEL DE UMA IMAGEM
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Cinza', gray)

blank = np.zeros((img.shape[:2]), dtype = 'uint8')

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(gray, gray, mask = circle)
#cv.imshow("Mask", mask)

#Histograma em grayscale
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

#plt.figure()
#plt.title('Histograma Grayscale')
#plt.xlabel('Bins')
#plt.ylabel('# of pixels')
#plt.plot(gray_hist)
#plt.xlim([0, 256])
#plt.show()

#Histograma em imagens coloridas



plt.figure()
plt.title('Histograma Colorido')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
cores = ('b', 'g', 'r')

mask2 = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask = mask2)
cv.imshow('mascara', masked)

for i, col in enumerate(cores):
    hist = cv.calcHist([img], [i], masked, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)