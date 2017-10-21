# -*- coding: utf-8 -*-

import json
import os
import random

sourceFile = file(r'src/buildings.json')

buildings = json.load(sourceFile)

newBuildings = []
newPolygon = []

height = 0

for building in buildings:
    if building['properties'].has_key('levels'):
        # print building['properties']['levels']
        height = building['properties']['levels'] * 5
    else:
        height = random.randint(1, 25)
    for item in building['geometry']['coordinates']:
        newBuildings.append({
            "height": height,
            "polygon": item
        })


print json.dumps(newBuildings)

distFile = r'dist/buildings.json'
if os.path.exists(distFile):
    message = 'OK, the "%s" file exists.'
    os.remove(distFile)
else:
    distFile = open('dist/buildings.json', 'w')


distFile.write(json.dumps(newBuildings))

sourceFile.close()
distFile.close()
