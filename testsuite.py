import unittest

from unittestkit.testchararraytools import TestCharArrayTools
from unittestkit.testchararraysearchtool import TestCharArraySearchTool
from unittestkit.testchararraysorttool import TestCharArraySortTool

from NumUnittest.testnumarraytools import TestNumArrayTools
from NumUnittest.testnumarraysearchtool import TestNumArraySearchTool
from NumUnittest.testnumarraysorttool import TestNumArraySortTool



def my_suite():
    suite = unittest.TestSuite()
    results = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestCharArrayTools))
    suite.addTest(unittest.makeSuite(TestCharArraySearchTool))
    suite.addTest(unittest.makeSuite(TestCharArraySortTool))
    suite.addTest(unittest.makeSuite(TestNumArrayTools))
    suite.addTest(unittest.makeSuite(TestNumArraySearchTool))
    suite.addTest(unittest.makeSuite(TestNumArraySortTool))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()