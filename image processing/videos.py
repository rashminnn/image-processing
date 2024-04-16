import cv2 as cv
import images

capture = cv.VideoCapture('videos/cod.mp4')
while True:
    isTrue, Frame = capture.read()
    cv.imshow('Video', Frame)
    re = images.rescale(Frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
