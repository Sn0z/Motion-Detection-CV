import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    cv2.imshow("Imag", frame)

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release