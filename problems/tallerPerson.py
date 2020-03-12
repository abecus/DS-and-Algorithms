def tallerPerson(arr):
    if arr:
        temp=arr[-1]
        res=[temp]
        for person in reversed(arr):
            if person>temp:
                temp=person
                res.append(temp)
        return reversed(res)
    return

if __name__ == "__main__":
    arr=[3,6,3,4,1]
    print(*tallerPerson(arr))