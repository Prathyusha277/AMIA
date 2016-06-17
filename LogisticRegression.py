#Applying LR on final data
from sklearn.cross_validation import cross_val_score
import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np

file = 'C:\Users\prath\Desktop\Capstone\TimeLine_Data_Final.csv'

df = pd.read_csv(file, index_col=False)
df = df.drop('NumberOfTestsTaken', 1)
df = df.drop('PID', 1)

df = df.iloc[np.random.permutation(len(df))]
dataset = df.ix[:, df.columns != 'Infection']

clf = LogisticRegression()

scores_accuracy = cross_val_score(clf, dataset, df.Infection.values, cv=10, scoring='accuracy')
print("Accuracy: %0.2f (+/- %0.2f) " % (scores_accuracy.mean(), scores_accuracy.std()))

scores_precision = cross_val_score(clf, dataset, df.Infection.values, cv=10, scoring='precision')
print("Precision: %0.2f (+/- %0.2f) " % (scores_precision.mean(), scores_precision.std()))

scores_recall = cross_val_score(clf, dataset, df.Infection.values, cv=10, scoring='recall')
print("Recall: %0.2f (+/- %0.2f) " % (scores_recall.mean(), scores_recall.std()))

scores_auc = cross_val_score(clf, dataset, df.Infection.values, cv=10, scoring='roc_auc')
print("AUC: %0.2f (+/- %0.2f) " % (scores_auc.mean(), scores_auc.std()))