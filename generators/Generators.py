def even_numbers():
    num = 0                #اولین عدد زوج
    while True:            #اجرای بی نهایت تابع
        yield num          #در generator function به جای return  از yield استفاده میشه
        num += 2
gen = even_numbers()       #ایجاد یک شی generator که مقداری تولید نکرده
for _ in range(10):
    print (next(gen))       # با next(gen) مقدارها را یکی یکی دریافت می کنیم

    #استفاده ازfor, چون خودش stopIteration  را مدیریت می کند.
# اگر بخواهیم فقط 20 مقدار تولید کنیم و نه بی نهایت:
def even_numbers_limited(n):
    num = 0
    for _ in range(n):
        yield num
        num += 2
gen = even_numbers_limited(20)
print (list(gen)) 
#تولید دنباله فیبوناچی با generator Function
def fibonacci():
    a, b = 0, 1     #دو عدد اول فیبوناچی
    while  True:
        yield a         #اجرای تابع متوقف نمیشه
        a, b = b, a+b
gen = fibonacci()
for _ in range(10):
    print(next(gen))     #اجرای تابع از همان حایی که yield متوقف شده بود ادامه پیدا می کن

#تولید اعداد اول و چاپ ده تای اول
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_numbers():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num +=1
gen = prime_numbers()
for _ in range(10):
    print (next (gen))