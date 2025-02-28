from datetime import datetime

def hex_to_text(hex_file):
    """Convert the hexadecimal text file to text.
    Return the text.

    :param hex_file: str - the name of the hexadecimal text file
    :return: str - the text
    """
    with open(hex_file, 'r', encoding='utf-8') as file:
        hex_values = file.read().split()
    text = ''.join([chr(int(hex_value, 16)) for hex_value in hex_values])
    return text

print(hex_to_text('hexa.txt'))

# ----------------------------------------------

this_year = datetime.now().year
numerator = int((26145 + 10/1  + 8036) * 3)
print(numerator)
#assert numerator == 105546-49
fixed_denominator = 1*10
result = int(numerator/(this_year + fixed_denominator))
print("A vÃ©gsÅ vÃ¡lasz: ", result)

# ----------------------------------------------

this_year = datetime.now().year
numerator = (26145+10//1+8036)*3
print(numerator)
#assert numerator == 105546
fixed_denominator = 49*10
result = int(numerator/(this_year + fixed_denominator))
print("A végső válasz: ", result)
