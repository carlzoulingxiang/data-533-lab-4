"""
Test class for chararraysearchtool module.

@Author: Nelson Tang
@Date: Dec 03. 2021
"""
import unittest

from arraytools.chararraytools.chararraysearchtool import CharArraySearchTool
from arraytools.chararraytools.chararraysearchtool import NotCharError


class TestCharArraySearchTool(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("######## Start Testing The CharArraySearchTool Module ########")

    @classmethod
    def tearDownClass(cls):
        print("######## Finish Testing The CharArraySearchTool Module ########")

    def setUp(self):
        print("Set Up: Initializing Object...")
        self.t1 = CharArraySearchTool(['a', 'g', 'c', 'e', 'r', 'h'])
        self.t2 = CharArraySearchTool(['o'])
        self.t3 = CharArraySearchTool(['r', 'r', 'e', 'p', 'h'])
        self.t4 = CharArraySearchTool(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        self.t5 = CharArraySearchTool(['a', 'a', 'a'])

    def tearDown(self):
        print("Tear Down: Deleting Object...")
        self.t1 = None
        self.t2 = None
        self.t3 = None
        self.t4 = None
        self.t5 = None

    # test case 1
    # testing function search_min()
    def test_search_min(self):
        self.assertEqual(self.t1.search_min(), 'a')
        self.assertEqual(self.t2.search_min(), 'o')
        self.assertEqual(self.t3.search_min(), 'e')
        self.assertEqual(self.t4.search_min(), 'e')
        self.assertEqual(self.t5.search_min(), 'a')
        # test error handler
        self.t6 = CharArraySearchTool([])
        with self.assertRaises(ValueError):
            self.t6.search_min()

    # test case 2
    # testing function search_max()
    def test_search_max(self):
        self.assertEqual(self.t1.search_max(), 'r')
        self.assertEqual(self.t2.search_max(), 'o')
        self.assertEqual(self.t3.search_max(), 'r')
        self.assertEqual(self.t4.search_max(), 'y')
        self.assertEqual(self.t5.search_max(), 'a')
        # test error handler
        self.t6 = CharArraySearchTool([])
        with self.assertRaises(ValueError):
            self.t6.search_max()

    # test case 3
    # testing function search_key()
    def test_search_key(self):
        self.assertEqual(self.t1.search_key('c'), 2)
        self.assertEqual(self.t2.search_key('c'), -1)
        self.assertEqual(self.t3.search_key('r'), 0)
        self.assertEqual(self.t4.search_key('t'), 4)
        self.assertEqual(self.t5.search_key('a'), 0)
        # test error handler
        with self.assertRaises(NotCharError):
            self.t1.search_key(1)
        with self.assertRaises(NotCharError):
            self.t2.search_key(1)
        with self.assertRaises(NotCharError):
            self.t3.search_key(1)
        with self.assertRaises(NotCharError):
            self.t4.search_key(1)
        with self.assertRaises(NotCharError):
            self.t5.search_key(1)

