#جمع ارقام عدد
#گرفتن عدد از کاربر
number = int (input("Enter a number:"))
#مقدار اولبه مجموع
total = 0
while number > 0:
    digit = number % 10     #گرفتن رقم آخر عدد
    total += digit          #اضافه کردن رقم به مجموع
    number //= 10           #حذف رقم آخر عدد
print (f"The sum of the digits is: {total}")


