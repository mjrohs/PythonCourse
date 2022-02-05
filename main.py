number_males = int(input('How many males are in this class? '))  # gets male and female counts
number_females = int(input('How many females are in this class? '))
class_total = number_males + number_females  # sets total number of people in class
percent_males = (number_males / class_total) * 100  # calculates percentage by sex
percent_females = (number_females / class_total) * 100
print('Percent male: ', format(percent_males, '1.0f'), '%', sep='')  # displays results as whole number
print('Percent female: ', format(percent_females, '1.0f'), '%', sep='')
