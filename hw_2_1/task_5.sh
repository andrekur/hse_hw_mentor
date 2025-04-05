#!/bin/bash
# Запускаем три команды sleep в фоновом режиме
set -m
sleep 5 &
pid1=$!
sleep 10 &
pid2=$!
sleep 15 &
pid3=$!

echo "Запущенные фоновые задачи:"
jobs -l
echo "Переводим первую задачу на передний план"
fg %1
jobs -l

echo "Переводим вторую задачу на задний план"
bg %2
echo "Список задач после перевода второй"
jobs -l
# wait all tasks
wait
echo "Все задачи завершены."
jobs -l
