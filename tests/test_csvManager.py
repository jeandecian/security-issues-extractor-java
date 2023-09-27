# test_csvManager.py
# Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
# Creation date : 2019/05/29
# Last modified : 2019/05/30

import unittest as ut

import csvManager


class Test(ut.TestCase):
    def test_read(self):
        file = csvManager.get_path(["information-system", "test_csvManager"])
        expected_fields = ["firstname", "lastname"]
        expected_contents = [["jean", "decian"]]
        csvManager.save(file, expected_fields, expected_contents)

        fields, contents = csvManager.read(file)
        self.assertEqual(fields, expected_fields)
        self.assertEqual(contents, expected_contents)

    def test_write(self):
        file = csvManager.get_path(["information-system", "test_csvManager"])
        fields, contents = csvManager.read(file)

        expected_fields = ["firstname", "lastname"]
        expected_contents = [["jean", "decian"]]
        self.assertEqual(fields, expected_fields)
        self.assertEqual(contents, expected_contents)


if __name__ == "__main__":
    ut.main()
