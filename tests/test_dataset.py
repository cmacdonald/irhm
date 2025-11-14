import unittest
class TestDataset(unittest.TestCase):

    def test_topics(self):
        import pyterrier as pt
        import os
        username = os.environ["IRHM_TEST_USERNAME"]
        password = os.environ["IRHM_TEST_PASSWORD"]
        topics = pt.get_dataset("irhm:50pct").get_topics("train", user=username, password=password)
        qrels = pt.get_dataset("irhm:50pct").get_qrels("train", user=username, password=password)
        self.assertTrue(len(topics)> 0)
        self.assertTrue(len(qrels)> 0)
