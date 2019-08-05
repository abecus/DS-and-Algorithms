from collections import deque
#%%
d = deque('ghi')                 # make a new deque with three items

#%%d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side
print(d)

#%%
d.pop()                          # return and remove the rightmost item

#%%
d.popleft()                      # return and remove the leftmost item

#%%
print(d)

#%%
print(d[0])                             # peek at leftmost item

#%%
print(d[-1])                            # peek at rightmost item


#%%
d.extend('jkl')                  # add multiple elements at once
print(d)

#%%
d.rotate(1)                      # right rotation
print(d)

#%%
d.rotate(-1)                     # left rotation
print(d)

#%%
deque(reversed(d))               # make a new deque in reverse order

#%%deque(['l', 'k', 'j', 'i', 'h', 'g'])
d.clear()                        # empty the deque

#%%
d.extendleft('abc')              # extendleft() reverses the input order 
print(d)
