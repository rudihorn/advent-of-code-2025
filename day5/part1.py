import sys

lines = sys.stdin.readlines()
ind = lines.index("\n")
rngs = [list(map(int, ln.split('-'))) for ln in lines[0:ind]]
avl = [int(ln) for ln in lines[ind+1:]]
avl = sorted(avl)
rngs = sorted(rngs, key=lambda x: x[0])

fresh = 0

while len(avl) > 0 and len(rngs) > 0:
    if rngs[0][0] > avl[0]:
        avl = avl[1:]
    elif rngs[0][0] <= avl[0] and avl[0] <= rngs[0][1]:
        fresh += 1
        avl = avl[1:]
    else:
        rngs = rngs[1:]

print(fresh)
