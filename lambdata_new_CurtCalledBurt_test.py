"""
unit tests for the functions in lambdata
"""

import unittest
from lambdata_new_CurtCalledBurt.df_utils import train_val_test_split
from lambdata_new_CurtCalledBurt.df_utils import Splitter
from lambdata_new_CurtCalledBurt.df_utils import count_nulls
from lambdata_new_CurtCalledBurt.__init__ import increment

from lambdata_new_CurtCalledBurt.df_utils import test_col_1
from lambdata_new_CurtCalledBurt.df_utils import test_col_2
from lambdata_new_CurtCalledBurt.df_utils import test_col_3
from lambdata_new_CurtCalledBurt.df_utils import test_col_4
from lambdata_new_CurtCalledBurt.df_utils import test_col_5

from lambdata_new_CurtCalledBurt.df_utils import test_1_df
from lambdata_new_CurtCalledBurt.df_utils import test_2_df
from lambdata_new_CurtCalledBurt.df_utils import test_3_df
from lambdata_new_CurtCalledBurt.df_utils import test_4_df
from lambdata_new_CurtCalledBurt.df_utils import test_5_df


class CountNullsTests(unittest.TestCase):
    """Tests the number of counted nulls in count_nulls"""
    def test_nulls_row(self):
        self.assertEqual(count_nulls(test_col_1), 1)
        self.assertEqual(count_nulls(test_col_2), 2)
        self.assertEqual(count_nulls(test_col_3), 3)
        self.assertEqual(count_nulls(test_col_4), 4)
        self.assertEqual(count_nulls(test_col_5), 5)

    def test_nulls_matrix(self):
        self.assertListEqual(count_nulls(test_1_df), [1, 2, 3, 4, 5])
        self.assertListEqual(count_nulls(test_2_df), [2, 3, 4, 5, 1])
        self.assertListEqual(count_nulls(test_3_df), [3, 4, 5, 1, 2])
        self.assertListEqual(count_nulls(test_4_df), [4, 5, 1, 2, 3])
        self.assertListEqual(count_nulls(test_5_df), [5, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()