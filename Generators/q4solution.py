# Generators must be able to iterate through any iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file and add code for the other generators.
from goody import irange
def hide(iterable):
    for v in iterable:
        yield v


# The combination of return and yield None make each of the following
#   a generator (yield None) that immediately raises the StopIteration
#   exception (return)

def sequence(*iterables):
    for v in iterables:
        for more in v:
            yield more
                       
def group_when(iterable,p):
    alist = list()
    for i in iterable: 
        alist.append(i)
        if p(i) == True: 
            yield alist
            alist = []
            
    if alist != []:
        yield alist
                    
def drop_last(iterable,n):
    buffer = list()
    
    for i in iter(iterable):
        if len(buffer) == n:
            poppy = buffer.pop(0)
            yield poppy
            
        buffer.append(i)
        
        
def yield_and_skip(iterable,skip):
    iterable = iter(iterable)
    for i in iterable:
        num = skip(i)
        yield i
        for x in range(num):
            next(iterable)
                      
def alternate_all(*args):
    alist = [iter(i) for i in args]
    
    new = []
    while len(new) < len(alist):
        
        for x in alist:
            try:
                z = next(x)
                yield z
                
            except:
                new.append('l')

def min_key_order(adict):
    history_of_yields = list()
    alist = [(k,v) for k, v in adict.items()]
    
    while len(alist) != 0:
        
        alist = [(k,v) for k, v in adict.items() if (k,v) not in history_of_yields]
        
        try:
            min_value = min(alist)
            history_of_yields.append(min_value)
            alist.remove(min_value)
            
            if max(history_of_yields) <= min_value:  
                yield min_value

        except:
            pass

            
                 
         
if __name__ == '__main__':
    from goody import irange
    
    # Test sequence; you can add your own test cases
#     print('Testing sequence')
#     for i in sequence('abc', 'd', 'ef', 'ghi'):
#         print(i,end='')
#     print('\n')
#  
#     print('Testing sequence on hidden')
#     for i in sequence(hide('abc'), hide('d'), hide('ef'), hide('ghi')):
#         print(i,end='')
#     print('\n')
 
 
    # Test group_when; you can add your own test cases
#     print('Testing group_when')
#     for i in group_when('combustibles', lambda x : x in 'aeiou'):
#         print(i,end='')
#     print('\n')
 
#     print('Testing group_when on hidden')
#     for i in group_when(hide('combustibles'), lambda x : x in 'aeiou'):
#         print(i,end='')
#     print('\n')


    # Test drop_last; you can add your own test cases
    print('Testing drop_last')
    for i in drop_last('combustible', 5):
        print(i,end='')
    print('\n')
   
    print('Testing drop_last on hidden')
    for i in drop_last(hide('combustible'), 5):
        print(i,end='')
    print('\n')


    # Test sequence; you can add your own test cases
#     print('Testing yield_and_skip')
#     for i in yield_and_skip('abbabxcabbcaccabb',lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
#         print(i,end='')
#     print('\n')
# 
#     print('Testing yield_and_skip on hidden')
#     for i in yield_and_skip(hide('abbabxcabbcaccabb'),lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
#         print(i,end='')
#     print('\n')


    # Test alternate_all; you can add your own test cases
#     print('Testing alternate_all')
#     for i in alternate_all('abcde','fg','hijk'):
#         print(i,end='')
#     print('\n')
#     
#     print('Testing alternate_all on hidden')
#     for i in alternate_all(hide('abcde'), hide('fg'),hide('hijk')):
#         print(i,end='')
#     print('\n\n')
       
         
#     Test min_key_order; add your own test cases
#     print('\nTesting Ordered')
#     d = {1:'a', 2:'x', 4:'m', 8:'d', 16:'f'}
#     i = min_key_order(d)
#     print(next(i))
#     print(next(i))
#     print(next(i))
#     d[3] = 'n'
#     d[10] = 'o'
#     d[32] = 'z'
#     print(next(i))
#     print(next(i))
#     print(next(i))
#     print(next(i))    


         
         
    import driver
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
