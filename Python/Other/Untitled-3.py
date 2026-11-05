js = input('输入购买商品的件数:')
gmje = input('输入购买商品总金额:')
print()
### 补充代码开始 ###
js=int(js)
gmje=float(gmje)
if 5>=js>=2:
    a=float(gmje*0.9)
    b=gmje-a
    print('可得到折扣额=%.2f' % b)
    print('折扣后应付金额=%.2f' % a)
elif js>5:
    a=float(gmje*0.85)
    b=gmje-a
    print('可得到折扣额=%.2f' % b)
    print('折扣后应付金额=%.2f' % a)
else:
    b=0
    print('可得到折扣额=%.2f' % b)
    print('折扣后应付金额=%.2f' % gmje)
### 补充代码结束 ###