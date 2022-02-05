# get speed and hours traveled from user
speed = int(input('What is the speed of the vehicle in mph? '))
hours = int(input('How many hours has it traveled? '))

# data validation: all values must be > 0
while speed <= 0 or hours <= 0:
    print('Error! values entered must be positive.')
    speed = int(input('What is the speed of the vehicle in mph? '))
    hours = int(input('How many hours has it traveled? '))

# generate table header
print('Hours \t Distance Traveled')
print('--------------------------')

# generate table contents starting at hour 1, continuing until #of hours specified by user
for i in range(1, hours + 1):
    distance_traveled = i * speed
    print(' ', i, '\t\t\t', distance_traveled)
