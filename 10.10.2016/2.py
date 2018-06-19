def find(word, letter, order):
    index = order
    while index < len(word):
        if word[index]==letter:
            return index
        index = index + 1
    return -1

find('Kanagattandirilmagandiktan', 'g',6)

