from collections import Counter

#%%
c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args

#%%
c = Counter(['eggs', 'ham'])
c['bacon']                              # count of a missing element is zero

#%%
c['sausage'] = 0                        # counter entry with a zero count
del c['sausage']                        # del actually removes the entry

#%%
c = Counter(a=4, b=2, c=0, d=-2)
list(c.elements())

#%%
Counter('abracadabra').most_common(3)

#%%
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
c

#%%
"""
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
"""
#%%
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c + d                       # add two counters together:  c[x] + d[x]
# Counter({'a': 4, 'b': 3})
c - d                       # subtract (keeping only positive counts)
# Counter({'a': 2})
c & d                       # intersection:  min(c[x], d[x])
# Counter({'a': 1, 'b': 1})
c | d                       # union:  max(c[x], d[x])
# Counter({'a': 3, 'b': 2})

