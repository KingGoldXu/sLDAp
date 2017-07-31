from __future__ import print_function, division
import json

with open('data/jdthalffilter.txt') as f1:
    with open('data/jdtfullfilter.txt', 'w+') as f2:
        for a in f1:
            x = eval(a)
            if x['sum'] <= 10:
                x['ctg'] = -1
            elif x['sum'] <= 50:
                x['ctg'] = 0
            else:
                x['ctg'] = 1
            json.dump(x, f2)
            f2.write('\n')
