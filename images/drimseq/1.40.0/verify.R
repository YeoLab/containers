suppressPackageStartupMessages(library(DRIMSeq))

stopifnot(packageVersion("DRIMSeq") == "1.40.0")

sample_ids <- paste0("sample", 1:6)
samples <- data.frame(
  sample_id = sample_ids,
  group = factor(rep(c("control", "treated"), each = 3))
)
counts <- data.frame(
  gene_id = rep(paste0("gene", 1:4), each = 2),
  feature_id = paste0("tx", 1:8),
  matrix(
    c(
      80, 82, 79, 20, 18, 22, 20, 18, 21, 82, 84, 80,
      60, 63, 58, 55, 57, 59, 40, 37, 42, 45, 43, 41,
      90, 92, 88, 86, 91, 89, 10, 12, 11, 14, 9, 13,
      55, 51, 57, 25, 28, 27, 45, 49, 43, 75, 72, 73
    ),
    nrow = 8,
    byrow = TRUE,
    dimnames = list(NULL, sample_ids)
  ),
  check.names = FALSE
)

d <- dmDSdata(counts = counts, samples = samples)
d <- dmFilter(
  d,
  min_samps_feature_expr = 2,
  min_feature_expr = 1,
  min_samps_feature_prop = 2,
  min_feature_prop = 0.01,
  min_samps_gene_expr = 2,
  min_gene_expr = 1
)

stopifnot(nrow(counts(d)) == 8, nrow(samples(d)) == 6)
message("DRIMSeq ", packageVersion("DRIMSeq"), " smoke test passed")
