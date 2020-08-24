import sys
import dfa
#taking in the two DFAs 
#creating instances of DFA objects to use in the program 

def intersection(m,m2):
#Set of Q* states
	Q1 = m.getStates()
	Q2 = m2.getStates()
	Qstar = list()
	for i in Q1:
		for x in Q2:
			Qstar.append(str(i+","+x))
	#q0 = (q0 + q0')
	Qzero = str(m.getStart() + ","+m2.getStart())

	#set of final states
	Fstar = list()
	for i in m.getAcceptStates():
		for x in m2.getAcceptStates():
			Fstar.append(str(i + "," + x))
	#generate transitions
	#generates 2 lists to create the transition function from
	list1 = list() 
	list2 = list()
	t1 = m.getTransitions()
	t2 = m2.getTransitions()
	for x in t1:
		list2.append(t2)
		for y in t2:
			list1.append(x)
	list2 = sum(list2,[])
	#generates the new transition function from the old values
	t3 = list()
	for i in range(len(list1)):
		a = list1[i].split(" ")
		b = list2[i].split(" ")
		t3.append(str(a[0] +"," +b[0] + " " + a[1] + "," + b[1]))
	intersection = dfa.DFA(len(Qstar),Qstar,m.getAlphabetSize(),m.getAlphabet(),t3,Qzero,len(Fstar),Fstar)
	return intersection
#allowing me to use the intersection function in Task 3 without executing the following code
if __name__ == "__main__":	
	m_file=sys.argv[1]
	m= dfa.decoder(m_file)
	m2_file=sys.argv[2]
	m2= dfa.decoder(m2_file)
	intersection(m,m2).printEncoding()

