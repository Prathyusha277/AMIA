import pandas as pd
import numpy as np
a = pd.read_csv("C:\Users\prath\Desktop\Capstone\TimeLine_Data_Annie.csv") #File created from "Timeline_Data.py"

df_infec = a.loc[a.Infection == 1]
df_no_infec = a.loc[a.Infection == 0]
df_infec = df_infec.fillna(df_infec.mean())
df_no_infec = df_no_infec.fillna(df_infec.mean())

df = pd.concat([df_infec,df_no_infec])
df = df.iloc[np.random.permutation(len(df))]

df.to_csv("C:\Users\prath\Desktop\Capstone\TimeLine_Data_Final_MissingFilled.csv")