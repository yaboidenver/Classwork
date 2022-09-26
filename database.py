def create_patient_entry(f_name, l_name, patient_id, patient_age):
    new_patient = {"First Name": f_name, "Last Name": l_name, "Id": patient_id, "Age": patient_age, "Tests": []}
    return new_patient


def main():
    db = []
    db.append(create_patient_entry("Ann", "Ables", 1, 30))
    db.append(create_patient_entry('Bob', 'Boyles', 2, 34))
    db.append(create_patient_entry('Chris', 'Chou', 3, 25))
    print_data(db)

    add_test(db, 3, 'HDL', 100)
    print(find_pat(db, 3))
    
    print("Patient {} is a {}".format(get_full_name(db[2]), adult_or_minor(db[2])))

#     room_list = ["Room 1", "Room 2", 'Room 3']

#     for i, patient in enumerate(db):
#         print('Name = {}, Room = {}'.format(patient[0], room_list[i]))

#     for patient, room in zip(db, room_list):
#         print('Name = {}, Room = {}'.format(patient[0], room))


def print_data(db):
    for patient in db:
        print('Patient name is {}, patient id is {}, and patient age is {}.'
              .format(get_full_name(patient), patient["Id"], patient["Age"]))


def get_full_name(patient):
        full_name = "{} {}".format(patient["First Name"], patient["Last Name"])
        return full_name


def find_pat(db, id):
    for patient in db:
        if id == patient["Id"]:
            return patient
    return False


def add_test(db, id, test_name, value):
    patient = find_pat(db, id)
    patient["Tests"].append((test_name, value))


def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "adult"
    else:
        return "minor"


if __name__ == '__main__':
    main()
