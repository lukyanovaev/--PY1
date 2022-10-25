DEFAULT_COUNT = 0


def get_count_char(str_):
    glossary = {}
    str_l = str_.lower()  # перевод строки в нижний регистр
    for i in str_l:
        if i.isalpha():  # проверка является ли символ буквой
            glossary[i] = glossary.get(i, DEFAULT_COUNT) + 1  # получение значения по ключу
    return glossary


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

# переход к написанию второй функции
glos = get_count_char(main_str)  # присваивание переменной словаря символов
total_count = sum(glos.values())  # поиск суммы символов в словаре


def percent(gl):
    glossary_2 = {}
    for i in gl:
        glossary_2[i] = round(100 * gl[i] / total_count, 3)  # вычисление процентного содержания каждого символа
    return glossary_2


print(percent(glos))
