import string, itertools

def allPossibleSum(digits, target):

    for i in itertools.product(["+", "-", ""], repeat=9):
        if i[0]!='+':        
            temp = ''.join(''.join(v) for v in zip(i, l))
            
            if eval(temp) == target:
                print(temp)        
                
if __name__ == "__main__":
    l = [i for i in '123456789']    
    target = 10    
    
    allPossibleSum(l, target)
            