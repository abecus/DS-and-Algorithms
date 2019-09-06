from collections import defaultdict


d = defaultdict(lambda: {})
doneTill = 0
index = 0
count = 0

def decibinaryNumbers(x):
    global d, doneTill, index, count

    def decibinToDeci(s):
        s = str(s)
        l = len(s)
        d = 0
        for i, ele in enumerate(s):
            t = l-i-1
            d += (2**(t)*int(ele))
        return d
                
    def computeAll(index, count, doneTill, target=x):
        # computes the all decibinary values 
        # for a decibel value starting form doneTill
        
        maxTill = int(bin(index)[2:])
    
        for val, ind in iter(d[index].items()):
            if ind!=1:
                count += 1
                d[index][val] = 1

        for i in range(doneTill, maxTill+1):
            
            if count == target:
                return i, count, index
            
            dbd = decibinToDeci(i)
            d[dbd][i] = 0
            
            if dbd == index:
                count+=1
                d[dbd][i] = 1
                
        return i, count, index+1
            
            
    while count!=x and count<x:
        doneTill, count, index = computeAll(index, count, doneTill)

    count = 0
    for key, val in iter(d.items()):
        temp = count+len(val)
        
        if temp>=x and count<x:
            for i, j in iter(val.items()):
                count+=1
                                
                if count == x:
                    return i
                
        else:
            count=temp
    
if __name__ == '__main__':
    q = [1, 2, 3, 4, 10]   # 0 1 2 10 100
    q = [8,23,19,16,26,7,6] # 12 23 102  14 111 4 11
    q = [19,25,6,8,20,10,27,24,30,11] # 102 103 11 12 110 100 8 31 32 5
    
    for i in q:
        print(decibinaryNumbers(i))
        print('_'*50)
