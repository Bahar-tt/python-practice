#1
number = list (range (1, 11))
for num in number[:]:
    if num % 2 == 0:
        number.remove(num)
print (number)

#The second method, LIst comprehenshion

numbers = list (range ( 1, 21))
numbers = [num for num in numbers if num % 2 != 0]
print (numbers)

#2
fruits = ["banana", "apple", "cherry", "date"]
fruits.reverse()
print (fruits)

#The second method, Keep the orginal list
fruits = ["banana", "apple", "cherry", "date", "grape"]
fruits = list(reversed (fruits))
print (fruits) 

#3
list = [1, 2, 3, 2, 4, 5, 2, 6, 2, 7, 2]
unique_list = set(list)
for num in unique_list:
    print (f"{num}: {list.count(num)}times")

#4
numbers = [12, 25, 65, 69, 52, 35, 14, 99]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print ("largest num:", largest)

#5
my_list1 = [1, 4, 5, 3, 10, 2]
my_list2 = [7, 6, 8, 9, 10, 5]
combined = sorted(list(set(my_list1+my_list2))) 
print ("newlist is:", combined)