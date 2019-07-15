# a simple balaced Paranthesis problem Using Stacks

def is_balanced(arr, mapping={'(':')', '{':'}', "[":"]"}):
    """
    itype: string or list
    rtype: True or False 
    
    arguments:
    mapping: dictionary containg inverse of each entry as its value
    """
    
    stack = []

    for i in arr:

        if i in mapping:
            stack.append(i)
            
        else:
            try:
                last = stack[-1]

            except:
                return False
                
            if i==mapping[last]:
                stack.pop()
            
            else:
                return False
    
    return len(stack)==0

if __name__ == "__main__":    
    l = '(((()))())))'
    b='()()()()' 

    s='lrlllrrr'
    print(is_balanced(b))