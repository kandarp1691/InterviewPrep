# https://www.hackerrank.com/challenges/angry-professor/problem

# !/bin/python

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n ,k = raw_input().strip().split(' ')
    n ,k = [int(n) ,int(k)]
    a = map(int ,raw_input().strip().split(' '))
    sum = 0
    for i in a:
        if i <= 0: k-=1
    if k <= 0:
        print 'NO'
    else:
        print 'YES'



