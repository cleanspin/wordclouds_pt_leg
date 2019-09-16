#!/usr/bin/python

inputs= ['cds.txt', 'alianca.txt', 'pan.txt', 'psd.txt', 'ps.txt', 'cdu.txt', 'be.txt']

for i in inputs:
    filename = i
    file = open(filename, 'rt')
    text = file.read()
    file.close()
    # split based on words only
    import re
    words = re.split(r'\W+', text)
    words = [word.lower() for word in words]
    file = open(filename, 'wt')
    for w in words:
        file.write(w + " ")
    file.close()
