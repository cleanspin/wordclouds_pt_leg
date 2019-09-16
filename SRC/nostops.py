#!/usr/bin/python

inputs= ['cds.txt', 'alianca.txt', 'pan.txt', 'psd.txt', 'ps.txt', 'cdu.txt', 'be.txt']

with open('stopwords.txt') as file:
    stops = [line.strip() for line in file]


for i in inputs:
    filename = i
    with open(i) as file:
        text = [line.strip() for line in file]
    file = open(filename, 'wt')
    for t in text:
        if t not in stops:
            file.write(t + " ")
    file.close()
