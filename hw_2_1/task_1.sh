#!/bin/bash
# 1. print files
echo "Список файлов и их типов в текущей директории:"
for item in *; do
    if [ -d "$item" ]; then
        echo "$item - каталог"
    elif [ -f "$item" ]; then
        echo "$item - файл"
    elif [ -L "$item" ]; then
        echo "$item - ссылка"
    else
        echo "$item - другой тип"
    fi
done
# 2. search file by name
if [ $# -eq 0 ]; then
    echo "Не указан файл для проверки."
    exit 1
fi
filename="$1"
if [ -e "$filename" ]; then
    echo "Файл '$filename' существует."
else
    echo "Файл '$filename' не найден."
fi
# 3. file name + permission
echo "Информация о файлах и их правах:"
for item in *; do
    if [ -e "$item" ]; then
        permissions=$(ls -ld "$item" | awk '{print $1}')
        echo "$item - права доступа: $permissions"
    fi
done
