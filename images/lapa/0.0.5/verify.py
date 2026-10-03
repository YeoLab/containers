from importlib.metadata import version

from lapa.cluster import Cluster


assert version("lapa") == "0.0.5"
cluster = Cluster("chr1", 10, 11, "+")
cluster.extend(11, 1)
cluster.extend(12, 5)
cluster.extend(13, 1)
assert cluster.total_count == 7
assert cluster.peak(window=3, std=1) == 12
print("LAPA 0.0.5 smoke test passed")
