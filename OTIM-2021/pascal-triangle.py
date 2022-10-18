with open("output-onlinemathtools.txt", "r") as pascals:
    numbers = pascals.read().split(" ")
    numbers = numbers[1:-2]

print(numbers)
result = 0

for num in numbers:
    result += int(num)

print(result)
