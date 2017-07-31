from __future__ import print_function, division
import json

pros = ['aspectj', 'birt', 'platform', 'pde', 'jdt']
for pro in pros:
    with open('data/{}_t.txt'.format(pro)) as f1:
        with open('data/{}_t_c.txt'.format(pro), 'w+') as f2:
            for a in f1:
                x = eval(a)
                if x['tc'] <= 604800:
                    x['tctg'] = -1
                elif x['tc'] <= 2592000:
                    x['tctg'] = 0
                else:
                    x['tctg'] = 1
                json.dump(x, f2)
                f2.write('\n')
