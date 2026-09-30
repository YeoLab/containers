suppressPackageStartupMessages(library(DESeq2))

stopifnot(packageVersion("DESeq2") == "1.52.0")

set.seed(52)
counts <- matrix(rnbinom(600, mu = 100, size = 2), nrow = 100)
counts[1:10, 4:6] <- counts[1:10, 4:6] + 150L
storage.mode(counts) <- "integer"
col_data <- data.frame(
  condition = factor(rep(c("control", "treated"), each = 3)),
  row.names = paste0("sample", seq_len(ncol(counts)))
)
colnames(counts) <- row.names(col_data)

dds <- DESeqDataSetFromMatrix(counts, col_data, design = ~ condition)
dds <- DESeq(dds, quiet = TRUE)
res <- results(dds)

stopifnot(nrow(res) == nrow(counts), "log2FoldChange" %in% colnames(res))
message("DESeq2 ", packageVersion("DESeq2"), " smoke test passed")
