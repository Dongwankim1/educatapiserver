from flask import Flask,request,Response
from flask_cors import CORS
import logging
from konlpy.tag import Mecab
import json
from jamo import h2j,j2hcj


logging.basicConfig(filename="/was/logs/flask.log",level = logging.WARNING)


app = Flask(__name__)
CORS(app,resources={r"/analysis":{"origins":"*"}})

@app.route('/')
def home():
    return 'Hello,World'

@app.route('/wordadd')
def add_word():
    
    with open('./tmp/mecab-ko-dic-2.1.1-20180720/user-dic'):
        
    
@app.route('/analysis',methods=['GET','POST'])
def text_analysis():
    

    res = Response("block")
    res.headers["Access-Control-Allow-Origin"]="*"

    jsonData = request.get_json()
    
    resultData = dict()
    tokenizer = Mecab()
    print(tokenizer.pos(jsonData['text']))
    resultData['result'] = tokenizer.pos(jsonData['text'])
    return json.dumps(resultData)



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5050)
