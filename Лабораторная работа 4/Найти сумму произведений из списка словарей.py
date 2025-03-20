# TODO решите задачу
import json
import random
file_input = "output.json"

# Так как сам файл пустой, запишем в него данные
with open(file_input, "w") as file:
    json.dump([{"score": 0.5740511, "weight": 4}, {"score": 0, "weight": 0}], file)

def task() -> float:

    with open(file_input) as f:
        t = json.load(f)
    list_items = [item["score"] * item["weight"] for item in t]
    return round(sum(list_items), 3)


print(task())
