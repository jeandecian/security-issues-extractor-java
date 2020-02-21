# test_search.py
# Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
# Creation date : 2019/05/29
# Last modified : 2019/05/30

import unittest as ut

import search

class Test(ut.TestCase):

    def test_multiHasDifferentForms(self):
        multi = ["Centre de Recherche Informatique de Montreal", "Ville de Montreal"]
        element = "montreal"

        self.assertTrue(search.multiHasDifferentForms(multi, element))

    def test_contains(self):
        multi = ["Centre de Recherche Informatique de Montreal", "Ville de Montreal"]
        elements = ["de", "Montreal"]

        self.assertTrue(search.contains(multi, elements))
        self.assertTrue(search.contains(multi[0], elements))
        self.assertTrue(search.contains(multi, elements[1]))

    def test_extractElement(self):
        left = "("
        element = "(CRIM)"
        right = ")"

        expected = "CRIM"
        self.assertEqual(search.extractElement(left, element, right), expected)

    def test_extractFile(self):
        text = "(test_search.py)"
        delimiter = "()"
        fileType = ".py"

        expected = "test_search.py"
        self.assertEqual(search.extractFile(text, delimiter, fileType), expected)

    def test_handleExtraction(self):
        paragraph = "(search.py)\n(test_search.py)"
        delimiter = "()"
        fileType = ".py"

        expected = ["search.py", "test_search.py"]
        self.assertEqual(search.handleExtraction(paragraph, delimiter, fileType), expected)

    def test_getFiles(self):
        extraction = ["search.py:20", "test_search.py:20"]

        expected = [["search.py", "20"], ["test_search.py", "20"]]
        self.assertEqual(search.getFiles(extraction), expected)

if __name__ == "__main__":
    ut.main()