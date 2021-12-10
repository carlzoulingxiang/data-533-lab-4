"""
This is Sample Test Code For arraytools Package

@Author: Nelson Tang, Ling Xiang Zou
@Date: Nov 25, 2021
"""

from arraytools.chararraytools import chararraysearchtool as csearch
from arraytools.chararraytools import chararraysorttool as csort
from arraytools.numarraytools import numarraysearchtool as numst
from arraytools.numarraytools import numarraysorttool as numsort

if __name__ == '__main__':

    """
    The following are sample test to demonstrating how to use the chararraytools package
    """
    charArr = ['e', 'a', 'd', 'c', 'b']
    charArr2 = ['e', 'a', 'd', 'c', 'b']
    # create an object of CharArraySortTool
    charSortTool = csort.CharArraySortTool(charArr)
    charSearchTool = csearch.CharArraySearchTool(charArr2)

    # check all element in this array are char
    if charSortTool.__instancecheck__():
        print("All elements in the sort tool array are character!")
    else:
        print("Character Sort Tool array containing an non-char element!")

    if charSearchTool.__instancecheck__():
        print("All elements in the search tool array are character!")
    else:
        print("Character Search Tool array containing an non-char element!")

    # check whether is an empty array
    if charSortTool.check_empty():
        print("Character Sort Tool array containing an empty array!")
    else:
        print("Character Sort Tool array containing an non-empty array!")

    if charSearchTool.check_empty():
        print("Character Search Tool array containing an empty array!")
    else:
        print("Character Search Tool array containing an non-empty array!")

    # append an new element into array
    charSortTool.append('f')
    charSearchTool.append('t')

    # print the array
    print("Sort tool array: ", charSortTool)
    print("Search tool array: ", charSearchTool)

    # find the max char in array
    maxNum = charSearchTool.search_max()
    print("The max character in Search tool array is: ", maxNum)

    # find the min char in array
    minNum = charSearchTool.search_min()
    print("The min character in Search tool array is: ", minNum)

    # search an target in array
    res = charSearchTool.search_key('c')
    if res == -1:
        print("Target not found!")
    else:
        print("The index of target in search tool array is: ", res)

    # check array is sorted
    if charSortTool.sorted:
        print("sort tool array is sorted!")
    else:
        print("sort tool array is unsorted!")

    # sort array in ascending alphabetical order
    charSortTool.sort_asc()
    print("The ascending sort tool array is: ", charSortTool)

    # sort array in descending alphabetical order
    charSortTool.sort_desc()
    print("The descending sort tool array is: ", charSortTool)

    # unsort this array
    charSortTool.unsort()
    print("The unsorted sort tool array is: ", charSortTool)

"""
The following are the outputs of the above test code:

All elements in the sort tool array are character!
All elements in the search tool array are character!
Character Sort Tool array containing an non-empty array!
Character Search Tool array containing an non-empty array!
Sort tool array:  ['e', 'a', 'd', 'c', 'b', 'f']
Search tool array:  ['e', 'a', 'd', 'c', 'b', 't']
The max character in Search tool array is:  t
The min character in Search tool array is:  a
The index of target in search tool array is:  3
sort tool array is unsorted!
The ascending sort tool array is:  ['a', 'b', 'c', 'd', 'e', 'f']
The descending sort tool array is:  ['f', 'e', 'd', 'c', 'b', 'a']
The unsorted sort tool array is:  ['a', 'e', 'f', 'c', 'd', 'b']
"""


"""
   The following are sample test to demonstrating how to use the chararraytools package
"""

print("----------------------Number Array tools---------------------")

if __name__ == '__main__':
    arr = [2,3,6,1,9,4]
    arr2 = [2,3,6,1,9,4]
    numSort = numsort.NumArraySortTool(arr)
    numSearch = numst.NumArraySearchTool(arr2)

    # check if the elements in the array are integers
    if numSort.isnumerial():
        print("All elements in the sort tool array are integers!")
    else:
        print("Number Sort Tool array containing an non-integer element!")

    if numSearch.isnumerial():
        print("All elements in the search tool array are integers!")
    else:
        print("Number Search Tool array containing an non-integer element!")

        # check whether is an empty array
    if numSort.isnull():
        print("number Sort Tool containing an empty array!")
    else:
        print("number Sort Tool containing an non-empty array!")

    if numSearch.isnull():
        print("number Search Tool containing an empty array!")
    else:
        print("number Search Tool containing an non-empty array!")

    # append an new element into array
    numSort.append(10)
    numSearch.append(11)

    # print the array
    print("Sort tool array: ", numSort.arr)
    print("Search tool array: ", numSearch.arr)

    # find the max char in array
    numMax = numSearch.searchMax()
    print("The max integer in Search tool array is: ", numMax)

    # find the min char in array
    numMin = numSearch.searchMin()
    print("The min integer in Search tool array is: ", numMin)

    print("Sort tool array: ", numSort.arr)
    print("Search tool array: ", numSearch.arr)

    # search an target in array
    numRes = numSearch.searchTarget(6)
    if numRes == -1:
        print("Target in search tool array is not found!")
    else:
        print("The index of target in search tool array is: ", numRes )

    # check array is sorted
    if sorted(numSort.arr) == numSort.arr:
        print("sort tool array is sorted!")
    else:
        print("sort tool array is unsorted!")

    # sort array in ascending alphabetical order
    numSort.AscendingSort()
    print("The ascending sort tool array is: ", numSort.arr)

    # sort array in descending alphabetical order
    numSort.DescendingSort()
    print("The descending sort tool array is: ", numSort.arr)

    # unsort this array
    numSort.Unsort()
    print("The unsorted sort tool array is: ", numSort.arr)

"""
The following are the outputs of the above test code:

All elements in the sort tool array are integers!
All elements in the search tool array are integers!
number Sort Tool containing an non-empty array!
number Search Tool containing an non-empty array!
Sort tool array:  [2, 3, 6, 1, 9, 4, 10]
Search tool array:  [2, 3, 6, 1, 9, 4, 11]
The max integer in Search tool array is:  11
The min integer in Search tool array is:  1
Sort tool array:  [2, 3, 6, 1, 9, 4, 10]
Search tool array:  [2, 3, 6, 1, 9, 4, 11]
The index of target in search tool array is:  2
sort tool array is unsorted!
The ascending sort tool array is:  [1, 2, 3, 4, 6, 9, 10]
The descending sort tool array is:  [10, 9, 6, 4, 3, 2, 1]
The unsorted sort tool array is:  [6, 1, 2, 10, 9, 4, 3]
"""
