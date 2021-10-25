from pprint import pprint

import requests

def hero_request(names):
    url = f"https://superheroapi.com/api/2619421814940190/search/{names}"
    response = requests.get(url)
    return response.json()


def hero_int(heroes):
    dict_heroes = {}
    for el in heroes:
        for i in hero_request(el)['results']:
            dict_heroes |= {int(i['powerstats']['intelligence']):hero_request(el)['results-for']}
    return dict_heroes

heroes_list = ['Hulk', 'Captain America', 'Thanos']

pprint(f'Самый умный супергерой {(hero_int(heroes_list)[max(hero_int(heroes_list))])} со значением интеллекта {max(hero_int(heroes_list))}')