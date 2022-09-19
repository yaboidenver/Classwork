def create_patient_entry(patient_name, patient_id, patient_age):
    new_patient = [patient_name, patient_id, patient_age, []]
    return new_patient


def main():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 30))
    db.append(create_patient_entry('Bob Boyles', 2, 34))
    db.append(create_patient_entry('Chris Chou', 3, 25))
    add_test(db, 3, 'HDL', 100)
    print(find_pat(db, 3))

    room_list = ["Room 1", "Room 2", 'Room 3']

    for i, patient in enumerate(db):
        print('Name = {}, Room = {}'.format(patient[0], room_list[i]))

    for patient, room in zip(db, room_list):
        print('Name = {}, Room = {}'.format(patient[0], room))


def print_data(db):
    for i in range(len(db)):
        print('Patient name is {}, patient id is {}, and patient age is {}.'
              .format(db[i][0], db[i][1], db[i][2]))


def find_pat(db, id):
    for patient in db:
        if id == patient[1]:
            return patient
    return False


def add_test(db, id, test_name, value):
    patient = find_pat(db, id)
    patient[3].append((test_name, value))


if __name__ == '__main__':
    main()
