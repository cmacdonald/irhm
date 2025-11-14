import unittest
class TestDataset(unittest.TestCase):

    def test_topics(self):
        import pyterrier as pt
        import os
        username = os.environ["IRHM_TEST_USERNAME"]
        password = os.environ["IRHM_TEST_PASSWORD"]
        dataset = pt.get_dataset("irhm:50pct", user=username, password=password)
        topics = dataset.get_topics("train")
        qrels = dataset.get_qrels("train")
        self.assertTrue(len(topics)> 0)
        self.assertTrue(len(qrels)> 0)
