'''
@author: Angelo Guo ag470
'''
import RecommenderEngine

def makerecs(name, items, ratings, size, top):
    '''
    This function calculates the top recommendations and returns a two-tuple consisting of two lists. 
    The first list is the top items rated by the rater called name (string).
    The second list is the top items not seen/rated by name (string)
    '''
    recs=RecommenderEngine.recommendations(name,items,ratings,size)
    seen=[]
    notseen=[]
    for r in recs:
        item=r[0]
        loc=items.index(item)
        if ratings[name][loc]==0 and len(notseen)!=top:
            notseen.append(r)
        if ratings[name][loc]!=0 and len(seen)!=top:
            seen.append(r)
        if len(seen)==top and len(notseen)==top:
            return (seen,notseen)
    return(seen,notseen)

if __name__ == '__main__':
    name = "student1367"
    items = ['127 Hours', 'The Godfather', '50 First Dates', 'A Beautiful Mind', 'A Nightmare on Elm Street', 'Alice in Wonderland', 'Anchorman: The Legend of Ron Burgundy', 'Austin Powers in Goldmember', 'Avatar', 'Black Swan']

    ratings = {'student1367': [2, 3, -5, 2, 3, 1, 5, 1, 3, 4], 
               'student1046': [2, 3, -5, 2, 3, 1, 5, 1, 3, 4], 
               'student1206': [2, 3, -5, 2, 3, 1, 5, 1, 3, 4], 
               'student1103': [2, 3, -5, 2, 3, 1, 5, 1, 3, 4]}

    size = 2
 
    top = 3
    print(RecommenderEngine.recommendations(name,items,ratings,size))
    print(makerecs(name,items,ratings,size,top))

             



