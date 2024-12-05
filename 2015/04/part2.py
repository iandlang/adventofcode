import hashlib
from itertools import count

stub = 'yzbqklnj'

for i in count(1):
    s = stub + str(i)
    md5 =  hashlib.md5(s.encode('utf-8')).hexdigest()
    if md5[:6] == '000000':
        print(i, md5)
        break
