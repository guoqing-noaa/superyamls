# 1. Generate superyamls
Run the following commands to get the latest super YAML files:
```
git clone https://github.com/NOAA-EMC/RDASApp.git
cd RDASApp/rrfs-test/validated_yamls/templates
git clone https://github.com/guoqing-noaa/superyamls
cd superyamls
./yaml_cat_together.py all
```
You will get `jedivar.yaml`, `getkf_solver.yaml`, `getkf_solver.yaml` under the current directory    
Run `yaml_cat_together.py ?` for more information.    
Run `yaml_cat_together.py t133,uv233` will generate a super YAML file that contains only the t133,uv233 observers.

### 2. Check available observers in a yaml file. eg:
```
./yaml_list_obs  jedivar.yaml
```

### 3. Use specified observers only and remove other observers in a YAML file. eg:
```
./yaml_use_obs  jedivar.yaml  "t133,q133,uv233,t120,q120,uv220"
./yaml_list_obs  jedivar.yaml
```

### 4. Remove specified observers in a YAML file. eg:
```
./yaml_remove_obs  jedivar.yaml  "t120,q120,uv220"
./yaml_list_obs   jedivar.yaml
```
