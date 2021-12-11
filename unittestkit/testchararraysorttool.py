"""
Test class for chararraysorttool module.

@Author: Nelson Tang
@Date: Dec 03. 2021
"""
import unittest

from arraytools.chararraytools.chararraysorttool import CharArraySortTool


class TestCharArraySortTool(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
        # print("######## Start Testing The CharArraySortTool Module ########")

    @classmethod
    def tearDownClass(cls):
        pass
        # print("######## Finish Testing The CharArraySortTool Module ########")

    def setUp(self):
        # print("Set Up: Initializing Object...")
        self.t1 = CharArraySortTool(['a', 'g', 'c', 'e', 'r', 'h'], False)
        self.t2 = CharArraySortTool(['o'])
        self.t3 = CharArraySortTool(['r', 'r', 'e', 'p', 'h'])
        self.t4 = CharArraySortTool(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        self.t5 = CharArraySortTool(['a', 'a', 'a'])

    def tearDown(self):
        # print("Tear Down: Deleting Object...")
        self.t1 = None
        self.t2 = None
        self.t3 = None
        self.t4 = None
        self.t5 = None

    # test case 1
    # testing function sort_asc()
    def test_sort_asc(self):
        self.t1.sort_asc()
        self.t2.sort_asc()
        self.t3.sort_asc()
        self.t4.sort_asc()
        self.t5.sort_asc()
        self.assertEqual(self.t1.arr, ['a', 'c', 'e', 'g', 'h', 'r'])
        self.assertEqual(self.t2.arr, ['o'])
        self.assertEqual(self.t3.arr, ['e', 'h', 'p', 'r', 'r'])
        self.assertEqual(self.t4.arr, ['e', 'i', 'o', 'p', 'q', 'r', 't', 'u', 'w', 'y'])
        self.assertEqual(self.t5.arr, ['a', 'a', 'a'])

        self.assertTrue(self.t1.sorted)
        self.assertTrue(self.t2.sorted)
        self.assertTrue(self.t3.sorted)
        self.assertTrue(self.t4.sorted)
        self.assertTrue(self.t5.sorted)

    # test case 2
    # testing function sort_desc()
    def test_sort_desc(self):
        self.t1.sort_desc()
        self.t2.sort_desc()
        self.t3.sort_desc()
        self.t4.sort_desc()
        self.t5.sort_desc()
        self.assertEqual(self.t1.arr, ['r', 'h', 'g', 'e', 'c', 'a'])
        self.assertEqual(self.t2.arr, ['o'])
        self.assertEqual(self.t3.arr, ['r', 'r', 'p', 'h', 'e'])
        self.assertEqual(self.t4.arr, ['y', 'w', 'u', 't', 'r', 'q', 'p', 'o', 'i', 'e'])
        self.assertEqual(self.t5.arr, ['a', 'a', 'a'])
        self.assertTrue(self.t1.sorted)
        self.assertTrue(self.t2.sorted)
        self.assertTrue(self.t3.sorted)
        self.assertTrue(self.t4.sorted)
        self.assertTrue(self.t5.sorted)

    # test case 3
    # testing function unsort()
    def test_unsort(self):
        self.t1.unsort()
        self.t2.unsort()
        self.t3.unsort()
        self.t4.unsort()
        self.t5.unsort()
        self.assertEqual(self.t1.sorted, False)
        self.assertEqual(self.t2.sorted, False)
        self.assertEqual(self.t3.sorted, False)
        self.assertEqual(self.t4.sorted, False)
        self.assertEqual(self.t5.sorted, False)
        self.assertFalse(self.t1.sorted)
        self.assertFalse(self.t2.sorted)
        self.assertFalse(self.t3.sorted)
        self.assertFalse(self.t4.sorted)
        self.assertFalse(self.t5.sorted)
        self.t6 = CharArraySortTool(['a', 'b', 'c'], True)
        self.t6.unsort()

