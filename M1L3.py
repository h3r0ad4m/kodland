meme_dict = {
    'LOL': 'Częsta reakcja na cos zabawnego',
    "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
}

contacts = {
    "Edwin": 20,
    "Michael": 15,
    "John": 22,
    "Gregory": 14,
    "Sophie": 30
}

def meme():
    word = input('Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ')

    if word in meme_dict.keys():
        print(word, ':', meme_dict[word])
    else:
        print('nie znaleziono takiego słowa')

def second():
    print(contacts)

def third():
    contacts["Jamal"] = 15

def fourth():
    person = input('who')
    if person in contacts.keys():
        print(contacts[person])
    else:
        print('nie ma takiej osoby')

def star():
    for name, age in contacts.items():
        print((name), ':', age)

meme()
second()
third()
fourth()
star()