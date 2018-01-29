import re
from goody import irange
from collections import defaultdict

'''
# Submitter: munirm(Munir, Maaz)
'''

# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the files repattern1a.txt, repattern1b.txt, repattern1c.txt, 
#   and repattern2.txt. The patterns must be all on the first line, enclosed in ^ and $


def expand_re(pat_dict:{str:str}):
    pattern_set = set()
    for k,v in pat_dict.items():
        for element in v.split('#'):
            if element in pat_dict:
                pattern_set.add(element)
                stealing_pattern = pattern_set.pop()
                
                hashtag_string = '#{}#'.format(stealing_pattern)
                poop_pattern = "(?:{})".format(pat_dict[element])
                
                pat_dict[k] = re.sub(hashtag_string, poop_pattern, pat_dict[k])
    
                             
    
def multi_search(pat_file : open, text_file : open) -> [(int,str,[int])]:
    alist = list()
    atuple = tuple()
    final = list()
    
    pattern_list = [pattern.rstrip() for pattern in pat_file]
    text_list = [line.rstrip() for line in text_file]
    
    for line in enumerate(text_list, start = 1):
        for pattern in enumerate(pattern_list, start = 1):
            if re.search(pattern[1], line[1]) != None:
                alist.append(pattern[0])
                atuple = (line[0], line[1], alist)
                            
        alist = []
        if atuple not in final:
            final.append(atuple)

    return final
        
    
         
if __name__ == '__main__':
    
#     p1a = open('repattern1a.txt').readline().rstrip() # Read pattern on first line
#     print('Testing the pattern p1a: ',p1a)
#     for text in open('bm1a.txt'):
#         text = text.rstrip()
#         print('Matching against:',text)
#         m = re.match(p1a,text)
#         print(' ','Matched' if m != None else "Not matched")
# 
# 
#     p1b = open('repattern1b.txt').readline().rstrip() # Read pattern on first line
#     print('\nTesting the pattern p1b: ',p1b)
#     for text in open('bm1b.txt'):
#         text = text.rstrip()
#         print('Matching against:',text)
#         m = re.match(p1b,text)
#         print('  ','Matched' if m != None else 'Not matched' )
#         
#         
#     p1c = open('repattern1c.txt').readline().rstrip() # Read pattern on first line
#     print('\nTesting the pattern p1c: ',p1c)
#     for text in open('bm1b.txt'):                 # Same file as before
#         text = text.rstrip()
#         print('Matching against:',text)
#         m = re.match(p1c,text)
#         print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
#         
#         
#     p2 = open('repattern2.txt').read().rstrip() # Read pattern on first line
#     print('\nTesting the pattern p2: ',p2)
#     for text in open('bm2.txt'):
#         text = text.rstrip()
#         print('Matching against:',text)
#         m = re.match(p2,text)
#         print('  ','Matched' if m != None else 'Not matched' )
        
    
    
#     print('\nTesting expand_re')
#     pd = dict(digit = r'\d', integer = r'[=-]?#digit##digit#*')
#     print('  Expanding ',pd)
#     expand_re(pd)
#     print('  result =',pd)
    # produces/prints the dictionary
    # {'digit': '\\d', 'integer': '[=-]?(?:\\d)(?:\\d)*'}
    
#     pd = dict(integer       = r'[+-]?\d+',
#               integer_range = r'#integer#(..#integer#)?',
#               integer_list  = r'#integer_range#(?,#integer_range#)*',
#               integer_set   = r'{#integer_list#?}')
#     print('\n  Expanding ',pd)
#     expand_re(pd)
#     print('  result =',pd)
    # produces/prints the dictionary 
    # {'integer': '[+-]?\\d+',
    #  'integer_range': '(?:[+-]?\\d+)(..(?:[+-]?\\d+))?',
    #  'integer_list': '(?:(?:[+-]?\\d+)(..(?:[+-]?\\d+))?)(?,(?:(?:[+-]?\\d+)(..(?:[+-]?\\d+))?))*',
    #  'integer_set': '{(?:(?:(?:[+-]?\\d+)(..(?:[+-]?\\d+))?)(?,(?:(?:[+-]?\\d+)(..(?:[+-]?\\d+))?))*)?}'
    # }
    
#     pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
#     print('\n  Expanding ',pd)
#     expand_re(pd)
#     print('  result =',pd)
    
    # produces/prints the dictionary 
    # {'a': 'correct',
    #  'b': '(?:correct)',
    #  'c': '(?:(?:correct))',
    #  'd': '(?:(?:(?:correct)))',
    #  'e': '(?:(?:(?:(?:correct))))',
    #  'f': '(?:(?:(?:(?:(?:correct)))))',
    #  'g': '(?:(?:(?:(?:(?:(?:correct))))))'
    # }
    
    
      
#     print('\nTesting multi_search on pats1.txt and texts1.txt')
#     print(multi_search(open("pats1.txt"),open("texts1.txt")))
# 
# #     print('\nTesting multi_search on pats2.txt and texts2.txt')
# #     print(multi_search(open("pats2.txt"),open("texts2.txt")))
#     
    
    
    print()
    print()
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
    
    
       
        
        
        
        

