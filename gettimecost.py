from __future__ import print_function, division
from bs4 import BeautifulSoup
from urllib import request
from dateutil import tz
from datetime import datetime
import re
import json

search_url = 'https://bugs.eclipse.org/bugs/show_activity.cgi?id='
pros = ['aspectj', 'birt', 'platform', 'pde', 'jdt']
for pro in pros:
    with open('data/{}fullfilter.txt'.format(pro)) as f1:
        with open('data/{}_t.txt'.format(pro), 'w+') as f2:
            for line in f1:
                data = eval(line)
                bugid = data['id']
                req = request.Request(search_url + bugid)
                start_time = ''
                end_time = ''
                fixed = False
                with request.urlopen(req) as f:
                    soup = BeautifulSoup(f.read().decode('utf-8'), 'lxml')
                    all_td = soup.find_all('td')
                    for td in all_td:
                        # print(td.text.strip(' \t\n'))
                        start_time = td.text.strip(' \t\n')
                        if re.match('\d{4}\-\d{2}\-\d{2}', start_time) is not None:
                            break
                    for td in reversed(all_td):
                        end_time = td.text.strip(' \t\n')
                        if 'FIXED' == end_time:
                            fixed = True
                        if re.match('\d{4}\-\d{2}\-\d{2}', end_time) is not None and fixed:
                            break
                print(start_time, 'start')
                print(end_time, 'end')
                if fixed:
                    st = start_time[:-4]
                    stz = start_time[-3:]
                    et = end_time[:-4]
                    etz = end_time[-3:]
                    s_t = datetime.strptime(st, '%Y-%m-%d %H:%M:%S')
                    s_t.replace(tzinfo=tz.gettz(stz))
                    e_t = datetime.strptime(et, '%Y-%m-%d %H:%M:%S')
                    e_t.replace(tzinfo=tz.gettz(etz))
                    time_cost = int(e_t.timestamp() - s_t.timestamp())
                    data['tc'] = time_cost
                    json.dump(data, f2)
                    f2.write('\n')
