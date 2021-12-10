import unittest
from arraytools.numarraytools import numarraysorttool as numsort


class TestNumArraySortTool(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('setup testnumarraysorttool')
        self.arr1 = [2, 3, 6, 1, 9, 4]
        self.arr2 = [0, 1, -1, 2, -2]
        self.arr3 = [-2, -3, -6, -1, -9, -4]
        self.arr4 = [0, 0, 0, 0, 0, 0]
        self.arr5 = [2]

    @classmethod
    def tearDownClass(cls):
        print('teardown testnumarraysorttool')

    def setUp(self):
        self.numSort1 = numsort.NumArraySortTool(self.arr1)
        self.numSort2 = numsort.NumArraySortTool(self.arr2)
        self.numSort3 = numsort.NumArraySortTool(self.arr3)
        self.numSort4 = numsort.NumArraySortTool(self.arr4)
        self.numSort5 = numsort.NumArraySortTool(self.arr5)

    def tearDown(self):
        pass

    def test_AscendingSort(self):  # test case 1
        self.numSort1.AscendingSort()
        self.assertEqual(self.numSort1.arr, [1, 2, 3, 4, 6, 9])
        self.numSort2.AscendingSort()
        self.assertEqual(self.numSort2.arr, [-2, -1, 0, 1, 2])
        self.numSort3.AscendingSort()
        self.assertEqual(self.numSort3.arr, [-9, -6, -4, -3, -2, -1])
        self.numSort4.AscendingSort()
        self.assertEqual(self.numSort4.arr, [0, 0, 0, 0, 0, 0])
        self.numSort5.AscendingSort()
        self.assertEqual(self.numSort5.arr, [2])

    def test_DescendingSort(self):
        self.numSort1.DescendingSort()
        self.assertEqual(self.numSort1.arr, [9, 6, 4, 3, 2, 1])
        self.numSort2.DescendingSort()
        self.assertEqual(self.numSort2.arr, [2, 1, 0, -1, -2])
        self.numSort3.DescendingSort()
        self.assertEqual(self.numSort3.arr, [-1, -2, -3, -4, -6, -9])
        self.numSort4.DescendingSort()
        self.assertEqual(self.numSort4.arr, [0, 0, 0, 0, 0, 0])
        self.numSort5.DescendingSort()
        self.assertEqual(self.numSort5.arr, [2])

    def test_Unsort(self):
        self.numSort1.Unsort()
        self.assertNotEqual(self.numSort1.arr, self.arr1)
        self.numSort2.Unsort()
        self.assertNotEqual(self.numSort2.arr, self.arr2)
        self.numSort3.Unsort()
        self.assertNotEqual(self.numSort3.arr, self.arr3)
        self.numSort4.Unsort()
        self.assertEqual(self.numSort4.arr, self.arr4)
        self.numSort5.Unsort()
        self.assertEqual(self.numSort5.arr, self.arr5)



