import csv


def load_dictionary():
    dictionary = {}

    with open("ecdict.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            dictionary[row["word"]] = row

    return dictionary