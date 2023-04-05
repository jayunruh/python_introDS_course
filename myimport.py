
def findnthsubstring(mystr,substr,n=2):
    #it's a good idea to describe what your function does with comments
    #this function finds the nth instance of substr in mystr
    pos=0
    i=0
    while(i<n):
        pos=mystr.find(substr,pos+1)
        i+=1
    return pos
