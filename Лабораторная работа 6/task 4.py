import json

INPUT_FILE = "input.csv"
DELIMITER = ','


def csv_to_list_dict(filename, delimiter) -> list[dict]:
    list_row = []
    my_list = []
    with open(filename, 'r') as f:
        text = f.readlines()
        change_text = text[0].rstrip().split(delimiter)
        for line in text[1:]:
            list_row.append(line.rstrip().split(delimiter))
        for row in list_row:
            elem = {k: v for k, v in zip(change_text, row)}
            my_list.append(elem)
    return my_list


print(json.dumps(csv_to_list_dict(INPUT_FILE, DELIMITER), indent=4))
