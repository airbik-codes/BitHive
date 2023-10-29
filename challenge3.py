
'''
Name: Aakib Kibria Khan
Student_ID: 157802224
'''


#prompting the user to input a decimal number and converting it to an integer and assigning it to the variable
decimal_number= int(input("Enter a decimal number."))
#initialize an empty string called binary_number to store the binary representation of the decimal number.
binary_number=""

#loop that continues as long as decimal_number is greater than or equal to 1.

while decimal_number>=1:
  #calculates the remainder when decimal_number is divided by 2.
  remainder=decimal_number%2
  # It converts the remainder to an integer, then to a string, and appends it to the beginning of the binary_number string.
  binary_number=str(int(remainder))+ binary_number
  #This line divides decimal_number by 2 using integer division (//). This updates decimal_number to the quotient, which will be used in the next iteration of the loop.
  decimal_number= decimal_number//2
  #loop completes, we add the most significant bit to the binary representation by prepending "1" to the binary_number string. This is because the loop exits when the quotient becomes 1
binary_number="1"+binary_number
print(binary_number) #printinng the binary number