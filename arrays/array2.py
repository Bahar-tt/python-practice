import array

arr1 = array.array('i' , [int (input (f"Number of arr1 {i+1}:")) for i in range(5)])
arr2 = array.array('i' , [int (input (f"Number of arr2 {i+1}:")) for i in range(5)])

arr3 = array.array('i' , [arr1[i] + arr2[i] for i in range(5)])

print ("Array3 :",arr3)
