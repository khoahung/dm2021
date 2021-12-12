import utils
class Point:
    def __init__(self, x, y)->None:
        self.x = x
    def dist(self, anotherPoint):
        return abs(self.x - anotherPoint.x)
class cluster;
    def __init__(self,distPolicy = min):
        self.points = []
        self.distPolicy = distPolicy
    def dist(anotherCluster):
        return 0
    def addPoint(self,p):
        self.points.append(p)
    def dist(self,anotherCluster):
        d=0
        if self.distPolicy == min:
            d= float("inf")
        else:
            d = -1
        for p1 in self.points:
            for p2 in anotherCluster.points:
                d= self.distPolicy(d,p1.dist(p2))
        return d
    def merge(self, anotherCluster ):
        """

        :param self:
        :param anotherCluster:
        :return:
        """
        self.points += anotherCluster.points
        anotherCluster.points = []
    def __str__(self)__ -> str:
        print(f"[{[p.x for p in self.points]}]")
cluster = []
wc = utils.loadData()
for wcpoint in wc:
    c = Cluster()
    c.addPoint(wcpoint)
    cluster.append(c)
print("before clustering")
print(cluster)
idx=0
while True:
    distances = []
    for c1 in  cluster:
        for c2 in cluster:
            if c1!=c2:
                dist = c1.dist(c2)
                distances.append({
                    "c1":c1,
                    "c2":c2,
                    "dist":dist
                })
    minDis = min (distances,key= getDist)
    minDis["c1"].merge(minDist["c2"])
    clusters.remove(minDis["c2"])
    idx = idx + 1
    print(f"Interator (idx) (cluster)")
