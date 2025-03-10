def calculate_sum(text_lines):
    total_sum = 0     #зберігання загальної суми
    for line in text_lines:
        digit_list = []
        for char in line:
            if char.isdigit(): # Перевіряємо, чи є символ цифрою
                digit_list.append(char)
        if digit_list:
            first_digit = digit_list[0]
            last_digit = digit_list[-1]
            calibration_value = int(first_digit + last_digit)
            total_sum = total_sum + calibration_value
    return total_sum

with open('lab_03/input_3.txt', 'r') as file:
    input_lines = file.readlines()

print(calculate_sum(input_lines))
#55538