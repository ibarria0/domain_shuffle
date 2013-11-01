import random
import unittest
from bs4 import BeautifulSoup,SoupStrainer
import domain

class TestDomain(unittest.TestCase):

    def setUp(self):
        self.not_exists = 'undomainquedeseguronoexisteaseguradosiempre.com'
        self.exists = 'prensa.com'
        self.domains = ['uno', 'dos', 'tres']

    def test_is_available(self):
       self.assertTrue(domain.is_available(self.not_exists)) 
       self.assertFalse(domain.is_available(self.exists)) 

    def test_permute(self):
        domains = self.domains
        permuted = domain.permute(domains)
        should_be = ['unodostres.com','dostresuno.com','unotresdos.com','tresdosuno.com','dosunotres.com','tresunodos.com']
        

if __name__ == '__main__':
    unittest.main()
