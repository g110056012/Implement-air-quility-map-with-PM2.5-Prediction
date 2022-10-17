#未來24小時預測資料
import pandas as pd
import requests
import json
from keras.models import load_model,Model
import numpy as np
import datetime
from sklearn import preprocessing
import sklearn.externals 
import joblib

scaler_load = ['/Users/user/Desktop/Coding/TJ專題/Project/scaler/scaler0_8.pkl',
               '/Users/user/Desktop/Coding/TJ專題/Project/scaler/scaler1_8.pkl',
               '/Users/user/Desktop/Coding/TJ專題/Project/scaler/scaler2_8.pkl',
               '/Users/user/Desktop/Coding/TJ專題/Project/scaler/scaler3_8.pkl',
               '/Users/user/Desktop/Coding/TJ專題/Project/scaler/scaler4_8.pkl',
               '/Users/user/Desktop/Coding/TJ專題/Project/scaler/scaler5_8.pkl']

model_load = ['/Users/user/Desktop/Coding/TJ專題/Project/finalmodel/GRUmodel0.h5',
              '/Users/user/Desktop/Coding/TJ專題/Project/finalmodel/GRUmodel1.h5',
              '/Users/user/Desktop/Coding/TJ專題/Project/finalmodel/GRUmodel2.h5',
              '/Users/user/Desktop/Coding/TJ專題/Project/finalmodel/GRUmodel3.h5',
              '/Users/user/Desktop/Coding/TJ專題/Project/finalmodel/lstmmodel4.h5',
              '/Users/user/Desktop/Coding/TJ專題/Project/finalmodel/GRUmodel5.h5',
              ]
#predict_data = predict_data.dropna()
predict_data= pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/predict/finalpredict.csv', encoding='utf-8')





df0 = pd.DataFrame()    
data = predict_data[predict_data['location']==0]   #取出選擇地區的資料
data = data.drop(columns=['location'])
deviceId = data['deviceId'].reset_index(drop=True) #保存感測器編號並順序編號
data_x = data.iloc[:,1:].values        #將資料轉換為array
print(data_x)
#StandardScaler = joblib.load(scaler_load[i])       #讀取標準化權重並標準化array
#data_x = StandardScaler.transform(data_x)
data_x = data_x.reshape(len(data_x),8,3)          #reshape成時間序列資料
model = load_model(model_load[0],custom_objects=None,
    compile=False) 
#print(data_x)#讀取model
predict = model.predict(data_x) #預測，結果為array
predict = pd.DataFrame(predict)                    #array轉為dataframe
predict = pd.concat([deviceId,predict],axis=1)     #與感測器編號合併
print(predict)
df0 = pd.concat([df0,predict])                       #與其他區資料合併
    
df0 = df0.reset_index(drop=True)




df1 = pd.DataFrame()    
data = predict_data[predict_data['location']==1]   #取出選擇地區的資料
data = data.drop(columns=['location'])
deviceId = data['deviceId'].reset_index(drop=True) #保存感測器編號並順序編號
data_x = data.iloc[:,1:].values        #將資料轉換為array
print(data_x)
#StandardScaler = joblib.load(scaler_load[i])       #讀取標準化權重並標準化array
#data_x = StandardScaler.transform(data_x)
data_x = data_x.reshape(len(data_x),8,3)          #reshape成時間序列資料
model = load_model(model_load[1],custom_objects=None,
    compile=False) 
#print(data_x)#讀取model
predict = model.predict(data_x) #預測，結果為array
predict = pd.DataFrame(predict)                    #array轉為dataframe
predict = pd.concat([deviceId,predict],axis=1)     #與感測器編號合併
print(predict)
df1 = pd.concat([df1,predict])                       #與其他區資料合併
    
df1 = df1.reset_index(drop=True)




