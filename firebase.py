import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from run import *

cred = credentials.Certificate("/home/pi/mu_code/hardware-project-fd428-firebase-adminsdk-p2e3f-d9df03cb64.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hardware-project-fd428-default-rtdb.firebaseio.com/'
})

ref = db.reference('/Data')
ref.push({
    'Temperature': celsTemp,
    'Humidity': humidity,
    'CO2': CO2,
    'tVOC': tVOC
})
