"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)

def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))

def check_drinks(drink_name, drink_ingredients):
    return drink_name + " Mocktail" if ALCOHOLS.isdisjoint(drink_ingredients) else drink_name + " Cocktail"

def categorize_dish(dish_name, dish_ingredients):
    for item in [("VEGAN", VEGAN), ("VEGETARIAN", VEGETARIAN), ("KETO", KETO), ("PALEO", PALEO), ("OMNIVORE", OMNIVORE)]:
        if set(dish_ingredients).issubset(item[1]):
            return dish_name + ": " + item[0]
    return 0

def tag_special_ingredients(dish):
    return (dish[0], SPECIAL_INGREDIENTS.intersection(dish[1]))

def compile_ingredients(dishes):
    out = set()
    for item in dishes:
        out = out.union(item)
    return out

def separate_appetizers(dishes, appetizers):
    return set(dishes).difference(appetizers)

def singleton_ingredients(dishes, intersection):
    out = set()
    for dish in dishes:
        out = out.union(dish)
    return out.difference(intersection)
