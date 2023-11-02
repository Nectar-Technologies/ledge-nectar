# Air quality project 

We aimed to access the impact of the air quality on the survival of honeybee in North America using BeeTrack dataset of over 100 000 hives tracked as of now. Once we access the impact, we want to predict the expected impact on mortality of colonies in 2023 which was a high forest fire year resulting in repeated very high AQHI days. (bad air quality)

***
### Setup

We used poetry to manage dependencies if you don't have it locally, you can go and following the installation steps [here](https://python-poetry.org/).

- `poetry install`
- `poetry run jupyter notebook`

If you don't want to use poetry, I've also provided a requirements.txt file that you can use in your virtualenv. 

- `pip install -r requirements.txt` 

You will also need to install R dependencies do it using the python package to ease system path management:

```bash
from rpy2.robjects.packages import importr


utils = importr('utils')
utils.chooseCRANmirror(ind=12)
utils.install_packages('lme4')
```

***
### Publications 

- [Revue l'abeille](https://docs.google.com/document/d/15AnYdtRFW2pcv2DzMdLt8dUpNkxKXdBhX5cH-WRXfas/edit)
- [Nectar data driven blog post](https://www.nectar.buzz/blog/the-impact-of-poor-air-quality-on-honeybees-and-the-influence-of-vegetation)
- Scientific paper:


***
### Data source 

You can retrieve the data from the google drive and store it under the data folder. 

Data link: 
- Merged:
- Raw AQI:



***
### Contacts

- Julien Vadnais, Ledge
- Nico Coallier, Nectar
- Yenny Cuellar, Ledge