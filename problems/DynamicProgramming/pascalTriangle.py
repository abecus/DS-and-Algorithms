def pascal(row, index):
    if index == 0 or row == index:
        ele =  1
    
    else:
        ele = pascal(row-1, index-1) + pascal(row-1, index)
    return ele


def pascalTriangle(n, log=None):
    if log==None:
        log=[[1]]
    if n==1:
        return log

    else:
        # adding last row(except last element) of triangle to it self(except first element)
        new_row = [1] + [sum(i) for i in zip(log[-1], log[-1][1:])] + [1]
        return pascalTriangle(n-1, log + [new_row])


if __name__ == "__main__":
    print(pascalTriangle(5))
