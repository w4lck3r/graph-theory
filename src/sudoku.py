from algorithms import Graph
from algorithms import Node

import sys

def main() : 
    inputf = open(sys.argv[2],"r")
    num_lines = sum(1 for line in inputf)
        
    g = Graph()
    for i in range(num_lines) :
        g.addNode(i)
    
    for line in inputf:
        print(line.rstrip('\n'))
        
    lines=inputf.readlines
    print ("this is lines",lines)
    g.addEdge(lines[0],lines[1],lines[2])
    
    
    results = color()
    
    with open(sys.argv[4],"w") as outputf:
        for row in results():
            print (row)
            outputf.writelines("%s\n" % str(row))
        
    inputf.close()
    outputf.close()
    
main()