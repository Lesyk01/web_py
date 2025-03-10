with open("lab_06/input_6.txt", "r") as file:
    lines = file.readlines()

points_X = 1  
points_Y = 2  
points_Z = 3  

total_score = 0  # Підсумковий рахунок

# Проходимося по кожному рядку з файлу
for line in lines:
    opponent_choice, my_choice = line.split()
    
    # Перевіряємо, хто переміг
    if (opponent_choice == 'A' and my_choice == 'X') or \
       (opponent_choice == 'B' and my_choice == 'Y') or \
       (opponent_choice == 'C' and my_choice == 'Z'):
        round_score = 3  # Нічія
    elif (opponent_choice == 'A' and my_choice == 'Y') or \
         (opponent_choice == 'B' and my_choice == 'Z') or \
         (opponent_choice == 'C' and my_choice == 'X'):
        round_score = 6  # Перемога
    else:
        round_score = 0  # Поразка

    if my_choice == "X":         #/
        shape_score = points_X   #/
    elif my_choice == "Y":       #/       # Визначаємо кількість очок за вибір
        shape_score = points_Y   #/
    else:                        #/
        shape_score = points_Z   #/
    total_score += round_score + shape_score
print("Підсумковий рахунок за всі раунди:", total_score)
#8933