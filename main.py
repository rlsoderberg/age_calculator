print("half plus seven calculator")

current_year = int(input('enter current year: '))
younger_birth = int(input('enter younger birth year: '))
older_birth = int(input('enter older birth year: '))
print('in '+str(current_year)+', young is '+str(current_year-younger_birth)+' and old is '+str(current_year-older_birth)+ '\n')
valid_years = []

for x in range (0,50):
    younger_age = (current_year - younger_birth)
    older_age = (current_year - older_birth)
    if (( older_age/2 )+7 <= younger_age):
        valid_years.append(current_year)
    current_year+=1

print('rule becomes valid in ' + str(valid_years[1]))
print('in '+str(valid_years[1])+', young is ' + str(valid_years[1]-younger_birth)+ ' and old is '+ str(valid_years[1]-older_birth))





