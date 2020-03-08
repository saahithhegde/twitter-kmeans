import json
import re
import random

import copy
import json
import re
import math



def remove_unwanted(param):
    param = re.sub("http://.*","", param)
    param = re.sub("https://.*", "", param)
    param=re.sub("@[a-zA-z0-9]*(:)*","",param)
    param = re.sub("RT", "", param)
    param=re.sub("#","",param)
    param=param.replace("\n","")
    param=param.lower()
    return param


tweets =[]
k=int(input("enter the number of clusters requiered"))
print("running......")
with open("cbchealth.txt", 'r') as f:
    for line in f:
       lines=line.split("|")
       line_updated=remove_unwanted(lines[2])
       tweets.append(line_updated)
centers=random.sample(tweets,k)


def jaccards_distance(param, param1):
    alist = param.split(" ")
    blist = param1.split(" ")
    intersections = list(set(alist) & set(blist))
    union = list(set(alist) | set(blist))
    return (1 - (len(intersections) / len(union)))


def updatecentroids(tweets, cluster,k):
    indices = []
    new_center_index = []
    new_centroid = []
    for i in range(k):

        indices.append([j for j, u in enumerate(cluster) if u == i])
        clusterpoints = indices[i]
        # m gives the indices if the elements of every cluster k

        if (len(clusterpoints) != 0):
            texts = [tweets[p] for p in clusterpoints]
            distance_matrix = [[jaccards_distance(texts[i], texts[j]) for j in range(len(clusterpoints))] for i in range(len(clusterpoints))]
            sum_matrix = [sum(i) for i in distance_matrix]
        # lower triangular matrix
        new_center_index.append(
            clusterpoints[(sum_matrix.index(min([sum(i) for i in distance_matrix])))])  # index of the point closer to all the other points
    return(new_center_index)


def printoutput(tweets, cluster, k,centers):
    final = []
    for i in range(k):
        final.append([j for j, u in enumerate(cluster) if u == i])
        p=[x for x in final[i]]

        #print("The items that belong to  cluster " + str(i + 1)+" are:" )
        #for j in p:
           # print((tweets[j]))
        print("cluster "+str(i+1)+" is: "+str(len(p))+" tweets")
def sumofsquarederrors(cluster, centers, tweets, k):
    indices=[]
    total=0
    for i in range(k):
        indices.append([j for j, u in enumerate(cluster) if u == i])
        gettweets=[]
        for x in indices[i]:
            gettweets.append(tweets[x])
        for j in range(len(indices[i])):
            total+=math.pow(jaccards_distance(gettweets[j],centers[i]),2)
    print("-----------------------------SSE----------------------------------------")
    print ("the sse is="+str(total))


def kmeansclustering(tweets, centers, k):
    cluster=[]
    for i in range(len(tweets)):
        distance = [jaccards_distance(tweets[i], centers[j]) for j in range(k)]
        ans = distance.index(min(distance))
        cluster.append(ans)

    newcenters=[]
    new_center_index=updatecentroids(tweets,cluster,k)

    for i in new_center_index:
        newcenters.append(tweets[i])

    count = 0
    for i in range(k):
        if (newcenters[i] == centers[i]):
            count = count + 1
        if (sum == k):
            break;
    centers = copy.deepcopy(newcenters)

    printoutput(tweets,cluster,k,centers)
    sumofsquarederrors(cluster,centers,tweets,k)





kmeansclustering(tweets,centers,k)











