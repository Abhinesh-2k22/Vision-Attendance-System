import cv2
import cvzone
import numpy as np
import os
import pickle
import face_recognition

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgbackground=cv2.imread('resources/whitebg.png')

folderpath='resources/modes'
modepathlist=os.listdir(folderpath)
imgmodelist=[]

for path in modepathlist:
    imgmodelist.append(cv2.imread(os.path.join(folderpath,path)))

file=open('EncodeFile.p','rb')
encodelistknownwithroll=pickle.load(file)
file.close()
encodelistknown,rollno=encodelistknownwithroll


while True:
    success,img=cap.read()
    
    img=cv2.resize(img,(480, 360))
    imgs=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    facecurrframe=face_recognition.face_locations(imgs)
    encocurrframe=face_recognition.face_encodings(imgs,facecurrframe) 
    
    imgbackground[150:150 + 360, 55:55 + 480]=img
    imgbackground[160:160 + 360, 760:760 + 480]=imgmodelist[1]


    for ef,fl in zip(encocurrframe,facecurrframe):
        matches=face_recognition.compare_faces(encodelistknown,ef)
        facedis=face_recognition.face_distance(encodelistknown,ef)
        matchindex=np.argmin(facedis)

        if matches[matchindex]:
            print(rollno[matchindex])
            y1,x2,y2,x1 = fl
            bbox= 55+x1,150 +y1,x2-x1,y2-y1
            imgbackground = cvzone.cornerRect(imgbackground,bbox,rt=0)

    cv2.imshow("face attendance",imgbackground)
    cv2.waitKey(1)