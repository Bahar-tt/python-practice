def save_number_to_file(number, file_path):
    try:
        # تلاش برای باز کردن فایل
        with open(file_path, 'w') as file:
            file.write(str(number))
        print(f"عدد {number} در فایل '{file_path}' ذخیره شد.")

    except ValueError:
        print("خطا: ورودی شما باید یک عدد باشد.")
    
    except FileNotFoundError:
        print(f"خطا: فایل '{file_path}' پیدا نشد.")
    
    except PermissionError:
        print(f"خطا: شما مجوز دسترسی به فایل '{file_path}' را ندارید.")
    
    except Exception as e:
        # هر خطای غیرمنتظره را می‌گیرد
        print(f"یک خطای غیرمنتظره رخ داد: {e}")


# درخواست ورودی از کاربر
try:
    user_input = input("لطفاً یک عدد وارد کنید: ")
    number = float(user_input)  # تبدیل ورودی به عدد (در صورتی که عدد نباشد، ValueError ایجاد می‌شود)
    save_number_to_file(number, 'output.txt')

except ValueError:
    print("خطا: ورودی شما باید یک عدد باشد.")
