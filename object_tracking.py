import cv2
import time
import math

fridayX = 530
fridayY = 300

porondeandationX = []
porondeandationY = []

video = cv2.VideoCapture("bb3.mp4")

tracker = cv2.TrackerCSRT_create()

returned, img = video.read()

bbox = cv2.selectROI("Rastreando", img, False)

tracker.init(img, bbox)

print(bbox)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x,y), ((x+w), (y+h)), (255,0,255), 3, 1)
    cv2.putText(img, "Rastreandation........", (75,90), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0,255,0), 2)

def acertation(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    positionationX = x + int(w/2)
    positionationY = y + int(h/2)
    cv2.circle(img, (positionationX, positionationY), 2, (0, 0, 255), 5)
    cv2.circle(img, (fridayX, fridayY), 2, (0, 0, 255), 5)
    disStancia = math.sqrt(((positionationX - fridayX)**2)+((positionationY - fridayY)**2))
    print(disStancia)
    if disStancia<= 20:
        cv2.putText(img, "acertou, cesta ou alguma coisa legal ai.", (300,90), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0,255,0), 2)
    porondeandationX.append(positionationX)
    porondeandationY.append(positionationY)
    for i in range (len(porondeandationX)-1):
        cv2.circle(img, (porondeandationX[i], porondeandationY[i]), 2, (0, 0, 255), 5)


while True:
    check,img = video.read() 

    success, bbox = tracker.update(img)  

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "Errroooooooou", (75,90), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0,0,255), 2)

    acertation(img, bbox)

    cv2.imshow("resultado",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Interrompido!")
        break


video.release()
cv2.destroyALLwindows()



