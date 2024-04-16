import cv2 as cv

webcam = cv.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    cv.imshow('frame', frame)
    if cv.waitKey(16) & 0xFF == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()
