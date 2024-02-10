def solution_1_word():
    print('введите сколькими битами кодируется каждое слово и на сколько байт слово стало меньше')
    symbol_weight = int(input('введите вес символа(в битах): '))
    string_weight = int(input('введите вес исходного предложения(в байтах): '))

    a = symbol_weight / 8

    print('Это стих?')
    answ = input("ответьте да или нет: ")

    if answ == 'да' or answ == "Да" or answ == 'ДА':
        return f'вычеркнули слово из {int(string_weight / a - 1)} символов'
    else:
        return f'вычеркнули слово из {int(string_weight / a - 2)} символов'


def solution_1_weight():
    print('введите по порядку: 1)количество страниц 2)количество строк 3) количество символов 4)вес символов (в битах)')
    pages, strings, count_symbol, symbol_weight = int(input("1)")), int(input('2)')), int(input('3)')), int(input('4)'))
    return f'статья весит {(pages * strings * count_symbol * symbol_weight) / 8192} Кбайт'


if __name__ == "__main__":
    print(solution_1_word())
