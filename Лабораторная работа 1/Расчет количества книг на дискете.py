Size_D = 1.44
pages = 100
lines = 50
sym_in_one_line = 25
size_symbol = 4

number_of_books = Size_D//(size_symbol * sym_in_one_line * lines * pages/(2 ** 20))
number_of_books = int(number_of_books)
print(f"Количество книг, помещающихся на дискету: {number_of_books}")