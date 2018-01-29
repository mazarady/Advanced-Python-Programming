from math import sqrt, pow
from collections import defaultdict


def delay(f : callable, n : int) -> callable:
    assert type(n) == int and n >=0
    alist = [None for i in range(n)]
    
    def internal_function(x: int):
        alist.append(f(x))
        return alist.pop(0)
        
    return internal_function


def mixed_sort1(alist : list) -> list:

    assert type(alist) == list and len([i for i in alist if type(i) is int or type(i) is str]) == len(alist)
    
    return sorted(alist, key = lambda x: int(x))

def mixed_sort2(alist : list) -> list:
    
    assert type(alist) == list and len([i for i in alist if type(i) is int or type(i) is str]) == len(alist)
 
    return [k for k in sorted(alist, key = lambda x: int(x)) if type(k) == int] + [k for k in sorted(alist, key = lambda x: int(x) ) if type(k) == str]

def mixed_sort3(alist : list) -> list:
    
    assert type(alist) == list and len([i for i in alist if type(i) is int or type(i) is str]) == len(alist)
 
    return [k for k in sorted(alist, key = lambda x: int(x)) if type(k) == int] + [k for k in sorted(alist, key = lambda x: int(x), reverse = True) if type(k) == str]



def mixed_sort4(alist : list) -> list:
    
    assert type(alist) == list and len([i for i in alist if type(i) is int or type(i) is str]) == len(alist)
 
    return [int(k) for k in sorted(alist, key = lambda x: int(x)) if type(k) == int] + [int(k) for k in sorted(alist, key = lambda x: int(x), reverse = True) if type(k) == str]




def distance_from (coord : (int,int), ps : {int:(int,int)}) -> [int]:
    pass

def reviewer_rank(db : {str:{(str,int)}}) -> [(str,int)]:
    alist = [name[0] for k, v in db.items() for name in v]
    final = []
    for k, v in db.items(): 
        for name in v:
                
            value = alist.count(name[0])
            atuple = (name[0], value)
            if atuple not in final:
                    
                final.append(atuple)
            
    final.sort(key = lambda x: (-x[1],x[0]))
    return final
        
                

def reviewer_nested_dict(db : {str:{(str,int)}}) -> {str:{str:int}}:
    adict = defaultdict(dict)
    temp = dict()
    
    for k, v in db.items(): 
        for name, rating in v:
            temp[k] = rating
            adict[name].update(temp)
            temp = dict()
            
    return dict(adict)
    
            
if __name__ == '__main__':
    # This code is useful for debugging your functions, especially
    #   when they raise exceptions: better than using driver.driver().
    # Feel free to add more tests (including tests showing in the bsc.txt file)
    # Use the driver.driver() code only after you have removed anybugs
    #   uncovered by these test cases.
    
    from goody import irange
    
#     print('\nTesting delay')
#     g = delay( (lambda x : x), 2)
#     print(g(0),g(1),g(2),g(3),g(4))
#     g = delay( (lambda x : 2*x), 5)
#     for i in irange(0,10):
#         print(g(i))

#     print('Testing mixed_sort1')
#     print(mixed_sort1([1,2,3,4,5]))
#     print(mixed_sort1(['1','2','3','4','5']))
#     print(mixed_sort1([1,'2','3',4,5,6,'7','8',9,'10']))
# 
#     print('\nTesting mixed_sort2')
#     print(mixed_sort2([1,2,3,4,5]))
#     print(mixed_sort2(['1','2','3','4','5']))
#     print(mixed_sort2(['2', 1,'3',4,5,6,'7','8',9,'10']))
# 
#     print('\nTesting mixed_sort3')
#     print(mixed_sort3([1,2,3,4,5]))
#     print(mixed_sort3(['1','2','3','4','5']))
#     print(mixed_sort3([1,'2','3',4,5,6,'7','8',9,'10']))
# 
#     print('\nTesting mixed_sort4')
#     print(mixed_sort4([1,2,3,4,5]))
#     print(mixed_sort4(['1','2','3','4','5']))
#     print(mixed_sort4([1,'2','3',4,5,6,'7','8',9,'10']))
# 
#     print('\nTesting distance_from')
#     ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2),6:(3,3),7:(1,-1)} 
#     print(distance_from((0,0),ps1))
#     print(distance_from((1,-1),ps1))
# 
#     print('\nTesting reviewer_rank')
#     db1 = {'Psycho':  {('Bob',5),  ('Carry',5), ('Diane', 1), }, 'Amadeus': {('Bob',3),  ('Carry',3), ('Diane',3)}, 'Up': {('Alan',2), ('Bob', 5), ('Diane',5)} }
#     db2 = {'Psycho':  {('Bob',5),  ('Carry',5), ('Alan', 1), ('Diane', 1), ('Evan',4), ('Fawn',2)},
#            'Amadeus': {('Bob',3),  ('Carry',3), ('Diane',3)},
#            'Up': {('Alan',2), ('Diane',5)},
#            'Casablaca': {('Alan',2), ('Diane',5), ('Evan',2)},
#            'Rashamon': {('Alan',2), ('Diane',5), ('Fawn',3), ('Gary',4)},
#            'Alien': {('Alan',2), ('Diane',5), ('Evan',5), ('Fawn',5)}}
#     print(reviewer_rank(db1))    
#     print(reviewer_rank(db2))    
#     
#     print('\nTesting reviewer_nested_dict')
#     db1 = {'Psycho':  {('Bob',5),  ('Carry',5), ('Diane', 1), }, 'Amadeus': {('Bob',3),  ('Carry',3), ('Diane',3)}, 'Up': {('Alan',2), ('Bob', 5), ('Diane',5)} }
#     db2 = {'Psycho':  {('Bob',5),  ('Carry',5), ('Alan', 1), ('Diane', 1), ('Evan',4), ('Fawn',2)},
#            'Amadeus': {('Bob',3),  ('Carry',3), ('Diane',3)},
#            'Up': {('Alan',2), ('Diane',5)},
#            'Casablaca': {('Alan',2), ('Diane',5), ('Evan',2)},
#            'Rashamon': {('Alan',2), ('Diane',5), ('Fawn',3), ('Gary',4)},
#            'Alien': {('Alan',2), ('Diane',5), ('Evan',5), ('Fawn',5)}}
#     print(reviewer_nested_dict(db1))    
#     print(reviewer_nested_dict(db2))    
    
    print('\ndriver testing with batch_self_check:')
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()           
