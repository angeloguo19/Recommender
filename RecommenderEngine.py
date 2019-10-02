'''
@author: Angelo Guo ag470
'''

def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''
    totals={}
    votes={}
    final=[]
    for item in items:
        totals[item]=0
        votes[item]=0
    for rating in ratings.items():
        nums=rating[1]
        for i in range(len(nums)):
            if nums[i]!=0:
                totals[items[i]]+=nums[i]
                votes[items[i]]+=1
    for k,v in totals.items():
        if votes[k] != 0:
            final.append((k,float(v/votes[k])))
        else:
            final.append((k,0.0))
    final.sort(key=lambda x:x[0])
    final.sort(key=lambda x:x[1], reverse=True)
    return final
        
def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    origin=ratings[name]
    final=[]
    for n,v in ratings.items():
        if n!= name:
            dot=[origin[i]*v[i] for i in range(len(v))]
            total=sum(dot)
            final.append((n,total))
    final.sort(key = lambda x:x[0])
    final.sort(key = lambda x:x[1], reverse=True)
    return final
            
 
def recommendations(name, items, ratings, size):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''
    weights=similarities(name,ratings)
    final=[]
    totals={}
    votes={}
    for item in items:
        totals[item]=0
        votes[item]=0
    for i in range(size):
        person=weights[i][0]
        r=ratings[person]
        w=weights[i][1]
        for i in range(len(r)):
            item=items[i]
            if r[i]!=0:
                totals[item]+=w*r[i]
                votes[item]+=1
    for k,v in totals.items():
        if votes[k] != 0:
            final.append((k,float(v/votes[k])))
        else:
            final.append((k,0.0))
    final.sort(key = lambda x:x[0])
    final.sort(key = lambda x:x[1], reverse=True)
    return final
        


if __name__ == '__main__':
    items = ['Cat', 'Dog']
    ratings = {'Liam': [0, 0], 'Man-Lin': [0, 3], 'Max': [0, 6]}
    print(averages(items,ratings))
