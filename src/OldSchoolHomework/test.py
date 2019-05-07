import numpy
import numpy as np
def char2num(s):
    return {'A': 0, 'C': 1, 'G': 2, 'T': 3}[s]   #translate the obervation sequences into numbers

def fn(x, y):
    return x * 10 + y        #switch the number string into int

def viterbi (priors,transition,emission,observations):  
    """Return the best path, given an HMM model and a sequence of observations"""
    # A - initialise stuff
    nSamples = len(observations)   
    nStates = transition.shape[0] # number of states   
    c = np.zeros(nSamples) #scale factors (necessary to prevent underflow)
    viterbi = np.zeros((nStates,nSamples)) # initialise viterbi table  
    psi = np.zeros((nStates,nSamples)) # initialise the best path table 
    best_path = np.zeros(nSamples); # this will be your output  
 
    # B- appoint initial values for viterbi and best path (bp) tables - Eq (32a-32b)
    for s in range (0,nStates):
        viterbi[s,0] = priors.T[s] * emission[s,observations[0]]   
        psi[0] = 0;

    # C- Do the iterations for viterbi and psi for time>0 until T           
    for t in range(1,nSamples): # loop through time                    
        for s in range (0,nStates): # loop through the states @(t-1)             
            trans_p = viterbi[:,t-1] * transition[:,s]               
            viterbi[s,t] = max((trans_p))     
            psi[s,t] =  max((trans_p))     
            viterbi[s,t] = viterbi[s,t]*emission[s,observations[t]]                         
    # D - Back-tracking          
    for t in range(nSamples,1,-1): # states of (last-1)th to 0th time step
        best_path[t-1] = viterbi[:,t-1].argmax()

    return best_path
if __name__ == '__main__':
    hmm_priors = np.array([1,0,0,0])  #prior probs
    hmm_transition = np.array([[0.4, 0.4, 0.2, 0],
                              [0, 0.6, 0.4, 0],
                              [0, 0, 0.4, 0.6],
                              [0.5, 0, 0, 0.5]])         # A = transition probs. / 4 states
    hmm_emission = np.array([[0.333, 0.167,0,0.5],   
                             [0.25, 0.25, 0.25, 0.25],
                             [0, 0.1875, 0.0625, 0.75],
                             [0.8, 0.1, 0.1, 0]])            # B = emission (observation) probs. / 4 obs modes
    f=open('/Users/Siyao/Desktop/Python/hello.txt','r')
    i=1
    while  True:
        a = f.readline()            #open the file
        if a:
            m = a.strip('\n')
            m = m.strip('\r')
            n = len(m)
            print '\nSeq   %d :'  %i,m,
            y = map(char2num,m)
            best_path_ind = viterbi(hmm_priors,hmm_transition,hmm_emission,y)        #get the best path
            p = map(int,best_path_ind)
            p = [i+1 for i in p]
            p = reduce(fn, p)
            print '\nState %d :'  %i,p,                     #get the result
            i=i+1

        else:
            break
    f.close()
