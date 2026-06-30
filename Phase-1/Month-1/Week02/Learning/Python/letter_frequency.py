# Day 9

from sys import argv
from os import path
from json import dump

def calc_frequency(content):
    freq = {}
    for ch in content:
        if ch not in freq:
            freq[ch] = 1
        else:
            freq[ch] = freq.get(ch, 0) + 1
    return {char: count for char, count in sorted(freq.items(), key=lambda x: -x[1])}



def save_json(my_dict):
    with open("answer.json", "w") as f:
        dump(my_dict, f, indent= 4)


def main():
    if len(argv) != 2:
        file_path = input("Please enter the file name: ")
    else:
        file_path = argv[1]

    if not path.exists(file_path):
        print("The file not exist")
        return None
    elif not path.isfile(file_path):
        print("That is not a file")
        return None
    with open(file_path, "r", encoding="UTF-8") as f:
        content = f.read()

    my_dict = calc_frequency(content)
    save_json(my_dict)

if __name__ == "__main__":
    main()