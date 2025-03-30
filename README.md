# superyamls
Run the following commands to get the latest super YAML files:
```
git clone https://github.com/NOAA-EMC/RDASApp.git
cd RDASApp/rrfs-test/validated_yamls/templates
git clone https://github.com/guoqing-noaa/superyamls
cd superyamls
./yaml_cat_together.py all
```
You will get `jedivar.yaml`, `getkf_solver.yaml`, `getkf_solver.yaml` under the current directory    

Tip:    
You can run
```
sed -n "/obs space:/{n;p;}" jedivar.yaml
```
to check available observers in jedivar.yaml
