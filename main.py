print(">>>calculate when the 'half-your-age-plus-seven' rule becomes valid for a pair of humans")

current_year = int(input('enter current year: '))
younger_birth = int(input('enter younger birth year: '))
older_birth = int(input('enter older birth year: '))
valid_years = []

for x in range (0,50):
    younger_age = (current_year - younger_birth)
    older_age = (current_year - older_birth)
    current_year += 1
    if ((older_age - younger_age) + 7) <= younger_age:
        valid_years.append(current_year)

print('rule becomes valid for these two humans in the year ' + str(valid_years[1]))

    
