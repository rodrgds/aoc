from math import sqrt
import sys

class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.directly_connected_to = set()
        self.cluster = {self}

    def distance_to(self, other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2)

    def connected_to(self):
        return self.cluster - {self}

    def is_directly_connected_to(self, other):
        return other in self.directly_connected_to

    def connect_to(self, other):
        self.directly_connected_to.add(other)

        if self.cluster is other.cluster:
            return

        if len(self.cluster) < len(other.cluster):
            small_cluster, large_cluster = self.cluster, other.cluster
        else:
            small_cluster, large_cluster = other.cluster, self.cluster

        large_cluster.update(small_cluster)

        for node in small_cluster:
            node.cluster = large_cluster

    def __str__(self):
        return str(self.x) + "," + str(self.y) + "," + str(self.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))


coords = [Coordinate(int(line.split(",")[0]), int(line.split(",")[1]), int(line.split(",")[2])) for line in open("input.txt", "r").readlines()]

for _ in range(1000):
    min_distance = sys.maxint
    min_coords = []
    for i in range(len(coords)):
        c1 = coords[i]
        for j in range(i+1, len(coords)):
            c2 = coords[j]

            if c1 == c2 or c1.is_directly_connected_to(c2):
                continue

            curr = c1.distance_to(c2)
            if curr < min_distance:
                min_distance = curr
                min_coords = [c1, c2]

    c1, c2 = min_coords

    c1.connect_to(c2)
    c2.connect_to(c1)

connected = set()
for coord in coords:
    ordered = sorted(list(coord.cluster))

    connected.add(tuple(ordered))

connected = list(connected)
connected.sort(key=lambda l: len(l), reverse=True)

res = 1
for c in connected[:3]:
    res *= len(c)

print(res)
