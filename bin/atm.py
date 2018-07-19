# Author:ZT

import os
#获取了相对路径
print(__file__)
#动态获取绝对路径 os.path.abspath
#获取目录名不要文件名：os.path.dirname()
BASE_ATM=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#设置环境变量
BASE_ATM_CONF = BASE_ATM+'\\conf'
BASE_ATM_CORE = BASE_ATM+'\\core'
import sys
sys.path.append(BASE_ATM_CORE)
import main
while True:
    user_choose = main.welcome()
    if user_choose in ['1','2','3','4','5']:
        menu = {
            '1': main.draw,
            '2': main.repay,
            '3': main.transfer,
            '4': main.show_bal,
            '5': main.show_bill
        }
        menu[user_choose]()
        cont = input('是否继续操作(y/n):')
        if (cont == 'n'):
            break
        elif(cont == 'y'):
            pass
        else:
            print("输入不合法")
            break
    elif user_choose == 'q':
        break
    else:
        print("输入不合法，请重新输入")