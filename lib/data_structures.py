spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [item["name"] for item in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [item for item in spicy_foods if item["heat_level"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    replacement_character = "🌶"
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        print(f'{name} ({cuisine}) | Heat Level: {heat_level * replacement_character}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if item["cuisine"] == cuisine:
            return item
    return None

def print_spiciest_foods(spicy_foods):
    replacement_character = "🌶"
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food["heat_level"]
            print(f'{name} ({cuisine}) | Heat Level: {heat_level * replacement_character}')

def get_average_heat_level(spicy_foods):
    count = 0
    for food in spicy_foods:
        count += food["heat_level"]
    return count / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods