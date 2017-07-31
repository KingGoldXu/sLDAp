from __future__ import print_function, division

import json

with open('jdtfullfilter.txt') as f1:
    with open('fjdtbugfix.txt') as f2:
        with open('data/jdtnofilter.txt', 'w+') as f3:
            id_commit = eval(f2.readline())
            for line in f1:
                a = eval(line)
                if a['id'] in id_commit:
                    files = id_commit[a['id']]
                    if len(files) != 0:
                        a['ts'] = files
                        json.dump(a, f3)
                        f3.write('\n')
