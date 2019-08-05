def urlfy(s, stringLength):
    """
    itype : s(string), stringLength(int)
    rtype: string
    """
    return s[: stringLength].replace(" ", '%20')
    

if __name__ == "__main__":
    print(urlfy('Mr John Smith     ', 13))