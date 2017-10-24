# -*- coding: utf-8 -*-

import json
import os
import requests

for x in range(26651, 26700):
    for y in range(13600, 13700):
        for s in ['a', 'b', 'c', 'd']:
            url = 'https://' + str(s) + '.data.osmbuildings.org/0.2/ph2apjye/tile/15/' + str(x) + '/' + str(y) + '.json'
            print url

            try:
                r = requests.get(url)
            except:
                print 'ERROR'
            finally:
                if r.status_code is 200:
                    distFile = r'dist/' + str(x) + '/' + str(y) + '.json'
                    if os.path.exists(distFile):
                        print 'File exist'
                    else:
                        os.makedirs('dist/' + str(x))
                        distFile = open('dist/' + str(x) + '/' + str(y) + '.json', 'w')

                    distFile.write(json.dumps(r.json()))

    #https://a.data.osmbuildings.org/0.2/ph2apjye/tile/15/27194/13302.json
