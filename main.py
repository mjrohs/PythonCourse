# Design a program that asks the user to enter a series of 20 numbers. The program should store the numbers in a list
# then display:
# lowest num
# highest num
# total
# average

# constant variable for number of elements allowed in the list
LIST_CONTENTS = 20


def main():
    my_list = get_list()
    print(my_list)
    # prints smallest number in list to console
    print('The lowest number in the list is:', min(my_list))
    # prints largest number in the list to the console
    print('The highest number in the list is:', max(my_list))
    print('The total of the entered numbers is:', total_list(my_list))
    print('The average of the entered numbers is:', format(average_list(my_list), '.2f'))


# fill list with user-generated data
def get_list():
    user_list = []
    i = 0
    # use constant to determine number of iterations
    while i < LIST_CONTENTS:
        try:
            number = int(input('Enter a number:'))
            user_list.append(number)
            i += 1
        # if user enters non-integer type, output error message
        except ValueError:
            print('Invalid entry. You must enter a whole number.')

    return user_list


# adds all numbers in list together and returns the sum
def total_list(user_list):
    total = 0
    for number in user_list:
        total += number
    return total


# uses the sum from total_list() to find and return the average
def average_list(user_list):
    total = total_list(user_list)
    average = total / LIST_CONTENTS
    return average


main()
