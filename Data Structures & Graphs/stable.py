
'''
# Submitter: munirm(Munir, Maaz)
# Partner  : ljoseph(Joseph, Liza)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
'''

from goody import safe_open
from collections import defaultdict

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    
    adict = defaultdict(list)
    
    for line in open_file:
        alist = list()
        line = line.rstrip()
        line = line.split(';')
        
        for match in line[1:]:
            alist.append(match)   
            
        adict[line[0]] = [None, alist]      
          
    return adict


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    
    string  = ''
    for k in sorted(d, key = key , reverse = reverse):
        string += "  {} -> {}\n".format(k, d[k])
    
    return string
    

def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    return p1 if order.index(p1)<order.index(p2) else p2
            

def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    return {(k, v[0]) for k,v in men.items()}
    

def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    men_copy = men
    unmatched_male = {k for k in men_copy}
#     print(trace)
    if trace == True: 
        
        print()
        print("Women Preferences (unchanging)")
        print(dict_as_str(women))
        
    
    while len(unmatched_male) != 0:
        
        if trace == True:
            print("Men Preferences (current)")
            print(dict_as_str(men_copy))
            print('unmatched men = ',unmatched_male)
        
        pop_male = unmatched_male.pop()
        pop_female = men_copy[pop_male][1].pop(0)
        
        if women[pop_female][0] == None:
            if trace == True: 
                string ='{} proposes to {}; the unmatched woman accepts the proposal'.format(pop_male, pop_female)
                print(string)
                print()
            men_copy[pop_male][0] = pop_female
            women[pop_female][0] = pop_male
            
        elif women[pop_female][0] != None:
            if who_prefer(women[pop_female][1], women[pop_female][0], pop_male) == pop_male:
                current_match = women[pop_female][0]
                if trace == True:
                    string = '{} proposes to {}; this matched woman accepts the proposal, rejecting match with {}'.format(pop_male, pop_female, current_match)
                    print(string)
                    print()
                men_copy[current_match][0] = None
                unmatched_male.add(current_match)
                women[pop_female][0] = pop_male
                men_copy[pop_male][0] = pop_female
            else:
                if trace == True:
                    string = '{} proposes to {}; this matched woman rejects the proposal (likes current match better)'.format(pop_male, pop_female)
                    print(string)
                    print()
                unmatched_male.add(pop_male)
    
    if trace == True:
        print('algorithm terminated with matches = ', extract_matches(men_copy))
        trace = False
    return extract_matches(men_copy)            

if __name__ == '__main__':
    # Write script here
    file1 = safe_open('Enter a file storing preferences of men:','r','Illegal file name')
    file2 = safe_open('Enter a file storing women preferences of women:', 'r', 'Illegal file name')
    men = read_match_preferences(file1)
    women = read_match_preferences(file2)
    print()
    print('Men Preferences')
    display = dict_as_str(men)
    print(display)
    
    print('Women Preferences')
    display = dict_as_str(women)
    print(display)
    
    trace = input('Trace The Algorithm[True]: ')
    var = (False if trace == 'False' else True)
    matches = make_match(men, women, var)
            
    if var == False: 
        print() 
        print('matches: ', matches)
        
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()