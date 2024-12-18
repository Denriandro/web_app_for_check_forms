import requests


data = [
    # существующие шаблоны
    {'email': 'test@mail.ru', 'phone': '+7 333 333 22 22'},
    {'text': 'test_text', 'date': '11.11.2024'},

    # несуществующие шаблоны
    {'email': 'test@mail.com', 'date': '11.11.2024'},
    {'contact': 'test_contact', 'username': 'admin'},
]

url = 'http://127.0.0.1:8000/get_form'


if __name__ == '__main__':
    for query in data:
        response = requests.post(url, query)
        print(response.text)
