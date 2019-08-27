def swap(head, i=2):
    # Pairwise swap elements of a given list

    if i>=len(head):
        return head 

    else:
        head[i-2], head[i-1] = head[i-1], head[i-2]
        return swap(head, i+2)


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    print(swap(a))
