def addition(x,y):
    return x + y

def substraction(x,y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y


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


def main():

    print("These are your choices for the following operations: ")
    print("Enter 1 to make an addition.")
    print("Enter 2 to make a substraction.")
    print("Enter 3 to make a  multiplication.")
    print("Enter 4 to make a division.")

    choice = int_input("Chose an option:", range(1,5))

    if choice == 1:
        first_value = int_input("Enter a number: ", )
        second_value = int_input("Enter a second number: ")
        print first_value, "+", second_value,  "=", addition(first_value, second_value)

    elif choice == 2:
        first_value = int_input("Enter a number: ")
        second_value = int(raw_input("Enter a second number: "))
        print first_value, "-", second_value, "=", substraction(first_value, second_value)

    elif choice == 3:
        first_value = int(raw_input("Enter a number: "))
        second_value = int(raw_input("Enter a second number: "))
        print first_value, "*", second_value, "=", multiplication(first_value, second_value)

    elif choice == 4:
        first_value = int(raw_input("Enter a number: "))
        second_value = int(raw_input("Enter a second number: "))
        print first_value, "/", second_value, "=", division(first_value, second_value)
 
if __name__ == '__main__':
    main()
