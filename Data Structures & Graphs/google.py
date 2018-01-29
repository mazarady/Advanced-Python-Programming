'''
# Submitter: munirm(Munir, Maaz)
# Partner  : ljoseph(Joseph, Liza)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
'''

import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use defaultdict for prefix and query


def all_prefixes(fq : (str,)) -> {(str,)}:
    return {tuple(fq[0:x+1]) for x in range(0,len(fq))}




def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    
    for i in all_prefixes(new_query):
        prefix[i].add(new_query)
        
    query[new_query]+=1


def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    prefix = defaultdict(set)
    query = defaultdict(int)
    for line in open_file:
        line = line.rstrip().split(' ')
        line = tuple(line)
        add_query(prefix, query, line)
    
    return (prefix, query)
        
#         print(all_prefixes(line))
   

def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    string  = ''
    for k in sorted(d, key = key , reverse = reverse):
        
        string += "  {} -> {}\n".format(k, d[k])
    
    return string


def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:

   
    final_list = []
    anew_list = []
    if a_prefix in prefix:
        alist = [prefix for prefix in sorted(prefix[a_prefix], key = lambda x: x)]
        
        if n > len(alist):
            quick = []
            for x in alist:
                quick.append((x,query[x]))
                
            quick = sorted(quick, key = lambda x:(-x[1],x[0]))
            return [x[0] for x in quick]

        for x in alist: 
            if x in([v[0] for v in query.items()]):
                anew_list.append((x,query[x]))
            else:
                pass
                          
        anew_list.sort(key = lambda x:(-x[1],x[0]))
        for x in range(n):
            final_list.append(anew_list[x][0])
        return final_list
    
    else:
        return []




# Script

if __name__ == '__main__':
    # Write script here
    file1 = safe_open('Enter a file storing a non-deterministic finite automaton','r','Illegal file name')
    atuple = read_queries(file1)
    print('Prefix dictionary: ')
    print(dict_as_str(atuple[0], key = None, reverse = False))
    print("Query dictionary: ")
    print(dict_as_str(atuple[1], key = None, reverse = False))
    
    while True:
            
        x = input("Enter any prefix sequence (or else quit): ")
        if x == 'quit':
            break
        
        print()
        x = x.rstrip().split(' ')
        print("Top 3 (no more) matching full queries: ")
        x = tuple(x)
        top_number = top_n((x), 3, atuple[0], atuple[1])
        print(top_number)
        print()
        
        x = input("Enter any full query sequence (or else quit): ")
        if x == 'quit':break
        x = x.rstrip().split(' ')
        x = tuple(x)
        print()
#         print(x)
        add_query(atuple[0], atuple[1],x)
        print('Prefix dictionary: ')
        print(dict_as_str(atuple[0], key = None, reverse = False))
        print("Query dictionary: ")
        print(dict_as_str(atuple[1], key = None, reverse = False))

              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
