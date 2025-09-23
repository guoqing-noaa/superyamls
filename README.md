# 1. Generate superyamls
Run the following commands to get the latest super YAML files:
```
git clone https://github.com/NOAA-EMC/RDASApp.git
cd RDASApp/rrfs-test/validated_yamls/templates
git clone git@github.com:guoqing-noaa/superyamls
cd superyamls
./yaml_cat_together.py all
```
You will get `jedivar.yaml`, `getkf.xml` under the current directory    
Run `yaml_cat_together.py ?` for more information.    
Run `yaml_cat_together.py t133,uv233` will generate a super YAML file that contains only the t133,uv233 observers.

# 2. compare with current rrfs-workflow version to finalize

