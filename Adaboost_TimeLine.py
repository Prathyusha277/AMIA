import pandas as pd
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from collections import Counter
import sklearn

df = pd.read_csv("C:\Users\prath\Desktop\Capstone\TimeLine_Data_Final_greater_10_missing_0.csv")
df = df.drop('NumberOfTestsTaken', 1)
dfList = np.array_split(df, 10)

df_shuffled = df.iloc[np.random.permutation(len(df))]
df = df_shuffled.reset_index(drop=True)
total_acc = []
total_auc = []
total_prec = []
total_recall = []
for x in range(10):
    trainList = []
    for y in range(10):
        if y == x :
            testdf = dfList[y]
        else:
            trainList.append(dfList[y])
    traindf = pd.concat(trainList)
    print len(testdf)
    print len(traindf)
    x_train = traindf.ix[:, df.columns != 'Infection']
    y_train = traindf['Infection']
    x_test = testdf.ix[:, df.columns != 'Infection']
    x_test = x_test.reset_index(drop=True)

    y_actual = testdf['Infection']

    #clf = tree.DecisionTreeClassifier()
    clf = AdaBoostClassifier(n_estimators=100)
    clf.fit(x_train, y_train)
    y_predict = clf.predict(x_test)
    # y_predict.append(int())
    # for index, row in x_test.iterrows():
    #     if row['no-result'] == 1:
    #         y_predict.append(0)
    #     else:
    #         y_predict.append(int(clf.predict(x_test.iloc[[index]])))
    # print y_predict
    counts = Counter(zip(y_predict, y_actual))
    true_pos = counts[1,1]
    true_neg = counts[0,0]
    false_pos = counts[1,0]
    false_neg = counts[0,1]
    accuracy = (true_pos + true_neg) / float(len(y_actual))
    if true_pos > 0:
        precision = (true_pos)/ float(true_pos+false_pos)
        recall = (true_pos) / float(true_pos + false_neg)
    else:
        precision = 0
        recall = 0
    roc_auc = sklearn.metrics.roc_auc_score(y_actual, y_predict)
    total_acc.append(accuracy)
    total_auc.append(roc_auc)
    total_prec.append(precision)
    total_recall.append(recall)

    print "================================================"

print "Accuracy: " + str(reduce(lambda x, y: x + y, total_acc) / len(total_acc))
print "AUC: " + str(reduce(lambda x, y: x + y, total_auc) / len(total_auc))
print "Precision: " + str(reduce(lambda x, y: x + y, total_prec) / len(total_prec))
print "Recall: "+ str(reduce(lambda x, y: x + y, total_recall) / len(total_recall))