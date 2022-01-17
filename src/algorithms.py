class Node : 
    
    def __init__(self, idx, data = 0,is_colored=False) : # Constructor   
        self.id = idx
        self.data = data
        self.connectedTo = dict()
        self.is_colored = is_colored

    def addNeighbour(self, neighbour , weight = 0) :
        if neighbour.id not in self.connectedTo.keys() :  
            self.connectedTo[neighbour.id] = weight

    # setter
    def setData(self, data) : 
        self.data = data 

    #getter
    def getConnections(self) : 
        return self.connectedTo.keys()

    def getID(self) : 
        return self.id
    
    def getData(self) : 
        return self.data

    def getWeight(self, neighbour) : 
        return self.connectedTo[neighbour.id]

    def __str__(self) : 
        return str(self.data) + " Connected to : "+ \
         str([x.data for x in self.connectedTo])
    
    
    
class Graph : 
    totalV = 0 # total vertices in the graph
    
    def __init__(self) : 
        self.allNodes = dict()

    def addNode(self, idx) : 
        if idx in self.allNodes : 
            return None
        
        Graph.totalV += 1
        node = Node(idx=idx)
        self.allNodes[idx] = node
        return node

    def addNodeData(self, idx, data) : 
        if idx in self.allNodes : 
            node = self.allNodes[idx]
            node.setData(data)
        else : 
            print("No ID to add the data.")

    def addEdge(self, src, dst, wt = 0) : 
        self.allNodes[src].addNeighbour(self.allNodes[dst], wt)
        self.allNodes[dst].addNeighbour(self.allNodes[src], wt)
    
    def isNeighbour(self, u, v) : 
        if u >=1 and u <= 81 and v >=1 and v<= 81 and u !=v : 
            if v in self.allNodes[u].getConnections() : 
                return True
        return False


    def printEdges(self) : 
        """ print all edges """
        for idx in self.allNodes :
            node =  self.allNodes[idx]
            for con in node.getConnections() : 
                print(node.getID(), " --> ", 
                self.allNodes[con].getID())
    
    # getter
    def getNode(self, idx) : 
        if idx in self.allNodes : 
            return self.allNodes[idx]
        return None

    def getAllNodesIds(self) : 
        return self.allNodes.keys()       
    
    def getNeighbours(sommet):
        neighbours=[]
        for i in range(allNodes):
            if isNeighbour(G,sommet,i):
                neighbours.append(i)
        return neighbours
        
        
    def new_color(couleurs):
            new_c = couleurs.lenght()
            
            
    def colorer():
        results = {}
        couleurs=[] #on represente les couleurs par les numeros dans un tableu
        for s in sommets_graphe(G): 
            c_voisins = voisins(G,s)
            for c in couleurs :
                for v in voisin(G):
                    if (color == v.couleur) not in c_voisins:
                        results += {s  : [c_voisins ,  color] }  #ajoute(color , c_voisins)
                if (couleurs.lenght == c_voisins.lenght):
                    new_c = new_color(couleurs)
                    s.setData(new_c) #colorer(s,new_c)  colorer c'est donner une valeur data au noeud
                    results += {s  : [couleurs ,  new_color] }  #ajouter(couleurs,new_color)
                else:
                    for color in couleurs:
                        if color not in c_voisins:
                            s.setData(color)
                            
        return results