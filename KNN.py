# Read the data
file='C:\Users\prath\Desktop\Capstone\AMIA_Corr.csv'
import csv
import random
from sklearn import metrics
from sklearn.cross_validation import KFold
import math
import operator

# Split it into test and train

def loadDataset(filename,split, trainingSet=[],testSet=[]):
    with open(filename,'rb') as csvfile:
        next(csvfile)
        lines=csv.reader(csvfile)
        dataset=list(lines)

        #print dataset[0][4]
        print len(dataset)
        kf = KFold(len(dataset), n_folds=10)
        for train, test in kf:
            print("%s %s" % (len(train), len(test)))

        for i in range(0, len(train)):
            trainingSet.append(dataset[train[i]])
        for i in range(0,len(test)):
            testSet.append(dataset[test[i]])
        #for x in range(1,len(dataset)-1):
         #   if(random.random()<split):
          #      trainingSet.append(dataset[x])

           # else:
            #    testSet.append(dataset[x])

# function to calcualte Euclidean distance between two instances
def euclidean_dist(instance1,instance2):
    distance=0
    #test = instance1[1].split(',')
    #train = instance2[1].split(',')

    #distance= len(set(test) & set(train))
    #print distance

    #print instance1[1]

    for x in range(1,len(instance1)-1):
        instance1[x]=float(instance1[x])
        instance2[x]=float(instance2[x])
        distance +=(pow((instance1[x]-instance2[x]),2))
        #print distance
    return pow(distance,2)

# Calculate the K-Nearest Neighbors
def getNeighbors(trainingSet,testInstance,k):
    distances=[]
    #length=len(testInstance)
    for x in range(len(trainingSet)):
        dist=euclidean_dist(testInstance,trainingSet[x])
        #print dist
        distances.append((trainingSet[x],dist))

        #print distances
    #print distances.sort(key=operator.itemgetter(2))
    sortedDistances =sorted(distances, key=lambda x: x[1])
    #print testInstance
    #print sortedDistances
    neighbors=[]
    for x in range(k):
        neighbors.append(sortedDistances[x][0])
        #print distances[x]
    return neighbors


def getResponses(neighbors):
    classVotes={}
    for x in range(len(neighbors)):
        response=neighbors[x][22]
        #print response
        if response in classVotes:
            classVotes[response]+=1

        else:
            classVotes[response]=1
    #sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    if classVotes.has_key('1'):
        if classVotes.has_key('0'):
           if classVotes['0'] > classVotes['1']:
               return '0'
           else:
               return '1'
        else:
            return '1'
    else:
        return '0'
    #print sortedVotes[0]

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][22] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

def main():
    # prepare data
    trainingSet=[]
    testSet=[]
    split = 0.75
    loadDataset(file, split, trainingSet, testSet)
    print 'Train set: ' + repr(len(trainingSet))
    print 'Test set: ' + repr(len(testSet))

    # generate predictions
    predictions = []
    actual = []
    k = 5
    print testSet[1]

    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        #print testSet[x]
        #print neighbors
     #   #print neighbors
        result = getResponses(neighbors)
        print result
        predictions.append(result)
        actual.append(testSet[x][22])
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][22]))

    accuracy = getAccuracy(testSet, predictions)
    #precision = getPrecission(testSet,predictions)
    print('Accuracy: ' + repr(accuracy) + '%')
    #print ('Precision:' + repr(precision) + '%')
    print(metrics.classification_report(actual, predictions))
    print(metrics.confusion_matrix(actual, predictions))

main()