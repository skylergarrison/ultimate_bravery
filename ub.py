import random
import traits_data

class Ub:
    def roll(self):
        self.trait1 = random.sample(traits_data.classes, 1)[0]
        self.trait2 = random.sample(traits_data.origins, 1)[0]
        self.legal_champs1 = traits_data.champions[self.trait1]
        self.legal_champs2 = traits_data.champions[self.trait2]
        self.all_champs = self.legal_champs1 + self.legal_champs2
        self.royal = random.sample(self.all_champs, 1)[0]

        print(self.trait1 + ' / ' + self.trait2)
        print(self.royal)
        print(self.all_champs)
