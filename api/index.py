from flask import Flask, request, render_template_string

app = Flask(__name__)


def calculate_bmi(height_cm, weight_kg):
    """키(cm)와 몸무게(kg)를 받아 BMI를 계산해 반환한다."""
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)


def bmi_category(bmi):
    """BMI 값에 해당하는 비만도 단계와 표시 색을 반환한다. (대한비만학회 기준)"""
    if bmi < 18.5:
        return "저체중", "#3498db"
    elif bmi < 23:
        return "정상", "#2ecc71"
    elif bmi < 25:
        return "과체중", "#f39c12"
    elif bmi < 30:
        return "비만", "#e67e22"
    else:
        return "고도비만", "#e74c3c"


PAGE = """
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>BMI 계산기</title>
  <style>
    * { box-sizing: border-box; }
    body {
      font-family: "맑은 고딕", "Malgun Gothic", sans-serif;
      background: #ecf0f1; margin: 0;
      display: flex; justify-content: center; align-items: center;
      min-height: 100vh;
    }
    .card {
      background: #fff; padding: 36px 32px; border-radius: 16px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.12);
      width: 340px; text-align: center;
    }
    h1 { color: #2c3e50; margin: 0 0 24px; font-size: 24px; }
    label { display: block; text-align: left; color: #2c3e50;
            margin: 12px 0 6px; font-size: 14px; font-weight: bold; }
    input[type=number] {
      width: 100%; padding: 10px; font-size: 15px;
      border: 1px solid #bdc3c7; border-radius: 8px; text-align: center;
    }
    button {
      width: 100%; margin-top: 20px; padding: 12px;
      background: #3498db; color: #fff; border: none; border-radius: 8px;
      font-size: 16px; font-weight: bold; cursor: pointer;
    }
    button:hover { background: #2980b9; }
    .result { margin-top: 24px; }
    .bmi-value { font-size: 30px; font-weight: bold; color: #2c3e50; }
    .category { font-size: 20px; font-weight: bold; margin-top: 6px; }
    .error { color: #e74c3c; margin-top: 20px; font-weight: bold; }
  </style>
</head>
<body>
  <div class="card">
    <h1>BMI 계산기</h1>
    <form method="post">
      <label for="height">키 (cm)</label>
      <input type="number" step="0.1" id="height" name="height"
             value="{{ height or '' }}" required>
      <label for="weight">몸무게 (kg)</label>
      <input type="number" step="0.1" id="weight" name="weight"
             value="{{ weight or '' }}" required>
      <button type="submit">계산하기</button>
    </form>

    {% if error %}
      <div class="error">{{ error }}</div>
    {% elif bmi is not none %}
      <div class="result">
        <div class="bmi-value">BMI: {{ '%.1f'|format(bmi) }}</div>
        <div class="category" style="color: {{ color }}">{{ category }}</div>
      </div>
    {% endif %}
  </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    bmi = category = color = error = None
    height = weight = ""

    if request.method == "POST":
        height = request.form.get("height", "").strip()
        weight = request.form.get("weight", "").strip()
        try:
            height_cm = float(height)
            weight_kg = float(weight)
        except ValueError:
            error = "숫자를 정확히 입력해주세요."
        else:
            if height_cm <= 0 or weight_kg <= 0:
                error = "키와 몸무게는 0보다 커야 합니다."
            else:
                bmi = calculate_bmi(height_cm, weight_kg)
                category, color = bmi_category(bmi)

    return render_template_string(
        PAGE, bmi=bmi, category=category, color=color,
        error=error, height=height, weight=weight,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
