text = input("请输入: ")
binary = ' '.join(format(byte, '08b') for char in text.encode('utf-8') for byte in bytes([char]))
print(binary)