def xor_cypher(input_string, key):
    # Convert input strings to bytes
    input_bytes = bytes.fromhex(input_string)
    key_bytes = key.encode('utf-8')

    # Repeat key until it matches the length of the input
    key_bytes = (key_bytes * (len(input_bytes) // len(key_bytes))) + key_bytes[:len(input_bytes) % len(key_bytes)]

    # Perform XOR operation between input bytes and key bytes
    output_bytes = bytes([b ^ k for b, k in zip(input_bytes, key_bytes)])

    # Convert output bytes back to string
    output_string = output_bytes.decode('utf-8')

    return output_string

# Define the encrypted string and the key
encrypted_string = "15 10 11 0C 1D 4E 73 3F 06 07 1D 49 54 59"
key = "Cyber Security"

# Decrypt the string
decrypted_string = xor_cypher(encrypted_string, key)

print(decrypted_string)
