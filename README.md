# Indecisive-Restaurant-Selector-
使用本选择器之前，你需要获取Google map的api。如果你完全懒得修改任何代码，那么你需要将api设置在环境变量中，并将变量名设置为'GOOGLE_MAP_API_KEY'.当然，如果你是ucdavis的学生，此时站在downtown旁边准备在dt挑家饭店吃饭，那么你可以省去生成的步骤。'places.json'文件以我目测的davis city dt中心为中心，获取了附近一公里的所有饭店，之所以这么设置是因为我经常想去dt吃饭但是不知道去哪。

'restaurant.ipynb'：获取指定以指定中心的指定半径内的所有饭店
'find_restaurant.py': 从'places.json'中，随机生成一个饭店和它的评分，太烂的话就别去吃了。
