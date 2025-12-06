import sys
import numpy as np

lines = sys.stdin.readlines()
mat = np.array([[int(x) for x in line.split()] for line in lines[:-1]])
ops = [sum if op == "+" else np.prod for op in lines[-1].split()]
res = sum([ops[i](mat[:,i]) for i in range(len(ops))])
print(res)
