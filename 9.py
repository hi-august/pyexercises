#coding=utf-8

f = open('9.txt','w') # 打开文件
f.write('9*9乘法口诀' + '\n') # 写入单行数据
for i in range(1, 10):
    for j in range(1, i + 1):
        if i != j:
            data =  '%d * %d' %(j,i) + ' = ' + str(i*j) + '\n'
            f.writelines(data) # 逐行写入
            print data # 打印





