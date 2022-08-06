calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(number_of_days):

    return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculate_value = days_to_units(user_input_number)
            print(calculate_value)

        elif user_input_number == 0:
            print("You enter Zero. No convert for you")

        else:
            print("You have entered a negative number that cannot be converted for you")

    except ValueError:
        if user_input == "exit":
            print("Good bye")
        else:
            print("Your input is not a number. Don't ruin my program")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number of day and i will convert it to hours: ")
    list_of_days = user_input.split(",")

    # print(list_of_days)
    # print(set(list_of_days))
    #
    # print(type(list_of_days))
    # print(type(set(list_of_days)))

    for num_of_days_element in set(list_of_days):
        validate_and_execute()







