# -*- coding: utf-8 -*-

import json, os, random

sourceFile = file(r'src/roads.json')

roads = json.load(sourceFile)

newRoads = []
newSegments = []

for road in roads:
    newSegments = []
    x = random.randint(5, 10)
    y = random.randint(1, 20)
    for item in road['geometry']['coordinates']:

        newItem = item[0] * x + item[1] * y
        item.append(newItem)

        newSegments.append(item)

    newRoads.append({
        "vendor": random.randint(0, 1),
        "segments": newSegments
    })



print json.dumps(newRoads)

distFile = r'dist/roads.json'
if os.path.exists(distFile):
    message = 'OK, the "%s" file exists.'
else:
    distFile = open('dist/roads.json', 'w')


distFile.write(json.dumps(newRoads))



sourceFile.close()
distFile.close()
