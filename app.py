from http import HTTPStatus
from flask import Flask, jsonify, redirect, render_template, request, url_for, json, make_response
import main

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

data = {
    "list" : [{ "TEXT": '가', "RANK": 2, "SCORE" : 3 }, { "TEXT": '나', "RANK": 1, "SCORE" : 2 }, { "TEXT": '다', "RANK": 3, "SCORE" : 1 } ]
}

@app.route('/get', methods=['GET'])
def index():
    return json.dumps(data, ensure_ascii=False)

@app.route('/getlank', methods=['POST'])
def post():
    param = request.get_json()
    text = param['TEXT']
    print(text)
    return json.dumps({"data": main.extract_keyworld(text)}, ensure_ascii=False)


@app.route('/getlank', mehods=['POST'])
def post():
    param = request.get_json()
    word_list = param['WORD']


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
