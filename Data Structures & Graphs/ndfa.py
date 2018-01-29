'''
# Submitter: munirm(Munir, Maaz)
# Partner  : ljoseph(Joseph, Liza)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
'''

from goody import safe_open
from collections import defaultdict


def read_ndfa(file : open) -> {str:{str:{str}}}:
    adict = defaultdict(dict)
    new_dict = defaultdict(set)
    
    for line in file:
        new_dict = defaultdict(set)
        line = line.rstrip()
        line = line.split(';')
 
        key = [line[v1] for v1 in range(1, len(line[1:]), 2)]        
        value = [line[v1+1] for v1 in range(1, len(line[1:]), 2)]
        
        for v1, v2 in zip(key, value):
            new_dict[v1].add(v2)
        
        adict[line[0]] = new_dict
        
    return adict


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    
    string = ''
    for k, v in sorted(ndfa.items()):
        v = [(sk,sorted(list(sv))) for sk, sv in sorted(v.items())]
        string += "  {} transitions: {}\n".format(k,v)
        
    return string

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    
    '''
   NDFA: {'start': {'0': {'near', 'start'}, '1': {'start'}}), 'near': {'1': {'end'}}), 'end': {})}
    
   INPUT: '1','0','1','1','0','1'
    
    OUTPUT: ['start', ('1', {'start'}), ('0', {'near', 'start'}), ('1', {'end', 'start'}), ('1', {'start'}),
    ('0', {'near', 'start'}), ('0', {'near', 'start'})]
    '''
    
    alist = [state]
    
    aset = set()
    aset.add(state)
    for entry in inputs:
        a_new_set = set()
        for el in aset:
            
            try:
                
                for poss in ndfa[el][entry]:
                    a_new_set.add(poss)
            except:
                pass
        if len(a_new_set) == 0:
            atuple = (entry, a_new_set)
            alist.append(atuple)
            break
                    
        aset = a_new_set
    
        atuple = (entry, a_new_set)
        
        alist.append(atuple)
        
    return alist


def interpret(result : [None]) -> str:
    string = 'Start state = {}\n'.format(result[0])
    
    for k in result[1:]:
        string += "  Input = {}; new possible states = {}\n".format(k[0], sorted(list(k[1])))        
    
    string += 'Stop state(s) = {}\n'.format(sorted(list(k[1])))
    
    return string


if __name__ == '__main__':
    # Write script here
    file1 = safe_open('Enter a file storing a non-deterministic finite automaton','r','Illegal file name')
    adict = read_ndfa(file1)
    print("The Description of this Non-Deterministic Finite Automaton")
    print(ndfa_as_str(adict))
    
    file2 = safe_open("Enter a file storing a start-state and its inputs" ,'r', 'Illegal file name')    

    for line in file2: 
        print()
        print("Starting up a new NDFA simulation")
        line = line.rstrip()
        line = line.split(';')
        pro = process(adict, line[0], line[1:])
        print(interpret(pro))
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
