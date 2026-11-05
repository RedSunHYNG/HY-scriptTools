#成语接龙
cy = input()  #输入第一个成语
last = cy[-1]  #保存第一个成语最后一个字
allcy = cy  #allcy用来保存所有成语,初值为第一个成语
while True:   #无限循环
    ## begin ##
    x=[allcy]
    cy = input()
    if last==cy[0]:
        last = cy[-1]
        x.append(cy)
        allcy = ' '.join(x)
    else:
        break
    ## end  ##
print('接龙结束，所有成语为：'+allcy)  #输出所有成语