def create_patient_entry(f_name, l_name, patient_id, patient_age):
    new_patient = {"First Name": f_name, "Last Name": l_name,
                   "Id": patient_id, "Age": patient_age, "Tests": []}
    return new_patient


def main():
    db = {}
    db[11] = (create_patient_entry("Ann", "Ables", 11, 30))
    db[22] = (create_patient_entry('Bob', 'Boyles', 22, 34))
    db[3] = (create_patient_entry('Chris', 'Chou', 3, 25))
    print_data(db)

    add_test(db, 3, 'HDL', 100)
    print(find_pat(db, 3))

    print("Patient {} is a {}".format(get_full_name(db[22]),
          adult_or_minor(db[22])))


def print_data(db):
    for patient in db.values():
        print('Patient name is {}, patient id is {}, and patient age is {}.'
              .format(get_full_name(patient), patient["Id"], patient["Age"]))


def get_full_name(patient):
    full_name = "{} {}".format(patient["First Name"], patient["Last Name"])
    return full_name


def find_pat(db, id):
    patient = db[id]
    return patient


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
