'''
# Submitter: munirm(Munir, Maaz)
# Partner  : ljoseph(Joseph, Liza)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
'''
from goody import safe_open
from collections import defaultdict



def read_fa(file : open) -> {str:{str:str}}:
    adict = defaultdict(dict)
    
    for line in file:
        line = line.rstrip()
        line = line.split(';')
        aint = [v1 for v1 in line[1:] if v1.isdigit()]
        astr = [v2 for v2 in line[1:] if v2.isdigit() == False]
        
        new_dict = {v1:v2 for v1, v2 in zip(aint, astr)}
        adict[line[0]] = new_dict
        
    return dict(adict)
        
def fa_as_str(fa : {str:{str:str}}) -> str:

    string = ''
    for k, v in sorted(fa.items()):
        v = [(sk,sv) for sk, sv in sorted(v.items())]
        string += "  {} transitions: {}\n".format(k,v)
    return string
        
    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    '''
    faparity.txt
    right: ['even', ('1', 'odd'), ('0', 'odd'), ('1', 'even'), ('1', 'odd'), ('0', 'odd'), ('1', 'even')]
    '''
    
    alist = [state]
    
    for num in inputs:
        
        try:
            int(num)
            tuple = (num, fa[state][num])
            state = fa[state][num]
            alist.append(tuple)
            
        except:
            atuple = (num, None)
            alist.append(atuple)
    
    return alist
        

def interpret(fa_result : [None]) -> str:
#     print(fa_result)

    string = 'Start state = {}\n'.format(fa_result[0])
    
    for k in fa_result[1:]:
        try: 
            int(k[0])
            string += "  Input = {}; new state = {}\n".format(k[0], k[1])
            
        except:
            string += "  Input = {}; illegal input: simulation terminated\n".format(k[0])
            
    
    string += 'Stop state = {}\n'.format(k[1])
    
    return string

if __name__ == '__main__':
    # Write script here
    file1 = safe_open('Enter a file storing a finite automaton','r','Illegal file name')
    adict = read_fa(file1)
    print()
    print("The Description of this Finite Automaton")
    print(fa_as_str(adict))
    
    file2 = safe_open("Enter a file storing a start-state and its inputs" ,'r', 'Illegal file name')    

    for line in file2: 
        print()
        print("Starting up a new FA simulation")
        line = line.rstrip()
        line = line.split(';')
        pro = process(adict, line[0], line[1:])
        print(interpret(pro))
        
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
