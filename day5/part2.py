import sys

lines = sys.stdin.readlines()
ind = lines.index("\n")
rngs = [list(map(int, ln.split('-'))) for ln in lines[0:ind]]
rngs = sorted(rngs, key=lambda x: x[0])

tot = 0
while len(rngs) > 0:
    if len(rngs) > 1 and rngs[1][0] <= rngs[0][1] + 1:
        rngs[1][0] = rngs[0][0]
        rngs[1][1] = max(rngs[0][1], rngs[1][1])
        rngs = rngs[1:]
    else:
        tot += rngs[0][1] - rngs[0][0] + 1
        rngs = rngs[1:]
        cnt += 1

print(tot)
