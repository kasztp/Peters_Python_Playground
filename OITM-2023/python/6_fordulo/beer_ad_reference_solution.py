import statistics

secret_dict = {0: ".", 1: "s", 2: "@", 3: '|', 4: "_", 5: "-", 6: "\\", 7: "/", 8: "", 9: "+", "X": "(", "Y": ")"}

file = open("titok.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()

with open("megfejtes.txt", "w", encoding="utf-8") as file:
    for line_index in range(len(lines)):
        temp_line = lines[line_index].replace("\n", "").split(",")
        original_line = []
        for i in temp_line:
            c, n = i.split(":")
            original_line.append(c*int(n))

        original_line = "".join(original_line)
        original_numbers = [int(item) for item in original_line if item.isnumeric()]
        median = int(statistics.median(original_numbers))
        original_line = original_line.replace(str(median), " ")
        
        for key in secret_dict:
            if key != median:
                original_line = original_line.replace(str(key), str(secret_dict[key]))

        original_line += "\n"            
        file.write(original_line)
