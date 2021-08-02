import xlrd
data = xlrd.open_workbook('12月份衣服销售数据.xls')
table = data.sheet_by_name('exe')
a=0
b=0
c=0
d=0
f=0
g=0
num={}
for i in range (1,table.nrows):
    for j in range (0,table.ncols):
        print (table.cell(i,j).value,end= ' ')
    print()
    if table.cell(i,1).value == '羽绒服':
        a=a+int(table.cell(i,4).value)
    if table.cell(i,1).value =='牛仔裤':
        b=b+int(table.cell(i,4).value)
    if table.cell(i,1).value =='风衣':
        c=c+int(table.cell(i,4).value)
    if table.cell(i,1).value =='皮草':
        d=d+int(table.cell(i,4).value)
    if table.cell(i,1).value =='T血':
        f=f+int(table.cell(i,4).value)
    if table.cell(i,1).value =='衬衫':
        g=g+int(table.cell(i,4).value)
a1=a*253.6          #羽绒服的总价
b1=b*86.3           #牛仔裤的总价
c1=c*96.8           #风衣的总价
d1=d*135.9          #皮草的总价
f1=f*65.8           #T恤的总价
g1=g*49.3           #衬衫的总价
zj=a1+b1+c1+d1+f1+g1   #总销售量

print('总销售额',zj)
print('衣服销售的总数量',a+b+c+d+f+g)
print('平均销售量',zj/30)
print('羽绒服的占比',a1/zj)
print('牛仔裤的占比',b1/zj)
print('风衣的占比',c1/zj)
print('皮草的占比',d1/zj)
print('T血的占比',f1/zj)
print('衬衫的占比',g1/zj)

