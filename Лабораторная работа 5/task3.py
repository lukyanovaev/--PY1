from random import randint


def get_unique_list_numbers() -> list[int]:
    mylist = []
    while len(mylist) < 15:
        k = randint(-10, 10)
        if k not in mylist:
            mylist.append(k)
    return mylist


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
