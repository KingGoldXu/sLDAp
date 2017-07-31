from __future__ import print_function

import json
with open('jdtbugfix.txt') as f1:
    with open('fjdtbugfix.txt', 'w+') as f2:
        id_commits = eval(f1.readline())
        id_com = dict()
        for id, commit in id_commits.items():
            com = []
            for x in commit:
                file, num = x.split('|')
                print(file)
                if file.endswith('.java') and file.count('src/') > 0:
                    newfile = file[file.index('src/')+4:-5].replace('/', '.')
                    print(newfile)
                    com.append(newfile + '|' + num)
            id_com[id] = com
        json.dump(id_com, f2)