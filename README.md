# heal_translator_queries
Set of interesting queries for heal + translator discovery

Currently runs set of queries in tranql_queries against heal instance and stores output in tranql_output.
A notebook is also generated to view results. 

Todo :
[ ] Add more queries exploring other ARAs and KPs


### Usage

##### Install 
```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

##### Run 
```shell
python main.py
```
##### View
###### Local
```shell
jupyter nbextension enable --py gamma_viewer 
jupyter notebook viewer.ipynb
```
###### Binder link

On web browser go to [this binder link.](https://mybinder.org/v2/gh/helxplatform/heal_translator_queries.git/HEAD?filepath=viewer.ipynb)