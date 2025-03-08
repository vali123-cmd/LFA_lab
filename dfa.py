# A DFA that accepts strings with even number of 0's and odd number of 1's -- Danciu Valentin - Nicolae 131

# Q = {q0,q1,q2,q3}
# q0 initial state
# Sigma = {0,1}
# Delta = {(q0,0) ->q2, (q0,1) ->q1, (q1,0) ->q3, (q1,1) ->q0, (q2,0) ->q0, (q2,1) ->q3, (q3,0) ->q1, (q3,1) ->q2}
# F = {q1}



class DFA:
    def __init__(self, states, alphabet, delta, start, accept):
        self.states = states
        self.alphabet = alphabet
        self.delta = delta
        self.start = start
        self.accept = accept

    def transition(self, state, symbol):
        return self.delta[(state, symbol)]

    def accepts(self, string):
        state = self.start
        for symbol in string:
            state = self.transition(state, symbol)
        return state in self.accept
    
    
    
states = {'q0', 'q1', 'q2', 'q3'}
alphabet = {'0', '1'}
delta = {('q0', '0'): 'q2', ('q0', '1'): 'q1', ('q1', '0'): 'q3', ('q1', '1'): 'q0', ('q2', '0'): 'q0', ('q2', '1'): 'q3', ('q3', '0'): 'q1', ('q3', '1'): 'q2'}
start = 'q0'
accept = {'q1'}



dfa = DFA(states, alphabet, delta, start, accept)
to_validate = input("Enter a string to validate: ")
print(dfa.accepts(to_validate))