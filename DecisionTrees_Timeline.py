import pandas as pd
import numpy as np
from collections import Counter
import sklearn
from sklearn import tree
from os import system
import subprocess


def visualize_tree(tree_names, feature_names):
    """Create tree png using graphviz.

    Args
    ----
    tree -- scikit-learn DecsisionTree.
    feature_names -- list of feature names.
    """
    with open("dt.dot", 'w') as f:
        tree.export_graphviz(tree_names, out_file=f,
                        feature_names=feature_names)
    system("dot -Tpng dt.dot -o dtree2.png")
    # command = ["C:\Anaconda2\Lib\site-packages\graphviz\dot", "-Tpng", "dt.dot", "-o", "C:\Users\prath\Desktop\Capstone\dt.png"]
    # try:
    #     subprocess.check_call(command)
    # except Exception as inst:
    #     print "Can not open"+str(inst)
    #     # exit("Could not run dot, ie graphviz, to "
    #     #      "produce visualization")


df = pd.read_csv("C:\Users\prath\Desktop\Capstone\TimeLine_Data_Final_MissingFilled.csv")
df = df.drop('NumberOfTestsTaken', 1)
df = df.drop('PID', 1)
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
    features = list(x_train.columns)
    print features
    y_actual = testdf['Infection']

    clf = tree.DecisionTreeClassifier()
    clf.fit(x_train, y_train)
    visualize_tree(clf, features)
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