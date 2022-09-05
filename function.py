def interface():
    print("Blood Calculator")
    print("Options:")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter your choice: ")
        if choice=='9':
            return

def input_HDL():
    HDL_input = input("Enter the HDL value:")
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

def output_HDL_result(hdl_value,charac):
    print("The results for an HDL value of {} is {}".format(hdl_value, charac))

interface()