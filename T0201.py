import pandas as pd
import numpy as np
import math
import operator


data = pd.read_csv("iris.csv")

def euclideanDistance(data1, data2, length):
	distance = 0
	for x in range(length):
		distance += np.square(data1[x] - data2[x])
	return np.sqrt(distance)

def nn(trainingSet, testInstance):
 
	distances = {}
	sort = {}
 
	length = testInstance.shape[1]
	
	
	for x in range(len(trainingSet)):
		
		dist = euclideanDistance(testInstance, trainingSet.iloc[x], length)

		distances[x] = dist[0]
 
	sorted_d = sorted(distances.items(), key=operator.itemgetter(1))
 
	neighbor = sorted_d[0][0]
	response = trainingSet.iloc[neighbor][-1]
	
	return (response, neighbor)

def dmc(trainingSet, testInstance):
	classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
	centroids = [[0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0]]
	length = testInstance.shape[1]
	cont = 0
	for x in range(len(classes)):
		for y in range(len(trainingSet)):
			current = [trainingSet.iloc[y]['SepalLength'],trainingSet.iloc[y]['SepalWidth'],trainingSet.iloc[y]['PetalLength'],trainingSet.iloc[y]['PetalWidth']]
			irisClass = trainingSet.iloc[y][-1] 
			if irisClass == classes[x]:
				cont += 1
				centroids[x] = [centroids[x][0]+current[0], centroids[x][1]+current[1], centroids[x][2]+current[2], centroids[x][3]+current[3]]

		for i in range(len(centroids[x])):
			centroids[x][i]= centroids[x][i]/cont

		centroids[x].append(classes[x])
		cont = 0

	testCentroid = pd.DataFrame(centroids)
	distances = {}
	sort = {}
	print("Centroides: ")
	print(testCentroid)


	length = testInstance.shape[1]
	for x in range(len(testCentroid)):
		
		dist = euclideanDistance(testInstance, testCentroid.iloc[x], length)

		distances[x] = dist[0]
 
	sorted_d = sorted(distances.items(), key=operator.itemgetter(1))
	
	neighbor = sorted_d[0][0]
	response = testCentroid.iloc[neighbor][4]
	
	return (response, neighbor)
	


def knn(trainingSet, testInstance, k):
 
	distances = {}
	sort = {}
 
	length = testInstance.shape[1]
	
	
	for x in range(len(trainingSet)):
		
		dist = euclideanDistance(testInstance, trainingSet.iloc[x], length)

		distances[x] = dist[0]
 
	sorted_d = sorted(distances.items(), key=operator.itemgetter(1))
 
	neighbors = []
	
	for x in range(k):
		neighbors.append(sorted_d[x][0])
	classVotes = {}
	
	for x in range(len(neighbors)):
		response = trainingSet.iloc[neighbors[x]][-1]
 
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1

	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return(sortedVotes[0][0], neighbors)


testSet = [[7.2, 3.6, 5.1, 2.5]]
test = pd.DataFrame(testSet)

k = 3
result1,neighbor1 = nn(data, test)
result2,neighbor2 = knn(data, test, k)
result3,neighbor3 = dmc(data, test)

print("\nResultados: ")
print("NN  - Resultado: {} - Vizinho: {}".format(result1, neighbor1))
print("KNN - Resultado: {} - Vizinho: {}".format(result2, neighbor2))
print("DMC - Resultado: {} - Vizinho(Centroide): {}".format(result3, neighbor3))
