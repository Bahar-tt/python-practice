#numbers =  input ("Enter numbers separated by space:").split()
#new_numbers = set (map (int , numbers))
#print ("New numbers:" , new_numbers)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print ("Union:" , A | B)

print ("Intersection:" , A & B)

print ("Difference A-B:" , A - B)
print ("Difference B-A:" , B - A)

print ("SymmetricDifference:" , A ^ B)