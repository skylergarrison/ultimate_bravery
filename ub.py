import random

traits = [
    'Arcanist',
    'Assassin',
    'Bodyguard',
    'Bruiser',
    'Challenger',
    'Colossus',
    'Chemtech',
    'Clockwork',
    'Debonair',
    'Enchanter',
    'Enforcer',
    'Hextech',
    'Innovator',
    'Mercenary',
    'Mutant',
    'Scholar',
    'Scrap',
    'Sniper',
    'Socialite',
    'Striker',
    'Syndicate',
    'Twinshot',
    'Yordle'
]
low_pop_traits = [
    'Glutton',
    'Mastermind',
    'Rival',
    'Yordle Lord',
    'Transformer'
]
champions = {
    'Arcanist':[
        'Ahri',
        'Brand',
        'Malzahar',
        'Swain',
        'Vex',
        'Viktor',
        'Ziggs'
    ],
    'Assassin':[
        'Ekko',
        'Kha\'zix',
        'Nocturne',
        'Talon',
        'Twitch'
    ],
    'Bodyguard':[
        'Blitzcrank',
        'Braum',
        'Darius',
        'Galio',
        'Leona',
        'Poppy'
    ],
    'Bruiser': [
        'Cho\'gath',
        'Illaoi',
        'Rek\'sai',
        'Sejuani',
        'Tahm Kench',
        'Vi',
        'Zac'
    ],
    'Challenger': [
        'Camille',
        'Draven',
        'Kai\'sa',
        'Quinn',
        'Tryndamere',
        'Warwick'
    ],
    'Colossus': [
        'Alistar',
        'Cho\'gath',
        'Galio'
    ],
    'Chemtech': [
        'Singed',
        'Twitch',
        'Warwick',
        'Tryndamere',
        'Zac',
        'Renata Glasc',
        'Viktor'
    ],
    'Clockwork': [
        'Camille',
        'Zilean',
        'Jhin',
        'Orianna'
    ],
    'Debonair': [
        'Brand',
        'Syndra',
        'Talon',
        'Leona',
        'Draven',
        'Zeri'
    ],
    'Enforcer': [
        'Caitlyn',
        'Sejuani',
        'Vi',
        'Jayce'
    ],
    'Enchanter': [
        'Lulu',
        'Morgana',
        'Orianna',
        'Senna'
    ],
    'Hextech': [
        'Jarvan',
        'Nocturne',
        'Sejuani',
        'Swain',
        'Lucian',
        'Alistar',
        'Sivir'
    ],
    'Innovator': [
        'Ekko',
        'Ezreal',
        'Jayce',
        'Seraphine',
        'Singed',
        'Zilean'
    ],
    'Mercenary': [
        'Illaoi',
        'Quinn',
        'Gangplank',
        'Miss Fortune',
        'Tahm Kench'
    ],
    'Mutant': [
        'Kassadin',
        'Rek\'sai',
        'Cho\'gath',
        'Malzahar',
        'Kha\'zix',
        'Kai\'sa'
    ],
    'Scholar': [
        'Kassadin',
        'Renata Glasc',
        'Silco',
        'Syndra',
        'Zyra'
    ],
    'Scrap': [
        'Ezreal',
        'Ziggs',
        'Blitz',
        'Ekko',
        'Irelia',
        'Jinx'
    ],
    'Sniper' : [
        'Ashe',
        'Caitlyn',
        'Jhin',
        'Miss Fortune',
        'Zeri'
    ],
    'Socialite': [
        'Gnar',
        'Senna',
        'Seraphine',
        'Galio'
    ],
    'Striker': [
        'Gnar',
        'Irelia',
        'Jarvan',
        'Rek\'sai',
        'Sivir'
    ],
    'Syndicate': [
        'Darius',
        'Ashe',
        'Zyra',
        'Morgana',
        'Ahri',
        'Braum'
    ],
    'Twinshot': [
        'Corki',
        'Gangplank',
        'Jinx',
        'Lucian'
    ],
    'Yordle': [
        'Poppy',
        'Ziggs',
        'Corki',
        'Lulu',
        'Gnar',
        'Vex'
    ]
}

roll = random.sample(traits, 2)
trait1 = roll[0]
trait2 = roll[1]
legal_champs = champions[trait1] + champions[trait2]
royal = random.sample(legal_champs, 1)

print(roll)
print(royal)
print(legal_champs)
