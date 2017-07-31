from __future__ import print_function, division

import numpy as np
import csv
import json

files = dict()
brif_list = list()
file_num = dict()
num_list = list()
data = []
i = 0
with open('data/jdtnofilter.txt') as f:
    for line in f:
        adata = eval(line)
        file_lines_list = eval(line)['ts']
        brif_list.append(file_lines_list)
        sum = 0
        files_ = []
        new_f_l_list = []
        for a in file_lines_list:
            file, lines = a.split('|')
            if file not in file_num:
                file_num[file] = 1
            else:
                file_num[file] = file_num[file] + 1
            if file not in files_:
                sum += int(lines)
                files_.append(file)
                new_f_l_list.append(file+'|'+lines)
            num_list.append(sum)
        if len(files_) > 0:
            adata['ts'] = new_f_l_list
            adata['sum'] = sum
            adata['ava'] = sum // len(files_)
            data.append(adata)

sparsefile = []
for x in file_num.keys():
    if file_num[x] <= 1:
        sparsefile.append(x)
print('files len:', len(files))
print('sparsefile len:', len(sparsefile))

with open('data/jdthalffilter.txt', 'w+') as f:
    for a in data:
        f_ls = a['ts']
        files_ = []
        sum = 0
        for f_l in f_ls:
            file, lines = f_l.split('|')
            if file not in sparsefile:
                sum += int(lines)
                files_.append(file)
        if len(files_) > 0:
            a['ts'] = files_
            a['sum'] = sum
            a['ava'] = sum // len(files_)
            json.dump(a, f)
            f.write('\n')
