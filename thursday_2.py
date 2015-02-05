#! /usr/bin/python
from __future__ import division

print "Hello World"

def bradysRevenge(bro):
        bigbro = bro.upper()
        print "You mad, " + bigbro + "?"


def get_at_content(dna):
    length = len(dna)
# make dna input all uppercase
    dna = dna.upper()
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
# round AT percentage to 2 significant figures
    return round(at_content, 2)


