import cv2 as cv

#PARA VÍDEOS E IMAGENS
def rescaleFrame(frame, scale = 0.20):
    largura = int(frame.shape[1] * scale)
    altura = int(frame.shape[0] * scale)
    dimensions = (largura, altura)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA) 

img = cv.imread('Fotos/mingrangre.jpeg')
cv.imshow('Minhoca', img)

resized_image = rescaleFrame(img)
cv.imshow('image', resized_image)



cv.waitKey(0) 

