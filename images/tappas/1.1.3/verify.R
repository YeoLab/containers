required <- c(
  "DEXSeq", "edgeR", "NOISeq", "goseq", "maSigPro",
  "callr", "devtools", "ggplot2", "MASS", "plyr", "VennDiagram",
  "ggrepel", "cowplot", "tidyverse", "UpSetR", "GOglm"
)

missing <- required[!vapply(required, requireNamespace, logical(1), quietly = TRUE)]
stopifnot(length(missing) == 0)
stopifnot(packageVersion("DEXSeq") == "1.58.0")

message(
  "tappAS R dependency smoke test passed (R ",
  paste(R.version$major, R.version$minor, sep = "."),
  ")"
)
