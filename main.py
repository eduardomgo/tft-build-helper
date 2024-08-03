from itertools import combinations
import math

all_champions = [
  {"name": "Briar", "cost": 5, "traits": ["Eldritch", "Ravenous", "Shapeshifter"]},
  {"name": "Camille", "cost": 5, "traits": ["Chrono", "Multistriker"]},
  {"name": "Diana", "cost": 5, "traits": ["Frost", "Bastion"]},
  {"name": "Milio", "cost": 5, "traits": ["Faerie", "Scholar"]},
  {"name": "Morgana", "cost": 5, "traits": ["Witchcraft", "Preserver"]},
  {"name": "Norra & Yuumi", "cost": 5, "traits": ["Portal", "Mage"]},
  {"name": "Smolder", "cost": 5, "traits": ["Dragon", "Blaster"]},
  {"name": "Xerath", "cost": 5, "traits": ["Arcana", "Ascendant"]},
  {"name": "Fiora", "cost": 4, "traits": ["Witchcraft", "Warrior"]},
  {"name": "Gwen", "cost": 4, "traits": ["Sugarcraft", "Warrior"]},
  {"name": "Kalista", "cost": 4, "traits": ["Faerie", "Multistriker"]},
  {"name": "Karma", "cost": 4, "traits": ["Chrono", "Incantor"]},
  {"name": "Nami", "cost": 4, "traits": ["Eldritch", "Mage"]},
  {"name": "Nasus", "cost": 4, "traits": ["Pyro", "Shapeshifter"]},
  {"name": "Olaf", "cost": 4, "traits": ["Frost", "Hunter"]},
  {"name": "Rakan", "cost": 4, "traits": ["Faerie", "Preserver"]},
  {"name": "Ryze", "cost": 4, "traits": ["Portal", "Incantor"]},
  {"name": "Tahm Kench", "cost": 4, "traits": ["Arcana", "Vanguard"]},
  {"name": "Taric", "cost": 4, "traits": ["Portal", "Bastion"]},
  {"name": "Varus", "cost": 4, "traits": ["Pyro", "Blaster"]},
  {"name": "Bard", "cost": 3, "traits": ["Sugarcraft", "Preserver", "Scholar"]},
  {"name": "Ezreal", "cost": 3, "traits": ["Portal", "Blaster"]},
  {"name": "Hecarim", "cost": 3, "traits": ["Arcana", "Bastion", "Multistriker"]},
  {"name": "Hwei", "cost": 3, "traits": ["Frost", "Blaster"]},
  {"name": "Jinx", "cost": 3, "traits": ["Sugarcraft", "Hunter"]},
  {"name": "Katarina", "cost": 3, "traits": ["Faerie", "Warrior"]},
  {"name": "Mordekaiser", "cost": 3, "traits": ["Eldritch", "Vanguard"]},
  {"name": "Neeko", "cost": 3, "traits": ["Witchcraft", "Shapeshifter"]},
  {"name": "Shen", "cost": 3, "traits": ["Pyro", "Bastion"]},
  {"name": "Swain", "cost": 3, "traits": ["Frost", "Shapeshifter"]},
  {"name": "Veigar", "cost": 3, "traits": ["Honeymancy", "Mage"]},
  {"name": "Vex", "cost": 3, "traits": ["Chrono", "Mage"]},
  {"name": "Wukong", "cost": 3, "traits": ["Druid"]},
  {"name": "Ahri", "cost": 2, "traits": ["Arcana", "Scholar"]},
  {"name": "Akali", "cost": 2, "traits": ["Pyro", "Warrior"]},
  {"name": "Cassiopeia", "cost": 2, "traits": ["Witchcraft", "Incantor"]},
  {"name": "Galio", "cost": 2, "traits": ["Portal", "Vanguard", "Mage"]},
  {"name": "Kassadin", "cost": 2, "traits": ["Portal", "Multistriker"]},
  {"name": "Kog'Maw", "cost": 2, "traits": ["Honeymancy", "Hunter"]},
  {"name": "Nilah", "cost": 2, "traits": ["Eldritch", "Warrior"]},
  {"name": "Nunu", "cost": 2, "traits": ["Honeymancy", "Bastion"]},
  {"name": "Rumble", "cost": 2, "traits": ["Sugarcraft", "Vanguard", "Blaster"]},
  {"name": "Shyvana", "cost": 2, "traits": ["Dragon", "Shapeshifter"]},
  {"name": "Syndra", "cost": 2, "traits": ["Eldritch", "Incantor"]},
  {"name": "Tristana", "cost": 2, "traits": ["Faerie", "Blaster"]},
  {"name": "Zilean", "cost": 2, "traits": ["Frost", "Chrono", "Preserver"]},
  {"name": "Ashe", "cost": 1, "traits": ["Eldritch", "Multistriker"]},
  {"name": "Blitzcrank", "cost": 1, "traits": ["Honeymancy", "Vanguard"]},
  {"name": "Elise", "cost": 1, "traits": ["Eldritch", "Shapeshifter"]},
  {"name": "Jax", "cost": 1, "traits": ["Chrono", "Multistriker"]},
  {"name": "Jayce", "cost": 1, "traits": ["Portal", "Shapeshifter"]},
  {"name": "Lillia", "cost": 1, "traits": ["Faerie", "Bastion"]},
  {"name": "Nomsy", "cost": 1, "traits": ["Dragon", "Hunter"]},
  {"name": "Poppy", "cost": 1, "traits": ["Witchcraft", "Bastion"]},
  {"name": "Seraphine", "cost": 1, "traits": ["Faerie", "Mage"]},
  {"name": "Soraka", "cost": 1, "traits": ["Sugarcraft", "Mage"]},
  {"name": "Twitch", "cost": 1, "traits": ["Frost", "Hunter"]},
  {"name": "Warwick", "cost": 1, "traits": ["Frost", "Vanguard"]},
  {"name": "Ziggs", "cost": 1, "traits": ["Honeymancy", "Incantor"]},
  {"name": "Zoe", "cost": 1, "traits": ["Portal", "Witchcraft", "Scholar"]}
]

