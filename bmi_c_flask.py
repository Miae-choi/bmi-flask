"""로컬 실행용 진입점.

실제 앱 정의는 Vercel 서버리스 함수 규격에 맞춰 api/index.py 에 있습니다.
로컬에서는 이 파일을 실행하면 동일한 앱이 개발 서버로 뜹니다.

    python bmi_c_flask.py
    -> http://127.0.0.1:5000
"""

from api.index import app

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
