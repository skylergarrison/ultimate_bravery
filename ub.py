import random
import traits_data
import os

class Ub:
    THUMBNAIL_PATH = os.path.join('static', 'champ_thumbs')

    def roll(self):
        self.trait1 = random.sample(traits_data.classes, 1)[0]
        self.trait2 = random.sample(traits_data.origins, 1)[0]

        self.legal_champs1 = [traits_data.champions_data[champ] for champ in traits_data.trait_champions[self.trait1]]
        self.legal_champs2 = [traits_data.champions_data[champ] for champ in traits_data.trait_champions[self.trait2]]

        self.all_champs = self.legal_champs1 + self.legal_champs2

        self.royal = random.sample(self.all_champs, 1)[0]
        self.royal_name = 'Scorpion King' if self.royal['name'] == 'Skarner' else self.royal['name']
        self.royal_alt = self.royal['name']
        self.royal_thumb = self.royal['thumb']
        self.royal_cost = self.royal['cost']

        self.display_champs1 = ', '.join(x['name'] for x in self.legal_champs1)
        self.display_champs2 = ', '.join(x['name'] for x in self.legal_champs2)

        self.full_filename = os.path.join(self.THUMBNAIL_PATH, self.royal_thumb)

        print(self.trait1 + ' / ' + self.trait2)
        print(self.royal)
        print(self.all_champs)
