"""
Test class for chararraytools module.

@Author: Nelson Tang
@Date: Dec 03. 2021
"""
import unittest

from arraytools.chararraytools.chararraytools import CharArrayTools, AppendIntegerError


class TestCharArrayTools(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
        # print("######## Start Testing The CharArrayTools Module ########")

    @classmethod
    def tearDownClass(cls):
        pass
        # print("######## Finish Testing The CharArrayTools Module ########")

    def setUp(self):
        # print("Set Up: Initializing Object...")
        self.t1 = CharArrayTools(['a', 'g', 'c', 'e', 'r', 'h'])
        self.t2 = CharArrayTools([])
        self.t3 = CharArrayTools(['r', 'r', 'e', 'p', 'h'])
        self.t4 = CharArrayTools(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        self.t5 = CharArrayTools(['a', 'g', 'c', 1])

    def tearDown(self):
        # print("Tear Down: Deleting Object...")
        self.t1 = None
        self.t2 = None
        self.t3 = None
        self.t4 = None
        self.t5 = None

    # test case 1
    # testing method __instancecheck__
    def test_instancecheck(self):
        self.assertTrue(self.t1.__instancecheck__())
        self.assertTrue(self.t2.__instancecheck__())
        self.assertTrue(self.t3.__instancecheck__())
        self.assertTrue(self.t4.__instancecheck__())
        self.assertFalse(self.t5.__instancecheck__())

    # test case 2
    # testing function check_empty()
    def test_check_empty(self):
        self.assertFalse(self.t1.check_empty())
        self.assertTrue(self.t2.check_empty())
        self.assertFalse(self.t3.check_empty())
        self.assertFalse(self.t4.check_empty())
        self.assertFalse(self.t5.check_empty())

    # test case 3
    # testing function append()
    def test_append(self):
        self.t1.append('m')
        self.t2.append('m')
        self.t3.append('m')
        self.t4.append('m')
        self.t5.append('m')
        self.assertEqual(self.t1.arr, ['a', 'g', 'c', 'e', 'r', 'h', 'm'])
        self.assertEqual(self.t2.arr, ['m'])
        self.assertEqual(self.t3.arr, ['r', 'r', 'e', 'p', 'h', 'm'])
        self.assertEqual(self.t4.arr, ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'm'])
        self.assertEqual(self.t5.arr, ['a', 'g', 'c', 1, 'm'])

        # test error handler
        with self.assertRaises(AppendIntegerError):
            self.t1.append(1)
        with self.assertRaises(AppendIntegerError):
            self.t2.append(1)
        with self.assertRaises(AppendIntegerError):
            self.t3.append(1)
        with self.assertRaises(AppendIntegerError):
            self.t4.append(1)
        with self.assertRaises(AppendIntegerError):
            self.t5.append(1)


        