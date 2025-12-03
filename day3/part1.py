import sys

lines = sys.stdin.readlines()
def jltage(x):
    ind = x.index(max(x[:-1]))
    return x[ind] * 10 + max(x[ind+1:])
jlts = [jltage(list(map(int, line.strip()))) for line in lines]
print(sum(jlts))

