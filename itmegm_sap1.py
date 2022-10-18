results = [123456789, ]

while results[-1] != 1:
    #print(results[:-1])
    if results[-1] != 1:
        if results[-1] == 123456789:
            results.append(int(results[-1]*3+1))
            #print(f"1st: {results}")
        elif (results[-2]) % 2 == 0:
            results.append(int(results[-2]/2))
            #print(f"Even: {results}")
        else:
            results.append(int(results[-2]*3+1))
            #print(f"Odd: {results}")

print(f"Sum of elements: {sum(results)}")


code = 130023423

for i in range(0,20):
    code -= 1
    code /= 2

print(code)

for i in range(0,20):
    code = code * 2 + 1

print(code)

deck = list(range(1, 100001))

while len(deck) > 1:
    temp = deck[0]
    deck.append(temp)
    deck.pop(0)
    deck.pop(0)

print(deck)