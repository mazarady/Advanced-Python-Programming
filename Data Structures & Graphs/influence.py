'''
# Submitter: munirm(Munir, Maaz)
# Partner  : ljoseph(Joseph, Liza)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
'''

import prompt
from goody       import safe_open, irange
from math        import ceil 
from collections import defaultdict
from ast import literal_eval


def read_graph(open_file : open) -> {str:{str}}:
    adict = defaultdict(set)
    for line in open_file:
        line = line.rstrip()
        line = line.split(';')
        
        if len(line) == 1: 
            adict[line[0]]
            
        else:
            adict[line[0]].add(line[1])
            adict[line[1]].add(line[0])
            
    return adict

def graph_as_str(graph : {str:{str}}) -> str:
    string = ''
    for k,v in sorted(graph.items(), key = lambda item : item[0]):
        v = list(v)
        v.sort()
        string += "  {} -> {}\n".format(k, v)
    return string

def find_influencers(graph : {str:{str}}, trace : bool = False) -> {str}:
    infl_dict = defaultdict(list)
    
    for k,v in sorted(graph.items(), key = lambda item: item[0]):
        friends = len(v)
        alist = [0,0,0]
        if len(v) == 0: 
            alist[0] = -1
        else:
            alist[0] = friends - ceil(friends/2)
        alist[1] = friends
        alist[2] = k
        infl_dict[k] = alist
        
    while True:
        if trace == True: print('influencer dictionary = ', dict(infl_dict))
        
        rlist = list()
        for j,k in infl_dict.items():
            if k[0] >= 0:
                new_k = tuple(k)
                rlist.append(new_k)
        
        if trace == True: print('removal candidates = ', rlist)
        
        if len(rlist) == 0: break
        minimum = min(rlist)
        
        if trace == True: 
            string = "{} is the smallest candidate".format(minimum)
            print(string)
        
        for x in graph[minimum[2]]:
            if x in infl_dict.keys():   
                infl_dict[x][0] = infl_dict[x][0]- 1
                infl_dict[x][1] = infl_dict[x][1]- 1
        if trace == True: 
            string = "Removing {} as key from influencer dictionary; decrementing friend's values there".format(minimum[2])
            print(string,'\n')
            
        del infl_dict[minimum[2]]
        
    return infl_dict.keys()


def all_influenced(graph : {str:{str}}, influencers : {str}) -> {str}:
    adict = defaultdict(bool)
    true_count = 0
    for k,v in sorted(graph.items()):
        if k in influencers:
            adict[k] = True
            true_count += 1
        else: adict[k] = False
    
    for i in range(50):
        for k, v in sorted(adict.items()):
            if v == False:
                count = 0
                for friends in graph[k]:
                    if friends in influencers: 
                        count += 1
                        
                if count >= ceil(len(graph[k])/2) and ceil(len(graph[k])/2) != 0:
                    adict[k] = True
                    influencers = set(influencers)
                    influencers.add(k)
        
    aset = set()
    for k, v in sorted(adict.items()):
        if adict[k] == True: 
            aset.add(k)
            
    return aset
          
                              
if __name__ == '__main__':
    # Write script here
    file = safe_open('Enter name of file to cross-reference','r','Illegal file name')
    print("Graph: source -> {destination} edges")
    adict = read_graph(file)
    alist = []
    for k in adict: 
        alist.append(k)
    display = graph_as_str(adict)
    print(display)
    trace = input('Trace The Algorithm[True]: ')
    var = (False if trace == 'False' else True)
    
    influencers = find_influencers(adict, var)
    print()
    print('Influencers = ', set(influencers))

    
    while True:
            
        print("Enter influencers set (or else quit)[",set(influencers),"]: ", end = '')
        new_influencers = input()
        
        if new_influencers == '':
            all_influenced_set = all_influenced(adict, influencers)
            string = "All Influenced ({:.0%} of graph)= ".format(len(all_influenced_set)/len(adict))
            print(string, all_influenced_set)
            print()
            continue
            
        elif new_influencers == 'quit': break
        
        new_influencers = set(literal_eval(new_influencers))
        
        if any(x not in adict for x in new_influencers):
            print("Entry Error: ", new_influencers)
            print('Please Enter a legal String')
            print()
            continue
        
        else:
            all_influenced_set = all_influenced(adict, new_influencers)
            string = "All Influenced ({:.0%} of graph)= ".format(len(all_influenced_set)/len(adict))
            print(string, all_influenced_set)
            print()
            continue
            
        
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()

