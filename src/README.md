## Описание проекта
web_app_for_check_forms - web-приложение для определения заполненных форм

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Denriandro/web_app_for_check_forms.git
```

```
cd web_app_for_check_forms
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить проект:
```
cd src
```
```
python -m uvicorn main:app --reload
```

Во 2-ом терминале запустить тестовые запросы:

```
python tests/test_post_get_form.py
```
