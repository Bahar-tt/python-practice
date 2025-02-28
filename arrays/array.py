#import array
#nums = array.array('i' , [int (input(f"number {i+1}:")) for i in range(5)])

#max_value = max (nums)

#print("Maxim number is:" , max_value)

import array
numbers = list (map(int , input("Enter the 5 numbers with space:").split()))

nums = array.array('i' , numbers)

max_value = max(nums)

print("Maxim number is:" , max_value)