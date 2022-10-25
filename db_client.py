import requests


out_data = {'Name': "Charlie", "id": 3, "blood_type": "AB-"}
r = requests.post("http://127.0.0.1:5000/new_patient", json=out_data)
