import pyterrier as pt
from typing import Iterable

from pyterrier.datasets._builtin import STANDARD_TERRIER_INDEX_FILES

FIFTY_PCT_INDEX_BASE = "http://www.dcs.gla.ac.uk/~craigm/IR_HM/"
FIFTY_PCT_FILES = {
    "index": {
        "ex2" : [(filename, FIFTY_PCT_INDEX_BASE + "index/" + filename) for filename in ["data.meta-0.fsomapfile"] + STANDARD_TERRIER_INDEX_FILES],
        "ex3" : [(filename, FIFTY_PCT_INDEX_BASE + "ex3/" + filename) for filename in ["data.meta-0.fsomapfile", "data-pagerank.oos"] + STANDARD_TERRIER_INDEX_FILES],   
    },
    "topics": { 
            "training" : ("training.topics", FIFTY_PCT_INDEX_BASE + "topics/" + "training.topics", "trec"),
            "validation" : ("validation.topics", FIFTY_PCT_INDEX_BASE + "topics/" + "validation.topics", "trec"),
    },
    "qrels": { 
            "training" : ("training.qrels", FIFTY_PCT_INDEX_BASE + "topics/" + "training.qrels", "trec"),
            "validation" : ("validation.qrels", FIFTY_PCT_INDEX_BASE + "topics/" + "validation.qrels", "trec"),
    }    
}

DATASET_MAP = {
    "50pct" : pt.datasets.RemoteDataset("50pct", FIFTY_PCT_FILES),
}

class IRHMDatasetProvider(pt.datasets.DatasetProvider):
    def get_dataset(self, name: str) -> pt.datasets.Dataset:
        return DATASET_MAP[name]

    def list_datasets(self) -> Iterable[str]:
        return list(DATASET_MAP.keys())