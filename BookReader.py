'''
@author: Angelo Guo ag470
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    file=open("data/books.txt")
    books=[]
    names={}
    lines=[line.strip() for line in file]
    for line in lines:
        line=line.split(",")
        ratings=[]
        for i in range(1,len(line)):
            if (i%2) != 0:
                if line[i] not in books:
                    books.append(line[i])
            else:
                ratings.append(int(line[i]))
        names[line[0]]=ratings
    return (books,names)
