x = (1 << 53) + 1
y = (x + 1.0 > x)

z = (2 if isinstance (type, object) else 3) \
    * (round (7 / 2) + round (9 / 2)) \
    * (4 if any ([]) else 5) \
    * (1 if all([]) else 2) \
    * (2 if len("lorem ipsum" * (-1)) > 0 else 3) \
    * (1 if y else 2)

print(z)
