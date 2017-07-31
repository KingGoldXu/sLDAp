from __future__ import print_function, division

import json

with open('data/aspectjhalffilter.txt') as f1:
    with open('data/aspectjfullfilter.txt', 'w+') as f2:
        for line in f1:
            a = eval(line)
            if(a['ava'] < 300):
                json.dump(a, f2)
                f2.write('\n')