import dfa
import sys

#the new accept states are all the non accept states from m
def Complementation(m):
	newAcceptStates  = list(set(m.getStates()).symmetric_difference(set(m.getAcceptStates())))
	#creates a new DFA object for the new complement DFA 
	m_complement = dfa.DFA(m.getNumberOfStates(),m.getStates(),m.getAlphabetSize()
		,m.getAlphabet(),m.getTransitions(),m.getStart(),len(newAcceptStates),newAcceptStates)
	return(m_complement)


if __name__ == "__main__":	
	#creates a new DFA object from the arguement passed. Will result in errors if endoded DFA is not in correct format
	m_file=sys.argv[1]
	#creates an instance of a DFA object (dfa.py)
	m= dfa.decoder(m_file)
	Complementation(m).printEncoding()
