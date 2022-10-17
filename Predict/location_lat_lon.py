import pandas as pd
import os
#Folder_Path = r'D:/download/test'          #處理資料的路徑 不包含csv名稱


#os.chdir(Folder_Path)
#file_list = os.listdir()
data=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/predict/TJ_predict_8hr_Allsection.csv')

south=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/sensor/south.csv')#六區感測器資料 在sensor文件夾裡
south1=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/sensor/kao.csv')#六區感測器資料 在sensor文件夾裡
central=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/sensor/central.csv')#六區感測器資料 在sensor文件夾裡
north1=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/sensor/tao.csv')#六區感測器資料 在sensor文件夾裡
north=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/sensor/north.csv')#六區感測器資料 在sensor文件夾裡
yi=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/sensor/yi.csv')#六區感測器資料 在sensor文件夾裡
data_frames = [south, south1, central,north1,north,yi]
for i in range(0,6,1):
    data_frames[i]=data_frames[i].astype('str')
data=data.dropna()#print(file_list)
data['deviceId']=data['deviceId'].astype('str')



result=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/predict/TJ_predict_8hr_Allsection.csv')
result=result.drop(index=result.index)
result

data=data.reset_index(drop=True)
#data


#分區感測器合併


for i in range(0,6,1):
    df=pd.DataFrame(data_frames[i])
    Left_Join = pd.merge(data, df,how='left',on="deviceId")

    #print(Left_Join)
    result=result.append(Left_Join)
    #result[i]=Left_Join.dropna()
#for i in range(0,6,1):
    
    #data1=data1.append(result[i])
    #data1=data1.dropna(axis=1)
    #print(dataall)
    
    
    
a=result.dropna()
a=a.reset_index(drop=True)
#a


a.to_csv("/Users/user/Desktop/Coding/TJ專題/Project/predict/TJ_predict_8hr_Allsection.csv",index=False)  #to frontend data