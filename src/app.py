import os

import pandas as pd
from flask import Flask, render_template, request, jsonify

from helpers import logger, load

# если сначала работало, а потом поломалось - можно удалить контейнеры
# sudo docker rm $(sudo docker ps -a -q)
# sudo docker rmi $(sudo docker images -a -q)
# docker volume prune -f

app = Flask(__name__)
bind_port = 5000

root_data_dir = '/srv/data'
input_file = os.path.join(root_data_dir, 'ocr_dataset.zip')
ocr_dataset_df = pd.read_csv(input_file, compression='zip')
transformer_file = os.path.join(root_data_dir, 'transformer.pkl')
transformer = load(transformer_file)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/feature_extractor')
def feature_extractor():
    doc_id = request.args.get("doc_id", type=int, default=100)
    raw_text = ocr_dataset_df.iloc[int(doc_id)]["text"]
    _, feature_vector = transformer.transform([raw_text]).nonzero()
    bag_of_words = [transformer.get_feature_names()[i] for i in feature_vector]
    return render_template('feature_extractor.html', raw_text=raw_text, feature_vector=feature_vector, bag_of_words=bag_of_words)


@app.route('/api/feature_extractor')
def get_features():
    doc_id = request.args.get("doc_id", type=int, default=100)
    raw_text = ocr_dataset_df.iloc[int(doc_id)]["text"]
    _, feature_vector = transformer.transform([raw_text]).nonzero()
    return jsonify(feature_vector)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(bind_port), debug=True)
