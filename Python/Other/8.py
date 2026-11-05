# coding=utf-8

# strings用来存储输入的字符串，lst1是将输入的字符串用空格分割，存储为列表
strings = input()
lst1 = strings.split(' ')  #全局变量

# 请在此添加代码，定义函数maxlen()求输入的列表中的最长的元素
########## Begin ##########
def maxlen():
    i=0
    st=''
    while i<len(lst1):
        if len(str(st))<len(str(lst1[i])):
            st=str(lst1[i])
        i=i+1
    return st
########## End ##########
st = maxlen()   #调用函数，得到最长字符串
print(st)
