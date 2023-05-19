class Node:
    def __init__(self,h,name):
        self.f=0
        self.g=99999
        self.h=h
        self.name=name
    def setNeghibhor(self,Neighbor={}):
        self.Neighbor=Neighbor
graph=[[-1,1,4,-1,-1],[1,-1,2,5,12],[4,2,-1,2,-1],[-1,5,2,-1,3],[-1,12,-1,3,-1]]

heuristic=[7,6,2,1,0]
s=Node(7,0)
a=Node(6,1)
b=Node(2,2)
c=Node(1,3)
d=Node(0,4)

s.setNeghibhor([a,b])
a.setNeghibhor([s,b,c,d])
b.setNeghibhor([s,a,c])
c.setNeghibhor([a,b,d])
d.setNeghibhor([a,c])

startNode=s
endNode=d

# def astar(start,goal):
#     openSet=set([start])
#     closeSet=set([])
#     comeFrom={}
#     start.g=0
#     start.f=start.h
    
#     while len(openSet)!=0:
#         current=FindVWFVale(openSet)
#         if(current== goal):
#             return contruct_path(comeFrom,current)
#         openSet.remove(current)
#         closeSet.add(current)
        
#         # for neghibour
#         for neghibour in current.Neighbor:
#             if neghibour in closeSet:
#                 continue
#             if neghibour not in openSet:
#                 openSet.add(neghibour)
                
#                 # for tentative score
#             tentative_score=current.g+graph[current][neghibour]
            
#             if tentative_score >= neghibour.g:
#                 continue
#             comeFrom[neghibour]=current
#             neghibour.g=tentative_score
#             neghibour.f=neghibourg+neghibour.h
#     return -1
def astar(start,goal):
    openSet=set([start])
    closeSet=set([])
    comeFrom={}
    start.g=0
    start.f=start.h
    
    while len(openSet)!=0:
        current=FVWFscore(openSet)
        if current==goal:
            return contruct_path(comeFrom,current)
        
        openSet.remove(current)
        closeSet.add(current)
        
        # for neighbours
        for neighbour in current.Neighbor:
            if neighbour  in closeSet:
                continue
            if neighbour not in openSet:
                openSet.add(neighbour)
            
            
            tentative_score=current.g+graph[current.name][neighbour.name]
            
            if tentative_score>=neighbour.g:
                continue
            comeFrom[neighbour]=current
            neighbour.g=tentative_score
            neighbour.f=neighbour.g+neighbour.h
    return  -1
def FVWFscore(openSet):
    fscore=9999
    node =None
    for eachNode in openSet:
        if eachNode.f<fscore:
            fscore=eachNode.f
            node=eachNode
    return node

def contruct_path(comeFrom,current):
    totalpath=[]
    while current in comeFrom.keys():
        current=comeFrom[current]
        totalpath.append(current)
    return totalpath

if __name__=='__main__':
    path=astar(startNode,endNode)
    print("path :",end=" ")
    for node in path[::-1]:
        print(str(node.name)+"-->",end=" ")
    print(endNode.name)
    print("\n Cpst: "+str(endNode.g))
    
        
    
                
                
        
    
    
        
        

