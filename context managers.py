class MyContextManager:
    def __enter__(self):
        print("Enter the context.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit the context.")
        if exc_type:
            print(f"An exception of type {exc_type} occurred with message: {exc_value}")

with MyContextManager():
    print("Inside the context.")
    # اگر خطایی رخ بدهد، از متد __exit__ استفاده می‌شود.
    # raise ValueError("Something went wrong")
