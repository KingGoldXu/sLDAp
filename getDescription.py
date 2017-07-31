from __future__ import print_function, division
from urllib import request
from bs4 import BeautifulSoup

import pymysql

search_url = 'https://bugs.eclipse.org/bugs/show_bug.cgi?id='
config = {
    'host': '114.212.82.204',
    'port': 3316,
    'user': 'xsb',
    'password': 'mmw83686590',
    'db': 'sLDA',
    'charset': 'utf8'
}
conn = pymysql.connect(**config)
cur = conn.cursor()
cur.execute('SELECT id FROM AspectJ where Description is null;')
ids = cur.fetchall()
print(ids)
sql = 'update AspectJ set Description=%s where id=%s;'
for a in ids:
    req = request.Request(search_url + str(a[0]))
    with request.urlopen(req) as f:
        soup = BeautifulSoup(f.read().decode('utf-8'), 'lxml')
        description = soup.pre.text
        print(a[0], description)
        cur.execute(sql, (description, str(a[0])))
        print(description)
conn.commit()
conn.close()
# with open('data/iddescription.csv', 'w', newline='') as csvf:

# req = request.Request('https://bugs.eclipse.org/bugs/show_bug.cgi?id=347185')
# with request.urlopen(req) as f:
#     soup = BeautifulSoup(f.read().decode('utf-8'), 'lxml')
#     # description = soup.find_all('pre')
#     print(soup.pre.string)
