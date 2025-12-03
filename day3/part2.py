import sys

lines = sys.stdin.readlines()
def jltage(x):
    val = 0
    for i in range(12):
        y = x if i == 11 else x[:(i-11)]
        ind = y.index(max(y))
        x = x[ind+1:]
        val = val * 10 + y[ind]
    return val
jlts = [jltage(list(map(int, line.strip()))) for line in lines]
print(sum(jlts))

