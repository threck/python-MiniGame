import random

level = 0
minnumber = 1
maxnumber = 1
maxnumber_count = 10


print('*******************************')
print('*          猜数游戏           *')
print('*******************************')
print('* 游戏说明：                *')
print('* 1. 请输入数字进行猜数游戏   *')
print('* 2. 游戏中可以随时输入q 退出 *')
print('*******************************')


while True:
    level += 1
    print("")
    print('-----------------------------')
    print('|-|          第{}关        |-|'.format(level))
    print('-----------------------------')

    maxnumber = maxnumber*maxnumber_count
    answer = random.randint(minnumber,maxnumber)
    print("数字范围：（{}-{}）".format(minnumber, maxnumber))
    print("猜猜我心里想的是哪个数字")
    i = 0
    while True:
        guess = input("请输入：")
        try:
            int(guess)
        except:
            if guess == "q":
                break
            else:
                print("错误的输入，请输入数字进行游戏，或者输入q 退出")
        else:
            i = i + 1
            if int(guess) == answer:
                if i <= 2:
                    print("你是我心里的蛔虫吗？")
                elif i >= 10:
                    print("你猜对了，但是猜了太多次，我很失望！！！")
                print('猜对了！！！你猜了{}次'.format(i))
                print('恭喜你完成了第{}关！'.format(level))
                while True:
                    select = input('进入第{}关??\n(y/n):'.format(level+1))
                    if select != 'y' and select != 'n':
                        print("请输入：y 或者 n")
                    else:
                        break
                if select and select == 'n' or select == 'y':
                    break
            elif int(guess) > answer:
                        print("猜大了!你猜了{}次".format(i))
                        print("")
            elif int(guess) < answer:
                        print("猜小了!你猜了{}次".format(i))
                        print("")
            if i == 10:
                print("猜了这么久都猜不对，我很失望！！！\n")
            elif i == 5:
                print("我是不是有点高估你的能力了？？！！！\n")
            elif i == 20:
                print("天啊！！！为什么我要让你来猜数？？\n")

    if guess == 'q' or select and select == 'n':
        print("退出！！")
        print('游戏结束！')
        break


