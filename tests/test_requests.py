# test_requests.py
# Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
# Creation date : 2019/05/29
# Last modified : 2019/05/29

import unittest as ut

import requests as req

class Test(ut.TestCase):
    def test_isValidUrl(self):
        url = "https://www.crim.ca/fr"

        self.assertTrue(req.isValidUrl(url))

    def test_getWebsiteHtml(self):
        url = "https://www.crim.ca/fr"

        expected = ""
        self.assertNotEqual(req.getWebsiteHtml(url), expected)

    def test_containsElements(self):
        url = "https://www.crim.ca/fr"
        elements = ["CRIM", "TI"]

        self.assertTrue(req.containsElements(url, elements))

if __name__ == "__main__":
    ut.main()