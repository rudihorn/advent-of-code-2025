import sys
import numpy as np
import scipy as sp

lines = sys.stdin.readlines()

gr = np.array([[0 if c == '.' else 1 for c in line] for line in lines])[:,:-1]
print(gr)

total = 0
cv = [ [1, 1, 1], [1, 0, 1], [1, 1, 1] ]
rmvd = 1
while rmvd > 0:
    gr2 = sp.signal.convolve2d(gr, cv)[1:-1,1:-1]
    res = gr * (gr2 < 4)
    gr = gr - res
    rmvd = sum(sum(res))
    total += rmvd

print(total)
