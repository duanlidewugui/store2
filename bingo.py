#这是一个赌博小游戏，规则如下
#开局你会注册一个账号，账号会有你的名字和密码（密码只支持数字），该游戏支持保存姓名，不保存密码
#游戏开始你会有5000个金币，你可以设置游戏的难度，有低级和普通和高级难度
#低级难度一次消耗100金币，数字范围在0-100之间，猜数次数只有8次，猜中会奖励300金币
#普通难度一次消耗500金币，数字范围在0-1000之间，猜数次数只有15次，猜中会奖励3000金币、
#高级难度一次消耗2000金币，数字范围在0-10之间，猜数次数只有3次，猜中奖励10000金币
#如果在低级难度连续8次没猜中，将从低级难度退出，并且无法再进入低级难度游戏
#如果在普通难度连续15次没猜中，将从普通难度退出，并且无法再进入普通难度游戏
#如果在困难难度连续3次没猜中，将从困难难度退出，并且无法再进入困难难度游戏
#如果三个游戏都无法进入，或者金币小于0，将会从游戏中退出，并显示你最后的金币数
#如果你在非以上情况下，退出了该游戏，会显示你最后的金币数，15000金币以上走的人会被称为赌圣

import random
print("\t\t\t\t\t欢迎进入澳门首家线上赌场\t\t\t\t\t")
name=input("请输入您的姓名：")
password=int(input("请输入您的新密码（只能输入纯数字）："))

password1 = int(input("请再输入您的新密码（只能输入纯数字）；"))

if password == password1:
    log_in = 1
else:
    log_in = 0
    print("你密码都能输错，故意的吧？别来玩了")

gold = 5000
easy = 0
normal = 0
difficult = 0
log_ine = 1
log_inn = 1
log_ind = 1
#次数
log_ins = [easy,normal,difficult]
#猜数范围
a1 = random.randint(0,100)
a2 = random.randint(0,1000)
a3 = random.randint(0,10)
answer = [a1,a2,a3]
#消耗金币数
expend = [100,500,2000]
#最多连续次数
time = [8,15,3]
#奖励
award = [300,3000,10000]
#游玩次数
play = 0

print("简单难度猜0-100的数字，一次消耗100金币，猜中奖励300金币")
print("普通难度猜0-1000的数字。一次消耗500金币，猜中奖励3000金币")
print("困难难度猜0-10的数字，一次消耗2000金币，猜中奖励10000金币")


while log_in>0:

    if log_ins[0] >= 8:
        log_ine = 0
        print("已不能选择简单难度")

    if log_ins[1] >= 13:
        log_inn = 0
        print("已不能选择普通难度")
    if log_ins[2] >= 3:
        log_ind = 0
        print("已不能选择困哪难度")

    if easy>=8 and normal>=13 and difficult>=3:
        print("所有难度皆不能选择，请退出游戏")
        log_in = 0
    elif gold <=0:
        log_in = 0
        print("金币已不足，将退出游戏")
        break
    else:
        log_in = 1





    while log_in > 0:
        print(('你还有', gold, "个金币,普通还有", time[0] - log_ins[0], "次机会，普通还有", time[1] - log_ins[1],
               "次机会，困难还有", time[0] - log_ins[0], "次机会"))
        a1 = random.randint(0, 100)
        a2 = random.randint(0, 1000)
        a3 = random.randint(0, 10)
        answer = [a1, a2, a3]
        print("请输入您想要选择的游戏难度")
        print("输入1是简单，输入2是普通，输入3是困难，输入4是退出该游戏")
        option=int(input("请输入："))
        if option==1 and log_ins[0]==time[0]:
            print("你已无法参加简单难度的游戏")

        elif option == 2 and log_ins[1] == time[1]:
            print("你已无法参加普通难度的游戏")

        elif option == 3 and log_ins[2] ==time[2]:
            print("你已经无法参加苦难难度的游戏")
        elif option == 4:
            print("你将退出游戏")
            log_in = 0
            break
        elif gold<=0:
            print("金币已不足，你甚至还欠我钱，速速出去，莫妨碍我做生意")
            break
        while gold>0 and log_ins[option-1]<=time[option-1]:
             e = int(input("请输入要猜的数字"))
             if answer[option-1]== e:
                 print("恭喜您猜中了，获得了",award[option-1],"个金币")
                 print("您将回到难度选择区域")
                 log_ins[option-1]=0
                 gold = gold +award[option-1]
                 print("你现在有",gold,"个金币")
                 play = play +1
                 break
             elif answer[option-1]>e:
                 print("猜错了，实际的数字更大")
             elif answer[option-1]<e:
                 print("猜错了，实际的数字更小")
             gold = gold - expend[option - 1]
             log_ins[option - 1] = log_ins[option - 1] + 1
             play=play+1
             print("你现在有",gold,"个金币")
             print("还有",time[option-1]-log_ins[option-1],"次机会")
             print("是否要继续，不继续请输入1，继续输入其他数字")
             z = int(input())
             if z == 1:
                 print("将回到选择难度界面")
                 break
if gold<=0:
    print("你总共进行了",play,"次游戏",name,"小赌怡情，大赌伤身啊")
elif gold<15000:
    print("你总共进行了",play,"次游戏",name,"苦海无涯，回头是岸啊")
else:
   print("你总共进行了",play,"次游戏",name,"赌圣大佬慢走，欢迎下次再来")






















