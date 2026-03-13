from pwn import xor

string = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for key in range(256):
    decoded = xor(string, bytes([key]))  # XOR with the single-byte key
    try:
        text = decoded.decode()        # Convert bytes to string
        if "crypto" in text:         
            print(f"Key: {key} -> {text}")
    except UnicodeDecodeError:
        continue