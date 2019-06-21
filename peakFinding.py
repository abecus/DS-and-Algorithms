import numpy as np


def one_dim_peak_finding(array):
    """
    finds a local maxima in a list if it exist
    """
    
    n = len(array)
    half_n = n//2

    if n==1 or n==2:
        return max(array)

    if n==0:
        return None

    if array[half_n] > array[half_n+1]:
        return one_dim_peak_finding(array[: half_n+1])
    
    elif array[half_n] < array[half_n+1]:
        return one_dim_peak_finding(array[half_n+1 :])

    else:
        return array[n//2]


def two_dim_peak_finding(numpy_matrix):
    '''
    finds a local maxima in a matrix if it exist
    '''
    
    array = numpy_matrix

    try: 
        n, m  = array.shape
    except: 
        return None
    
    half_m = m//2
    half_n = n//2
    arg = np.argmax(array[:, half_m], axis=0)   # finding index of maximum of middle column
    maximum = array[arg, half_m]

    if m==1 or n==1:
        '''feeds last column to one_dim_peak_finding.'''
        return one_dim_peak_finding(np.squeeze(array).tolist()) 
    
    elif m==2:
        '''
        finds index of last two columns row index == arg and 
        feeds that column containning it to one_dim_peak_finding
        '''
        arg2 = np.argmax(array[arg, :], axis=0)
        return one_dim_peak_finding(np.squeeze(array[:, arg2]).tolist())
    
    elif maximum > array[arg, half_m+1]:
        return two_dim_peak_finding(array[:, : half_m+1])

    elif maximum < array[arg, half_m+1]:
        return two_dim_peak_finding(array[:, half_m+1 :])
        
    else:
        return maximum


if __name__ == "__main__":

    # arr = [2, 3, 2]
    # print(one_dim_peak_finding(arr))

    mat = np.array([
        [1, 0, 2],
        [0, 2, 0],
        [100, 6, 20],
        [50, 5, 21]
        ])

    print(two_dim_peak_finding(mat))
        
    