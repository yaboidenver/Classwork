import requests


r = requests.get('http://vcm-7631.vm.duke.edu:5002/get_patients/db402')
patients = r.json()

donor = requests.get(('http://vcm-7631.vm.duke.'
                      'edu:5002/get_blood_type/'+patients['Donor']))
recipient = requests.get(('http://vcm-7631.vm.duke.'
                          'edu:5002/get_blood_type/'+patients['Recipient']))

print(donor.text)
print(recipient.text)

out_data = {"Name": 'db402', "Match": 'No'}
answer = requests.post("http://vcm-7631.vm.duke."
                       "edu:5002/match_check", json=out_data)
print(answer.text)
