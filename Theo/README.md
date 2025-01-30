## DigiTheo Ground Truth

This directory contains transcriptions for some books and journals which were digitized
by the University Library of Tübingen in the
[DigiTheo project](https://opendigi.ub.uni-tuebingen.de/digitue/theo/).

The transcriptions were done with eScriptorium, a transcription platform
developed as part of the Scripta and RESILIENCE projects
(https://gitlab.com/scripta/escriptorium/).

After exporting the transcriptions as PAGE XML files, those files were
processed to remove empty lines:

    perl -i -ne "tr|\r||d; next if /^\s*$/;print" *.xml

### List of transcriptions

#### Journals
- [Allgemeine kirchliche Zeitschrift Band 1 (1860)](https://opendigi.ub.uni-tuebingen.de/opendigi/akzs_1860) (30 pages / 1166 lines)
- [Defensio episcopi Rottenburgensis (1870)](https://opendigi.ub.uni-tuebingen.de/opendigi/hefele1870) (14 pages / 283 lines)
- [Die päpstliche Unfehlbarkeit und die Säcularisation des Kirchenstaats](https://opendigi.ub.uni-tuebingen.de/opendigi/zeller1871) (20 pages 731 lines)
- [Stimmen aus Maria-Laach Band 1 (1871)](https://opendigi.ub.uni-tuebingen.de/opendigi/stml_1871_01) (25 pages / 945 lines)
- [Stimmen aus Maria-Laach Band 2 (1872)](https://opendigi.ub.uni-tuebingen.de/opendigi/stml_1872_02) (88 pages / 3340 lines)

#### Books
- [Konrad Summenhart (1877)](https://opendigi.ub.uni-tuebingen.de/opendigi/linsenmann1877) (19 pages / 478 lines) – italic script
- [The use of Moltmann's Theology of hope in parish preaching (1976)](https://opendigi.ub.uni-tuebingen.de/opendigi/walz_1976) (71 pages / 2028 lines) - modern typewriter

Total 196 pages / 6943 lines.
