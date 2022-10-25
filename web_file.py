import requests


# r = requests.get('https://api.github.com/repos/dward2/BME547/branches')
# print(r)
# print(type(r))
# print(r.text)
# if r.status_code == 200:
#     answer = r.json()
#     print(type(answer))
#     for branch in answer:
#         print(branch["name"])
# else:
#     print("Bad request: {}".format(r.text))

output_info = {"name": "Denver Bradley",
               "net_id": "db402",
               "e-mail": "db402@duke.edu"}

# r = requests.post("http://vcm-21170.vm.duke.edu:5000/student",
#                   json = output_info)
# print(r)

# r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
# print(r.text)

output = {"user": "denver", "message": "Hello :)"}

r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json=output)

r_get = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/denver")
print(r_get.text)
