current_year = 2025
younger_birth = int(input('enter younger birth year: '))
older_birth = int(input('enter older birth year: '))
valid_years = []


for x in range (0,50):
    younger_age = (current_year - younger_birth)
    older_age = (current_year - older_birth)
    current_year += 1
    print('current year: '+str(current_year))
    print('older_age: '+str(older_age))
    print('younger_age: '+str(younger_age))
    print('(older_age - younger_age) + 7): '+str((older_age - younger_age) + 7))
    if ((older_age - younger_age) + 7) <= younger_age:
        valid_years.append(current_year)
        print('valid year!')
    else:
        print('not valid year!')

print('list of valid years: ' + str(valid_years))


    
