import os
import pickle
import logging

import pandas as pd
from typing import Any
from sklearn.feature_extraction.text import TfidfVectorizer

from helpers import save, logger


if __name__=='__main__':
  root_data_dir = '/srv/data'
  input_file = os.path.join(root_data_dir, 'ocr_dataset.zip')
  logger.info('Читаем файл из %s', input_file)
  ocr_dataset_df = pd.read_csv(input_file, compression='zip')
  vectorizer = TfidfVectorizer(
      analyzer='word',
      lowercase=True,
      token_pattern=r'\b[\w\d]{3,}\b'
  )

  vectorizer.fit(ocr_dataset_df.text.values)
  
  save(vectorizer, os.path.join(root_data_dir, 'transformer.pkl'))
