import cv2 as cv
import numpy as np


img = cv.imread('Fotos/anelideos.jpg')

vazio = np.zeros(img.shape[:3], dtype = 'uint8')
#cv.imshow('Vazio', vazio)

vazio[:] = 0, 100, 0



ret = cv.line(vazio.copy(), (0, img.shape[0]//2), (img.shape[1]//2, img.shape[0]), (0, 255, 255), thickness = 2)
ret2 = cv.line(vazio.copy(), (img.shape[1]//2, img.shape[0]), (img.shape[1], img.shape[0]//2), (0, 255, 255), thickness = 2)
junto = cv.bitwise_or(ret, ret2)
ret3 = cv.line(vazio.copy(), (img.shape[1], img.shape[0]//2), (img.shape[1]//2, 0), (0, 255, 255), thickness = 2)
junto2 = cv.bitwise_or(junto, ret3)
ret4 = cv.line(vazio.copy(), (img.shape[1]//2, 0), (0, img.shape[0]//2), (0, 255, 255), thickness = 2)
junto3 = cv.bitwise_or(junto2, ret4)

circ = cv.circle(junto3, (img.shape[1]//2, img.shape[0]//2), 100, (128, 0, 0), thickness = -1)
cv.imshow('Com circulo', circ)

circ2 = cv.circle(vazio.copy(), (img.shape[1]//16 + img.shape[1]//2, img.shape[0]//4 + img.shape[0]//2), 130, (255, 255, 255), thickness = 8)
circ3 = cv.circle(vazio.copy(), (img.shape[1]//2, img.shape[0]//2), 100, (128, 0, 0), thickness = -1)
junto4 = cv.bitwise_or(circ2, circ3)
cv.imshow('Faixa', junto4)


cv.waitKey(0)