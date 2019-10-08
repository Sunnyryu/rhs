from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

if __name__ == '__main__':
  app.run()

# terminal 에서 python3 hello~~~.py를 하면 주소가 나오는데 해당 주소에 가면 hello world가 나오게 됨!                             
