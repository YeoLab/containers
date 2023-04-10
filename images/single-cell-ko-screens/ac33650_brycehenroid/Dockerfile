################## BASE IMAGE ######################

FROM brianyee/singlecellkoscreens:ac33650

################## METADATA ######################

LABEL base_image="brianyee/singlecellkoscreens:ac33650"
LABEL version="1"
LABEL software="R"
LABEL software.version="4.0.5"
LABEL about.summary="Repository containing all code for secondary analysis in the manuscript \"On the design of CRISPR-based single cell molecular screens,\" Hill, McFaline-Figueroa et al."
LABEL about.home="https://github.com/shendurelab/single-cell-ko-screens#enrichment-pcr"
LABEL about.documentation=""
LABEL about.license_file=""
LABEL about.license=""
LABEL about.tags="Genomics"

COPY preprocess_cfg.R /opt/single-cell-ko-screens/preprocess_cfg.R
ENV PATH=/opt/single-cell-ko-screens:$PATH
