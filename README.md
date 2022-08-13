# xgboost_model

#要load xgboost model一點注意事項

#載xgboost  
# AttributeError: 'XGBClassifier' object has no attribute 'use_label_encoder'    => pip install xgboost==1.2.0
#載scikit-learn         =>  pip install -U scikit-learn
#load model  XXX.pkl  =>  xgb_model_loaded = joblib.load('train.pkl')    pkl檔為qoca aim training 好 下載下來
#傳入的資料型態是Dataframe
