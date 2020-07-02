# implements permutation of a iterable

def unorderedPermutation(arr, r, t=[]):
        if len(t)==r:
            yield t

        for c in arr:
            arr.remove(c)
            t.append(c)

            yield from unorderedPermutation(arr, r, t)

            t.pop()
            arr.add(c)

def orderPermutation(arr):
    perms = [[]]
    for num in arr:
        res=[]
        for perm in perms:
            for i in range(len(perm)+1):
                res.append( perm[i:]+[num]+perm[:i] )
            perms=res
    return perms


if __name__ == "__main__":
    res = []
    for i in orderPermutation(set([*"abd"])):
        res.append([*i])
    print(*res, sep='\n')
