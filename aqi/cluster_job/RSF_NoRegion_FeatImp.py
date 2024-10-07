# Import libraries ---------------------------------------

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.inspection import permutation_importance
from sksurv.ensemble import RandomSurvivalForest
from sksurv.preprocessing import OneHotEncoder
import joblib
from memory_profiler import memory_usage
import joblib



# Import data --------------------------------------------

# Data
data = pd.read_csv(os.path.join(os.getcwd(), 'clean_data.csv'))

# Model fit
rf_random = joblib.load(os.path.join(os.getcwd(), 'best_RSF_NoRegion.pkl'))



# Select features ----------------------------------------

features = [
    'aqhi_average_og','tavg_average_og'
    ,'wspd_average_og','ndvi_average'
    ,'prcp_average_og'
]



# Prepare features ---------------------------------------

# Drop NAs
X = data.dropna(subset = ['death_next_season', 'hive_age_next_season'], axis = 0)
X.fillna(0, inplace = True)

# Features object adding region
X = X[features]

# Convert y to boolean
data['death_next_season'] = data['death_next_season'].astype(bool)



# Split data ---------------------------------------------

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    np.array(data.apply(lambda x: (x["death_next_season"], x["hive_age_next_season"]), axis = 1)\
        .tolist(), dtype = [('cens', '?'), ('time', '<f8')]),
    test_size = 0.15,
    random_state = 8
)

# Apply min-max transform
mx = StandardScaler()
X_train = mx.fit_transform(X_train)
X_test = mx.transform(X_test)



# Compute variable importance ----------------------------

result = permutation_importance(
    rf_random,
    X_test, y_test,
    n_repeats = 15,
    random_state = 8,
    n_jobs = 16
)

output_dir = os.getcwd()  # Use current working directory
filename = os.path.join(output_dir, "RSF_NoRegion_FeatImp.pkl")

joblib.dump(result, filename)