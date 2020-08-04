from alive_progress import alive_bar
import matplotlib.pyplot as plt
import numpy as np


def get_iter(c:complex, thresh:int =4, max_steps:int =25) -> int:
    # Z_(n) = (Z_(n-1))^2 + c
    # Z_(0) = c
    z=c
    i=1
    while i<max_steps and (z*z.conjugate()).real < thresh:
        z = z*z + c
        i+=1
    return i

def plotter(n, thresh, max_steps=25):
    # since we know the bounds of x and y use it to save 
    # redundant computations
    # x \in {-2, 0.47} , y \in {-1.17, 1.17}
    
    # image_coordinate (integers) --> real value to use 
    # on complex plane
    mx = 2.48 / (n-1)
    my = 2.26 / (n-1)
    mapper = lambda x,y: (mx*x - 2, my*y - 1.13)

    # create image array (n*n) fill value 255
    img = np.full((n,n), 255)
    
    with alive_bar(n*n) as bar:
        for x in range(n):
            for y in range(n):
                
                it = get_iter(complex(*mapper(x,y)), 
                                thresh=thresh, 
                                max_steps=max_steps)
                
                # image get rotated with -90 dergee (don't know why)
                # so know rotating 90 by changing coordinate below
                img[y][x] = 255 - it
                bar()

        return img


if __name__ == "__main__":
    n=12500
    img = plotter(n, thresh=4, max_steps=50)
    np.save("mandelbrotSetNP_12500", img)
    # img=np.load("mandelbrotSetNP_1000.npy")
    plt.imshow(img, cmap="plasma")
    plt.axis("off")
    plt.show()

