import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://smart-attendence-system-c51b8-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1BG21EC029":
        {
            "name": "Deepak Aditya Y",
            "major": "ECE",
            "Starting_year": 2021,
            "total_attendance": 0,
            "Standing": "Male",
            "year": 4,
            "last_attendance": "2024-10-15 00:54:34"
        },
    "1BG21EC031":
        {
            "name": "Dheemanth B Gowda ",
            "major": "AI & ML",
            "Starting_year": 2022,
            "total_attendance": 7,
            "Standing": "Male",
            "year": 4,
            "last_attendance": "2022-12-11 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)
