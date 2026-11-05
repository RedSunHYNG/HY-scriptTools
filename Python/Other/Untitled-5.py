ch = input()
## 请在下面补充代码
### Begin ###
num=ord(ch)
if 48<=num<=57:
    print('数字字符')
elif 65<=num<=90:
    print('大写英文字母')
elif 97<=num<=122:
    print('小写英文字母')
else:
    print('其它字符')
### End ###