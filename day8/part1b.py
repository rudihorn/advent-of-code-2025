import sys
import numpy as np

lines = sys.stdin.readlines()
coords = np.array([[int(x) for x in line.split(',')] for line in lines])

class Group:
    def __init__(self, id):
        self._id = id
        self._merged = None
        self._count = 0
        self._set = set()
        self._set.add(id)

    def get_leaf(self):
        if self._other:
            return self._other.get_leaf()
        return self

    def merge(self, other):
        l1 = self.get_leaf()
        l2 = other.get_leaf()
        l1._set = l1._set.union(l2._set)
        l2._other = l1

grps = np.transpose([[Group(i) for i in range(len(coords))]])

dists = np.hstack([grps, coords[0:], np.transpose([np.sqrt(np.sum(np.square(coords[0:] - coords[0]), axis=1))])])
sdists = np.array(sorted(dists, key= lambda x: x[3]))
mindist = sdists[1,3]
minp = [sdists[0,0:3],sdists[1,0:3]]
stack = []
for i in range(0, len(coords)):
    j = i + 1
    while j < len(coords) and sdists[j, 3] - sdists[i, 3] < mindist:
        j += 1
    dists2 = np.hstack([coords[i+1:j], np.transpose([np.sqrt(np.sum(np.square(coords[i+1+1:j] - coords[i]), axis=1))])])
    stack.append(dists2)
dists2 = np.vstack(stack)
sdists2 = np.array(sorted(dists2, key=lambda x: x[3]))
print(sdists2)
if len(sdists2) > 1 and sdists2[1,3] < mindist:
    mindist = sdists2[1,3]
    minp = [sdists2[0,0:3],sdists2[1,0:3]]
print(mindist)
print(minp)


