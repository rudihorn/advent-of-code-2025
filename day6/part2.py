import sys
import numpy as np
import itertools

lines = sys.stdin.readlines()
mat = np.transpose(np.array([list(line) for line in lines[:-1]]))
mat = [''.join(l).strip() for l in mat]
groups = [list(grp) for eq, grp in itertools.groupby(mat, lambda x: x == '') if not eq]
ops = [sum if op == "+" else np.prod for op in lines[-1].split()]
res = sum([ops[i](list(map(int, groups[i]))) for i in range(len(ops))])
print(res)
