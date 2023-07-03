from http import HTTPStatus
from flask import Flask, jsonify, redirect, render_template, request, url_for, json
import main

app = Flask(__name__)


data = {
    "list" : [{ "TEXT": '가', "RANK": 2, "SCORE" : 3 }, { "TEXT": '나', "RANK": 1, "SCORE" : 2 }, { "TEXT": '다', "RANK": 3, "SCORE" : 1 } ]
}

@app.route('/get', methods=['GET'])
def index():
    return jsonify({"data": data, "status": HTTPStatus.OK})

@app.route('/getlank', methods=['POST'])
def post():
    param = request.get_json()
    text = param['TEXT']
    print(text)
    return jsonify({"data": main.extract_keyworld(text)})


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
