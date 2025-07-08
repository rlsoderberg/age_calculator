current_year = 2025
becca_birth = 1994
subject_birth = int(input('enter subject birth year: '))
valid_years = []


for x in range (0,50):
    becca_age = (current_year - becca_birth)
    subject_age = (current_year - subject_birth)
    current_year += 1
    print('current year: '+str(current_year))
    print('subject_age: '+str(subject_age))
    print('becca_age: '+str(becca_age))
    print('(subject_age - becca_age) + 7): '+str((subject_age - becca_age) + 7))
    if ((subject_age - becca_age) + 7) <= becca_age:
        valid_years.append(current_year)
        print('valid year!')
    else:
        print('not valid year!')

print('list of valid years: ' + str(valid_years))


    
