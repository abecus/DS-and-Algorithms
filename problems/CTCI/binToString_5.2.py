
def binToString(num):
    temp = bin(num)[2:]
    return temp if len(temp)<=32 else 'error can\'t process'

if __name__ == "__main__":
    print(binToString(725110))