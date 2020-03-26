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
        perms = [perm[i:]+[num]+perm[:i] for perm in perms for i in range(len(perm)+1)]
    return perms


if __name__ == "__main__":
    res = []
    for i in unorderedPermutation(set([*"abdul"]), 2):
        res.append([*i])
    print(res)
