import sys 
from collections import deque 
import pprint



if len(sys.argv)>4: #if the length of sys.argv is bigger than 4 the user chose the second method 
    chose1 = False 
    input_filename = sys.argv[4]
    rm_num = int(sys.argv[3])
    radius = int(sys.argv[2])
else:# the user chose the first method 
    chose1 = True
    input_filename = sys.argv[3]
    rm_num = int(sys.argv[2])
    
def getList(g):
    list = [] 
    for key in g.keys(): 
        list.append(key) 
          
    return list

def create_graph(filename):#read graph from command line file 
    g = {}
    with open(filename) as graph_input:
        for line in graph_input:
            nodes = [int(x) for x in line.split()]
            if len(nodes) != 2:
                continue
            if nodes[0] not in g:
                g[nodes[0]] = []
            if nodes[1] not in g:
                g[nodes[1]] = []
            g[nodes[0]].append(nodes[1])
            g[nodes[1]].append(nodes[0])
    return g

def method1(g, rm_num):
    for times in range(0, rm_num):
        maxneighb = 0
        indexmax = 0
        keys =[] 
        keys = getList(g)
        keys.sort()
        for i in keys:#find the node with the longet adjacency list 

            if len(g[(i)])>maxneighb:
                maxneighb = len(g[(i)])
                indexmax = i
        print(indexmax, maxneighb)
        del g[indexmax]
        for i in g.keys():#remove the node from the adjacency lists of the other nodes 
            for j in g[(i)]:
                if j==indexmax:
                    g[(i)].remove(j)



def bfs(g, node, radius):

    q = deque()
    q.clear()
    visited = []
    for i in range(0, nodes):
        visited.append(False)
    inqueue =[]
    for i in range(0, nodes):
        inqueue.append(False)
    q.appendleft(node)
    inqueue[node] = True
    counter = 0
    limit = 1
    while not (len(q) == 0) and counter <= radius:
        limit = limit - 1
        if limit==0:
            myqueue=[]
            counter = counter + 1
            limit =  len(q)
            for i in q:
                myqueue.append(i)
            #print(limit, "11111111111111111111111111111111111111", myqueue)
        #print("Queue", q)
        c = q.pop()

        #print("Visiting", c)
        
        inqueue[c] = False
        visited[c] = True
        for v in g[c]:
            if not visited[v] and not inqueue[v]:
                q.appendleft(v)
                inqueue[v] = True
    return myqueue


def calculateCI(g, radius):
    ki=[]
    for i in range(0, nodes):
        ki.append(0)
        
    ci = []
    for i in range(0, nodes):
        ci.append(0)
    keys = getList(g)   
    for i in keys:
        ki[i] = (len(g[(i)]) - 1)
        q = []
        q = bfs(g, i, radius)

        kj=[]
        for k in range(0, nodes):
            kj.append(0)
        sumi = 0
        for j in q:
            sumi = sumi + (len(g[(j)]) - 1)
        kj[i] = sumi
        ci[i] = (ki[i]*kj[i])
    return ci
        
   
def method2(g, radius):
    maxCI = 0
    count = -1
    indexmax=0
    ci = calculateCI(g, radius)
    for i in ci:
        count = count + 1
        if i>maxCI:
            maxCI = i 
            indexmax = count
    del g[indexmax]
    for i in g.keys():#remove the node from the adjacency lists of the other nodes 
            for j in g[(i)]:
                if j==indexmax:
                    g[(i)].remove(j)
    print(indexmax, maxCI )
    return g
          
g = create_graph(input_filename)
nodes = len(g.keys())+1
if chose1:   
    method1(g, rm_num)
else:
    for i in range(0, rm_num):
        method2(g,radius )

                
    