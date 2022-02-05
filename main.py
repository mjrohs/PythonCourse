# this program calculates calories as a function of fat and carbohydrates consumed in a day

def main():
    fat = get_fat()
    carbs = get_carbs()
    cals_from_fat = calculate_cals_from_fat(fat)
    cals_from_carbs = calculate_cals_from_carbs(carbs)
    output(cals_from_fat, cals_from_carbs)


# gets grams of fat consumed from user input and passes to calculator function
def get_fat():
    fat = int(input('How many grams of fat did you consume today?: '))
    while is_invalid(fat):
        print('Invalid entry. Grams of fat consumed must be greater than or equal to 0')
        fat = int(input('How many grams of fat did you consume today?: '))
    return fat


# gets grams of carbs consumed from user input and passes to calculator function
def get_carbs():
    carbs = int(input('How many grams of carbohydrates did you consume today?: '))
    while is_invalid(carbs):
        print('Invalid entry. Grams of carbohydrates consumed must be greater than or equal to 0')
        carbs = int(input('How many grams of carbohydrates did you consume today?: '))
    return carbs


# data validation. Consumption must be at least 0 for both carbs and fat
def is_invalid(user_entry):
    if user_entry < 0:
        return True
    else:
        return False


# formula for calculating calories from fat = fat (in grams) * 9
def calculate_cals_from_fat(fat):
    cals_from_fat = fat * 9
    return cals_from_fat


# formula for calculating calories from carbs = carbs (in grams) * 4
def calculate_cals_from_carbs(carbs):
    cals_from_carbs = carbs * 4
    return cals_from_carbs


# displays calculations for user
def output(cals_from_fat, cals_from_carbs):
    print()
    print('You have consumed', cals_from_fat, 'calories from fat today.')
    print('You have consumed', cals_from_carbs, 'calories from carbohydrates today.')


main()
