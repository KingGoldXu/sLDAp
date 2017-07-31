from __future__ import print_function, division

import numpy as np
import csv
import json

files = dict()
brif_list = list()
file_num = dict()
num_list = list()
# with open('sparsefile.txt') as f:
#     sparsefile = eval(f.readline())

i = 0
aaaa = 0
data = []
with open('data/birtnofilter.txt') as f:
    for line in f:
        adata = eval(line)
        file_lines_list = eval(line)['ts']
        brif_list.append(file_lines_list)
        sum = 0
        files_ = []
        # if len(file_lines_list) <= 1:
        #     aaaa += 1
        for a in file_lines_list:
            file, lines = a.split('|')
            if file not in sparsefile:
                if file not in files:
                    files[file] = i
                    i = i + 1
                if file not in file_num:
                    file_num[file] = 1
                else:
                    file_num[file] = file_num[file] + 1
                sum += int(lines)
                files_.append(file)
        num_list.append(sum)
        if len(files_) > 0:
            adata['ts'] = files_
            adata['sum'] = sum
            data.append(adata)

with open('data/aspectjfullfilter.txt', 'w+') as f:
    for a in data:
        json.dump(a, f)
        f.write('\n')
print(aaaa)
# sparsefile = []
# for x in file_num.keys():
#     if file_num[x] <= 1:
#         sparsefile.append(x)
# print(len(files))
# print(len(sparsefile))
# with open('sparsefile.txt', 'w+') as f:
#     f.write(str(sparsefile))

# print(len(files))
# mat = np.zeros([len(brif_list), len(files)], dtype='int')
# for a in range(len(brif_list)):
#     for b in brif_list[a]:
#         x, y = b.split('|')
#         mat[a][files[x]] = int(y)
# print(mat.tolist())
#
# with open('filechange.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     for a in mat:
#         writer.writerow(a)
