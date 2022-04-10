import os
import logging
import pickle
from typing import Any

import pandas as pd

logging.basicConfig(format='%(asctime)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Инициализировали логгер')
ROOT_DATA_DIR = '/srv/data'


def save(source_obj: Any, output_file_path: str):
    with open(output_file_path, 'wb') as f:
        pickle.dump(source_obj, f, protocol=pickle.HIGHEST_PROTOCOL)
        logger.info('%s dumped to %s', source_obj, output_file_path)

def load(input_file_path: str):
    print(os.path.exists(input_file_path))
    with open(input_file_path, 'rb') as f:
        source_obj = pickle.load(f)
        logger.info('loaded from %s', input_file_path)
        return source_obj

def load_dataset():
    input_file = os.path.join(ROOT_DATA_DIR, 'ocr_dataset.zip')
    ocr_dataset_df = pd.read_csv(input_file, compression='zip')

    return ocr_dataset_df

def load_transformer():
    transformer_file = os.path.join(ROOT_DATA_DIR, 'transformer.pkl')
    transformer = load(transformer_file)
    return transformer



