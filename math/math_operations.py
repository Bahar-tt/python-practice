#Make costom modules

def sum_list(numbers):
    return sum(numbers)

def average_list(numbers):
    return sum (numbers) / len (numbers) if numbers else 0

def max_number (a , b):
    return a if a>b else b