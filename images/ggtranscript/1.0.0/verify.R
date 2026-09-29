suppressPackageStartupMessages({
  library(ggplot2)
  library(ggtranscript)
})

stopifnot(as.character(packageVersion("ggtranscript")) == "1.0.0")

exons <- data.frame(
  seqnames = c("chr1", "chr1", "chr1"),
  start = c(1, 101, 1),
  end = c(50, 150, 150),
  strand = c("+", "+", "+"),
  transcript_name = c("tx1", "tx1", "tx2")
)
introns <- to_intron(exons, "transcript_name")
stopifnot(nrow(introns) == 1L)

plot <- ggplot(exons, aes(xstart = start, xend = end, y = transcript_name)) +
  geom_range()
stopifnot(length(ggplot_build(plot)$data) == 1L)
message("ggtranscript 1.0.0 smoke test passed")
