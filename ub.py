import random
import os
import traits_data
import traits_data_revival

class Ub:

    def roll(self, seed = None, throwback = False, ignore_class = False, exclude_low = False, lobby_size = 1):
        self.lobby_rolls = []
        for member in range(lobby_size):
            try:
                random.seed(int(seed))
            except:
                return

            #old logic for 3.5 nostalgia set that can be used for future nostalgia/concurrent sets
            if throwback:
                self.thumb_path = os.path.join('static', 'revival_thumbs')
                self.rolling_data = traits_data_revival
            else:
                self.thumb_path = os.path.join('static', 'champ_thumbs')
                self.rolling_data = traits_data

            if exclude_low:
                rolling_origins = dict(self.rolling_data.origins)
                rolling_classes = dict(self.rolling_data.classes)
                for trait in self.rolling_data.low_pop_traits:
                    rolling_origins.pop(trait, 0)
                    rolling_classes.pop(trait, 0)
            else:
                rolling_origins = self.rolling_data.origins
                rolling_classes = self.rolling_data.classes
            
            if ignore_class:
                all_attributes = {**rolling_origins, **rolling_classes}
                roll = random.sample(list(all_attributes.items()), 2)
                
                self.trait1 = roll[0][0]
                self.trait2 = roll[1][0]
                self.origin_array = roll[0][1]
                self.class_array = roll[1][1]
            else:
                origin_roll = random.sample(list(rolling_origins.items()), 1)[0]
                class_roll = random.sample(list(rolling_classes.items()), 1)[0]

                self.trait1 = origin_roll[0]
                self.trait2 = class_roll[0]
                self.class_array = class_roll[1]
                self.origin_array = origin_roll[1]

            self.legal_champs1 = [self.rolling_data.champions_data[champ] for champ in self.origin_array]
            self.legal_champs2 = [self.rolling_data.champions_data[champ] for champ in self.class_array]

            self.all_champs = self.legal_champs1 + self.legal_champs2

            self.royal = random.sample(self.all_champs, 1)[0]
            self.royal_name = 'Scorpion King' if self.royal['name'] == 'Skarner' else self.royal['name']
            self.royal_alt = self.royal['name']
            self.royal_thumb = self.royal['thumb']
            self.royal_cost = self.royal['cost']

            self.display_champs1 = ', '.join(x['name'] for x in self.legal_champs1)
            self.display_champs2 = ', '.join(x['name'] for x in self.legal_champs2)

            self.full_filename = os.path.join(self.thumb_path, self.royal_thumb)

            self.title_string = self.trait1 + ' / ' + self.trait2 + ' with ' + self.royal_name
            self.lobby_rolls.append(self.title_string)
            rolling_origins.pop(self.trait1, 0)
            rolling_classes.pop(self.trait2, 0)

            print(self.title_string)
            print(self.all_champs)

            #TODO make it more clear what the auxiliary traits are
            #TODO roll lobbies
        return self.lobby_rolls
