from importlib.metadata import version

import pandas as pd
import pyranges as pr
import pyrle  # noqa: F401  (needed by LAPA's coverage method)

from lapa.cluster import Cluster


assert version("lapa") == "0.0.5"
cluster = Cluster("chr1", 10, 11, "+")
cluster.extend(11, 1)
cluster.extend(12, 5)
cluster.extend(13, 1)
assert cluster.total_count == 7
assert cluster.peak(window=3, std=1) == 12

# LAPA rebuilds PyRanges from their own tables and joins them by strand;
# newer pyranges/pandas combinations lose the strand information here.
gr = pr.PyRanges(pd.DataFrame({
    "Chromosome": ["chr1", "chr1"], "Start": [10, 20], "End": [15, 25], "Strand": ["+", "-"],
}))
gr = pr.PyRanges(gr.df)
assert gr.stranded
assert len(gr.join(gr, strandedness="same")) == 2

# LAPA smooths coverage with a gaussian window (needs scipy < 1.13 with pandas 1.5)
assert pd.Series(range(10)).rolling(5, win_type="gaussian", center=True).sum(std=1).notna().any()
print("LAPA 0.0.5 smoke test passed")
