'''
Name: Aakib Kibria Khan
Student ID: 157802224

'''

number=float(input("Enter a decimal number: ")) #taking input from user and converting it to float

#adding 0.5 to the decimal_number because if the decimal part of the number is less than 0.5 then adding 0.5 to it won't change its integer part but 
#if the decimal  part of the number is greater than or equal to 0.5, adding 0.5 to it will change its integer part
#then using the int() function to remove the decimal part

rounded_integer= int((number + 0.5))



print("Rounded integer: " + str(rounded_integer))
