import sys
import numpy as np

lines = sys.stdin.readlines()
coords = np.array([[int(x) for x in line.split(',')] for line in lines])


dists = np.hstack([coords[0:], np.transpose([np.sqrt(np.sum(np.square(coords[0:] - coords[0]), axis=1))])])
sdists = np.array(sorted(dists, key= lambda x: x[3]))
mindist = sdists[1,3]
minp = [sdists[0,0:3],sdists[1,0:3]]
for i in range(0, len(coords)):
    j = i + 1
    while j < len(coords) and sdists[j, 3] - sdists[i, 3] < mindist:
        j += 1
    dists2 = np.hstack([coords[i:j], np.transpose([np.sqrt(np.sum(np.square(coords[i:j] - coords[i]), axis=1))])])
    sdists2 = np.array(sorted(dists2, key=lambda x: x[3]))
    print(sdists2)
    if len(sdists2) > 1 and sdists2[1,3] < mindist:
        mindist = sdists2[1,3]
        minp = [sdists2[0,0:3],sdists2[1,0:3]]
print(mindist)
print(minp)


