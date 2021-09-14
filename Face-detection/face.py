import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 900)

while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
        cv2.putText(frame, 'Face', (x, y-7), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 2)
        print((x+w/2), (y+h)/2)
        
        center_x = int((x+x+w)/2)
        center_y = int((y+y+h)/2)
        cv2.line(frame, (center_x, center_y), (center_x, center_y), (255,215,0), 20)

    cv2.imshow("My Sunflower", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  #q to quit
        break

cap.release()

cv2.destroyAllWindows()