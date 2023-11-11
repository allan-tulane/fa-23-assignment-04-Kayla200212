import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    elif (S[0] == T[0]):
        return(MED(S[1:], T[1:]))
    else:
        insertion = 1 + MED(S, T[1:])
        deletion = 1 + MED(S[1:], T)
        subst = 1 + MED(S[1:], T[1:])
        #not super different from the above functions
        return min(insertion, deletion, subst)#return the lowest costing one


def fast_MED(S, T, MED={}):
    # TODO -  implement top-down memoization
    s_len = len(S)
    t_len = len(T)#assign a variable to the length of each
    fM = [[0 for x in range (t_len+1)] for x in range(s_len)]#create an array to memoize
    for i in range(s_len):
      for j in range(t_len):
        if i==0:#if i is 0, j is bigger so its our min
          fM[i][j] = j
        elif j == 0:#vice versa
          fM[i][j] = i
        elif S[i-1] == T[j-1]:#if last chars are same
          fM[i][j] = fM[i-1][j-1]#change to 2nd to last and go down
        else: #last chars are diff so you have to do them all
          fM[i][j] = 1 + min(fM[i][j-1], fM[i-1][j], fM[i-1][j-1])
    return fM
          
def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
    fM = fast_MED(S,T)#find the min distance using the above
    s_list = []
    t_list = []
    i = len(S)
    j = len(T)
    while True:
      if(i == 0 and j==0):
        break #this would be the end of aligning it showing S and T are done
      else:#otherwise we go thru the loop until the lists are empty
        add = fM[i][j-1]#cost to add a char to S
        remove = fM[i-1][j]#cost of removing a char from S
        subst = fM[i-1][j-1] #cost of subbing a char
        mins = min(add,remove,subst)#pull the min
        if(subst==mins):#if subst is equal to min
          s_list = [S[i-1]] + s_list#add aligned char from S to list
          t_list = [T[j-1]] + t_list#same for t
          i -= 1#go back up the row 
          j -= 1#same here
        elif (add == mins):
          s_list = ['_'] + s_list#the underscore represents a new char in s
          t_list = [T[j-1]] + t_list#add aligned from t to list
          j -= 1#move up again
        elif (remove == mins):
          t_list = ['_'] + t_list#same as above but the other group
          s_list = [S[i-1]] + s_list
          i -= 1
    s_string = ""
    t_string = ""
    s_string = s_string.join(s_list)#turn the chars into a string
    t_string = t_string.join(t_list)
    return s_string, t_string#and return the strings but aligned

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
