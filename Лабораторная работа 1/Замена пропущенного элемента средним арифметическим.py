numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
new_numbers = list(filter(lambda x: x != None, numbers))
average = sum(new_numbers)/len(numbers)



for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = average

print("Измененный список:", numbers)


