# -*- coding: utf-8 -*-
"""
程式: CsvSendCloud.py 
功能: send csv_data to cloud
modified on 8/19 2020
@author: Barry Wang

"""
import requests
from urllib import request, parse
import json
import datetime
import csv
from datetime import datetime
from datetime import timedelta

# 01_44379A 02_443AE8 03_443796 04_443990 05_442BC4
# 06_443792 07_4428EA 08_442E45 09_443191
name = "20200817_0826.csv"#"01_44379A.csv" #input('(1)請輸入欲上傳之csv檔名：')
N=1-1

# 使用 csv.DictReader 來讀取 CSV 檔案的內容，
# 會自動把第一列（row）當作欄位的名稱，將第二列
# 以後的每一列轉為 dictionary
#test = datetime.strptime("24/7/2020T13", "%d/%m/%YT")
#print(test)

conTime = timedelta(minutes = 0)
disconTime = timedelta(minutes = 0)
conCount = 0
disconCount = 0
print ("connectTime:" + str(conTime))
print ("DisconnectTime:" + str(disconTime))
print ("DisconnectCount:" + str(disconCount))

with open(name, newline='') as csvfile:
    
  # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
  rows = csv.DictReader(csvfile)
  # 以迴圈輸出指定欄位
  previousTime = datetime.now()
  count = 0
  
  for row in rows: 
	  print(row['FirstRecordDatetime'])		  
	  time = datetime.strptime(str(row['FirstRecordDatetime']), "%d/%m/%YT%H:%M:%S")
	  if(count == 0):
		  previousTime = time
	  if(count > 0):
		  if ((time - previousTime) > timedelta(minutes = 10)):
			  print(previousTime)
			  print(time)
			  print(time - previousTime)
			  #print ("DisconnectTime:" + str(disconTime))
			  disconTime = disconTime + (time - previousTime)
			  disconCount = disconCount + 1
		  else:
			  conCount = conCount + 1
			  conTime = conTime + (time - previousTime)
			  #print ("connectTime:" + str(conTime))
		  previousTime = time
	  count = count + 1
	  #print(time) 
    
print ("totalTime:" + str(conTime + disconTime))
print ("connectTime:" + str(conTime))
print ("DisconnectTime:" + str(disconTime))
print ("ConnectCount:" + str(conCount))
print ("DisconnectCount:" + str(disconCount))
print ("Ratio:" + str(conTime /(conTime + disconTime)))
#print('(2)---- Send CSV data to Cloud completely -----') 
#print('        CSV data 總筆數=',N) 







    


  
  

          
