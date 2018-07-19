# Author:ZT
import os
import sys
BasePath = os.path.dirname(os.getcwd())+'\\core'
sys.path.append(BasePath)
import accounts
while True:
    user_choose = accounts.welcome()
    if user_choose in ['1','2','3']:
        menu = {
            '1': accounts.useradd,
            '2': accounts.usercredit,
            '3': accounts.frozenuser,
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