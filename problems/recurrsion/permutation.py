# implements permutation of a iterable

def permutation(arr, r, t=[]):
        if len(t)==r:
            yield t

        for i, c in enumerate(arr):
            arr.remove(c)
            t.append(c)

            yield from permutation(arr, r, t)

            del t[-1]
            arr.insert(i, c)

for i in permutation([*"abdul"], 3):
    print(i)
