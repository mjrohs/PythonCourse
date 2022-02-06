# write a program that reads a string from the user containing a date in the form mm/dd/yyyy. it should print the data
# in the format March 12, 2018

def main():
    user_list = get_date()
    # sends user back to input date again if month can't be converted
    if get_month(user_list) == 'Error: Not a valid month':
        print(get_month(user_list))
        user_list = get_date()
    # outputs converted date
    print(get_month(user_list) + ' ' + user_list[1] + ', ' + user_list[2])


# gets a date from user in format mm/dd/yyyy and splits components into list elements using / as separator
def get_date():
    user_date = str(input('Enter date (mm/dd/yyyy): '))
    # validation to ensure exactly 10 elements in string
    while len(user_date) != 10:
        print('Invalid entry. Date must be in format mm/dd/yyyy')
        user_date = str(input('Enter date (mm/dd/yyyy: '))
    date_list = user_date.split('/')
    return date_list


# converts numeric month stored in index 0 of list to English language month
def get_month(date_list):
    if date_list[0] == '01':
        return 'January'
    elif date_list[0] == '02':
        return 'February'
    elif date_list[0] == '03':
        return 'March'
    elif date_list[0] == '04':
        return 'April'
    elif date_list[0] == '05':
        return 'May'
    elif date_list[0] == '06':
        return 'June'
    elif date_list[0] == '07':
        return 'July'
    elif date_list[0] == '08':
        return 'August'
    elif date_list[0] == '09':
        return 'September'
    elif date_list[0] == '10':
        return 'October'
    elif date_list[0] == '11':
        return 'November'
    elif date_list[0] == '12':
        return 'December'
    else:
        return 'Error: Not a valid month'


main()
