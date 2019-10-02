'''
@author: Angelo Guo ag470
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    file=open("data/movies.txt")
    items=[]
    names={}
    lines=[line.strip() for line in file]
    file.close()
    for line in lines:
        line=line.split(",")
        if line[1] not in items:
            items.append(line[1])
    items.sort()
    for line in lines:
        line=line.split(",")
        if line[0] not in names:
            names[line[0]]=[0 for _ in range(len(items))]
        loc=items.index(line[1])
        names[line[0]][loc]=int(line[2])

    return(items,names)