import cv2

webcamera = cv2.VideoCapture(0)
classificaddorVideoFace = cv2.CascadeClassifier("Haarcascade\haarcascade_frontalface_default.xml")

while True:
    camera, frame = webcamera.read()

    cinza = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)
    detecta = classificaddorVideoFace.detectMultiScale(cinza)
    for(x, y, l, a) in detecta:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (255, 0, 0 ), 2)

    cv2.imshow(" Video WebCamera", frame)

    if cv2.waitKey(1) == ord('f'):
        break

webcamera.release()
cv2.destroyAllWindows()    