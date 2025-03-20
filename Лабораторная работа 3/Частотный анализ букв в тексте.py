# TODO  Напишите функцию count_letters

def count_letters(text:str):

    text_ = text.lower() # приведем все буквы к нижнему регистру
    dict_letters = dict()


    for letter in text_:
        if letter.isalpha():# Проверка, является ли символ буквой

            if dict_letters.get(letter) is not None:
                dict_letters[letter] += 1
            else:
                dict_letters[letter] = 1
    return dict_letters

'''
    for letter in set(text_):

    #set(text_) содержит без повторений все символы,
    # встречающиеся в тексте

        if letter.isalpha():
            l = len(text_.split(letter)) - 1 #Возвращает количество повторений буквы letter
            dict_letters[letter] = l
'''




# TODO Напишите функцию calculate_frequency

def calculate_frecuency(dict_letters:dict, text:str):
    total = len([x for x in text if x.isalpha()]) # подсчет количества букв в тексте
    dict_letters_frecuency = {t: dict_letters[t]/total for t in dict_letters}
    # t - ключ-буква, которому соотвествует частота

    return dict_letters_frecuency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dict_main_str_letters = count_letters(main_str)
dict_frecuency_letters = calculate_frecuency(dict_main_str_letters, main_str)

#Округление выполняется в выводе через f-строки
for item in dict_frecuency_letters:
    print(f"{item}: {dict_frecuency_letters[item]:.2f}")