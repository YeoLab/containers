suppressPackageStartupMessages(library(bambu))
stopifnot(as.character(packageVersion("bambu")) == "3.14.0")

gtf <- tempfile(fileext = ".gtf")
writeLines(c(
  'chr1\tsmoke\ttranscript\t1\t200\t.\t+\t.\tgene_id "g1"; transcript_id "t1";',
  'chr1\tsmoke\texon\t1\t50\t.\t+\t.\tgene_id "g1"; transcript_id "t1"; exon_id "e1";',
  'chr1\tsmoke\texon\t101\t200\t.\t+\t.\tgene_id "g1"; transcript_id "t1"; exon_id "e2";'
), gtf)
annotations <- prepareAnnotations(gtf)
stopifnot(length(annotations) == 1L)
message("Bambu 3.14.0 smoke test passed")
