from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES


def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext_pad = cipher.decrypt(ciphertext)
    return unpad(plaintext_pad, 16, style = 'pkcs7')


with open('EEPROM_IMG', 'r') as file:
    lines = file.readlines()
    sum_lines = ''
    for line in lines:
        line = "".join(line[5:].split())
        sum_lines = sum_lines + line

for i in range(0,len(sum_lines)-32):
    possible_key = sum_lines[i:i+32]
    possible_key_raw = bytes.fromhex(possible_key)
    try:
        print(decrypt(bytes.fromhex('19DB452EE321ABBF240D9130B7430687'), possible_key_raw))
    except Exception as e:
        pass
