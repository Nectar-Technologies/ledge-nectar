# Import libraries ---------------------------------------

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sksurv.ensemble import RandomSurvivalForest
from sksurv.preprocessing import OneHotEncoder
import joblib
from memory_profiler import memory_usage



# Import data --------------------------------------------

data = pd.read_csv(os.path.join(os.getcwd(), 'clean_data.csv'))



# Define hyperparameters ---------------------------------

# Number of trees in random forest
#n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1250, num = 10)]
n_estimators = [100, 500, 1000]  # Reduced

# Number of features to consider at every split
#max_features = ['auto', 'sqrt']
max_features = ['sqrt', 'log2']

# Maximum number of levels in tree
#max_depth = [int(x) for x in np.linspace(10, 60, num = 10)]
#max_depth.append(None)
max_depth = [10, 30, 60]  # Reduced

# Minimum number of samples required to split a node
# min_samples_split = [10, 20, 40, 60]
min_samples_split = [10, 20, 40] # Reduced

# Minimum number of samples required at each leaf node
#min_samples_leaf = [10, 20, 40, 60]
min_samples_leaf = [10, 20, 40] # Reduced

# Method of selecting samples for training each tree
bootstrap = [True, False]

# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}



# Select features ----------------------------------------

features = [
    'aqhi_average_og','tavg_average_og'
    ,'wspd_average_og','ndvi_average'
    ,'prcp_average_og'
]



# Prepare features ---------------------------------------

# One-hot enconding of region
gr = pd.get_dummies(data['region'])

# Drop NAs
X = data.dropna(subset = ['death_next_season', 'hive_age_next_season'], axis = 0)
X.fillna(0, inplace = True)

# Features object adding region
X = X[features]
X = pd.concat([X, gr], axis = 1)

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



# Fit model ----------------------------------------------

def fit_model():
    rf = RandomSurvivalForest()

    rf_random = RandomizedSearchCV(
        estimator=rf,
        param_distributions=random_grid,
        n_iter=5,
        cv=3,
        verbose=1,
        random_state=8,
        n_jobs=16,
    )

    # Fit the random search model
    rf_random.fit(X_train, y_train)

    # Save best model
    output_dir = os.getcwd()  # Use current working directory
    filename = os.path.join(output_dir, "best_RSF2.pkl")
    joblib.dump(rf_random.best_estimator_, filename)



# Monitor memory usage -----------------------------------

mem_usage = memory_usage(fit_model, interval=1)
print(f"Maximum memory usage: {max(mem_usage)} MB")