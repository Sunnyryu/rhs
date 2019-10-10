from flask import Flask, jsonify

count = 0 # 변수 선언
app = Flask(__name__)

@app.route('/')
def home():
    global count # 실제로는 이렇게 하면 안되옵니다.
    count += 1
    return jsonify(
        text='Hello, world',
        count = count
    )


@app.route('/abuse')
def abuse_count():
    global count
    count += 100
    return ''
