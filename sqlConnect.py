# sqlConnect.py
# Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
# Creation date : 2019/05/17
# Last modified : 2019/05/30

import pymysql.cursors

import database as db

def checkValuesValidity(columns, values):
    # print if errors
    for row in values:
        if (len(columns) != len(row)):
            print("[MySQL] Columns and Row aren't of same size")
            print(columns)
            print(row)
            break

def connect():
    # connection to database
    return pymysql.connect(host = db.HOST, port = db.PORT, user = db.USER, passwd = db.PASSWD, db = db.DB)

def save(table, tableColumns, columns, values):
    # save values in database
    connection = connect()
        
    try:
        with connection.cursor() as cursor:
            cursor.execute(db.dropTable(table))
            cursor.execute(db.createTable(table, tableColumns))

            checkValuesValidity(columns, values)
            cursor.executemany(db.insertInto(table, columns), values)
            print("[MySQL] Finished saving " + table + " (" + str(len(values)) + " entries)")

        connection.commit()
            
    finally:
        connection.close()
