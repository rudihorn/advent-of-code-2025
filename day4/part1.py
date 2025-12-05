import sys
import numpy as np
import scipy as sp

lines = sys.stdin.readlines()

gr = np.array([[0 if c == '.' else 1 for c in line] for line in lines])[:,:-1]
print(gr)
cv = [ [1, 1, 1], [1, 0, 1], [1, 1, 1] ]
gr2 = sp.signal.convolve2d(gr, cv)[1:-1,1:-1]
res = gr * (gr2 < 4)
print(res)
print(sum(sum(res)))
