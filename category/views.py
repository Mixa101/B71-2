# Create your views here.
from django.http.response import HttpResponse


def hello_world(request):
    return HttpResponse("hello world!")


def button(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Тестовая страница</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
      background: linear-gradient(135deg, #667eea, #764ba2);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .card {
      background: #fff;
      max-width: 420px;
      width: 100%;
      padding: 32px;
      border-radius: 16px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
      text-align: center;
    }

    h1 {
      color: #333;
      margin-bottom: 12px;
    }

    p {
      color: #666;
      line-height: 1.5;
      margin-bottom: 24px;
    }

    button {
      background: #667eea;
      color: #fff;
      border: none;
      padding: 12px 24px;
      font-size: 16px;
      border-radius: 8px;
      cursor: pointer;
      transition: transform 0.15s, background 0.15s;
    }

    button:hover {
      background: #5568d3;
      transform: translateY(-2px);
    }

    #counter {
      margin-top: 16px;
      font-weight: bold;
      color: #333;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>Привет, мир! 👋</h1>
    <p>Это простая тестовая страница с HTML и CSS. Нажмите на кнопку, чтобы проверить, что JavaScript тоже работает.</p>
    <button id="btn">Нажми меня</button>
    <div id="counter">Нажатий: 0</div>
  </div>

  <script>
    let count = 0;
    document.getElementById('btn').addEventListener('click', () => {
      count++;
      document.getElementById('counter').textContent = 'Нажатий: ' + count;
    });
  </script>
</body>
</html>""")
