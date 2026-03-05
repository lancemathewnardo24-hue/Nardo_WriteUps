from pwn import xor

text = b"label" ## b is for bytes, which is what the xor function takes in as input. If you don't put b, it will be a string and the xor function will not work.
result = xor(text, 13)

print(result.decode())