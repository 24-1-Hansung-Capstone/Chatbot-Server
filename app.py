# -- coding: utf-8 --
import json
from flask import Flask, jsonify, request, make_response
from Model import *
import torch

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

summary = ""
@app.route('/')
def indexPage():  # put application's code here
    return str(torch.cuda.is_available())

@app.route('/docSummary', methods=['POST'])
def doc_summary() :
    try:
        title = request.json['title']
        query = request.json['result']
    except KeyError:
        return make_response(jsonify({"error": "잘못된 데이터 요청입니다."}), 400)

    print(f"요약 요청 {title} : {query}")
    summary_result = DocumentSummaryModel.summary(query)
    return make_response(
        json.dumps(summary_result, ensure_ascii=False, indent=2),
        200,
        {'Content-Type': 'application/json'}
    )

@app.route('/sentimental', methods=['POST'])
def review_sentimental():
    query = request.json['target']
    res = list(map(lambda x : float(x), SentimentalAnalysisModel.sentences_analysis([query])))
    print(f"sentimental query : {query}")
    print(f"sentimental score : {res}")
    return make_response(
                json.dumps(
                    res,
                    indent=2))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555)