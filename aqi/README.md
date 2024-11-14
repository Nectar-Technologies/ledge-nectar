# Air quality project 

We aimed to assess the impact of air quality on the survival of honeybee in Canada and the U.S. using the BeeTrack dataset which tracks over 100 000 hives as of now. Our objective was to predict the expected impact on mortality of colonies in 2024, based on data from 2021 to 2023, which were years with record-breaking forest fires. This resulted in days of very poor air quality (high AQHI) throughout the beekeeping seasons.


***
### Setup

We used `poetry` to manage dependencies. You can follow the steps [here](https://python-poetry.org/) for a local installation.

- `poetry install`
- `poetry run jupyter notebook`

If you don't want to use `poetry`, we've also provided a `requirements.txt` file that you can use in your virtualenv.

- `pip install -r requirements.txt` 

You will also need to install `R` dependencies. You can perform it using the python package to ease system path management:

```bash
from rpy2.robjects.packages import importr

utils = importr('utils')
utils.chooseCRANmirror(ind=12)
utils.install_packages('lme4')
```


***
### Publications 

- [Revue l'abeille](https://docs.google.com/document/d/15AnYdtRFW2pcv2DzMdLt8dUpNkxKXdBhX5cH-WRXfas/edit)
- [Nectar data driven blog post](https://www.nectar.buzz/en/blog/6/)
- [Pre-print](https://www.researchsquare.com/article/rs-3760367/v1)
- Peer-reviewed publication: Coming soon!


***
### Data source 

You can contact Nico Coallier for inquiries regarding the data.


***
### Contacts

- [Nico Coallier, Nectar](https://scholar.google.com/citations?user=7v4Iiv4AAAAJ)
- [Maxime Fraser Franco, Nectar](https://www.researchgate.net/profile/Maxime-Fraser-Franco)
- [Liliana Perez, LEDGE](https://scholar.google.com.sg/citations?user=iCCIPAoAAAAJ&hl=en)
- Yenny Cuellar, LEDGE
- Julien Vadnais, LEDGE