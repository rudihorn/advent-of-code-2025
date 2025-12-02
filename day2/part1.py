import sys

lines = sys.stdin.readlines()
to_range = lambda x: range(x[0],x[1]+1)
is_invalid = lambda x: x == x[:int(len(x)/2)]*2
vs = [y for rng in lines[0].split(',') for y in to_range(list(map(int, rng.split('-')))) if is_invalid(str(y)) ]
print(sum(vs))
