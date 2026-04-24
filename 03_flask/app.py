from flask import Flask
app = Flask(__name__)

# [메인 화면 라우팅]
@app.route('/')
def home():
    return 'welcome'

# [동적 URL 처리]
@app.route('/read/<id>/')
def read(id):
    return f'Read {id}'

# [서버 실행 및 디버그 모드]
if __name__ == '__main__':
    app.run(debug=True)