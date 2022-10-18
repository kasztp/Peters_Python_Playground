from math import sqrt

with open("50_million_primes_0.txt", "r") as primes:
    primes_list = primes.read().split(",")

# print(primes_list[1])

six_length_primes = []

for item in primes_list:
    if len(item) == 6:
        six_length_primes.append(item)

# print(len(six_length_primes))

fourteen_sum_numbers = []

for number in six_length_primes:
    digits = 0
    for digit in str(number):
        digits += int(digit)
    if digits == 14:
        fourteen_sum_numbers.append(int(number))

print(len(fourteen_sum_numbers))
print(fourteen_sum_numbers)
# print(fourteen_sum_numbers[0],fourteen_sum_numbers[-1])


odd_squares = []

for number in range(100000, 1000000):
    if number % 2 == 1:
        if sqrt(number) % 1 == 0:
            odd_squares.append(number)

print(len(odd_squares))

valid_primes = []

for prime in fourteen_sum_numbers:
    for index, a in enumerate(odd_squares):
        if index < len(odd_squares)-1:
            if abs(prime - a) == abs(prime - odd_squares[index+1]):
                valid_primes.append(prime)

print(valid_primes)
