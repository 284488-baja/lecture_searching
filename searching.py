import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if field not in data:
        return None

    return data[field]


def linear_search(prohledavana_sekvence, hledane_cislo):
    positions = []
    count = 0
    for i, hodnota in enumerate(prohledavana_sekvence):
        if hodnota == hledane_cislo:
            positions.append(i)
            count += 1

    return {"positions" : positions,
            "count" : count}

def binary_search(prohledavany_seznam, hledane_cislo):
    nizky = 0
    vysoky = len(prohledavany_seznam) - 1
    while nizky <= vysoky:
        prostredek = (nizky + vysoky) // 2

        if prohledavany_seznam[prostredek] == hledane_cislo:
            return prostredek
        elif prohledavany_seznam[prostredek] > hledane_cislo:
            vysoky = prostredek - 1
        else:
            nizky = prostredek + 1
    return None



def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    volam_linear = linear_search(sequential_data, 0)
    print(volam_linear)
    volam_binary = binary_search(sequential_data, 8)
    print(volam_binary)


if __name__ == '__main__':
    main()