# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as csv_file: # TODO считать содержимое csv файла
        data = csv.DictReader(csv_file)

        text = [dict_ for dict_ in data] # преобразуем в словарь


    with open(OUTPUT_FILENAME, "w") as json_file: # TODO Сериализовать в файл с отступами равными 4
        json.dump(text, json_file, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
