import unittest
import os
import pandas as pd
from sqlalchemy import create_engine


class SystemTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Execute the data pipeline
        os.system("python pipeline.py")

    def test_output_files_exist(self):
        # Check if the output files exist
        self.assertTrue(os.path.exists("MunsterAutoScout24.db"))

    def test_output_data_valid(self):
        # Load the data from the output database
        data_engine = create_engine("sqlite:///MunsterAutoScout24.db")
        munster_df = pd.read_sql_table("Munster", data_engine)
        autoscout_df = pd.read_sql_table("AutoScout24", data_engine)

        # Validate the data
        self.assertIsInstance(munster_df, pd.DataFrame)
        self.assertIsInstance(autoscout_df, pd.DataFrame)
        self.assertGreater(len(munster_df), 0)
        self.assertGreater(len(autoscout_df), 0)

        # You can add further assertions to validate specific columns, data types, etc.

if __name__ == "__main__":
    unittest.main()
