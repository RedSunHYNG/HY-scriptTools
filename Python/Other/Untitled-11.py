# s2-8统计字符个数
s=input("请输入一串字符")
zm,sz,kg,qt = 0,0,0,0    #sz-字母,sz-数字,kg-空格,qt-其它
# 请在下面编写代码
# ********** Begin ********** #
#统计不同字符的个数
i = 0
for i in range(len(s )):
    if 'a' <= s [i] <= 'z' or 'A' <= s [i] <= 'Z':
        qt += 1
    elif '0' <= s [i] <= '9':
        zm += 1
    elif s [i] == ' ':
        sz += 1
    else:
        kg += 1
# ********** End ********** #
# 请不要修改下面的代码
print("\n数字字符{}个，英文字符{}个，空格{}个，其他字符{}个".format(zm,qt,sz,kg))