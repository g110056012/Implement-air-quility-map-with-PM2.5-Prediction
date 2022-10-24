# Implement-air-quility-map-with-PM2.5-Prediction
Implement air quality maps with open data and build multiple PM2.5 prediction models based on deep learning


一、專案概念
(1) 專案目標 : 建構一個具有參考價值，準確率較高的 PM2.5
    預測模型，且易於查看的空氣品質地圖。
(2) 專案技術 : Python, Keras, HTML/CSS/Javascript, Leaflet,
    PHP, MySQL
(3) 專案內容 : 
    - 透過民生物聯網資料服務平台提供的環保署智慧城鄉空品微型感測器監測資料來做深度學習訓練，探討 LSTM 以及 GRU 模型的差異，以及預測台灣地區未來24小時內的預測結果做比對，找出最佳的預       測方式。
    - 利用網頁爬蟲將環保署智慧城鄉空品微型感測器監測資料之最新一筆的微型感測器 PM2.5 數值抓下，並且將這些資料放入訓練好的模型產生預測結果。
    - 利用 PHP 以及 MySQL 等工具將監測資料與功能合併到Leaflet 地圖套件上，最後打包成 API 串聯前後端呈現視覺化，提供Realtime、Predict、測站資訊等頁面。
      (**本專案當時只負責網站內容的歷史、即時、預測資料前後端功能部分，其餘功能不負責)

二、	流程圖

![image](https://user-images.githubusercontent.com/107039489/196293510-1d4941c0-1def-4aaf-831a-88ee1e18f58e.png)

分為三大部分：
1.	建立模型：本系統使用Keras基於TensorFlow建立預測模型，空氣品質資料來源使用民生公共物聯網資料服務平台，使用LSTM和GRU模型技術架構以及處理PM2.5時間序列資料，預測出未來8小時內的PM2.5數值。
2.	預測：每一小時自動做資料爬蟲，將過去8小時資料當作預測資料集，丟入模型產出預測後8小時資料。
3.	網頁前後端：將預測後8小時資料與地圖疊合，再以Apache作為伺服器輸出成網頁，完成地圖的繪製。

三、	程式執行流程說明 (Trace Code)
1.	建立模型
程式碼 : 位於 file < Create_model> 
-	由於訓練資料龐大以及訓練時間過於長，因此已經將訓練好的model檔及scaler檔匯出，預測時可以直接load model即可。


2.	預測
程式碼 : 位於 file<Predict> 
-	執行topredict_data_formmat.py
  
![image](https://user-images.githubusercontent.com/107039489/196293913-25720eaa-aa31-4eee-a3ea-520037b99ba9.png)
  
: 將每一小時溫濕度、PM2.5資料爬蟲下來。
: 生成預測資料集to_predict.csv。
  
![image](https://user-images.githubusercontent.com/107039489/196294022-b75f53ae-d458-4a94-a148-839d9630fc38.png)
  

- 執行predict_preformmat.py
  
![image](https://user-images.githubusercontent.com/107039489/196294107-7319da32-6666-418c-924f-ee346c7829b1.png)
  
: 將to_predict.csv增加感測器分區欄位 (file <sensor>)。
: 生成最終預測資料集finalpredict.csv。
  
![image](https://user-images.githubusercontent.com/107039489/196294180-4addddb8-97c7-4459-98b3-2269d171f312.png)
  

-	執行Final_predict.py
  
![image](https://user-images.githubusercontent.com/107039489/196294213-ec68d920-7815-42c6-8fa3-b44b2cb45e1b.png)
  
  : load model檔及scaler檔
  : 將finalpredict.csv丟入模型，進行預測。
  : 生成未來8小時預測資料 TJ_predict_8hr_Allsection.csv。

-	執行location_lat_lon.py
  
![image](https://user-images.githubusercontent.com/107039489/196294277-2085e4d7-8454-4e65-b831-1bd9259c93a3.png)
  
  : 將TJ_predict_8hr_Allsection.csv增加經緯度欄位。
  : 輸出覆蓋未來8小時預測資料 TJ_predict_8hr_Allsection.csv。
  : TJ_predict_8hr_Allsection.csv輸出至網頁後端資料夾。
  
![image](https://user-images.githubusercontent.com/107039489/196294308-b7f26357-5669-4a69-8ca0-ab812aa884ea.png)


  
3.	網頁
程式碼 : 位於 file<Web> 
-	在Wordpress架構下架設，所以將整個htdocs包裝，可以直接匯入。
-	前端程式碼:  file<Web> \\htdocs\\wp-content\\themes\\TJ project\\
-	後端程式碼api 
  :  file<Web> \\htdocs\\wp-content\\plugins\\tj\\includes\\api\\
  : getPredictData.php
將TJ_predict_8hr_Allsection.csv轉換成Geojson以及json格式，讓前端可以使用Leaflet好打點於地圖上。
  
![image](https://user-images.githubusercontent.com/107039489/196294376-d370cf28-2bbb-4077-99a4-2b3d25a581c3.png)

-	TJ_predict_8hr_Allsection.csv在網頁後端資料夾
  :  file<Web> \\htdocs\\wp-content\\plugins\\tj\\includes\\data\\

  
  
4.	程式排程
-	終端機執行: cronjob –l
-	設定一小時執一次: 0 * * * * 
  
![image](https://user-images.githubusercontent.com/107039489/196294601-7e6c520e-f419-4827-9ebf-7c075392d6a6.png)

cronjob.sh
  
![image](https://user-images.githubusercontent.com/107039489/196294631-97f693ed-252f-4939-b1b2-543d0225dfe5.png)




