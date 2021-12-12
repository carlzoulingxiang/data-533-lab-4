import unittest
from arraytools.numarraytools import numarraysearchtool as numst

class TestNumArraySearchTool(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # print('setup testNumArraySearchTool')
        self.arr1 = [2, 3, 6, 1, 9, 4]
        self.arr2 = [0, 1, -1, 2, -2]
        self.arr3 = [-2, -3, -6, -1, -9, -4]
        self.arr4 = [0, 0, 0, 0, 0, 0]
        self.arr5 = [2]


    @classmethod
    def tearDownClass(cls):
        # print('teardown testNumArraySearchTool')
        pass

    def setUp(self):
        self.numSearch1 = numst.NumArraySearchTool(self.arr1)
        self.numSearch2 = numst.NumArraySearchTool(self.arr2)
        self.numSearch3 = numst.NumArraySearchTool(self.arr3)
        self.numSearch4 = numst.NumArraySearchTool(self.arr4)
        self.numSearch5 = numst.NumArraySearchTool(self.arr5)


    def tearDown(self):
        pass

    def test_searchMin(self):  # test case 1
        self.assertEqual(self.numSearch1.searchMin(), 1)
        self.assertEqual(self.numSearch2.searchMin(), -2)
        self.assertEqual(self.numSearch3.searchMin(), -9)
        self.assertEqual(self.numSearch4.searchMin(), 0)
        self.assertEqual(self.numSearch5.searchMin(), 2)

    def test_searchMax(self):
        self.assertEqual(self.numSearch1.searchMax(), 9)
        self.assertEqual(self.numSearch2.searchMax(), 2)
        self.assertEqual(self.numSearch3.searchMax(), -1)
        self.assertEqual(self.numSearch4.searchMax(), 0)
        self.assertEqual(self.numSearch5.searchMax(), 2)

    def test_searchTarget(self):
        self.assertEqual(self.numSearch1.searchTarget(2), 0)
        self.assertEqual(self.numSearch2.searchTarget(-1), 2)
        self.assertEqual(self.numSearch3.searchTarget(5), -1)
        self.assertEqual(self.numSearch4.searchTarget(0), 0)
        self.assertEqual(self.numSearch5.searchTarget(2), 0)




