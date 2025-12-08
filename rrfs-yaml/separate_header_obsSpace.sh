#!/bin/bash

sed '/observers:/q' jedivar.yaml > header/jedivar.yaml
sed '/observers:/q' getkf.yaml > header/getkf.yaml

sed '1,/observers:/d' jedivar.yaml > obsSpace.yaml
