import sys
import numpy as np

lines = sys.stdin.readlines()
mapto = lambda line: [0 if c == '.' else 1 for c in line[:-1]]
start = np.array(mapto(lines[0]))
mp = np.array([mapto(l) for l in lines[1:]])
def proc_next(prev, line):
    new = np.convolve(prev * line, [1, 0, 1], mode = 'same')
    direct = prev * (np.logical_not(line))
    return np.sum(prev * line), new + direct

count = 0
cur = start
for ln in mp:
    added, cur = proc_next(cur, ln)
    count += added
print(sum(cur))
