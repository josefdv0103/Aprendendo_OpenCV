import cv2 as cv

#LENDO IMAGENS

#img = cv.imread('Fotos/mingrangre.jpeg')

#cv.imshow('Minhoca', img)

#LENDO VÍDEOS

capture = cv.VideoCapture('Fotos/teste.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release
cv.destroyAllWindows
