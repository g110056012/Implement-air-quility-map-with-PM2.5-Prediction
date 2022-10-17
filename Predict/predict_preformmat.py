import pandas as pd
import os
#Folder_Path = r'D:/download/test'          #處理資料的路徑 不包含csv名稱


#os.chdir(Folder_Path)
#file_list = os.listdir()
data=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/predict/topredict_data.csv')

south=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/sensor/south.csv')#六區感測器資料 在sensor文件夾裡
south1=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/sensor/kao.csv')#六區感測器資料 在sensor文件夾裡
central=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/sensor/central.csv')#六區感測器資料 在sensor文件夾裡
north1=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/sensor/tao.csv')#六區感測器資料 在sensor文件夾裡
north=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/sensor/north.csv')#六區感測器資料 在sensor文件夾裡
yi=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/sensor/yi.csv')#六區感測器資料 在sensor文件夾裡
data_frames = south.append([south1,central, north1,north,yi])
#data_frames

data=pd.read_csv('/Users/user/Desktop/Coding/TJ專題/Project/predict/topredict_data.csv')
#data

data=data.dropna(thresh=12)
#data

data=data.reset_index(drop=True)
#data



#分區感測器合併

Left_Join = pd.merge(data, data_frames,how='left',on="deviceId")

#Left_Join

a = Left_Join.drop(columns=['lat','lon'])
a=a.dropna(thresh=12)
#a

for i in range(25):
    mean=a.iloc[:,i].mean()
    mean=round(mean,0)
    a.iloc[:,i]=a.iloc[:,i].fillna(mean)
    
    
a.isna()


a.to_csv("/Users/user/Desktop/Coding/TJ專題/Project/predict/finalpredict.csv",index=False)


