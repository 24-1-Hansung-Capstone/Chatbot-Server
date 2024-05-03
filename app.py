# -- coding: utf-8 --
import json

from flask import Flask, jsonify, request, make_response
from Model import *
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

summary = ""
@app.route('/')
def indexPage():  # put application's code here
    return '24-1 Hansung univ Capstone 찾아줘 홈즈 플라스크 서버'

@app.route('/docSummary', methods=['POST'])
def doc_summary() :
    query = request.json['result']
    filtered_query = [
        item['esDto']['mainBody']
        for item in query
        if 'esDto' in item and 'mainBody' in item['esDto']]
    print(f"filtered_query : {filtered_query}")
    return make_response(
        json.dumps(
            DocumentSummaryModel.summary(filtered_query[:7]),
            ensure_ascii=False,
            indent=2
        )
    )

@app.route('/chat', methods=['POST'])
def chatQA() :
    query = request.json
    res = ChatbotModel.getAnswer(query['question'])
    return res

if __name__ == '__main__':
    app.run(debug=True, port=5000)