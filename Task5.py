import sys,dfa,Task1,Task2,Task4

m_file=sys.argv[1]
m= dfa.decoder(m_file)
m2_file = sys.argv[2]
m2 = dfa.decoder(m_file)

##STEP 1 
##complement of B 
m_complement = Task1.Complementation(m)
m2_complement = Task1.Complementation(m2)

#STEP 2 
#An automation that is the intersection of the complement A and B 
m_intersection = Task2.intersection(m_complement,m2_complement)


#STEP 3 
## check intersection for emptyness 
first = Task4.dfs(m_intersection,m_intersection.getStart(),m_intersection.getAcceptStates())



##step 4.
##DO IT BACKWARDS
m2_intersection = Task2.intersection(m2_complement,m_complement)
#m2_intersection.printEncoding()
second =Task4.dfs(m_intersection,m2_intersection.getStart(),m2_intersection.getAcceptStates())
if first == False and second == False:
	print("equivalent")
else:
	print("not equivalent")
