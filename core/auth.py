# Author:ZT
import json
import os
import accounts
import logger
BASE_AUTH = os.path.dirname(os.getcwd())+'\\db\\accounts'
user_list = os.listdir(BASE_AUTH)

def auth_login(func):
    def login(*check):
        user = input('请输入账户名：')
        passwd = input('请输入密码：')
        if user+'.json' in user_list:
            if accounts.user_load(user)["access"]:
                if accounts.user_load(user)['password'] == passwd:
                    logger.acc_login(user)
                    func(user,*check)
                else:
                    print('密码错误！！')
            else:
                print("账户已被锁定！")
        else:
            print("用户名错误")
    return login

