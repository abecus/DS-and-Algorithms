def reverseList(s):
    '''
    Itype: list

    rtype: list

    Reverses the list entries
    '''
    
    
    if len(s)<=0:
        return s  

    else:
        return reverseList(s[1:]) + [s[0]]
  

if __name__ == "__main__":
    print(reverseList(["h","e","l","l","o"]))
