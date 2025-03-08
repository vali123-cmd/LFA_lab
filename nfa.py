# NFA that accepts strings that end in 01 or 10 -- Danciu Valentin - Nicolae 131
# Q = {q0,q1,q2,q3}
# q0 initial state
# Sigma = {0,1}
# Delta = {(q0,0) ->[q0,q1] , (q0,1) ->[q3,q0], (q1,1) ->q2, (q3,0) ->q2}
# F = {q2}


class NFA:
    def __init__ (self, states, alphabet, delta, start, accept):
        self.states = states
        self.alphabet = alphabet
        self.delta = delta
        self.start = start
        self.accept = accept
    
    def transition(self, state, symbol):
        if (state, symbol) not in self.delta:
            return []
        return self.delta[(state, symbol)]
    
    def accepts(self, string, state):
        if len(string) == 0:
            return state in self.accept
        else:
            next_states = self.transition(state, string[0])
            for next_state in next_states:
                if self.accepts(string[1:], next_state):
                    return True
            return False
    

states = {'q0', 'q1', 'q2', 'q3'}
alphabet = {'0', '1'}
delta = {('q0', '0') : ['q0', 'q1'], ('q0', '1') : ['q3', 'q0'], ('q1', '1') : ['q2'], ('q3', '0') : ['q2']}
start = 'q0'
accept = {'q2'}


nfa = NFA(states, alphabet, delta, start, accept)
to_validate = input("Enter a string to validate: ")
print(nfa.accepts(to_validate, start))


        
