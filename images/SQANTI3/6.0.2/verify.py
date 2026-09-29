import subprocess
import tempfile
from pathlib import Path

from src.config import __version__
from src.parsers import isoforms_parser


assert __version__ == "6.0.2"
assert "SQANTI3 6.0.2" in subprocess.check_output(
    ["sqanti3_qc.py", "--version"], text=True
)

Path("/test/logs").mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory() as directory:
    gene_pred = Path(directory) / "isoforms.genePred"
    gene_pred.write_text(
        "tx1\tchr1\t+\t0\t200\t0\t200\t2\t0,100,\t50,200,\t0\tgene1\tcmpl\tcmpl\t0,0,\n"
    )
    parsed = isoforms_parser(str(gene_pred))
    assert len(parsed["chr1"]) == 1
    assert parsed["chr1"][0].junctions == [(50, 100)]

for executable in ("gffread", "gmap", "minimap2", "samtools", "STAR"):
    subprocess.run(["bash", "-c", f"command -v {executable}"], check=True)

subprocess.run(
    ["Rscript", "-e", "stopifnot(as.character(packageVersion('RColorConesa')) == '1.0.0')"],
    check=True,
)
print("SQANTI3 6.0.2 smoke test passed")
