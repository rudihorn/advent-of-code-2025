import sys

lines = sys.stdin.readlines()
nos = map(lambda x: int(x.replace("L","-").replace("R","")), lines)
acc = 50
mapped = [acc := (acc + x) % 100 for x in nos]
print(len([x for x in mapped if x == 0]))
