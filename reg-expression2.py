import re

pattren = ['java','python','c']
text = 'i love python'

for i in pattren:
    if re.search(i,text):
        print('item Found')
    else:
        print('item Not found')
