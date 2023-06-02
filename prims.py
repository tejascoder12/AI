INF=99999
N=5
G=[[0,19,5,0,0],[19,0,5,9,2],[5,5,0,1,6],[0,9,1,0,1],[0,2,6,1,0]]
selected_node=[0,0,0,0,0]
no_edge=0
selected_node[0]=True

print("Edge  :  Wegiht\n")
while(no_edge<N-1):
    mini=INF
    a=0
    b=0
 #The outer loop iterates over m, representing the selected vertices.
# The inner loop iterates over n, representing the unselected vertices.
# If vertex m is selected (selected_node[m] is True) and vertex n is unselected (not selected_node[n] is True), and there is an edge between m and n (G[m][n] is not 0), it checks if the weight of the edge G[m][n] is smaller than the current minimum weight mini. If so, it updates mini with the new minimum weight and stores the indices a and b of the vertices that form this edge.
    for m in range(N):
        if(selected_node[m]):
            for n in range(N):
                if((not selected_node[n]) and G[m][n]):
                    if(mini>G[m][n]):
                        mini=G[m][n]
                        a=m
                        b=n
    print(str(a)+" - "+str(b) + " : "+str(G[a][b]))
    selected_node[b]=True
    no_edge+=1
            
