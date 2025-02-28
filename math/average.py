numbers = []
while True:
    user_input = input ("Enter a number: (Type 'exite' to quit!)")
    if user_input.lower() == "exit":
       break
    try:
       num = float(user_input)
       numbers.append(num)
    except ValueError:
        print ("Please Enter a Valid Number!")
if numbers:
    average = sum(numbers) / len(numbers)
    print (f"Average numbers is: {average}")
else:
    print ("No Number entered!!")
