from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import AdaBoostClassifier
import pandas as pd

file = 'C:\Users\prath\Desktop\Capstone\AMIA_Annie_emergency.csv'

df = pd.read_csv(file, index_col=False)
#df = df.iloc[np.random.permutation(len(df))]
dataset = df.ix[:, df.columns != 'Infection']

clf = AdaBoostClassifier(n_estimators=100)

scores_accuracy = cross_val_score(clf, dataset, df.Infection.values, cv=10, scoring='accuracy')
print("Accuracy: %0.2f (+/- %0.2f) " % (scores_accuracy.mean(), scores_accuracy.std()))

scores_precision = cross_val_score(clf, dataset, df.Infection.values, cv=10, scoring='precision')
print("Precision: %0.2f (+/- %0.2f) " % (scores_precision.mean(), scores_precision.std()))

scores_recall = cross_val_score(clf, dataset, df.Infection.values, cv=10, scoring='recall')
print("Recall: %0.2f (+/- %0.2f) " % (scores_recall.mean(), scores_recall.std()))

scores_auc = cross_val_score(clf, dataset, df.Infection.values, cv=10, scoring='roc_auc')
print("AUC: %0.2f (+/- %0.2f) " % (scores_auc.mean(), scores_auc.std()))