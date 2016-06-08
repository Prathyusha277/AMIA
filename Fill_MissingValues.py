import pandas as pd
import numpy as np
a = pd.read_csv("C:\Users\prath\Desktop\Capstone\TimeLine_Data_Annie.csv")
a = a.fillna(0)
# df_infec = a.loc[a.Infection == 1]
# df_no_infec = a.loc[a.Infection == 0]
# df_infec = df_infec.fillna(df_infec.mean())
# df_no_infec = df_no_infec.fillna(df_infec.mean())
#
# df = pd.concat([df_infec,df_no_infec])
# df = df.iloc[np.random.permutation(len(df))]

a.to_csv("C:\Users\prath\Desktop\Capstone\TimeLine_Data_Annie_MissingFilled_zero.csv")