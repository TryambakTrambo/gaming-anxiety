#Reading in the data
import pandas as pd
data=pd.read_csv('Gaming Data.csv',encoding='latin-1')



#Extracting Columns of Interest

data_sub=data[['Game','Platform','Hours','earnings','streams','Narcissism','Gender','Age','Work','Degree',
               'Playstyle','Residence_ISO3']]
data_sub.describe()
