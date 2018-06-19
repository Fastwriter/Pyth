prefixes='JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if(letter == 'O'):
        letter = 'Ou'+letter[1:]
    if(letter == 'Q'):
        letter = 'Qu'+letter[1:]
    print(letter + suffix)
