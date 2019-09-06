def maxArea(heights):
    """
    itype: list
    rtype: int
    """
    
    stack = []
    res = 0

    def popper(idx, height, res):
        # removes heights from stack untill the 
        # current height is not >= the top height of stack
        # and returns the index at which the last height 
        # was popped and the result
        while stack and stack[-1][1] > height:
                build = stack.pop()
                area = build[1]*(idx-build[0])
                res = max(res, area)
            
        return res, [build[0]]


    for idx, height in enumerate(heights):
        # loop throught all heights and if height is greater
        # >= than the top at stack or  stack is empty 
        # adds the height to the stack with its index as (index, height)
        if not stack or height>=stack[-1][1]:
            stack.append((idx, height))
        
        else:
            # call popper and add the height to the stack
            # with the index as last height index popped from the stack
            res, isempty = popper(idx, height, res)
            stack.append((isempty[0], height))


    temp = idx+1
    while stack:
        # loop through the remainig heights in stack if any and 
        # find the area corresponding to it and check if its max area
        build = stack.pop()
        area = build[1]*(temp-build[0])
        res = max(res, area)
      
    return res


if __name__ == "__main__":
    arr = [1,3,6,8,9,2,4,1]
    print(maxArea(arr))