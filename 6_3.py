# ------------- LESSON 6, EXERCISE 3 -------------------
# There is the dictionary where keys are country name and values are
# cities from this country. Show from what country an input city

cities_dict = {"Беларусь": ["Минск", "Могилев", "Гродно", "Витебск", "Гомель", "Брест"],
               "Россия": ["Москва", "Санкт-Петербург", "Ростов", "Калининград"],
               "Польша": ["Варшава", "Краков", "Гданьск"],
               "США": ["Нью-Йорк", "Вашингтон", "Филадельфия", "Чикаго", "Лос-Анджелес"]}


def select_country(city):
    return ', '.join([key for key, values in cities_dict.items() if city in values])


while True:

    country = select_country(input('Enter any city>'))
    if country == '':
        print('No country found')
    else:
        print(country)
