class DFA():
	#initialisation
	def __init__(self, numberOfStates,states,alphabetSize,alphabet,transitions,start,numberOfAcceptStates,acceptStates):
		self.numberOfStates = numberOfStates
		self.states = states
		self.alphabetSize = alphabetSize
		self.alphabet = alphabet
		self.transitions = transitions
		self.start = start
		self.numberOfAcceptStates = numberOfAcceptStates
		self.acceptStates = acceptStates
	#getters
	def getNumberOfStates(self):
		return self.numberOfStates
	def getStates(self):
		return self.states
	def getAlphabetSize(self):
		return self.alphabetSize
	def getAlphabet(self):
		return self.alphabet
	def getTransitions(self):
		return self.transitions
	def getStart(self):
		return self.start
	def getNumberOfAcceptStates(self):
		return self.numberOfStates
	def getAcceptStates(self):
		return self.acceptStates
	#setters 
	def setNumberOfStates(self,n):
		self.numberOfStates = n
	def setStates(self,n):
		self.States = n
	def setAlphabetSize(self,n):
		self.alphabetSize = n
	def setAlphabet(self,n):
		self.alphabet = n
	def setTransitions(self,n):
		self.transitions = n	
	def setStart(self,n):
		self.start = n
	def setNumberOfAcceptStates(self,n):
		self.numberOfAcceptStates = n
	def setAcceptStates(self,n):
		self.acceptStates = n
	#prints the dfa in the encoded format	
	def printEncoding(self):
		print(self.numberOfStates)
		print(" ".join(self.states ))
		print(self.alphabetSize)
		print(" ".join(self.alphabet))
		print("\n".join(self.transitions))
		print(self.start)
		print(self.numberOfAcceptStates)
		print(" ".join(self.acceptStates))
#returns a DFA object when passed a text file with the correct encoding
def decoder(filename):
		f = open(filename,"r")
		fl = f.readlines()
		numberOfStates = int(fl[0])
		states = fl[1].split()
		alphabetSize = int(fl[2])
		alphabet = fl[3].split()
		transitions = [None] * (numberOfStates)
		
		for i in range(1,int(numberOfStates)+1):
			transitions[i-1] = fl[i+3].rstrip()
		
		start = fl[4 + int(fl[0])].rstrip()
		numberOfAcceptStates = fl[5 + int(fl[0])].rstrip()
		acceptStates = fl[6 + int(fl[0]) ].rstrip().split()
		newDFA = DFA(numberOfStates,states,alphabetSize,alphabet,transitions,start,numberOfAcceptStates,acceptStates)
		return newDFA