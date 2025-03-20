# TODO Напишите функцию find_common_participants
def find_common_participants(participants_one_group:str, participants_another_group:str, x=","):

    # Создадим для каждой группы по списку,
    # В каждом из которых находятся фамилии участников
    list_one_group = participants_one_group.split(x)
    list_another_group = participants_another_group.split(x)


    # Используем метод capitalize()
    # Чтобы каждая фамилия была записана с заглавной буквы
    # А остальные буквы фамилии - с прописной.

    list_one_group = [participant.capitalize() for participant in list_one_group]

    list_another_group = [participant.capitalize() for participant in list_another_group]


    #Находим общих участников(сразу преобразуем в список)
    common_participants = list(set(list_one_group).intersection(list_another_group))

    #Сортируем список
    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

#TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, x="|"))