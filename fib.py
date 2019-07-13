'''
 # @ Author: Krystian Spandel
 # @ Create Time: 2019-07-13 14:47:02
 # @ Modified by: Krystian Spandel
 # @ Modified time: 2019-07-13 14:47:11
 # @ Description:
 '''

import argparse

parser = argparse.ArgumentParser(description='Calculate [n] amount of fibonacci numbers')
parser.add_argument('amount', help='How many numbers to calculate', type=int)
parser.add_argument('-l', '--last', help='Print out only the last number', action='store_true')
args = parser.parse_args()
n = args.amount
last = args.last

i = 0
a = 0
b = 1
if not last:
    print('F[{0}]: {1}'.format(i, a)) 
# print(b)

while ( i != n ):
    c = a + b
    # print('[{}]'.format(i))
    # print(c)
    a = b
    b = c
    i += 1
    if not last:
        print('F[{0}]: {1}'.format(i, a))

if last:
    print('F[{0}]: {1}'.format(i, a))
