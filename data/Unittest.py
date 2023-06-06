import unittest
import os
import pandas as pd
from pandas.testing import assert_frame_equal
import pipeline
import sqlite3
import numpy as np

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Create example dataframes for testing
        self.df1 = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [np.nan, 2, 3, np.nan]})
        self.df2 = pd.DataFrame({'C': [1, 2, np.nan, 4], 'D': [np.nan, 2, 3, np.nan]})


    def test_extraction(self):
        extract = pipeline.extract_data()
        MunsterData, AutoScout24Data = pipeline.extract_data()
        self.assertTrue(MunsterData, msg="Extraction of MunsterData failed :(")
        self.assertTrue(AutoScout24Data, msg="Extraction of AutoScout24Data failed :(")

    # def test_output(self):
    #     directory_path = os.path.join(os.getcwd(), './data')
    #     print(directory_path)
    #     assert os.path.exists(os.path.join(directory_path, "MunsterAutoScout24.db"))

    # def test_transformation(self):
    #     # Connect to the SQLite database
    #     conn = sqlite3.connect('MunsterAutoScout24.db')
    #     # Munster AutoScout24
    #     cur = conn.execute('SELECT Jahr FROM AutoScout24') # if the column name is change then it will fetch else jhar
    #     self.assertTrue(cur,msg=" jhar != year")

    def test_save_to_database(self, mock_to_sql, mock_create_engine):
        # Call the function
        pipeline.save_to_database(self.df1, self.df2)

        # Assert that the correct arguments are passed to to_sql function
        mock_to_sql.assert_any_call('Munster', mock_create_engine.return_value, if_exists='replace')
        mock_to_sql.assert_any_call('AutoScout24', mock_create_engine.return_value, if_exists='replace')




if __name__ == '__main__':
    print("Starting Unit test for Pipeline!")
    unittest.main()
    # test_extraction()
    # test_output()
