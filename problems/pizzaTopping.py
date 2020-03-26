
def pizzaTopping(pizza, toppings, bank):
    pizza.sort()
    toppings.sort()
    
    error = float("inf")
    sol = float("inf")
    
    for i in range(len(pizza)):
        for j in range(len(toppings)):
            temp = pizza[i]+toppings[j]
            diff = abs(temp-bank)
            
            if diff < error:
                if abs(pizza[i]-bank) == diff:
                    sol = pizza[i]
                
                else:
                    sol = temp
                    
                error = diff
            
            else:
                break
            
    return sol

if __name__ == "__main__":
    p = [800, 850, 900]
    t = [100, 150]
    x = 1000
    
    # p = [850, 900]
    # t = [200, 250]
    # x = 1000
    
    # p = [1100, 900]
    # t = [200]
    # x = 1000
    
    # p = [800, 800, 800, 800]
    # t = [100]
    # x = 1000
    
    print(pizzaTopping(p, t, x))
        
    