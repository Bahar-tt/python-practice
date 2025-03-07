def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()  # تفکیک متن به کلمات
            return len(words)  # شمارش تعداد کلمات
    except FileNotFoundError:
        print(f"خطا: فایل '{file_path}' پیدا نشد.")
    except IOError:
        print("خطا در باز کردن یا خواندن فایل.")
    except Exception as e:
        print(f"یک خطای غیرمنتظره رخ داد: {e}")

# تست تابع
file_path = 'example.txt'  # مسیر فایل خود را اینجا وارد کنید
word_count = count_words_in_file(file_path)

if word_count is not None:
    print(f"تعداد کلمات در فایل: {word_count}")
