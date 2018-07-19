# Author:ZT
import os
import time
BASE_LOGGER = os.path.dirname(os.getcwd())+'\\logs'

def isFirst(name):
    with open(name,'a+',encoding='utf-8') as f:
        return False if f.tell() else True
def acc_write(s):
    with open('access.log','a+',encoding='utf-8') as f:
        f.write(s)
def tran_write(s):
    with open('transactions.log','a+',encoding='utf-8') as f:
        f.write(s)

def handfile(name):
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    os.chdir(BASE_LOGGER)
    newln = '' if isFirst(name) == True else '\n'
    return newln,nowtime

def acc_login(user):
    user_list = handfile('access.log')
    user_line = user_list[0]+"%s登录了ATM"%user+'\t'+user_list[1]
    acc_write(user_line)
def acc_logout(user):
    user_list = handfile('access.log')
    user_line = user_list[0] + "%s退出了ATM" % user + '\t' + user_list[1]
    acc_write(user_line)
def acc_draw(user,user_draw):
    user_list = handfile('access.log')
    user_line = user_list[0] + "%s取款%d元" % (user,user_draw) + '\t' + user_list[1]
    acc_write(user_line)
def acc_repay(user,user_repay):
    user_list = handfile('access.log')
    user_line = user_list[0] + "%s还款%d元" % (user, user_repay) + '\t' + user_list[1]
    acc_write(user_line)
def acc_transfer(user,user_tranuser,user_tranmon):
    user_list = handfile('access.log')
    user_line = user_list[0] + "%s转账%d元给%s" % (user,user_tranmon,user_tranuser) + '\t' + user_list[1]
    acc_write(user_line)
def acc_show_bal(user):
    user_list = handfile('access.log')
    user_line = user_list[0] + "%s查看余额" % user + '\t' + user_list[1]
    acc_write(user_line)

def acc_show_bill(user,year,month):
    os.chdir(BASE_LOGGER)
    listnum = 0
    print("查询结果如下：")
    with open('transactions.log','r',encoding='utf-8') as f:
        for line in f:
            loglist = line.strip().split('\t')
            _year = int(time.strftime('%Y',time.strptime(loglist[2],'%Y-%m-%d %H:%M:%S')))
            _month = int(time.strftime('%m',time.strptime(loglist[2],'%Y-%m-%d %H:%M:%S')))
            if user == loglist[0] and _year == year and _month ==month :
                print(line.strip())
                listnum +=1
    print('共计%d条记录'%listnum)

def acc_show_bill_log(user):
    user_list = handfile('access.log')
    user_line = user_list[0] + "%s查看账单" % user + '\t' + user_list[1]
    acc_write(user_line)

def acc_shopping(user, check):
    user_list = handfile('access.log')
    user_line = user_list[0] + "%s购物%d元" % (user, check) + '\t' + user_list[1]
    acc_write(user_line)

def tran_draw(user,user_draw,balance):
    user_list = handfile('transactions.log')
    user_line = user_list[0]+user+'\t提现支出%d,余额为%.2f\t'%(user_draw,balance)+user_list[1]
    tran_write(user_line)

def tran_repay(user, user_repay, balance):
    user_list = handfile('transactions.log')
    user_line = user_list[0]+user+'\t还款收入%d,余额为%.2f\t'%(user_repay,balance)+user_list[1]
    tran_write(user_line)

def tran_tran_out(user, user_tranmon,user_tranuser, balance):
    user_list = handfile('transactions.log')
    user_line = user_list[0] + user + '\t转账支出%d给%s,余额为%.2f\t' % (user_tranmon,user_tranuser, balance) + user_list[1]
    tran_write(user_line)

def tran_tran_in(user_tranuser, user_tranmon,user, balance):
    user_list = handfile('transactions.log')
    user_line = user_list[0] + user_tranuser + '\t转账收入%d自%s,余额为%.2f\t' % (user_tranmon,user, balance) + user_list[1]
    tran_write(user_line)

def tran_shopping(user, check, balance):
    user_list = handfile('transactions.log')
    user_line = user_list[0] + user + '\t购物支出%d,余额为%.2f\t' % (check, balance) + user_list[1]
    tran_write(user_line)