df2 = pd.DataFrame()    
data = predict_data[predict_data['location']==2]   #取出選擇地區的資料
data = data.drop(columns=['location'])
deviceId = data['deviceId'].reset_index(drop=True) #保存感測器編號並順序編號
data_x = data.iloc[:,1:].values        #將資料轉換為array
print(data_x)
#StandardScaler = joblib.load(scaler_load[i])       #讀取標準化權重並標準化array
#data_x = StandardScaler.transform(data_x)
data_x = data_x.reshape(len(data_x),8,3)          #reshape成時間序列資料
model = load_model(model_load[2],custom_objects=None,
    compile=False) 
#print(data_x)#讀取model
predict = model.predict(data_x) #預測，結果為array
predict = pd.DataFrame(predict)                    #array轉為dataframe
predict = pd.concat([deviceId,predict],axis=1)     #與感測器編號合併
print(predict)
df2 = pd.concat([df2,predict])                       #與其他區資料合併
    
df2 = df2.reset_index(drop=True)




df3 = pd.DataFrame()    
data = predict_data[predict_data['location']==3]   #取出選擇地區的資料
data = data.drop(columns=['location'])
deviceId = data['deviceId'].reset_index(drop=True) #保存感測器編號並順序編號
data_x = data.iloc[:,1:].values        #將資料轉換為array
print(data_x)
#StandardScaler = joblib.load(scaler_load[i])       #讀取標準化權重並標準化array
#data_x = StandardScaler.transform(data_x)
data_x = data_x.reshape(len(data_x),8,3)          #reshape成時間序列資料
model = load_model(model_load[3],custom_objects=None,
    compile=False) 
#print(data_x)#讀取model
predict = model.predict(data_x) #預測，結果為array
predict = pd.DataFrame(predict)                    #array轉為dataframe
predict = pd.concat([deviceId,predict],axis=1)     #與感測器編號合併
print(predict)
df3 = pd.concat([df3,predict])                       #與其他區資料合併
    
df3 = df3.reset_index(drop=True)




df4 = pd.DataFrame()    
data = predict_data[predict_data['location']==4]   #取出選擇地區的資料
data = data.drop(columns=['location'])
deviceId = data['deviceId'].reset_index(drop=True) #保存感測器編號並順序編號
data_x = data.iloc[:,1:].values        #將資料轉換為array
print(data_x)
#StandardScaler = joblib.load(scaler_load[i])       #讀取標準化權重並標準化array
#data_x = StandardScaler.transform(data_x)
data_x = data_x.reshape(len(data_x),8,3)          #reshape成時間序列資料
model = load_model(model_load[4],custom_objects=None,
    compile=False) 
#print(data_x)#讀取model
predict = model.predict(data_x) #預測，結果為array
predict = pd.DataFrame(predict)                    #array轉為dataframe
predict = pd.concat([deviceId,predict],axis=1)     #與感測器編號合併
print(predict)
df4 = pd.concat([df4,predict])                       #與其他區資料合併
    
df4 = df4.reset_index(drop=True)





df5 = pd.DataFrame()    
data = predict_data[predict_data['location']==5]   #取出選擇地區的資料
data = data.drop(columns=['location'])
deviceId = data['deviceId'].reset_index(drop=True) #保存感測器編號並順序編號
data_x = data.iloc[:,1:].values        #將資料轉換為array
print(data_x)
#StandardScaler = joblib.load(scaler_load[i])       #讀取標準化權重並標準化array
#data_x = StandardScaler.transform(data_x)
data_x = data_x.reshape(len(data_x),8,3)          #reshape成時間序列資料
model = load_model(model_load[5],custom_objects=None,
    compile=False) 
#print(data_x)#讀取model
predict = model.predict(data_x) #預測，結果為array
predict = pd.DataFrame(predict)                    #array轉為dataframe
predict = pd.concat([deviceId,predict],axis=1)     #與感測器編號合併
print(predict)
df5 = pd.concat([df5,predict])                       #與其他區資料合併
    
df5 = df5.reset_index(drop=True)




df = df1.append([df0,df2, df3,df4,df5])
#df

df.to_csv("/Users/user/Desktop/Coding/TJ專題/Project/predict/TJ_predict_8hr_Allsection.csv",index=False)

