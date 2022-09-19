def interface():
    print("Blood Calculator")
    print("Options:")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
    print("3-Analyze Cholesterol")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_Driver()
        elif choice == '2':
            LDL_Driver()
        elif choice == '3':
            Chol_driver()


def input_HDL():
    HDL_input = input("Enter the HDL value: ")
    return int(HDL_input)


def check_HDL(HDL_input):
    if HDL_input >= 60:
        return "Normal"
    elif HDL_input >= 40:
        return "Borderline low"
    else:
        return "Low"


def HDL_Driver():
    hdl_value = input_HDL()
    answer = check_HDL(hdl_value)
    output_HDL_result(hdl_value, answer)


def output_HDL_result(hdl_value, charac):
    print("The results for an HDL value of {} is {}".format(hdl_value, charac))


def input_LDL():
    LDL_input = input("Enter the LDL value: ")
    return int(LDL_input)


def check_LDL(LDL_input):
    if LDL_input >= 190:
        return "Very High"
    elif LDL_input >= 160:
        return "High"
    elif LDL_input >= 130:
        return "Borderline High"
    else:
        return "Normal"


def LDL_Driver():
    ldl_value = input_LDL()
    answer = check_LDL(ldl_value)
    output_LDL_result(ldl_value, answer)


def output_LDL_result(ldl_value, charac):
    print("The results for an LDL value of {} is {}".format(ldl_value, charac))


def input_cholesterol():
    Chol_input = input("Enter cholesterol:")
    return int(Chol_input)


def check_Chol(cholesterol):
    if cholesterol < 200:
        return "Normal"
    elif cholesterol >= 240:
        return "High"
    elif cholesterol >= 200 < 240:
        return "Borderline High"


def Chol_driver():
    Chol = input_cholesterol()
    answer = check_Chol(Chol)
    output_cholesterol_results(Chol, answer)


def output_cholesterol_results(cholesterol_level, ans):
    print("The results for a Cholesterol value of {} are {}"
          .format(cholesterol_level, ans))


if __name__ == '__main__':
    interface()
