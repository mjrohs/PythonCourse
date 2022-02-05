MONTHS = 12  # constant for months/year
rain_accum = 0.0  # initializes accumulator

number_of_years = int(input('How many years do you want to enter data? '))  # gets number of years

while number_of_years < 1:
    print('error! Data must be entered for at least 1 year!')
    number_of_years = int(input('How many years do you want to enter data? '))

# algorithm for data accumulation
for number in range(0, number_of_years):
    for counter in range(MONTHS):
        monthly_rain = float(input('Enter the rainfall in inches:'))
        rain_accum += monthly_rain
        while monthly_rain < 0:
            print('Error! must enter data for the month.')
            print('If no rainfall occurred, enter 0')
            counter -= 0
            monthly_rain = float(input('Enter the rainfall in inches:'))
            rain_accum += monthly_rain

#   calculates average of all rainfall data
total_months = number_of_years * MONTHS
average_rain = rain_accum / total_months

#   returns calculations
print('Over a period of', total_months, 'months, the total rainfall was:', rain_accum, 'inches')
print('The average rainfall was:', format(average_rain, '.2f'), 'inches')
