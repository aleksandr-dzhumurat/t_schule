import requests

if '__name__' == '__main__':
    API_URL = 'http://0.0.0.0:5000/api/feature_extractor?doc_id=1'
    res = requests.get(API_URL).json()
    print(res)
