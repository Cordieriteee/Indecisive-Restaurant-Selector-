import random
import json

#加载饭店信息
def load_restaurant(filename = 'places.json'):
    with open(filename, 'r') as file:
        places = json.load(file)
    return places

#随机选择饭店
def random_select_restaurant(places):
    if not places:
        print("No places to choose from.")
        return None
    
    selected = random.choice(places)
    return selected

places = load_restaurant()
selected = random_select_restaurant(places)
name = selected['name']
rating = selected['rating']
print(name, "rating: ", rating)