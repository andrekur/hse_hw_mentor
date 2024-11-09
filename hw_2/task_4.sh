#!/bin/bash

greet() {
    echo "Hello, $1"
}
# Функция для вычисления суммы двух чисел
sum() {
    echo $(($1 + $2))
}
# Вызов первой функции
read -p "Введите имя: " user_name
greet "$user_name"
# Вызов второй функции
read -p "Введите первое число: " first_number
read -p "Введите второе число: " second_number
result=$(sum "$first_number" "$second_number")
# Вывод результата суммы
echo "Сумма $first_number и $second_number равна: $result"

