# test_csvManager.py
# Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
# Creation date : 2019/05/29
# Last modified : 2019/05/30

import unittest as ut

import csvManager

class Test(ut.TestCase):
    def test_read(self):
        file = csvManager.getPath(["information-system", "test_csvManager"])
        expectedFields = ["firstname", "lastname"]
        expectedContents = [["jean", "decian"]]
        csvManager.save(file, expectedFields, expectedContents)

        fields, contents = csvManager.read(file)
        self.assertEqual(fields, expectedFields)
        self.assertEqual(contents, expectedContents)

    def test_write(self):
        file = csvManager.getPath(["information-system", "test_csvManager"])
        fields, contents = csvManager.read(file)

        expectedFields = ["firstname", "lastname"]
        expectedContents = [["jean", "decian"]]
        self.assertEqual(fields, expectedFields)
        self.assertEqual(contents, expectedContents)

if __name__ == "__main__":
    ut.main()