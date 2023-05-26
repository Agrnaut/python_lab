from Current_account import Account
from DB import db_create_account, db_get_account, db_update_account
import random


def create_acc_obj(number, name, cpf, balance):
    account = Account(number, name, cpf, balance)
    return account


def create_account():
    name = input("Insert your name: ")
    number = random.randrange(1, 500)
    cpf = int(input("Insert your CPF: "))
    balance = float(input("Insert your balance $: "))
    passwd = int(input("Create your password (only numbers): "))

    db_create_account(name, number, balance, cpf, passwd)

    list_for_obj = show_account(cpf, passwd)
    check_acc = create_acc_obj(list_for_obj[0], list_for_obj[1], list_for_obj[3], float(list_for_obj[2]))
    return check_acc

    # print(list_for_obj)
    print("Account created!")

def show_account(cpf = 0, passwd = 0):
    if(cpf == 0 and passwd == 0):
        cpf = int(input("Please, insert your CPF: "))
        passwd = int(input("Please, insert your passwd: "))
        account = str(db_get_account(cpf, passwd))

        if(account == "[]"):
            print("Invalid password OR CPF !!!")
        else:
            account = account.strip("[()]'")
            account = account.replace("'", "")
            account = account.replace("Decimal", "")
            spl = account.split(',')
            result = []
            text = ['Account_number: ', 'Name: ', 'Balance R$:', 'CPF: ']
            for x in range(0, 4):
                print(f"{text[x].strip()}{spl[x].strip()}")
    else:
        account = str(db_get_account(cpf, passwd))
        if (account == "[]"):
            print("Invalid password OR CPF !!!")
        else:
            account = account.strip("[()]'")
            account = account.replace("'", "")
            account = account.replace("Decimal", "")
            account = account.replace("(", "")
            account = account.replace(")", "")
            spl = account.split(',')
            result = []
            for x in range(0, 4):
                result.append(f"{spl[x].strip()}")
            return result


def edit_account():
    cpf = int(input("Please, insert your CPF: "))
    passwd = int(input("Please, insert your password: "))
    cookie = db_get_account(cpf, passwd)
    if(cookie == []):
        print("Password And/Or CPF Invalid!")
    else:
        operation = int(input("What do you wanna do?\n"
                     "[1] Outdraw money\n"
                     "[2] Deposit money\n"
                     "[3] Change name\n"
                     "Option: "))
        if(operation == 1):
            balance_less = int(input("how much do you wanna draw $: "))
            account_obj.outdraw(balance_less)
            new_balance = account_obj.balance
            db_update_account(passwd, cpf, '', new_balance)
        elif(operation == 2):
            balance_more = int(input("how much do you wanna deposit $: "))
            account_obj.deposit(balance_more)
            new_balance = account_obj.balance
            db_update_account(passwd, cpf, '', new_balance)
        elif(operation == 3):
            name_change = str(input("insert your new name: "))
            account_obj.change_name(name_change)
            new_name = account_obj.name
            db_update_account(passwd, cpf, new_name, 0)
        else:
            print("INVALID OPTION!")


def wanna_loop():
    wanna = int(input("What do you want to do?\n"
                      "[1] Show your account\n"
                      "[2] Edit your account\n"
                      "[3] End session\n"
                      "Option: "))
    if(wanna == 1):
        show_account()
        return False
    elif(wanna == 2):
        edit_account()
    elif(wanna == 3):
        return True
        print("You're Welcome")
    else:
        print("INVALID OPTION_loop")


option = int(input("Are you already a client of ours?\n"
               "[1] Yes\n"
               "[2] No\n"
               "Option:"))
end_of_loop = False

if(option == 1):
    already_cc_cpf = int(input("Please, insert your CPF: "))
    already_cc_passwd = int(input("Please, insert your password: "))
    account_list = show_account(already_cc_cpf, already_cc_passwd)
    account_obj = create_acc_obj(account_list[0], account_list[1], account_list[3], float(account_list[2]))
    while(not end_of_loop):
        end_of_loop = wanna_loop()
elif(option == 2):
    account_obj = create_account()
    while(not end_of_loop):
        end_of_loop = wanna_loop()
else:
    print("INVALID OPTION !")