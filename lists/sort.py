list = [ (1 , "cherry"), (4 , "banana"),(2, "tananas"), (2, "apple"), (3,"grape")]
sorted_list = sorted (list , key=lambda list : (list[0] , list[1]) , reverse = True)
print (list)
print (sorted_list)