import os 
import ast
import pickle
from datetime import datetime, date,timezone, timedelta

import pandas as pd 
import numpy as np
from collections import Counter

import seaborn as sns 
import matplotlib.pyplot as plt 
import matplotlib.ticker as mtick

from sklearn.preprocessing import MinMaxScaler
from scipy.stats import skew, kurtosis
from pymer4.models import Lmer
from pymer4.io import save_model, load_model
from lifelines import KaplanMeierFitter, CoxPHFitter
from sklearn.model_selection import train_test_split
from sksurv.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sksurv.ensemble import RandomSurvivalForest
from sklearn.model_selection import RandomizedSearchCV

from sksurv.metrics import (
    concordance_index_censored,
    concordance_index_ipcw,
    cumulative_dynamic_auc,
    integrated_brier_score,
)

from tqdm.notebook import tqdm

import warnings
warnings.filterwarnings("ignore")

ROOT_PATH = "../data"
SEASONS_INCLUDED = [2021, 2022, 2023] # Don't include 2024 
FEATURES_MONTH = [4,5,6,7,8,9] # You might wanna change this since now lots of Californian in 2023
RUN_PREPROCESS = False # Only run when needed

BUFFER = 15 # Include winter deadout 15 days pass the season start 

START_SEASON_MONTH = 6
START_SEASON_DAY = 1
END_SEASON_MONTH = 11
END_SEASON_DAY = 15