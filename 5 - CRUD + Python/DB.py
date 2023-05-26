import pyodbc

def connection_db():
    conection_data = (
        "Driver={SQL Server};"
        "Server=DESKTOP-FPFEPJ1\SQLEXPRESS;"
        "Database=PythonSQL;"

    )
    return conection_data

def db_create_account(name, number, balance, cpf, passwd):
    connection = pyodbc.connect(connection_db())
    cursor = connection.cursor()

    command = f"""INSERT INTO CheckingAccount(account_number, account_name, account_balance, account_cpf, account_passwd)
    VALUES
	    ({number}, '{name}', {balance}, '{cpf}', {passwd})"""
    cursor.execute(command)
    cursor.commit()

    cursor.close()
    connection.close()

def db_get_account(cpf, passwd):
    connection = pyodbc.connect(connection_db())
    cursor = connection.cursor()

    cpf_to_verify = cpf
    passwd_to_verify = passwd
    command = f"""SELECT * FROM CheckingAccount WHERE account_passwd ='{passwd_to_verify}' AND account_CPF ='{cpf_to_verify}'"""
    cursor.execute(command)
    result = cursor.fetchall()
    return (result)
    cursor.close()
    connection.close()

def db_update_account(passwd, cpf, name = '', value = 0):
    connection = pyodbc.connect(connection_db())
    cursor = connection.cursor()

    #to verify
    value_to_change = value
    name_to_change = name
    passwd_to_verify = passwd
    cpf_to_verify = cpf
    if(name == ''):
        command = f"""UPDATE CheckingAccount SET account_balance = {value_to_change} WHERE account_passwd = '{passwd_to_verify}' AND account_cpf = '{cpf_to_verify}'"""
    else:
        command = f"""UPDATE CheckingAccount SET account_name = '{name_to_change}' WHERE account_passwd = '{passwd_to_verify}' AND account_cpf = '{cpf_to_verify}'"""

    cursor.execute(command)
    cursor.commit()



    cursor.close()
    connection.close()