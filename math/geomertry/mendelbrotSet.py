import matplotlib.pyplot as plt
import numpy as np


def get_iter(c:complex, thresh:int =4, max_steps:int =25) -> int:
    # Z_(n) = (Z_(n-1))^2 + c
    # Z_(0) = c
    z=c
    i=1
    while i<max_steps and (z*z.conjugate()).real < thresh:
        z=z*z +c
        i+=1
    return i

def plotter(n, thresh, max_steps=25):

    # image_coordinate (integers) --> real value to use on 
    # complex plane
    mapper = lambda x,y: (4*(x-n//2)/n, 4*(y-n//2)/n)

    # create image array (n*n) fill value 255
    img=np.full((n,n), 255)
    
    # since we know the bounds of x and y use it to save 
    # redundant computations
    # x \in {-2, 0.47} , y \in {-1.17, 1.17}
    x_lower = 0
    x_upper = 5*n//8
    y_lower = 2*n//10
    y_upper = 8*n//10
    
    for x in range(x_lower, x_upper):
        for y in range(y_lower, y_upper):
            
            it = get_iter(complex(*mapper(x,y)), 
                           thresh=thresh, 
                           max_steps=max_steps)
            
            # image get rotated with -90 dergee (don't know why)
            # so know rotating 90 by changing coordinate below
            img[y][x] = 255 - it

    return img[y_lower:y_upper, x_lower:x_upper]


n=1000
img = plotter(n, thresh=4, max_steps=50)
plt.imshow(img, cmap="plasma")
plt.axis("off")
plt.show()