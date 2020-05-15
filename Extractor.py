import pandas as pd
import csv
import re
import os

path = 'F:\SEM 2\Cloud\ASSIGNMENT\A3\Text files'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))
            
Title=[]
Author=[]
start_time=[]
end_time=[]
time_taken=[]


for i in files:
    
    f = open(i, "r" , encoding='utf-8')
    start_time.append(time.time())                  ## Starting time of the file
    
    line=f.readlines()


    ## Extractor Engine 

    for l in line:
        if ', by' in l:
            Data = l.split(', by')
            Title.append(Data[0])
            Data[1] = re.sub('\W+','', ''.join(filter(lambda x: x.isalpha(), Data[1])).strip('by'))
            Author.append(Data[1])
            
    end_time.append(time.time())                    ## Ending time of the file
    time_taken.append(end_time-start_time)          ## Time taken to process a file
    time.sleep(5)                                   ## Static Delay of 5 minutes

print(Title)
print(Author)


df = pd.DataFrame({'Title':Title,'Author':Author})
df.to_csv('Data.csv',index=False)

df1 = pd.DataFrame({'Start Time':start_time,'End Time':end_time,'Time Taken':time_taken})
df1.to_csv('Time_Taken.csv',index=False)
