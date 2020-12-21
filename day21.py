# day21
from collections import Counter
from collections import defaultdict


def allergen(input_str):
    lines = [line for line in input_str.split('\n') if line]
    allergen_dict = defaultdict(list)
    all_ingredients = []
    for line in lines:
        ingredients = line.split('(')[0].strip().split()
        allergens = [
            item.strip(',')
            for item in line.split('(')[1].strip(')').split()[1:]
        ]
        all_ingredients += ingredients
        #         print(ingredients)
        #         print(allergens)
        for alg in allergens:
            allergen_dict[alg].append(set(ingredients))
    ingredients_counter = Counter(all_ingredients)
    allergen_dict_pruned = {
        key: set.intersection(*value)
        for key, value in allergen_dict.items()
    }
    # build the mapping from bottom up
    allergen_dict_final = {}
    confirmed_ingredients = set()
    while len(allergen_dict_final) < len(allergen_dict_pruned):
        for key, value in allergen_dict_pruned.items():
            if len(value) == 1:
                allergen_dict_final[key] = next(iter(value))
                confirmed_ingredients.add(next(iter(value)))
        allergen_dict_pruned = {
            key: value.difference(confirmed_ingredients)
            for key, value in allergen_dict_pruned.items()
        }

    count_no_known_allergen = sum([
        value for key, value in ingredients_counter.items()
        if key not in confirmed_ingredients
    ])
    algs = list(allergen_dict_final.keys())
    algs.sort()
    food = ','.join([allergen_dict_final[alg] for alg in algs])
    return count_no_known_allergen, food


def main():
    with open('./input_folder/day21.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    # part1 and part2
    count_no_known_allergen, food = allergen(input_text)
    assert count_no_known_allergen == 2230
    # part2
    assert food == 'qqskn,ccvnlbp,tcm,jnqcd,qjqb,xjqd,xhzr,cjxv'
    print('success!!')


if __name__ == '__main__':
    main()
