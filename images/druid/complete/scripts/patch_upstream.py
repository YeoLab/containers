"""Small, checked patches to pinned upstream; the original stays in *.upstream.*."""
from pathlib import Path
import shutil
root = Path('/opt/DRUID')
p = root / 'DRUID.R'
shutil.copy(p, root / 'DRUID.upstream.R')
s = p.read_text()
s = s[:s.index('#                                   Example')]
old = '''  introns.mean.filt.norm <- introns.mean.filt / lib.sizes
  maxes <- apply(introns.mean.filt.norm, 1, max)
  maxes.matrix <- matrix(rep(maxes, length(maxes)), ncol = length(maxes))
  introns.mean.filt.norm <- introns.mean.filt.norm / maxes.matrix'''
assert s.count(old) == 1
s = s.replace(old, '''  introns.mean.filt.norm <- sweep(as.matrix(introns.mean.filt), 2, lib.sizes, "/")
  maxes <- apply(introns.mean.filt.norm, 1, max)
  introns.mean.filt.norm <- sweep(introns.mean.filt.norm, 1, maxes, "/")''')
p.write_text(s)
# coverage.py was Python 2 with mixed tabs; preserve numerical coverage semantics.
p = root / 'coverage.py'
shutil.copy(p, root / 'coverage.upstream.py')
shutil.copy('/opt/workflow/coverage.py', p)
# Replace the hard-coded-path shell wrapper with a fail-fast equivalent.
p = root / 'preDRUID.sh'
shutil.copy(p, root / 'preDRUID.upstream.sh')
shutil.copy('/opt/workflow/preDRUID.sh', p)
# GenomicFeatures renamed the exons() selection argument from vals to filter.
p = root / 'process_GTF.R'
shutil.copy(p, root / 'process_GTF.upstream.R')
s = p.read_text()
old = 'vals = list(tx_id=transcripts.length$tx_id)'
assert s.count(old) == 1
p.write_text(s.replace(old, 'filter = list(tx_id=transcripts.length$tx_id)'))
# Modern GenomicRanges no longer accepts ignoreSelf in this method. Remove
# diagonal self hits explicitly, preserving strand-aware exon overlap filtering.
p = root / 'process_GTF.R'
s = p.read_text()
old = '''ov <- findOverlaps(
  exons,
  type = "any",
  ignoreSelf = TRUE,
  select = "arbitrary"
)
exons <- exons[is.na(ov)]'''
assert s.count(old) == 1
s = s.replace(old, '''ov <- findOverlaps(exons, exons, type = "any")
overlapping <- queryHits(ov)[queryHits(ov) != subjectHits(ov)]
exons <- exons[!seq_along(exons) %in% overlapping]''')
p.write_text(s)
