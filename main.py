import json
from os import path

from shutil import copyfile

from platformdirs import user_data_dir

CLANGEN_PATH: str = None

dev = input('Type `dev` (without quotes) to convert saves on development, or paste in a path if running from source (leave blank for stable): ')

if dev == 'dev':
    CLANGEN_PATH = user_data_dir("ClanGenBeta", "ClanGen")
elif not dev:
    CLANGEN_PATH = user_data_dir("ClanGen", "ClanGen")
else:
    CLANGEN_PATH = dev

PRONOUNS = {
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
    try:
        clan_name = input('Enter a Clan name (leave blank to quit): ')
    except KeyboardInterrupt:
        print('Ctrl-C detected, exiting')
        break

    clan_path = f"{CLANGEN_PATH}/saves/{clan_name}"

    print(clan_path)

    if not clan_name:
        print('Exiting')
        break
    if not path.exists(clan_path):
        print('Clan could not be found. Please enter another name.')
        continue

    copyfile(clan_path + '/clan_cats.json', 
             clan_path + '/clan_cats_backup.json')

    clan_cats = json.load(open(clan_path + '/clan_cats.json'))

    for cat in clan_cats:
        cat['pronouns'] = [PRONOUNS[cat['gender_align']]]

    json.dump(clan_cats, open(clan_path + '/clan_cats.json', 'w'), indent=4)


    print('Conversion successful')