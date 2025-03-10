def possible_games_sum(filename):
    limits = {'red': 12, 'green': 13, 'blue': 14}
    total = 0  

    with open(filename) as file:
        for line in file:
            game_id, rounds = line.split(": ")# Розділяємо рядок на ідентифікатор гри та раунди
            game_id = int(game_id.split()[1])  # Беремо число з "Game X"
            rounds_list = []
            for round in rounds.split("; "):  # Розділяємо раунди
                for pair in round.split(", "):  # Розділяємо пари в раунді
                    num, color = pair.split()  # Розділяємо число і колір
                    rounds_list.append((int(num), color))  # Додаємо в список
            if all(num <= limits[color] for num, color in rounds_list):
                total += game_id  # Додаємо ідентифікатор гри до суми

    return total
print(possible_games_sum("lab_05/input_5.txt"))
#2810