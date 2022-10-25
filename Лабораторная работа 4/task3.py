def delete(list_, index=None):
    if index is not None:
        first_part = list_[:index]  # слайсирование списка (до индекса)
        second_part = list_[index+1:]  # слайсирование списка (после индекса)
        new_list = first_part + second_part
    else:
        new_list = list_[:-1]
    return new_list


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
