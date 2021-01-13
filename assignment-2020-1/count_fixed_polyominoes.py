import sys 
import pprint

#method that creates graph 
def create_graph(n):
    g={}
    counter =0
    for x in range(2-n, 0):
        counter = counter + 1
        for y in range(1,counter+1):
            k1 = False 
            k2 = False 
            k3 = False 
            k4 = False 
            if (y>0 or (y==0 and x+1>0))and (abs(x+1)+y+1<=n):
                k1= True
                n1=(x+1, y)
            if(y+1>0 or (y+1==0 and x>0))and(abs(x)+y+2<=n):
                k2= True
                n2=(x, y+1)
            if(y>0 or (y==0 and x-1>0))and(abs(x-1)+y+1<=n):
                k3= True
                n3=(x-1, y)
            if(y-1>0 or (y-1==0 and x>0))and(abs(x)+abs(y-1)+1<=n):
                k4= True
                n4=(x,y-1)
            g[(x,y)] =[]
            if k1:
                g[(x,y)].append(n1)
            if k2:
                g[(x,y)].append(n2)
            if k3:
                g[(x,y)].append(n3)
            if k4:
                g[(x,y)].append(n4)
    g[(0,0)] = [(0,1), (1,0)]
    counter = n+1
    for x in range(0, n):
        counter = counter -1
        for y in reversed(range(counter)):
            k1 = False 
            k2 = False 
            k3 = False 
            k4 = False 
            if (y>0 or (y==0 and x+1>=0))and (abs(x+1)+y+1<=n):
                k1= True
                n1=(x+1, y)
            if(y+1>0 or (y+1==0 and x>=0))and(abs(x)+y+2<=n):
                k2 = True
                n2=(x, y+1)
            if(y>0 or (y==0 and x-1>=0))and(abs(x-1)+y+1<=n):
                k3 = True
                n3=(x-1, y)
            if(y-1>0 or (y-1==0 and x>=0))and(abs(x)+abs(y-1)+1<=n):
                k4 = True
                n4=(x, y-1)
            g[(x,y)] =[]
            if k1:
                g[(x,y)].append(n1)
            if k2:
                g[(x,y)].append(n2)
            if k3:
                g[(x,y)].append(n3)
            if k4:
                g[(x,y)].append(n4)
    return g

#method that takes the graph from the previous mwthod and counts the possible
# fixed polyonimoes
def countFixedPlmns(g, untried,n , p ,k ):
    global c
    c = k
    while len(untried)>0:
        u = untried.pop()
        p.append(u)
        if len(p)== n:
            c = c+1
        else:
            new_neighbors = set()
            for v in g[(u)]:
                exists = False
                for i in p:
                    if v in g[(i)]:
                        if i!= u:
                            exists = True 
                if( v not in untried) and( v not in p) and (not exists):
                    
                    new_neighbors.add(v)
            new_untried = untried.union(new_neighbors)
            countFixedPlmns(g, new_untried, n, p, c)
        p.remove(u)
    return c


#main program 
n=5
g = create_graph(n)
plmns = countFixedPlmns(g,{(0,0)},n , [] ,0)
pprint.pprint(g)
pprint.pprint(plmns)  

         
     

                
            
            
            









