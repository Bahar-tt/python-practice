#Import modules and test

import math_operations

numbers1 = [4, 7, 1, 9, 3]
numbers2 = [10, 20, 30, 40, 50]

total_sum = math_operations.sum_list(numbers1)
print (f"Sum list {numbers1} is: {total_sum}")

average = math_operations.average_list (numbers2)
print (f"Average list {numbers2} is: {average}")

bigger_number = math_operations.max_number(25 , 17)
print (f"Bigger number between 25 & 17 is: {bigger_number}")
