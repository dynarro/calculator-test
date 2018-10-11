import sys

def addition(x,y):
    return x + y

def substraction(x,y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

# Gets an input from the user. If the choice is wrong it automatically asks again without stopping the program
def int_input(msg, num_range=None, loop=True):
    choice = None

    while choice is None:
        try:
            choice = int(raw_input(msg))
            if num_range and choice not in num_range:
                raise ValueError
        except ValueError:
            if not loop:
                raise

            choice = None
            print("Wrong choice. Try again!")

    return choice

# Assumes that interactive is always true, but if a file is given, it takes the values within the file.
def get_values(interactive=True):
    if interactive:
        first_value = int_input("Enter a number: ", )
        second_value = int_input("Enter a second number: ")
    else:
        with open(sys.argv[1]) as f:
            vals = f.readlines()
            # If there is less than 2 lines in the file, it shows an error.
            if len(vals) < 2:
                raise RuntimeError("Not enough numbers")
            first_value, second_value = int(vals[0]), int(vals[1])
    return first_value, second_value

def main():

    print("These are your choices for the following operations: ")
    print("Enter 1 to make an addition.")
    print("Enter 2 to make a substraction.")
    print("Enter 3 to make a  multiplication.")
    print("Enter 4 to make a division.")

    choice = int_input("Choose an option:", range(1,5))

    # If the commands given don't include a file, then it assumes it's interactive.
    interactive = not len(sys.argv) > 1

    if choice == 1:
        first_value, second_value = get_values(interactive)
        print first_value, "+", second_value,  "=", addition(first_value, second_value)

    elif choice == 2:
        first_value, second_value = get_values(interactive)
        print first_value, "-", second_value, "=", substraction(first_value, second_value)

    elif choice == 3:
        first_value, second_value = get_values(interactive)
        print first_value, "*", second_value, "=", multiplication(first_value, second_value)

    elif choice == 4:
        first_value, second_value = get_values(interactive)
        print first_value, "/", second_value, "=", division(first_value, second_value)


if __name__ == '__main__':
    main()
