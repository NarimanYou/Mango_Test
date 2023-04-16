
import requests
import pandas as pd
from dotenv import load_dotenv
import pymongo
import os


dfmath = pd.read_csv(r'C:\Users\narim\Documents\GitHub\Mango_Test\Student_Performance\student-mat.csv', sep=';')
dfpor = pd.read_csv(r'C:\Users\narim\Documents\GitHub\Mango_Test\Student_Performance\student-por.csv', sep= ';')


dfmath.columns = dfmath.columns.str.upper()
dfpor.columns = dfmath.columns.str.upper()


dfpor.rename(columns={'G1': 'POR_G1', 'G2': 'POR_G2', 'G3': 'POR_G3'}, inplace=True)
print(dfpor.columns)

dfmath.rename(columns={'G1': 'MATH_G1', 'G2': 'MATH_G2', 'G3': 'MATH_G3'}, inplace=True)
print(dfmath.columns)

df = pd.concat([dfpor,dfmath],ignore_index=True)


df = df.drop_duplicates()


load_dotenv()
mongo_url = os.getenv('MONGO_URL')
client = pymongo.MongoClient(mongo_url)

db = client.db
Student_per = db.Student_per

for i in df.index:
    Student_per.insert_one(df.loc[i].to_dict())


