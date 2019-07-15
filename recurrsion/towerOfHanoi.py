def printSteps(frm, to):
    print(f"move from {frm} --> to {to}")


def towerOfHanoi(n, frm, to, spare):
    if n==1:
        return printSteps(frm, to)
    
    else:
        towerOfHanoi(n-1, frm, spare, to)
        towerOfHanoi(1, frm, to, spare)
        towerOfHanoi(n-1, spare, to, frm)
        

if __name__ == "__main__":
    towerOfHanoi(4, 1, 0, 2)
