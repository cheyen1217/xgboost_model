import pickle
import pandas as pd
import joblib
import numpy as np
from xgboost import XGBClassifier
import xgboost as xgb
import gzip
from xgboost import plot_importance

import sklearn
    
xgb_model_loaded = joblib.load('train.pkl')
b = {
    "Beacon_1": [0.641509434
],
    "Beacon_2": [0.603773585
],
    "Beacon_3": [0.377358491
],
    "Beacon_4": [0.377358491
],
    "Beacon_5": [0.603773585
],
    "Beacon_7": [0.377358491
]
}
    



b = pd.DataFrame(b)

print(xgb_model_loaded.predict(b))
