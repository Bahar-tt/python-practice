#Dictionary comprehension
#{key:value for key,value in iterable}


words = ["apple" , "banana" , "cherry" , "date"]
words_lenght = {word:len(word) for word in words}
print (words_lenght)

#2
numbers ={1: "one" , 2: "two" , 3: "three" , 4: "four" , 5: "five" , 6: "six" , 7: "seven" , 8: "eight"}
even_numbers = {num:value for num,value in numbers.items() if num % 2 == 0}
print (even_numbers)

#3
text = "Michigan"
char_count = {char:text.count(char) for char in set(text)}
#تبدیل به مجموعه به دلیل حذف فاصله های بین کلمات و جلوگیری از حطا
print (char_count)
