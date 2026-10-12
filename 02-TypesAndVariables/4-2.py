father_income = 5450
mother_income = 4920
family_members = 5
finc = float(father_income)
minc = float(mother_income)
mem = int(family_members)

total_income = finc + minc
income_per_person = total_income/mem
print('Total family income is', total_income ,' and income per person is', income_per_person)
