from collections import Counter
for p in ['aspectj', 'jdt', 'pde', 'birt']:

    d = [eval(l)['cm'] for l in open(p + 'fullfilter.txt')]
    cm = Counter(d)
    print(p, cm)
