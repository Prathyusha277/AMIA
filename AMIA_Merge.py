import pandas as pd
import numpy as np

a = pd.read_csv("C:\Users\prath\Desktop\Capstone\AMIA_Annie.csv")
b = pd.read_csv("C:\Users\prath\Desktop\Capstone\AMIA_emergency.csv")
merged = pd.merge(a, b, on='PID')
merged = merged.fillna(0)
merged.to_csv("C:\Users\prath\Desktop\Capstone\AMIA_Annie_emergency.csv", index=False)
