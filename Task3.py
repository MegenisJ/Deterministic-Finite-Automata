import Task2,dfa,sys

m_file=sys.argv[1]
m= dfa.decoder(m_file)
m2_file=sys.argv[2]
m2= dfa.decoder(m2_file)
#takes the intersection and just changes the F value from and to OR 
SymmetricDifference =Task2.intersection(m,m2)
F1 = m.getAcceptStates()
F2 = m2.getAcceptStates()
Fstar = list()
for finalstate in F1:
	for state in SymmetricDifference.getStates():
		if finalstate in state and state not in Fstar:
			Fstar.append(state)
for finalstate in F2:
	for state in SymmetricDifference.getStates():
		if finalstate in state and state not in Fstar:
			Fstar.append(state)

##assigns the new values
SymmetricDifference.setAcceptStates(Fstar)
SymmetricDifference.setNumberOfAcceptStates(len(Fstar))
SymmetricDifference.printEncoding()
