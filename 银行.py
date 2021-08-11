
import random,pymysql
db=pymysql.connect(host='localhost',user='root',password='root',db='bank')
cursor = db.cursor()
db_name='工商银行'


def welcome():
    print("************************")
    print("*      中国工商银行       *")
    print("*      账户管理系统       *")
    print("          v1.0          *")
    print("*************************")
    print("*1.开户                  *")
    print("*2.存钱                  *")
    print("*3.取钱                  *")
    print("*4.转账                  *")
    print("*5.查询                  *")
    print("*6.bye!                 *")
    print("*************************")
#开户列表
def bank_adduser(account,username,password,country,provice,street,gate,money):
    global db_name
    #print(account)
    sql="select count(*) from bank"
    cursor.execute(sql)
    data = cursor.fetchall()
    if len(data)>100:
        return 3
    sql="insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param=[account, username, password, country, provice, street, gate, money, db_name]
    cursor.execute(sql,param)
    return 1
#随机account值和判断重复'
def randomcard():
    while 1:
        cardnum=random.randint(10000000000,99999999999)
        sql = "select account from bank"
        cursor.execute(sql)
        data=cursor.fetchall()
        if cardnum not in data and cardnum!=0:
            return  cardnum
#开户操作部分
def adduser():
    username =input("请输入用户名")
    password =int(input("请输入密码"))
    country = input("请输入国籍")
    provice = input("请输入省份")
    street = input("请输入街道")
    gate =input("请输入门牌号")
    money =int(input("请输入余额"))
    account = randomcard()
    #print(account)
    startup =bank_adduser(account,username,password,country,provice,street,gate,money)
    if startup ==3:
        print("用户已满，请去别的银行办理")
    if startup == 1:
        print("开户成功以下是您的开户信息")
        info='''
        ---------个人信息--------
        用户名:%s
        密码:%s
        账号:%s
        国籍:%s
        省份:%s
        街道:%s
        门牌号:%s
        余额:%s
        开户行地址:%s
        ------------------------
        '''
        print(info%(username,password,account,provice,country,street,gate,money,db_name))
 #存钱函数定义
def banke_store(account_one):
    sql="select money from bank where account = %s"
    param=[account_one]
    cursor.execute(sql,param)
    data=cursor.fetchone()
    if not data:
        return 1
    return 0
#存钱的操作
def  store_money():
    account_one=input("请输入账号")
    money_one =int(input("请输入您要存款的金额"))
    startup=banke_store(account_one)
    if startup==1:
        print("您输入的账号不存在")
    if startup==0:
        sql="update bank set money = money + %s where account = %s"
        b=[money_one,account_one]
        cursor.execute(sql,b)
        sql="select money from bank where account = %s"
        b1=[account_one]
        cursor.execute(sql,b1)
        data=cursor.fetchall()
        print("存入成功您当前的余额为:",data[0][0])
#取钱的函数
def bank_dropcash(account,password,cash):
    sql="select * from bank where account = %s"
    a=[account]
    cursor.execute(sql,a)
    data=cursor.fetchall()
    if not data:
        return 1
    sql="select * from bank where account = %s and password = %s "
    param=[account,password]
    cursor.execute(sql,param)
    data=cursor.fetchall()
    if not data:
        return 2
    sql="select money from bank where account = %s"
    a=[account]
    cursor.execute(sql,a)
    data = cursor.fetchone()
    if cash>data[0]:
        return 3
def dropcash():
    account=input("请输入账号")
    password = input("请输入密码")
    cash = int(input("请输入取出的金额"))
    startup = bank_dropcash(account,password,cash)
    if startup == 1:
        print("您输入的账号不存在")
    elif startup == 2:
        print("您输入的密码不正确")
    elif startup ==3:
        print("您的账户余额不足")
    elif startup ==0:
        sql="update bank set money = money - %s where account = %s"
        a=[cash,account]
        cursor.execute(sql,a)
        sql = "select money from bank where account = %s"
        param =[account]
        cursor.execute(sql,param)
        data=cursor.fetchall()
        print("取款成功")
        info='''
        --------取款信息-----------
        账号:%s
        密码:%s
        余额:%s
        -------------------------
        '''
        print(info%(account,password,data[0][0]))
#转账的函数
def bank_transfermoney(cardnum,collection,password,money):
    sql = "select * from bank where account = %s"
    param=[cardnum]
    cursor.execute(sql,param)
    data=cursor.fetchone()
    if not data[0]:
        return 1
    sql = "select * from bank where account = %s"
    param1=[collection]
    cursor.execute(sql,param1)
    data1=cursor.fetchone()
    if not data1:
        return 1
    if cardnum == collection:
        return 4
    sql = "select * from bank where account = %s and password = %s"
    param = [cardnum,password]
    cursor.execute(sql,param)
    data= cursor.fetchone()
    if not data:
        return 2
    sql ="select money from bank  where account = %s"
    param = [cardnum]
    cursor.execute(sql,param)
    data=cursor.fetchone()
    if data[0]<money :
        return 3
    return 0
#转账的操作
def transfermoney():
    cardnum = int(input("请输入账号"))
    collection = int(input("请输入转入账号"))
    password =input("请输入密码")
    money = int(input("请输入转账金额"))
    startup =bank_transfermoney(cardnum,collection,password,money)
    if startup == 1:
        print("账号异常")
    elif startup ==2:
        print("输入密码错误")
    elif startup == 3:
        print("您的账户余额不足")
    elif startup == 4:
        print("操作非法")
    elif startup == 0:
        sql="update bank set money = money - %s where account = %s"
        param=[money,cardnum]
        cursor.execute(sql,param)
        sql = "update bank set money = money + %s where account = %s"
        param=[collection,money]
        cursor.execute(sql,param)
        sql="select money from bank where account = %s"
        param=[cardnum]
        cursor.execute(sql,param)
        data =cursor.fetchall()
        print("转账成功")
        info='''
        -------转账信息-------
        转出账号：%s
        转入账号：%s
        转账金额：%s
        转账后余额：%s
        ---------------------
        '''
        print(info%(cardnum,collection,money,data[0][0]))
#查询的逻辑
def bank_check(account,password):
    sql ="select * from bank where account = %s"
    param = [account]
    cursor.execute(sql,param)
    data = cursor.fetchall()
    print(data)
    if not data:
        return 1
    sql ="select * from bank where account = %s and password = %s"
    param = [account,password]
    cursor.execute(sql,param)
    data = cursor.fetchall()
    if not data:
        return 2
    return 0
#查询的操作
def check():
    account=int(input("请输入账号"))
    password = input("请输入密码")
    startup =bank_check(account,password)
    if startup == 1:
        print("您输入的账号错误")
    elif startup == 2:
        print("您输入的密码错误")
    elif startup == 0:
        sql="select * from bank where account = %s"
        param=[account]
        cursor.execute(sql,param)
        data = cursor.fetchall()
        print(data)
        print("查询成功以下是详细信息")
        info='''
        -------账户信息--------
        账号：%s
        密码：%s
        余额：%s
        用户当前居住地址:%s
        开户行：%s
        ----------------------
        '''
        print(info%(account,password,data[0][7],data[0][3],db_name))

while 1:
    welcome()
    choose=int(input("请输入使用模块"))
    if choose == 1:
        adduser()
        db.commit()
    elif choose == 2:
        store_money()
        db.commit()
    elif choose == 3:
        dropcash()
        db.commit()
    elif choose == 4:
        transfermoney()
        db.commit()
    elif choose == 5:
        check()
        db.commit()
    elif choose == 6:
        cursor.close()
        db.close()
        break
    else:
        print("请从新输入")