from pythagoreanTriplets import *
import matplotlib.pyplot as plt


def oeis(n):
    spf=EratosthenesSieve((n - int(sqrt((n<<1) -1)))<<1)
    y=[]
    x=[]
    for b2 in range(4, (n - int(sqrt((n<<1) -1)))<<1, 2):
        val=getReducedFactorization(b2, spf)
        count=0
        for i in range(max(int(sqrt(b2)//val), 1), int(sqrt(b2*((b2>>1)-1)))//val+1):
            i*=val
            sqVal = i*i
            q=sqVal//b2
            if q+i+(b2>>1)>n:
                break
            else:
                # x=q+i
                # print(x, (b2>>1)+i, x+(b2>>1))
                count+=1
        y.append(count)
        x.append(b2)
    return x,y


x,y=oeis(1_00)
print([(i,j) for i,j in zip(x,y)])
plt.scatter(x, y, c="k", s=0.5)
plt.show()
