# 衣服各种数据的显示
print("---------------------------------------------------------------------------")
print("\t日期\t\t\t服装名称\t\t\t价格/件\t\t\t库存数量\t\t\t销售量/每日\t\t\t")
#衣服的名称数组
char=["T血","衬衫","风衣","牛仔裤","皮草","羽绒服"]
clothing_names = ([char[5],char[3],char[2],char[4],char[0],char[1],
                   char[3],char[5],char[3],char[5],char[3],char[4],
                   char[0],char[2],char[3],char[0],char[5],char[2],
                   char[0],char[3],char[4],char[2],char[0],char[3],
                   char[0],char[2],char[4],char[5],char[0],char[2]])
#衣服的单价
prices = ([253.6,86.3,96.8,135.9,65.8,49.3,86.3,253.6,86.3,253.6,86.3,
           135.9,65.8,96.8,86.3,65.8,253.6,96.8,65.8,86.3,135.9,96.8,
           65.8,86.3,65.8,96.8,135.9,253.6,65.8,96.8])
#库存数量
quantitys = ([500,600,335,855,632,562,600,500,600,500,600,855,632,335,
              600,632,500,335,632,600,855,335,632,600,632,335,855,500,
              632,335])
#销售量
saless = ([10,60,43,63,63,120,72,69,35,140,90,24,45,25,
           60,129,10,43,63,60,63,60,58,140,48,43,57,10,63,78])
#销量的记录表
day = 0
while day<30:
    days=day+1
    print("\t",days,"号\t\t",clothing_names[day],"\t\t\t",
          prices[day],"\t\t\t",quantitys[day],"\t\t\t",saless[day])
    day+=1
#总价
total = 0
day = 0
while day<30:
    i = prices[day]
    k = saless[day]
    total = total+i*k
    day+=1
totals = int(total*10)
total= totals/10
print("该月衣服销量",total,"元")

#平均销售量
average_sales = total/30
average = int(average_sales*10)
average_sales=average/10
print("该月平均每日销售量为",average_sales,"元")


#每日销售额占比  proportion
day = 0
while day<30:
    i = prices[day]
    k = saless[day]
    proportion = i*k/total
    propor = int(proportion*10000)
    propor = propor/100
    print("第",day+1,"日",clothing_names[day],"的销售额占当月的",propor,"%")
    day+=1














