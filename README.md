# demo_flask

Небольшое демонстрационное Flask‑приложение из нескольких файлов,
предназначенное для прогона SonarQube.

## Установка

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск

**CLI‑версия:**
```bash
python -m demo_flask.cli --version
python -m demo_flask.cli --serve
```

**Через Flask напрямую:**
```bash
python -m demo_flask.app
```

Приложение будет доступно на http://localhost:5000/
* `/version` — версию,
* `/static/hello.html` — статический файл,
* `/` — простое сообщение JSON.
