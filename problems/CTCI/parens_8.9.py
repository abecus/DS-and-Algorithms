
def pren(l):
    d = {}
    def helper(l, p):
        if l==0:
            p = ''.join(p)
            if p not in d:
                d[p]=1
                print(p)            
            return ['(', ')']
        
        helper(l-1, ['('] + p + [')'])
        helper(l-1, ['(', ')'] + p)
        helper(l-1, p + ['(', ')'])
        
    return  helper(l, [])
    
    
if __name__ == "__main__":
    pren(4)