dir_sizes = {}
current_path = []

with open("lab_04/input_4.txt") as file:
    for line in file:
        parts = line.split()

        if parts[0] == "$" and parts[1] == "cd":
            if parts[2] == "/":
                current_path = ["/"]
            elif parts[2] == "..":
                current_path.pop()
            else:
                current_path.append(parts[2])

        elif parts[0].isdigit():
            size = int(parts[0])
            for i in range(len(current_path)):
                path = "/".join(current_path[:i+1])
                dir_sizes[path] = dir_sizes.get(path, 0) + size

total = sum(size for size in dir_sizes.values() if size <= 100000)
print("Сума:", total)
# Answer will be: 1453349