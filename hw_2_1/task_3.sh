#!/bin/bash
read -p "Введите число: " number
if [ "$number" -gt 0 ]; then
    echo "Число $number является положительным."
    
    # считает от 1 до введенного числа
    count=1
    while [ "$count" -le "$number" ]; do
        echo "$count"
	count=$(( $count + 1 ))
    done
elif [ "$number" -lt 0 ]; then
    echo "Число $number является отрицательным."
else
    echo "Вы ввели ноль."
fi

