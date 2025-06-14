import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

ret, frame1 = cap.read()
frame1 = cv2.flip(frame1, 1)

ret, frame2 = cap.read()
frame2 = cv2.flip(frame2, 1)

while cap.isOpened():

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    for contours in contours:
        (x,y,w,h) = cv2.boundingRect(contours)

        if cv2.contourArea(contours) < 1500:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame1, "Status: {}".format('Movement'), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
    # cv2.drawContours(frame1, contours, -1, (0,255, 0), 2)


    cv2.imshow("Imag", frame1)
    frame1 = frame2.copy()
    ret, frame2 = cap.read()

    if not ret or cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release