import cv2 as cv


def redimensionada(frame, scale = 2):
    altura = int(frame.shape[0] * scale)
    largura = int(frame.shape[1] * scale)
    dimensoes = (largura, altura)

    return cv.resize(frame, dimensoes, interpolation = cv.INTER_CUBIC)

img  = cv.imread('Fotos/anelideos.jpg')

redimensio = redimensionada(img)
cv.putText(redimensio, 'MINHOCA', (250, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 255), 2)
cv.line(redimensio, (400, 260), (250, 260), (0, 0, 255), thickness = 2)
cv.circle(redimensio, ())
cv.imshow('Minhoca', redimensio)

cv.waitKey(0)

