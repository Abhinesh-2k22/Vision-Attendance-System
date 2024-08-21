import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://vision-based-attendance-default-rtdb.firebaseio.com/"
})

ref=db.reference('Students')

data={
        "22N201":
        {
            "Name":"Abhinesh K M"
            
    
        },
        "22N204":
        {
            "Name":"Agilan E D"
    
        },
        "22N206":
        {
            "Name":"Akshay A S"
    
        },
        "22N214":
        {
            "Name":"Dhanush A S"
    
        },
        "22N229":
        {
            "Name":"Madhavan"
    
        }
}

for key,value in data.items():
    ref.child(key).set(value)