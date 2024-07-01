import requests
import json
import os

api_key = os.getenv('GOOGLE_MAP_API_KEY')

if not api_key:
    raise ValueError("API key not found. Please set the environment variable 'GOOGLE_MAP_API_KEY'.")

#基础数据设置
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
radius = float(input("enter search radius in meters: "))
center = '38.544657, -121.740501' ##目测dt中心

#获取饭店信息
def get_place(api_key = api_key, location = center, radius = radius, place_type = 'restaurant'):
    para = {
        'key': api_key,
        'location': location,
        'radius': radius,
        'type': place_type
    }

    response = requests.get(url, params = para)

    #check status
    if response.status_code == 200:

        #转换为python字典（response.json()内置方法），用['results']提取数据
        places = response.json()['results']
        return places
    else:
        print('Error:', response.status_code, response.text)
        return []
    
places = get_place()

# 保存饭店信息到 JSON 文件,供后续使用
def save_places(places, filename = 'places.json'):
    with open(filename, 'w') as file:
        json.dump(places, file, indent = 2)

save_places(places)