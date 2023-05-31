import unittest
import os
import pandas as pd
from pandas.testing import assert_frame_equal
import pipeline
import sqlite3

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_extraction(self):
        extract = pipeline.extract_data()
        self.assertTrue(extract, msg="Extraction failed :(")

    # def test_output(self):
    #     directory_path = os.path.join(os.getcwd(), './data')
    #     print(directory_path)
    #     assert os.path.exists(os.path.join(directory_path, "MunsterAutoScout24.db"))






if __name__ == '__main__':
    print("Starting Unit test for Pipeline!")
    unittest.main()
    # test_extraction()
    # test_output()
