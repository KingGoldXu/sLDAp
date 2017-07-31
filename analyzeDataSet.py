import time
pros = ['aspectj', 'jdt', 'pde', 'birt']

for p in pros:
    data = [eval(l) for l in open(p + 'fullfilter.txt')]
    maxtm = max([l['tm'] for l in data])
    mintm = min([l['tm'] for l in data])
    toTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(maxtm))
    fromTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mintm))
    fixed_files = []
    for d in data:
        fixed_files += d['ts']

    sourcefiles = len(open(p + '.csv').read().split('\n'))
    print(p, fromTime, toTime, len(set(fixed_files)), sourcefiles, len(data), len(fixed_files))
