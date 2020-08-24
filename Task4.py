import sys,dfa
from collections import defaultdict
m_file=sys.argv[1]
#creates an instance of a DFA object (dfa.py)
m= dfa.decoder(m_file)
#print(m.getTransitions())

#depth first search to check for emptyness
def dfs(m,start_vertex,end_vertex):
	graph = {}
	
	for i in range(len(m.getStates())):
		x = m.getTransitions()[i].split(" ")
		graph[m.getStates()[i]]=x
	
	visited = set()
	traversal = []
	#WorkingString = []
	stack = [start_vertex]
	
	if start_vertex in end_vertex:
		traversal.append("e")
		return traversal
	
	while stack:
		vertex = stack.pop()
		
		if vertex not in visited:
			visited.add(vertex)
			traversal.append(vertex)
			stack.extend(reversed(graph[vertex]))
	
	return m.getAcceptStates() in traversal

if __name__ == "__main__":	
	if  not dfs(m,m.getStart(),m.getAcceptStates()):
		print("laguage empty") 
	else:
		print("language non-empty -" + " accepted")