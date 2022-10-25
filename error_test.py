def function_name():
    try:
        division = "5" / 6
    except TypeError:
        print('Cannot divide string by int')


def main():
    function_name()


if __name__ == "__main__":
    main()
