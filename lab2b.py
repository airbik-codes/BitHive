'''
Name: Aakib Kibria Khan
Student ID: 157802224

'''
gross_income=int(input("Enter your gross income $: ")) #taking input from the user and converting it to int

dependents=int(input("Enter the number of dependents: ")) #taking input from the user and converting it to int

tax_rate= 0 #initializing variables

total_tax= 0 #initializing variables

# checking for tax rate
if gross_income<=32000:
    tax_rate=0.1
elif gross_income>32000 and gross_income<=64000:
    tax_rate= 0.15
else:
    tax_rate=0.25
deductibles= 10000 + (2000 * dependents) #calculating deductibles
taxable_income= gross_income - deductibles #calculating taxable income
result= taxable_income * tax_rate # storing the tax amount in result
#checking if tax amount is negative
if result<0:
    total_tax= 0
#printing the tax amaount
else:
    total_tax = result
print("The income tax is $" + str(int(total_tax))+ ".")