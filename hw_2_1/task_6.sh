#!/bin/bash

input_file="input.txt"
output_file="output.txt"
error_file="error.log"

# clear files
> "$output_file"
> "$error_file"

if [ ! -f "$input_file" ]; then
    echo "Файл $input_file не найден."
    exit 1
fi

while IFS= read -r line; do
    if [ -f "$line" ]; then
        # write file str count
        line_count=$(wc -l < "$line")
        echo "$line: $line_count" >> "$output_file"
    else
        # write err
        echo "Ошибка: Файл $line не найден." >> "$error_file"
    fi
done < "$input_file"

echo "Скрипт выполнен. Результаты записаны в $output_file и $error_file."

