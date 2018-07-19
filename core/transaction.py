# Author:ZT
import accounts
import logger
def draw(user):
    user_dic = accounts.user_load(user)
    user_balance = user_dic['balance']
    user_credit = user_dic['credit']/2
    user_limit = user_balance if user_credit>user_balance else user_credit
    print('您的余额为：%.2f'%user_balance)
    user_draw = input('请输入取款金额（0-%.2f）'%round(user_limit,2))
    if int(user_draw)<user_limit and int(user_draw)>0:
        user_balance -=int(user_draw)+float(user_draw)*0.05
        user_dic['balance'] = round(user_balance,2)
        accounts.user_dump(user,user_dic)
        print("取款%d，余额为%.2f"%(int(user_draw),round(user_balance,2)))
        logger.tran_draw(user,int(user_draw),user_dic['balance'])
        logger.acc_draw(user,int(user_draw))
        logger.acc_logout(user)
    else:
        print("不合法数值")
        logger.acc_logout(user)

def repay(user):
    user_dic = accounts.user_load(user)
    user_balance = user_dic['balance']
    user_credit = user_dic['credit']
    user_repay = input("欠款%.2f,请输入还款金额："%round((user_credit-user_balance),2))
    if user_repay.isdigit() and int(user_repay)>0:
        user_balance+=int(user_repay)
        user_dic['balance'] = user_balance
        accounts.user_dump(user,user_dic)
        print("还款成功！欠款为：%.2f"%(user_credit-user_balance))
        logger.tran_repay(user, int(user_repay), user_dic['balance'])
        logger.acc_repay(user,int(user_repay))
        logger.acc_logout(user)
    else:
        print("非法输入！！")
        logger.acc_logout(user)

def transfer(user):
    user_dic = accounts.user_load(user)
    user_balance = round(user_dic['balance'],2)
    print("%s,您的余额为：%.2f"%(user,user_balance))
    import os
    BaseFile = os.path.dirname(os.getcwd())+'\\accounts'
    os.chdir(BaseFile)
    user_list = os.listdir(BaseFile)
    user_tranuser = input("请输入转账账户：")
    if user_tranuser+'.json' in user_list:
        user_tranuser_dic = accounts.user_load(user_tranuser)
        user_tranuser_balance = user_tranuser_dic['balance']
        user_tranmon = input("请输入转账金额(0-%.2f)"%user_balance)
        if int(user_tranmon)<user_balance and int(user_tranmon)>0:
            user_balance -= round(float(user_tranmon),2)
            user_tranuser_balance += round(float(user_tranmon),2)
            user_dic['balance'] = user_balance
            user_tranuser_dic['balance'] = user_tranuser_balance
            accounts.user_dump(user,user_dic)
            accounts.user_dump(user_tranuser,user_tranuser_dic)
            print("%s转账%.2f给%s成功"%(user,round(float(user_tranmon),2),user_tranuser))
            logger.tran_tran_out(user, int(user_tranmon),user_tranuser, user_dic['balance'])
            logger.tran_tran_in(user_tranuser, int(user_tranmon),user, accounts.user_load(user_tranuser)['balance'])
            logger.acc_transfer(user,user_tranuser,int(user_tranmon))
            logger.acc_logout(user)
        else:
            print("输入金额有误")
            logger.acc_logout(user)
    else:
        print("账户名：%s不存在"%user_tranuser)
        logger.acc_logout(user)

def show_bal(user):
    print("余额为：%.2f"%(accounts.user_load(user)['balance']))
    logger.acc_show_bal(user)
    logger.acc_logout(user)

def show_bill(user):
    while True:
        year = int(input("请输入年份："))
        month = int(input("请输入月份："))
        if (year>=1970 and year<=2038) and (month>0 and month<13):
            break
    logger.acc_show_bill(user,year,month)
    logger.acc_show_bill_log(user)
    logger.acc_logout(user)

def shopping(user,check):
    user_dic = accounts.user_load(user)
    user_balance = user_dic['balance']
    if check < user_balance and check > 0:
        user_balance -= check
        user_dic['balance'] = round(user_balance, 2)
        accounts.user_dump(user, user_dic)
        print("支付%d，余额为%.2f" % (check, user_dic['balance']))
        logger.tran_shopping(user, check, user_dic['balance'])
        logger.acc_shopping(user, check)
        logger.acc_logout(user)
    else:
        print("余额不足")
        logger.acc_logout(user)