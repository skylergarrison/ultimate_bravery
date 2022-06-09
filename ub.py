import random
import traits_data

class Ub:
    def roll(self):
        traits = traits_data.classes + traits_data.origins
        self.roll_result = random.sample(traits, 2)
        trait1 = self.roll_result[0]
        trait2 = self.roll_result[1]
        self.legal_champs = traits_data.champions[trait1] + traits_data.champions[trait2]
        self.royal = random.sample(self.legal_champs, 1)

        print(self.roll_result)
        print(self.royal)
        print(self.legal_champs)
