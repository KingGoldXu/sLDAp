from __future__ import print_function, division

import json

file_nums_dict = dict()

proj = ['aspectj', 'birt', 'platform', 'pde', 'jdt']

for a in proj:
    with open('data/{}nofilter.txt'.format(a)) as f1:
        with open('{}_file_nums.txt'.format(a), 'w+') as f2:
            for line in f1:
                lnlist = eval(line)['ts']
                for ln in lnlist:
                    file, num = ln.split('|')
                    if file in file_nums_dict:
                        file_nums_dict[file].append(int(num))
                    else:
                        file_nums_dict[file] = [int(num), ]
            json.dump(file_nums_dict, f2)
