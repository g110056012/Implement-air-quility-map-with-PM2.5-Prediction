import requests
import urllib.request
import pandas as pd
import json
import datetime
time = datetime.datetime.now()
column_name_pm25_hour = 'pm2.5:'+str(datetime.datetime.now().hour)
column_name_humi_hour = 'humi:'+str(datetime.datetime.now().hour)
column_name_temp_hour = 'temp:'+str(datetime.datetime.now().hour)

    
#==========濕度===========#

url=['https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams?$expand=Thing,Observations($orderby=phenomenonTime%20desc;$top=1)&$filter=name%20eq%20%27Relative%20humidity%27&$count=true']
humi_data = pd.DataFrame(columns = ['deviceId',column_name_humi_hour])
row = 0
for i in range(200):
    res = requests.get(url[i])
    res_data = json.loads(res.text)
    try:
        url.append(res_data['@iot.nextLink'])
    except:
        pass
    for j in range(len(res_data['value'])):
        humi_data.loc[row,'deviceId'] = res_data['value'][j]['Thing']['properties']['stationID']
        try:
            if res_data['value'][j]['Observations'][0]['result']==0:
                pass
            else:
                humi_data.loc[row,column_name_humi_hour] = res_data['value'][j]['Observations'][0]['result']
        except:
            pass
        row = row + 1
    if url[i]==url[-1]:
        break 

    
    
    
#==========溫度===========#
        
url=['https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams?$expand=Thing,Observations($orderby=phenomenonTime%20desc;$top=1)&$filter=name%20eq%20%27Temperature%27&$count=true']
temp_data = pd.DataFrame(columns = ['deviceId',column_name_temp_hour])
row = 0
for i in range(200):
    res = requests.get(url[i])     #request 忽略對SSL驗證)
    res_data = json.loads(res.text)
    try:
        url.append(res_data['@iot.nextLink'])
    except:
        pass
    for j in range(len(res_data['value'])):
        temp_data.loc[row,'deviceId'] = res_data['value'][j]['Thing']['properties']['stationID']
        try:
            if res_data['value'][j]['Observations'][0]['result']==0:
                pass
            else:
                temp_data.loc[row,column_name_temp_hour] = res_data['value'][j]['Observations'][0]['result']
        except:
            pass
        row = row + 1 
    if url[i]==url[-1]:
        break
        
        
        
#==========PM2.5===========#
        
url=['https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams?$expand=Thing,Observations($orderby=phenomenonTime%20desc;$top=1)&$filter=name%20eq%20%27PM2.5%27&$count=true']
PM25_data = pd.DataFrame(columns = ['deviceId',column_name_pm25_hour])
row = 0
for i in range(200):
    res = requests.get(url[i])
    res_data = json.loads(res.text)
    try:
        url.append(res_data['@iot.nextLink'])
    except:
        pass
    for j in range(len(res_data['value'])):
        PM25_data.loc[row,'deviceId'] = res_data['value'][j]['Thing']['properties']['stationID']
        try:
            if res_data['value'][j]['Observations'][0]['result']==0:
                pass
            else:
                PM25_data.loc[row,column_name_pm25_hour] = res_data['value'][j]['Observations'][0]['result']
        except:
            pass
        row = row + 1 
    if url[i]==url[-1]:
        break
        
        
         
#==========?蔥===========#

#topredict_data = PM25_data    #file < 8小時
topredict_data = pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/predict/topredict_data.csv')
try:
    topredict_data = topredict_data.drop([column_name_pm25_hour,column_name_humi_hour,column_name_temp_hour],axis=1)
except:
    pass

while True:
    col_num = topredict_data.shape
    if col_num[1]<=74:
        break
    else:
        topredict_data = topredict_data.drop(topredict_data.iloc[:,2:5],axis=1)

topredict_data['deviceId'] = topredict_data['deviceId'].astype(str)
PM25_data[column_name_pm25_hour] = PM25_data[column_name_pm25_hour].astype('float16')
humi_data[column_name_humi_hour] = humi_data[column_name_humi_hour].astype('float16')
temp_data[column_name_temp_hour] = temp_data[column_name_temp_hour].astype('float16')


topredict_data = pd.merge(topredict_data,PM25_data,how='left')
topredict_data = pd.merge(topredict_data,humi_data,how='left')
topredict_data = pd.merge(topredict_data,temp_data,how='left')

topredict_data = topredict_data.drop_duplicates('deviceId')

topredict_data = topredict_data.drop(topredict_data.columns[[1]], axis=1)
topredict_data = topredict_data.drop(topredict_data.columns[[1]], axis=1)
topredict_data = topredict_data.drop(topredict_data.columns[[1]], axis=1)



topredict_data.to_csv('/Users/user/Desktop/Coding/TJ專題/Project/predict/topredict_data.csv',index=False)
#predict_data = predict_data.drop('location',axis=1)
topredict_data.to_json('/Users/user/Desktop/Coding/TJ專題/Project/predict/data_recent24.json', orient='records')


