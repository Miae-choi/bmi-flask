# BMI 계산기 (Flask)

키와 몸무게를 입력하면 BMI(체질량지수)와 비만도 단계를 보여주는 간단한 Flask 웹 앱입니다.

## 기능
- 키(cm)·몸무게(kg) 입력 후 BMI 계산
- 비만도 단계 표시 (저체중 / 정상 / 과체중 / 비만 / 고도비만 — 대한비만학회 기준)
- 단계별 색상 표시, 모바일 대응 반응형 UI
- 잘못된 입력(숫자 아님, 0 이하)에 대한 예외 처리

## 설치 및 실행

```bash
# 의존성 설치
pip install -r requirements.txt

# 실행
python bmi_c_flask.py
```

실행 후 브라우저에서 http://127.0.0.1:5000 에 접속하세요.

## Vercel 배포

이 저장소는 Vercel 서버리스(Python) 규격에 맞춰져 있습니다.

- `api/index.py` : Flask 앱 (서버리스 함수 진입점)
- `vercel.json` : 모든 요청을 `/api/index` 로 라우팅

[vercel.com](https://vercel.com) 에서 **Add New → Project → Import Git Repository** 로
이 저장소를 선택하면 자동으로 빌드·배포됩니다. 이후 `git push` 할 때마다 자동 재배포됩니다.

## BMI 계산식

```
BMI = 몸무게(kg) / (키(m) ** 2)
```

| BMI 범위 | 단계 |
|----------|------|
| 18.5 미만 | 저체중 |
| 18.5 ~ 23 미만 | 정상 |
| 23 ~ 25 미만 | 과체중 |
| 25 ~ 30 미만 | 비만 |
| 30 이상 | 고도비만 |
