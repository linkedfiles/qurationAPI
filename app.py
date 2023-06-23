from flask import Flask
import main

app = Flask(__name__)

@app.route('/')
def index():
    return main.extract_keyworld()

app.run(host="0.0.0.0", debug=True, port=5000)

