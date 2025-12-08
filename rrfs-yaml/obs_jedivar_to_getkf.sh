#!/bin/bash

sed '/observers:/q' getkf.yaml > .tmp.getkf.yaml
sed '1,/observers:/d' jedivar.yaml > .tmp.obsSpace.yaml
mv .tmp.getkf.yaml getkf.yaml
cat .tmp.obsSpace.yaml >> getkf.yaml
rm .tmp.obsSpace.yaml
