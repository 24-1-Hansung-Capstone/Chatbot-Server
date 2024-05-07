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
    # print('{' + f"query : {query}" + '}')
    # visitkorea는 요약 대상이 아니다.
    query = [
        item
        for item in query
        if item['category'] != "visitkorea"]

    # 뉴스와 블로그를 골고루 추출한다.
    news_result = [
        item['esDto']['mainBody']
        for item in query
        if 'esDto' in item
            and 'mainBody' in item['esDto']
            and item['category'] == 'news']
    blog_result = [
        item['esDto']['mainBody']
        for item in query
        if 'esDto' in item
           and 'mainBody' in item['esDto']
           and item['category'] == 'blog']

    filtered_query = [*news_result[:2], *blog_result[:2]]

    print(f"filtered_query : {filtered_query}")
    if len(filtered_query) == 0:
        return ["검색결과가 없습니다."]
    else :
        return make_response(
                json.dumps(
                    DocumentSummaryModel.summary(filtered_query),
                    ensure_ascii=False,
                    indent=2))

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
    app.run(host="0.0.0.0", port=5000)