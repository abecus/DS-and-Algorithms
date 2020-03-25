"""
A 10*10 Crossword grid is provided to you, along with 
a set of words (or names of places) which need to be 
filled into the grid. Cells are marked either + or -. 
Cells marked with a - are to be filled with the word list.
"""

def solver(crossword:[str], words:str)->[str]:
    # making matrix of size n*n to make each element editable
    crossword = [[j for j in i] for i in crossword]
    # array of words
    words=words.split(';')
    l=len(words)
    # keeps track of used words in crossword matrix/board
    seen=[0]*l

    def get_row(crossword:[str], r:int, c:int)->(int, int):
        """
        returns the length of word in a given row "r",
        column of the first alphabet (word[0]) in that row 
        """
        l=0
        initial=10
        for i in reversed(range(c)):
            if crossword[r][i]!="+":
                l+=1
                initial=min(initial, i)
            else:
                break
        for i in range(c,10):
            if crossword[r][i]!="+":
                l+=1
                initial=min(initial, i)
            else:
                break
        return l, initial

    def get_col(crossword:[str], r:int, c:int)->(int, int):
        """
        returns the length of word in a given column "c",
        row of the first alphabet (word[0]) in that column
        """
        l=0
        initial=10
        for i in reversed(range(r)):
            if crossword[i][c]!="+":
                l+=1
                initial=min(initial, i)
            else:
                break
        for i in range(r,10):
            if crossword[i][c]!="+":
                l+=1
                initial=min(initial, i)
            else:
                break
        return l, initial

    def put_word_hor(crossword:[str], word:str, r:int, initial: int)->bool:
        """
        inserts the "word" in the row "r" of board 
        from coordinate crossword[r][initial] to 
        crossword[r][initial+len(word)] if its possible.
        if insertion was successful, returns 1
        """
        # checking if there any word intersecting with word where it have to be and if 
        # at that place the alphabets match.if they math or nothing is intersecting 
        # put the word there
        if all(0 if (crossword[r][i].isalpha() and crossword[r][i]!=word[i-initial]) else 1
               for i in range(initial,initial+len(word))):
            for i in range(initial,initial+len(word)):
                crossword[r][i]=word[i-initial]
            return 1

    def undo_word_hor(crossword:[str], word:str, r:int, initial: int)->bool:
        """
        removes the word from coordinate crossword[r][initial] to 
        crossword[r][initial+len(word)] but skips the
        intersecting alphabets to other words if any
        """
        for i in range(initial,initial+len(word)):
            if r-1>=0 and not crossword[r-1][i].isalpha():
                crossword[r][i]="-"
            elif r+1<10 and not crossword[r+1][i].isalpha():
                crossword[r][i]="-"
                
    def put_word_vert(crossword:[str], word:str, c:int, initial: int)->bool:
        """
        inserts the "word" in the column "c" of board 
        from coordinate crossword[initial][c] to 
        crossword[initial+len(word)][c] if its possible.
        if insertion was successful, returns 1
        """
        # checking if there any word intersecting with word where it have to be and if 
        # at that place the alphabets match.if they math or nothing is intersecting 
        # put the word there
        if all(0 if (crossword[i][c].isalpha() and crossword[i][c]!=word[i-initial]) else 1
               for i in range(initial,initial+len(word))):
            for i in range(initial,initial+len(word)):
                crossword[i][c]=word[i-initial]
            return 1

    def undo_word_vert(crossword:[str], word:str, c:int, initial: int)->bool:
        """
        removes the word from coordinate crossword[initial][c] to 
        crossword[initial+len(word)][c] but skips the
        intersecting alphabets to other words if any
        """
        for i in range(initial,initial+len(word)):
            if c-1>=0 and not crossword[i][c-1].isalpha():
                crossword[i][c]="-"
            elif c+1<10 and not crossword[i][c+1].isalpha():
                crossword[i][c]="-"
                    
    def foo(i:int, j:int, crossword:[[str]], words:[str], seen:[bool])->[[str]]:
        "solves the cross word puzzle"

        # checks if all words have been used if they are then returns the board
        if all(seen):
            return crossword
        
        # loop through all the coordinates/cell of the board
        for r in range(i,10):
            for c in range(j,10):
                # if cell can be filled with some word
                if crossword[r][c]=='-':
                    # gets len of word that can be filled in that col and row
                    # with there initial coordinates in that col and row
                    horlen, horinitial = get_row(crossword, r,c)
                    vertlen, vertinitial = get_col(crossword, r,c)

                    # loop through all the words, check if length of word mathes
                    # the available space in that row and col, and also word is 
                    # not in the board, make the word seen and reccurse on the board
                    # again with next cell, if solution is found return it, else
                    # remove the last word from the board and again do the same.
                    for idx in range(l):
                        if len(words[idx])==horlen and not seen[idx]:
                            if put_word_hor(crossword, words[idx], r, horinitial):
                                seen[idx]=1
                                temp=foo(r,c,crossword,words,seen)
                                if temp:
                                    return temp
                                seen[idx]=0
                                undo_word_hor(crossword, words[idx], r, horinitial)
                            
                        if len(words[idx])==vertlen and not seen[idx]:
                            if put_word_vert(crossword, words[idx], c, vertinitial):
                                seen[idx]=1
                                temp=foo(r,c,crossword,words,seen)
                                if temp:
                                    return temp
                                seen[idx]=0
                                undo_word_vert(crossword, words[idx], c, vertinitial)

    # returns the board, same style as the board at input
    return ["".join(i) for i in foo(0,0,crossword,words,seen)]


if __name__ == "__main__":
    # crossword=["+-++++++++","+-++++++++","+-++++++++","+-----++++","+-+++-++++","+-+++-++++","+++++-++++","++------++","+++++-++++","+++++-++++"]
    # words="LONDON;DELHI;ICELAND;ANKARA"

    # crossword=['+-++++++++', '+-++++++++', '+-------++', '+-++++++++', '+-++++++++', '+------+++', '+-+++-++++', '+++++-++++', '+++++-++++', '++++++++++'] 
    # words="AGRA;NORWAY;ENGLAND;GWALIOR"

    # crossword=["++++++++++","+------+++","+++-++++++","+++-++++++","+++-----++","+++-++-+++","++++++-+++","++++++-+++","++++++-+++","++++++++++"]
    # words="POLAND;LHASA;SPAIN;INDIA"

    # crossword=['XXXXXX-XXX','XX------XX','XXXXXX-XXX','XXXXXX-XXX','XXX------X','XXXXXX-X-X','XXXXXX-X-X','XXXXXXXX-X','XXXXXXXX-X','XXXXXXXX-X']
    # words="ICELAND;MEXICO;PANAMA;ALMATY"

    crossword=["+-++++++++","+-++-+++++","+-------++","+-++-+++++","+-++-+++++","+-++-+++++","++++-+++++","++++-+++++","++++++++++","----------"]
    words="CALIFORNIA;NIGERIA;CANADA;TELAVIV"
    print(*solver(crossword, words), sep="\n")