import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 900)

while True:    
    ret, frame = cap.read()
    cv2.imshow("My Sunflower", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  #q to quit
        break

cap.release()

cv2.destroyAllWindows()