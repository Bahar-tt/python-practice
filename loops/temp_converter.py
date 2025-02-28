def convert_temperature(value, scale):
    if scale.upper() == "C":
        return (value * 9/5) + 32  # تبدیل سلسیوس به فارنهایت
    elif scale.upper() == "F":
        return (value - 32) * 5/9  # تبدیل فارنهایت به سلسیوس
    else:
        return "The scale is invalid. please enter 'C' or 'F' "

temp = float(input("Enter the temperature value: "))
scale = input("Enter the scale (C/F): ")

result = convert_temperature(temp, scale)
print(f"converted temperature: {result}")
