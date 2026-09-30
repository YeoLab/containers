from importlib.metadata import version
from pathlib import Path

import swan_vis as swan


assert version("swan-vis") == "3.2"

gtf = Path("/tmp/swan-smoke.gtf")
gtf.write_text(
    'chr1\tsmoke\tgene\t1\t200\t.\t+\t.\tgene_id "g1"; gene_name "G1";\n'
    'chr1\tsmoke\ttranscript\t1\t200\t.\t+\t.\tgene_id "g1"; '
    'transcript_id "t1"; gene_name "G1"; transcript_name "T1";\n'
    'chr1\tsmoke\texon\t1\t50\t.\t+\t.\tgene_id "g1"; '
    'transcript_id "t1"; exon_number "1";\n'
    'chr1\tsmoke\texon\t101\t200\t.\t+\t.\tgene_id "g1"; '
    'transcript_id "t1"; exon_number "2";\n'
)

graph = swan.SwanGraph()
graph.add_transcriptome(str(gtf))
assert graph.t_df.shape[0] == 1
assert graph.edge_df.shape[0] == 3
print("Swan 3.2 smoke test passed")
