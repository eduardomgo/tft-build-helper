from itertools import combinations
import math
import json

set_data = json.load(open("set12.json"))

all_champions = set_data["champions"]

all_traits = set_data["traits"]

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