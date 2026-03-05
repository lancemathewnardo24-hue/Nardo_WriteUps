from pwn  import xor

Key_1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
Key_2and1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
Key_2and3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
final = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

Key_2 = xor(Key_2and1, Key_1)
Key_3 = xor(Key_2, Key_2and3)
flag = xor(final, xor(Key_1, xor(Key_3, Key_2)))

print(flag.decode())