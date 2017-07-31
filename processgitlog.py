from __future__ import print_function, division

import re
import json

commits = []
history = []
with open('jdt.gitlog') as f:
    commit = []
    for a in f:
        if a.startswith('commit ') and commit != []:
            if a not in history:
                history.append(a)
                commits.append(commit)
            commit = []
        commit.append(a)

bug_commits = {}
for commit in commits:
    id0 = re.findall('\d{5,7}', commit[4])
    for id_ in id0:
        if '' + id_ in bug_commits:
            val = bug_commits[''+id_]
        else:
            val = []
        for line in commit:
            if line.startswith(' ') \
                    and (not line.startswith('  ')):
                pureline = line.strip(' +-\n').replace(' ', '')
                if (not pureline.startswith('test')) \
                        and (pureline.count('|') == 1) \
                        and (pureline.count('->') == 0):
                    val.append(pureline)
        bug_commits['' + id_] = val

print(len(bug_commits))
with open('jdtbugfix.txt', 'w+') as f:
    json.dump(bug_commits, f)
