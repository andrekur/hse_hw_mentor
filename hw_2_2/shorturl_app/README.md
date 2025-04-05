# hse_hw_mentor
Домашние задания по дисциплине Семинар наставника shorturl_app

Добавлен url для выдачи всех адресов GET /urls
Добавлен q-параметр для поиска по full_url

Запуск:
1) docker build -t shorturl_app .
2) docker run -d --name shorturl-app -p 8000:80 -v shorturl_data:/app/data shorturl-app

Или альтернативный:
1) docker pull andrekur/shorturl-service:latest
2) docker run -d --name shorturl-app -p 8000:80 -v shorturl_data:/app/data andrekur/shorturl-service:latest