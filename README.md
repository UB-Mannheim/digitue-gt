## DigiTheo Ground Truth

This repository contains transcriptions for some journals which were digitized
by the University Library of Tübingen in the DigiTheo project
(http://idb.ub.uni-tuebingen.de/digitue/theo/).

The transcriptions were done with eScriptorium, a transcription platform
developed as part of the Scripta and RESILIENCE projects
(https://gitlab.com/scripta/escriptorium/).

After exporting the transcriptions as PAGE XML files, those files were
processed to remove empty lines:

    perl -i -ne "tr|\r||d; next if /^\s*$/;print" *.xml

### List of transcriptions

- [Allgemeine kirchliche Zeitschrift Band 1 (1860)](http://idb.ub.uni-tuebingen.de/opendigi/akzs_1860) (30 pages / 1166 lines)
- [Stimmen aus Maria-Laach Band 1 (1871)](http://idb.ub.uni-tuebingen.de/opendigi/stml_1871_01) (25 pages / 945 lines)
- [Stimmen aus Maria-Laach Band 2 (1872)](http://idb.ub.uni-tuebingen.de/opendigi/stml_1872_02) (88 pages / 3340 lines)

Total 143 pages / 5451 lines.
