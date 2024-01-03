name=input("Please enter your name: ")
age=float(input("Now please enter your age: "))
current_year=2024
num=int(input("Enter the number of times you want the message to be printed: "))
year_they_will_turn_hundred=  current_year + (100-age)
for i in range(num):
    print("Hi,",name,"You will turn 100 years old on ",year_they_will_turn_hundred)


