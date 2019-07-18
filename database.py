# database.py
# Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
# Creation date :  2019/05/17
# Last modified : 2019/05/29

# configurations
HOST = "127.0.0.1"
PORT = 8000
USER = "root"
PASSWD = "jeandeciancrim"
DB = "crim"

DELIMITER = "()"

def join(columns, delimiter):
    # join columns with delimiter
    return delimiter[0] + ", ".join(columns) + delimiter[1]

def createTable(table, columns):
    # create table with columns
    return "CREATE TABLE " + table + " " + join(columns, DELIMITER)

def dropTable(table):
    # drop table if exists
    return "DROP TABLE IF EXISTS " + table

def insertInto(table, columns):
    # insert into table following columns
    return "INSERT INTO " + table + " " + join(columns, DELIMITER) + " VALUES " + join(["%s"] * len(columns), DELIMITER)
