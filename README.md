## DigiTue Ground Truth

This repository contains transcriptions for digitized books and journals of
the University Library of Tübingen (https://opendigi.ub.uni-tuebingen.de/digitue/).

The transcriptions were done with eScriptorium, a transcription platform
developed as part of the Scripta and RESILIENCE projects
(https://gitlab.com/scripta/escriptorium/).

Get the related images in JPEG format using this script:
```
for xml in $(find DigiRegio Theo Tue VD18 -name "*.xml"); do (cd $(dirname $xml); page=$(basename $xml .xml); base=$(echo $page|sed 's/_[0-9]*$//'); test -f $page.jpg || (echo $page; curl --silent -Lo $page.jpg https://opendigi.ub.uni-tuebingen.de/opendigi/image/$base/$page.jp2/full/full/0/default.jpg)); done
```