all_traits = [
  {"name": "Arcana", "levels": [2, 3, 4, 5]},
  {"name": "Chrono", "levels": [2, 4, 6]},
  {"name": "Dragon", "levels": [2, 3]},
  {"name": "Druid", "levels": [1]},
  {"name": "Eldritch", "levels": [3, 5, 7, 10]},
  {"name": "Faerie", "levels": [2, 4, 6, 9]},
  {"name": "Frost", "levels": [3, 5, 7, 9]},
  {"name": "Honeymancy", "levels": [3, 5, 7]},
  {"name": "Portal", "levels": [3, 6, 8, 10]},
  {"name": "Pyro", "levels": [2, 3, 4, 5]},
  {"name": "Ravenous", "levels": [1]},
  {"name": "Sugarcraft", "levels": [2, 4, 6]},
  {"name": "Witchcraft", "levels": [2, 4, 6, 8]},
  {"name": "Ascendant", "levels": [1]},
  {"name": "Bastion", "levels": [2, 4, 6, 8]},
  {"name": "Bat Queen", "levels": [1]},
  {"name": "Best Friends", "levels": [1]},
  {"name": "Blaster", "levels": [2, 4, 6]},
  {"name": "Hunter", "levels": [2, 4, 6]},
  {"name": "Incantor", "levels": [2, 4]},
  {"name": "Mage", "levels": [3, 5, 7, 9]},
  {"name": "Multistriker", "levels": [3, 5, 7]},
  {"name": "Preserver", "levels": [2, 3, 4, 5]},
  {"name": "Scholar", "levels": [2, 4, 6]},
  {"name": "Shapeshifter", "levels": [2, 4, 6, 8]},
  {"name": "Vanguard", "levels": [2, 4, 6]},
  {"name": "Warrior", "levels": [2, 4, 6]}
]


def is_trait_active(trait_counts, trait_name, emblem_traits=[]):
    trait = next(trait for trait in all_traits if trait['name'] == trait_name)
    if trait["levels"] == [1]:
        return False
    required_count = trait["levels"][0] - (1 if trait_name in emblem_traits else 0)
    return trait_counts >= required_count

def sort_compositions_by_cost(compositions):
    return sorted(compositions, key=lambda combo: sum(champ['cost'] for champ in combo["Champions"]))

def find_compositions(min_cost, max_cost, max_num_champions, min_traits, current_champions_name=[], emblem_traits=[]):
    filtered_champions = [champ for champ in all_champions if champ["cost"] >= min_cost and champ["cost"] <= max_cost]

    required_champions = [champion for champion in all_champions if champion['name'] in current_champions_name]
    remaining_champions = [champion for champion in filtered_champions if champion["name"] not in current_champions_name]

    max_remaining_champions = max_num_champions - len(required_champions)

    print("Amount of champions: ", len(filtered_champions))
    print("Max number of champions: ", max_remaining_champions)
    print("Complexity: ", math.comb(len(filtered_champions), max_remaining_champions))
    
    valid_compositions = []

    for num in range(1, max_remaining_champions + 1):
        for combo in combinations(remaining_champions, num):
            full_combo = tuple(required_champions) + combo 
            trait_counts = {}
            for champ in full_combo:
                for trait in champ["traits"]:
                    if trait in trait_counts:
                        trait_counts[trait] += 1
                    else:
                        trait_counts[trait] = 1
            
            active_traits = [trait for trait, count in trait_counts.items() if is_trait_active(count, trait, emblem_traits)]
            
            if len(active_traits) >= min_traits:
                valid_compositions.append({"Champions": full_combo, "Traits": active_traits})
    
    return sort_compositions_by_cost(valid_compositions)

min_cost = 1
max_cost = 3
max_num_champions = 7
min_traits = 7
current_champions = []
emblem_traits = []

valid_compositions = find_compositions(min_cost, max_cost, max_num_champions, min_traits, current_champions_name=current_champions, emblem_traits=emblem_traits)

for composition in valid_compositions:
    print(f"Champions: {', '.join([champ['name'] for champ in composition['Champions']])} - Traits: {', '.join(composition.get('Traits', []))}")