print("'half-your-age-plus-seven' calculator")

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

print('rule becomes valid in ' + str(valid_years[1]))

    
