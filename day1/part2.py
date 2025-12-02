import sys
from itertools import repeat

lines = sys.stdin.readlines()
nos = map(lambda x: int(x.replace("L","-").replace("R","")), lines)
nos = [y for x in nos for y in repeat(x/abs(x),abs(x)) ]
acc = 50
mapped = [acc := (acc + x) % 100 for x in nos]
print(len([x for x in mapped if x == 0]))
