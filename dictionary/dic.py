book = {
    "title": "Shazde Kuchulu",
    "author": "Antovan du Sent",
    "year": 1943
}
print ("Information Book:")
print (book)

#2
student = {
    "name" : "Bahar",
    "age" : 36,
    "city" : "Turento",
    "grade" :"A"
}
num_keys = len (student.keys())
num_values = len (student.values())

print ("Num of keys:" , num_keys)
print ("Num of values:" , num_values)

#3
ages = {
    "Bahar":36,
    "Taher":8,
    "Taha":8,
    "Helma":1,
    "Mahdiyar":7,
    "yeganeh":16,
    "Mahsa":17
}
name = input("Enter the name:")

if name in ages:
    print (f"{name} is {ages[name]} years old!")
else:
    print ("The is not to Dic!!")

#Dictionary_Comprehension
people = {
    "Bahar":36,
    "Taher":8,
    "Taha":8,
    "Helma":1,
    "Mahdiyar":7,
    "yeganeh":16,
    "Mahsa":18
}
result = {name : age for name , age in people.items() if age >= 15}
print (result)
