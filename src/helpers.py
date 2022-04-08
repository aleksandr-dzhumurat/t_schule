import os

import logging
import pickle

from typing import Any

logging.basicConfig(format='%(asctime)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Инициализировали логгер')


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