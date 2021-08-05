import random
print("随机选择人物：1、普通人物 2、稀有人物（初始30） 3、传奇人物（不会减少）")
hero =[10,30,10]
a=random.randint(1,3)
print("您的角色是",a)
b=hero[a-1]
while 1:
    num1=(random.randint(1,50))
    num2=(random.randint(1,50))
    num3=(random.randint(1,50))
    num4=[num1,num2,num3]
    print("请选择一个数字\n(1)",num4[0],"(2)",num4[1],"(3)",num4[2])
    ch=input()
    if ch.isdigit():
        ch=int(ch)
    else:
        print("输入非法字符")
        continue
    co=random.randint(0,1)
    if co==0 or a==3:
        b+=num4[ch-1]
        print("分数增加，当前分数为:",b)
    else:
        b-=num4[ch-1]
        print("分数减少，当前分数为：",b)
    if b>100:
        print("任务成功")
        break
    elif b<=0:
        print("任务失败")
        break