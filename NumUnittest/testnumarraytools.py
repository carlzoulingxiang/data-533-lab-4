import unittest
from arraytools.numarraytools import numarraytools as numtool


class TestNumArrayTools(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('setup testNumArraySearchTool')
        self.arr1 = [2, 3, 6, 1, 9, 4]
        self.arr2 = [0, 1, -1, 2, -2]
        self.arr3 = [-2, -3, -6, -1, -9, -4]
        self.arr4 = ["a", "b", "c", 2, 5]
        self.arr5 = []

    @classmethod
    def tearDownClass(cls):
        print('teardown testNumArraySearchTool')

    def setUp(self):
        self.numTool1 = numtool.NumArrayTools(self.arr1)
        self.numTool2 = numtool.NumArrayTools(self.arr2)
        self.numTool3 = numtool.NumArrayTools(self.arr3)
        self.numTool4 = numtool.NumArrayTools(self.arr4)
        self.numTool5 = numtool.NumArrayTools(self.arr5)


    def tearDown(self):
        pass

    def test_isnumerial(self):  # test case 1
        self.assertTrue(self.numTool1.isnumerial())
        self.assertTrue(self.numTool2.isnumerial())
        self.assertTrue(self.numTool3.isnumerial())
        with self.assertRaises(ValueError):
            self.numTool4.isnumerial()

        self.assertFalse(self.numTool5.isnumerial())

    def test_isnull(self):
        self.assertFalse(self.numTool1.isnull())
        self.assertFalse(self.numTool2.isnull())
        self.assertFalse(self.numTool3.isnull())
        self.assertFalse(self.numTool4.isnull())
        with self.assertRaises(ValueError):
            self.numTool5.isnull()

    def test_append(self):
        self.numTool1.append(100)
        self.assertEqual(self.numTool1.arr, [2, 3, 6, 1, 9, 4, 100])
        self.numTool2.append(100)
        self.assertEqual(self.numTool2.arr, [0, 1, -1, 2, -2, 100])
        self.numTool3.append("x")
        self.assertEqual(self.numTool3.arr, [-2, -3, -6, -1, -9, -4])
        self.numTool4.append(100)
        self.assertEqual(self.numTool4.arr, ["a", "b", "c", 2, 5, 100])
        self.numTool5.append("a")


