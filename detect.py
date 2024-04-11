import cv2
from cvzone.FaceDetectionModule import FaceDetector

screen = cv2.VideoCapture(0)

detector = FaceDetector()

while True:
    _,img = screen.read()
    img,bboxes = detector.findFaces(img,draw=True)

    cv2.imshow("Imagem",img)
    if cv2.waitKey(1) ==27:
        break