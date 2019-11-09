
def pren(l):
    d = set()
    def helper(l, p):
        if l==1:
            if p not in d:
                d.add(p)
                print(p)            
            return 
        
        helper(l-1, "("+p+")")
        helper(l-1, "()"+p)
        helper(l-1, p+"()")

    return  helper(l, "()")
    
    
if __name__ == "__main__":
    pren(4)