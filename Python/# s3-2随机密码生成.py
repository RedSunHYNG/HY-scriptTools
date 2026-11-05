# s3-2随机密码生成

import random    
lt = []
for i in range(48,58):   #48对应'0'的码值,此循环生成列表['0','1'， ...，'9']
    lt.append(chr(i))
#生成列表['0',...'9','A',...,'Z','a', ...,'z']
for i in (65,97):      #65对应'A'的码值，97对应'a'的码值
    for j in range(26):
        lt.append(chr(i+j))
pd = []   #生成一个空列表，用于存放密码
########## 补充代码开始 ##########
n=0
while n<10:
    m=0
    hy=[]
    while m<8:
        hy.append(random.choice(lt))
        redsun =''.join(hy)
        if m==7:
            pd.append(redsun)
        m=m+1
    n=n+1
#print(pd)
########## 补充代码结束 ##########
  