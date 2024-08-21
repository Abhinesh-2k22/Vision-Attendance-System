import os
import cv2
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://vision-based-attendance-default-rtdb.firebaseio.com/",
    'storageBucket':"vision-based-attendance.appspot.com"
})

imgfolderpath='Images'
pathlist=os.listdir(imgfolderpath)
imglist=[]
rollno=[]

for path in pathlist:
    imglist.append(cv2.imread(os.path.join(imgfolderpath,path)))
    rollno.append(os.path.splitext(path)[0])
    
    fileName = f'{imgfolderpath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


def createencode(imglist):
    encodelist=[]
    for img in imglist:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodelist.append(encode)

    return encodelist

encodelistknown=createencode(imglist)
encodelistknownwithroll=[encodelistknown,rollno]


file=open("EncodeFile.p",'wb')
pickle.dump(encodelistknownwithroll,file)
file.close()
 