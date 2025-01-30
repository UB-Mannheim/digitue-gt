#!/usr/bin/python3

# Add new fileGrp sections for THUMBS and FULLTEXT to existing mets file.

import re

# https://docs.python.org/3/library/xml.dom.html

BASE_URL = 'https://ub-backup.bib.uni-mannheim.de/~stweil/digitue/theo/Monographien'

# Extract from METS file:
#
# [...]
#  <fileSec>
#    <fileGrp USE="DEFAULT">
#      <file ID="file_andlaw1863_1" MIMETYPE="image/jpeg">
#        <FLocat LOCTYPE="URL" xlink:href="https://opendigi.ub.uni-tuebingen.de/opendigi/image/andlaw1863/andlaw1863_00001.jp2/full/full/0/default.jpg"/>
#      </file>
# [...]
#  <structMap TYPE="PHYSICAL">
#    <div ID="phys_andlaw1863" TYPE="physSequence">
#      <div ID="phys_andlaw1863_1" ORDER="1" ORDERLABEL="0" TYPE="page">
#        <fptr FILEID="file_andlaw1863_1"/>
#      </div>
# [...]

import xml.dom.minidom
p = xml.dom.minidom.parse('mets')
fileSec = p.getElementsByTagName('fileSec')[0]

fileGrps = p.getElementsByTagName('fileGrp')
fptrs = p.getElementsByTagName('fptr')

fileGrpDefault = None
fileGrpFulltext = None
fileGrpThumbs = None
for fg in fileGrps:
    if fg.getAttribute('USE') == 'DEFAULT':
        fileGrpDefault = fg
    if fg.getAttribute('USE') == 'FULLTEXT':
        fileGrpFulltext = fg
    if fg.getAttribute('USE') == 'THUMBS':
        fileGrpThumbs = fg

if not fileGrpDefault:
    print('Missing fileGrp DEFAULT')
elif fileGrpFulltext:
    print('Existing fileGrp FULLTEXT')
else:
    # Add fileGrp FULLTEXT.
    fileGrp = p.createElement('fileGrp')
    fileGrp.setAttribute('USE', 'FULLTEXT')
    for fileDefault in fileGrpDefault.childNodes:
        id = fileDefault.getAttribute('ID')
        altoID = re.sub(r'^file', r'alto', id)
        thumbID = re.sub(r'^file', r'thmb', id)
        for fptr in fptrs:
            if fptr.getAttribute('FILEID') == id:
                fptrAlto = p.createElement('fptr')
                fptrAlto.setAttribute('FILEID', altoID)
                fptr.parentNode.appendChild(fptrAlto)
                if not fileGrpThumbs:
                    fptrThumb = p.createElement('fptr')
                    fptrThumb.setAttribute('FILEID', thumbID)
                    fptr.parentNode.appendChild(fptrThumb)
                break
        flocat = fileDefault.getElementsByTagName('FLocat')[0]
        href = flocat.getAttribute('xlink:href')
        match = re.match(r'^http.*opendigi.image.([^/]+)/(.*).jp2.*', href)
        project = match.group(1)
        name = match.group(2)
        file = p.createElement('file')
        file.setAttribute('ID', altoID)
        file.setAttribute('MIMETYPE', 'text/xml')
        FLocat = p.createElement('FLocat')
        FLocat.setAttribute('LOCTYPE', 'URL')
        FLocat.setAttribute('xlink:href', BASE_URL + '/' + project + '/' + name + '.xml')
        file.appendChild(FLocat)
        fileGrp.appendChild(file)
        fileSec.appendChild(fileGrp)
    # Add fileGrp THUMBS.
    fileGrp = p.createElement('fileGrp')
    fileGrp.setAttribute('USE', 'THUMBS')
    for fileDefault in fileGrpDefault.childNodes:
        id = fileDefault.getAttribute('ID')
        thumbID = re.sub(r'^file', r'thmb', id)
        flocat = fileDefault.getElementsByTagName('FLocat')[0]
        href = flocat.getAttribute('xlink:href')
        href = re.sub(r'full/full', r'full/,150', href)
        file = p.createElement('file')
        file.setAttribute('ID', thumbID)
        file.setAttribute('MIMETYPE', 'image/jpeg')
        FLocat = p.createElement('FLocat')
        FLocat.setAttribute('LOCTYPE', 'URL')
        FLocat.setAttribute('xlink:href', href)
        file.appendChild(FLocat)
        fileGrp.appendChild(file)
        fileSec.appendChild(fileGrp)

print(p.toprettyxml(indent='  ').strip())
