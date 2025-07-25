import unittest
import pandas as pd

from irhm import MyAwesomeTransformer


class TestIrhm(unittest.TestCase):
    def test_something(self):
        # Arrange
        transformer = MyAwesomeTransformer()
        inp = pd.DataFrame()

        # Act
        res = transformer(inp)

        # Assert
        pd.testing.assert_frame_equal(inp, res)
