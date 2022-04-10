import os

import pandas as pd
from flask import Flask, render_template, request, jsonify

from helpers import logger, load_transformer, load_dataset

# если сначала работало, а потом поломалось - можно удалить контейнеры
# sudo docker rm $(sudo docker ps -a -q)
# sudo docker rmi $(sudo docker images -a -q)
# docker volume prune -f

app = Flask(__name__)
bind_port = 5000
# загружаем данные приложения
ocr_dataset_df = load_dataset()
transformer = load_transformer()


@app.route('/')
def hello():
    """Главная страничка приложения

    Можно открыть в браузере
    """
    return render_template('index.html')


@app.route('/feature_extractor')
def feature_extractor():
    """Визуализация работы в браузере"""
    doc_id = request.args.get("doc_id", type=int, default=100)
    raw_text = ocr_dataset_df.iloc[int(doc_id)]["text"]
    _, feature_vector = transformer.transform([raw_text]).nonzero()
    bag_of_words = [transformer.get_feature_names()[i] for i in feature_vector]
    return render_template('feature_extractor.html', raw_text=raw_text, feature_vector=feature_vector, bag_of_words=bag_of_words)


@app.route('/api/feature_extractor')
def get_features():
    """Метод API

    Сюда можно ходить из Postman
    """
    doc_id = request.args.get("doc_id", type=int, default=100)
    raw_text = ocr_dataset_df.iloc[int(doc_id)]["text"]
    _, feature_vector = transformer.transform([raw_text]).nonzero()
    result_dict = {
        'doc_id': doc_id,
        'feature_vectoe': [i for i in feature_vector]
    }
    return jsonify(f"{result_dict}")


if __name__ == '__main__':
    logger.info('Flask app started')
    app.run(host="0.0.0.0", port=int(bind_port), debug=True)
