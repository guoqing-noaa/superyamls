#!/usr/bin/env python
#
import os
import sys
f_jedivar = "jedivar.yaml"
f_getkf = "getkf.yaml"
#
with open(f_jedivar, 'r') as infile, open('.observer.yaml', 'w') as outfile:
    observer_zone = False
    for line in infile:
        if "observations:" in line:
            observer_zone = True
        elif observer_zone:
            outfile.write(line)

# getkf.yaml
with open(f_getkf, 'r') as infile, open('.observer.yaml', 'r') as infile2, open('.tmp.yaml', 'w') as outfile:
    for line in infile:
        if "observers:" in line:
            break
        else:
            outfile.write(line)
    # add the observers from jedivar.yaml
    outfile.write(infile2.read())
os.replace('.tmp.yaml', f_getkf)

os.remove(".observer.yaml")
