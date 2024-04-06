from flask import Flask, jsonify, request
from Model import *
app = Flask(__name__)

summary = ""
@app.route('/')
def indexPage():  # put application's code here
    return '24-1 Hansung univ Capstone 찾아줘 홈즈 플라스크 서버'

@app.route('/docSummary', methods=['POST'])
def doc_summary() :
    query = request.args
    res = DocumentSummaryModel.summary(query['query'])
    summary = res
    return res

@app.route('/chat', methods=['POST'])
def chatQA() :
    query = request.json
    res = ChatbotModel.getAnswer(query['question'])
    return res

if __name__ == '__main__':
    app.run(debug=True)
