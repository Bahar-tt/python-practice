message = """ hello Bahar
           welcome to Conoda and our community
           """
print (message)
#گرفتن عدد از کاربر
number = int (input("Enter a number:"))
#مقدار اولبه مجموع
total = 0
#تا وقتی عدد مثبت باشد
while number > 0:
#اگر عدد فرد باشد
    if number % 2 != 0:
#عدد را به مجموع اضافه کن        
        total += number 
#عددرا یکی کم کن
    number -= 1        
#چاپ مجموع
print (f"The SUM of odd numbers is {total}!!")
    