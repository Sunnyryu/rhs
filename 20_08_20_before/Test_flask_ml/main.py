import flask
from flask import Flask, request, render_template
from sklearn.externals import joblib
import numpy as np
from scipy import misc
from ml.model import export_model # ml 폴데에 model.py 의 export_model 임포트!
from flask_restful import Resource, Api
import imageio

app = Flask(__name__)
api = Api(app)


# 메인 페이지 라우팅
@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')


# 데이터 예측 처리
@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method == 'POST':

        # 업로드 파일 처리 분기
        file = request.files['image']
        if not file:
            return render_template('index.html', ml_label="No Files")

        # 이미지 픽셀 정보 읽기
        # 알파 채널 값 제거 후 1차원 Reshape
        img = imageio.imread(file)
        img = img[:, :, :3]
        img = img.reshape(1, -1)

        # 입력 받은 이미지 예측
        model = joblib.load('./model/model.pkl')
        prediction = model.predict(img)

        # 예측 값을 1차원 배열로부터 확인 가능한 문자열로 변환
        label = str(np.squeeze(prediction))

        # 숫자가 10일 경우 0으로 처리
        if label == '10':
            label = '0'

        # 결과 리턴
        return render_template('index.html', ml_label=label)


# 데이터 모델 재학습
@app.route('/retrain', methods=['POST'])
def make_model():
    if request.method == 'POST':
        # 모델 재 생성
        export_model()
        print('R')
        return render_template('index.html', md_label='모델 재생성 완료')


# 데이터 모델 재학습(RestApi)
class RestMl(Resource):
    def get(self):
        export_model()
        print('R')
        return {'result': True, 'modelName': 'model.pkl'}


# Rest 등록
api.add_resource(RestMl, '/retrainModel')

if __name__ == '__main__':
    # 모델 로드
    # ml/model.py 선 실행 후 생성
    model = joblib.load('./model/model.pkl')
    # Flask 서비스 스타트
    app.run(host='0.0.0.0', port=8000, debug=True)
