import os
import pickle

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

logging.basicConfig(format='%(asctime)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Инициализировали логгер')

def save(source_obj: Any, output_file_path: str):
    with open(output_file_path, 'wb') as f:
        pickle.dump(source_obj, f, protocol=pickle.HIGHEST_PROTOCOL)
        logger.info('%s dumped to %s', source_obj, output_file_path)


if __name__=='__main__':
  root_data_dir = '/srv/data'
  input_file = os.path.join(root_data_dir, 'ocr_dataset.zip')
  imput_data = pd.read_csv(input_file, compression='zip')
  vectorizer = TfidfVectorizer(
      analyzer='word',
      lowercase=True,
      token_pattern=r'\b[\w\d]{3,}\b'
  )

  vectorizer.fit(ocr_dataset_df.text.values)
  
  save(vectorizer, os.path.join(root_data_dir, 'transformer.pkl'))
