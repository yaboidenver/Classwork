from flask import Flask, request, josonify


"""
Database format

[{
"name": <string>,
"id": <int>,
"blood_type": <string>,
"test_name": [<string1>, <string2>, ...]
"test_result": [<string1>, <string2>, ...]
}]

"""
db = []

app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_on():
    return "DB server is on"


def add_patient(patient_name, patient_id, blood_type):
    new_patient = {"name": patient_name,
                   "id": patient_id,
                   "blood_type": blood_type,
                   "test_name": [],
                   "test_result": []}
    db.append(new_patient)


def init_server():
    add_patient("Anne Ables", 1, "A+")
    add_patient("Bob Boyles", 2, "B+")
    # initialize logging


@app.route("/new_patient", methods=["POST"])
def add_new_patient_to_server():
    """
    Recieve data from post request
    Call other functions to do all the work
    Return information
    """
    in_data = request.json()
    message, status_code = add_new_patient_worker(in_data)
    return message, status_code


def add_new_patient_worker(in_data):
    result = validate_new_patient_info(in_data)
    if result is not True:
        return result, 400
    add_patient(in_data["name"],
                in_data['id'],
                in_data['blood_type'])
    return "Patient successfully added", 200


def validate_new_patient_info(in_data):
    if type(in_data) is not dict:
        return "POST data was not a dictionary"
    expected_keys = ['name', 'id', 'blood_type']
    for key in expected_keys:
        if key not in in_data:
            return "Key {} is missing from POST data".format(key)
    expected_types = [str, int, str]
    for key, ex_type in zip(expected_keys, expected_types):
        if type(in_data[key]) is not ex_type:
            return "Key {} has the wrong data type".formate(key)
    return True


if __name__ == "__main__":
    init_server()
    app.run()
