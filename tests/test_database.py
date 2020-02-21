# test_database.py
# Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
# Creation date : 2019/05/29
# Last modified : 2019/05/29

import unittest as ut

import database as db

class Test(ut.TestCase):
    def test_join(self):
        columns = ["firstname", "lastname"]
        delimiter = "()"

        expected = "(firstname, lastname)"
        self.assertEqual(db.join(columns, delimiter), expected)

    def test_createTable(self):
        table = "test"
        columns = ["id INT AUTO_INCREMENT PRIMARY KEY", "firstname VARCHAR(255)", "lastname VARCHAR(255)"]

        expected = "CREATE TABLE test (id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255))"
        self.assertEqual(db.createTable(table, columns), expected)

    def test_dropTable(self):
        table = "test"

        expected = "DROP TABLE IF EXISTS test"
        self.assertEqual(db.dropTable(table), expected)

    def test_insertInto(self):
        table = "test"
        columns = ["firstname", "lastname"]

        expected = "INSERT INTO test (firstname, lastname) VALUES (%s, %s)"
        self.assertEqual(db.insertInto(table, columns), expected)

if __name__ == "__main__":
    ut.main()