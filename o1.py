# Ctrl+/是注释
# a = 73
# a +=1
# print(a)
# age = 24
# name = "小药"              # %s是字符串  %d是整数
# print("我推的名字:%s,年龄:%d"%(name,age))
# a = 123
# print("%6d"%a)            #%nd是多少位数
# a = 123
# print("%06d"%a)
# a = 123
# print("%f"%a)             # %f默认补到6位小数
# a = 123
# print("%.2f"%a)           # %.nf一定要有点，才表示几位小数
# name = "小药"              # 记得加上""
# age = 24
# print(f"我推的名字是{name},他的年龄是{age}")  # f()意思是格式化,要用{}
# + - * /对应加减乘除  # //意思是取整除   # %意思是取余数
#  print(5//2)  输出结果为2  # print(5%2)   输出结果为1
# **的意思是取幂
# print(5**2)  输出为25
# name = input("你的名字:")
# if name == "小药":
#     print("欢迎回家！")
# else:
#     print("回答错误")         # 一定记得加上:  以及格式
# \t的意思为空四格   制表符
# print("小\t药")
# \n为换行符
# print("小药\n你是世界上最萌的人")    输出为两行
# \r的意思为回车，可以用于前面部分无用时
# print("sdhiwkxuw\r小药你是天使")    输出就为小药你是天使
# \\表示为一个\  \\\ == \\   \\\\ == \\
# 想要表示为原本样子，加入r
# print(r"我爱\\\小药")   加上r就是三个\\\
# ==意思为等于   !=意思为不等于  not为假的意思
# a = 555
# b = 111
# print(a == b)  输出为False
# print(a != b)    输出为True
# print(not a == b)  输出为True
# if-else 二选一  if-elif 多选一
# name = input("你的名字是:")
# if name == "逍遥":
#     print("欢迎回家,逍遥!")
# elif name == "莲华渡":
#     print("欢迎回家，莲华渡!")
# else:
#     print("名字错误，请重新输入")
# if 的嵌套结构
# relation = "spouse"
# love = 999
# if love >= 100:
#     print("祝福你们99!",end="")
#     if relation == "spouse" or "sweetheart":
#         print("一定要幸福快乐！")
# else:
#     print("还要多加主动!!!")       # 格式对，逻辑不太对，不用理会
# ctrl+z是撤销的意思

# i = 1
# s = 0                            # s = 0
# while i <= 100:                  # for i in range(1,101):
# while i <= 100:                  #     s += i
#     i += 1                       # print(s)
#     s += i
# print(s)                        # 效果一样，但是for比while更加简单

# i = 1
# while i <= 10:                       # for i in range(1,11):
#     print(f"第{i}次见面")              #     print(f"第{i}此见面")
                                       #     if i == 3:
    # if i == 3:                       #         break
    #     print("互相吸引")
    #     i += 1      / break
    #     continue    /
    # i += 1
# for i in range(1,11):
#     if i == 3:
#         break
#     print(f"第{i}次见面")
# 小练习
# 1.
# name = input("请输入名字:")
# print(f"你好{name}!欢迎来学python")
# num = float(input("请输入:"))
# if num >= 60:
#     print("及格")
# else:
#     print("不及格")
# for i in range(1,6):
#     print(i)
# s = 0
# for i in range(1,11):
#     s += i
# print(s)
# for i in range(2,21,2):
#     print(i)
for i in range(1,31):
    if i % 3 == 0:
        print(i)
# i = int(input("请输入:"))
# for i in range(1,i+1):
#     print(i)




