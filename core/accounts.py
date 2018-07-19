# Author:ZT

import json
import os
BASE_ACCOUNTS = os.path.dirname(os.getcwd())+'\\db\\accounts'

def welcome():
    print("欢迎使用zt全自动ATM用户管理系统：\n1.添加账户"
          "\n2.更改用户额度\n3.冻结账户")
    user_choose = input("请选择一项进行操作：(q:退出)")
    return user_choose

def user_load(user):
    os.chdir(BASE_ACCOUNTS)
    with open(user+'.json','r',encoding='utf-8')as f:
        return json.loads(f.read())

def user_dump(user,user_dic):
    os.chdir(BASE_ACCOUNTS)
    with open(user+'.json','w',encoding='utf-8')as f_w:
        f_w.write(json.dumps(user_dic))

def useradd():
    while True:
        user_name = input("创建用户名：")
        if user_name+'.json' in os.listdir(BASE_ACCOUNTS):
            print("用户名已存在，请重新输入!")
        else:
            break
    user_passwd = input("创建密码：")
    user_credit = input("请输入额度(默认15000)")
    user_credit = 15000 if user_credit == '' else int(user_credit)
    user_balance = user_credit
    user_dic={
        "password":user_passwd,
        "credit":user_credit,
        "balance":user_balance,
        "access":True
    }
    user_dump(user_name,user_dic)
    print("%s账户创建成功"%user_name)

def usercredit():
    while True:
        user_name = input("需要修改的账号：")
        if user_name+'.json' in os.listdir(BASE_ACCOUNTS):
            break
        else:
            print("用户名不存在，请重新输入!")
    user_dic = user_load(user_name)
    user_credit = input("请输入额度")
    user_dic["credit"] = int(user_credit)
    user_dump(user_name,user_dic)
    print("%s账户额度修改成功！"%user_name)
def frozenuser():
    while True:
        user_name = input("需要修改的账号：")
        if user_name+'.json' in os.listdir(BASE_ACCOUNTS):
            break
        else:
            print("用户名不存在，请重新输入!")
    user_dic = user_load(user_name)
    user_dic["access"] = False
    user_dump(user_name,user_dic)
    print("账户%s冻结成功！"%user_name)
