# Author:ZT
import auth
import transaction
import logger

def welcome():
    print("欢迎使用zt全自动ATM：\n1.提款"
          "\n2.还款\n3.转账\n4.查询余额\n5.查账单")
    user_choose = input("请选择一项进行操作：(q:退出)")
    return user_choose

@auth.auth_login
def draw(user):
    transaction.draw(user)
@auth.auth_login
def repay(user):
    transaction.repay(user)
@auth.auth_login
def transfer(user):
    transaction.transfer(user)
@auth.auth_login
def show_bal(user):
    transaction.show_bal(user)
@auth.auth_login
def show_bill(user):
    transaction.show_bill(user)
@auth.auth_login
def shopping(user,check):
    transaction.shopping(user,check)
