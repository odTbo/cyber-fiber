from random import choice

with open("static/csv/english-adjectives.txt", "r") as file:
    adjectives_list = file.readlines()
    adjectives = [item.strip() for item in adjectives_list]

with open("static/csv/concrete-nouns.txt", "r") as file:
    nouns_list = file.readlines()
    nouns = [item.strip() for item in nouns_list]


def generate_name():
    name = choice(adjectives).title() + choice(nouns).title()
    return name
