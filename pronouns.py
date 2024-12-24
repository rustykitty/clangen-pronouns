import json
from os import path

from shutil import copyfile

from typing import Dict, List, Any

CLANGEN_MACOS_PATH='/Users/rusty/Library/Application Support/ClanGen/saves/'

PRONOUNS: Dict[str, Dict[str, str]] = {
    'male': {
        'subject': 'he',
        'object': 'him',
        'poss': 'his',
        'inposs': 'his',
        'self': 'himself',
        'conju': 2 # singular
    },
    'female': {
        'subject': 'she',
        'object': 'her',
        'poss': 'her',
        'inposs': 'hers',
        'self': 'herself',
        'conju': 2 # singular
    },
    'nonbinary': {
        'subject': 'they',
        'object': 'them',
        'poss': 'their',
        'inposs': 'theirs',
        'self': 'themself',
        'conju': 1 # plural
    }
}

PRONOUNS['trans female'] = PRONOUNS['female']
PRONOUNS['trans male'] = PRONOUNS['male']

while True:

    clan_name = input('Enter a Clan name (leave blank to quit): ')

    print(CLANGEN_MACOS_PATH + clan_name)

    if not clan_name:
        print('Exiting')
        break
    if not path.exists(CLANGEN_MACOS_PATH + clan_name):
        print('Clan could not be found. Please enter another name.')
        continue

    clan_cats: List[Dict[str, Any]] = json.load(open(CLANGEN_MACOS_PATH + clan_name + '/clan_cats.json'))

    for cat in clan_cats:
        cat['pronouns'] = [PRONOUNS[cat['gender_align']]]

    json.dump(clan_cats, open(CLANGEN_MACOS_PATH + clan_name + '/clan_cats_new.json', 'w'), indent=4)