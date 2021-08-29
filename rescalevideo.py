import cv2 as cv
#PARA VÍDEOS, IMAGENS E LIVES
def rescaleFrame(frame, scale = 0.75):
    largura = int(frame.shape[1] * scale)
    altura = int(frame.shape[0] * scale)
    dimensions = (largura, altura)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA) 

#PARA LIVES/AO VIVO
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)
#----------------------------------------------------------------------

capture = cv.VideoCapture('Fotos/teste.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale = .2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release
cv.destroyAllWindows
