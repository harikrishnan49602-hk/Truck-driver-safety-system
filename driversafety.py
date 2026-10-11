import cv2
import serial
import time

arduino = serial.Serial('COM6', 9600)
time.sleep(2)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

eye_closed_time = None
sleep_sent = False
awake_sent = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        print("No face")

        if not sleep_sent:
            arduino.write(b'S')
            print("Sent S")
            sleep_sent = True
            awake_sent = False

    else:
        for (x, y, w, h) in faces:
            face_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(face_gray)

            if len(eyes) == 0:
                print("Eyes Closed")

                if eye_closed_time is None:
                    eye_closed_time = time.time()

                elif time.time() - eye_closed_time > 3:
                    if not sleep_sent:
                        print("🚨 DRIVER SLEEPING")
                        arduino.write(b'S')
                        sleep_sent = True
                        awake_sent = False

            else:
                print("Eyes Open")
                eye_closed_time = None

                if not awake_sent:
                    arduino.write(b'R')
                    print("Sent R")
                    awake_sent = True
                    sleep_sent = False

            # Draw face box
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    cv2.imshow("Driver Monitor", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()