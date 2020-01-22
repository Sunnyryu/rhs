from flask import Flask 

app = Flask(__name__)

@app.route("/")
def http_prepost_response():
    return "/"

@app.before_first_request
def before_first_request():
    print("앱 기동하고 나서 첫 http 요청만 응답")

@app.before_request
def before_request():
    print("매 http 요청이 처리되고 나서 실행 !")

@app.after_request
def after_request(response):
    print("매 http 요청이 처리되기 전에 실행됨 ")

@app.teardown_request
def teardown_request(exception):
    print(" 매 http 요청의 결과가 브라우저에 응답하고 나서 호출 ")

@app.teardown_appcontext
def teardown_appcontext(exception):
    print("HTTP 요청의 어플리케이션 컨텍스트가 종료될 때 실행됨")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
