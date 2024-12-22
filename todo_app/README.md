# hse_hw_mentor
Домашние задания по дисциплине Семинар наставника todo-app

Добавлен q-параметр для поиска по title

Запуск:
1) docker build -t todo-app .
2) docker run -d --name todo-app -p 8000:80 -v todo_data:/app/data/ todo-app

Или альтернативный:
1) docker pull andrekur/todo-service:latest
2) docker run -d --name todo-app -p 8000:80 -v todo_data:/app/data/ andrekur/todo-service:latest