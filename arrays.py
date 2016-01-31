from numpy import arange


#a= np.array(range(10),dtype=float)
#print a

#an index can be created to search through the array that match the same position

#x=array([3,5.7])
# the 3 is changed automatically to a higher type, float in this case
#arrays can be changed x[1]=3 would return x=3.,3.
# for 3d arrays 
#indexes can be made and searched from an array to get data faster
#to make a quick array use arange() ex. arange(10) would return arange([1,2,3,4,5,6,7,8,9])
#rubics cube
#a=np.arange(1,10)
#a.shape=(3,3)
#b=a.copy()
#a[0,0]=b[2,0]
#a[0,1]=b[1,0]
#a[0,2]=b[0,0]
#a[1,2]=b[0,1]
#a[2,2]=b[0,2]
#a[2,1]=b[1,2]
#a[2,0]=b[2,2]
#a[1,0]=b[2,1]
#a[0,0]=b[2,0]

def rotate_cube():
    a=np.arange(1,10)
    a.shape=(3,3)
    b=a.copy()
    for r in range(0,3):
    
        for c in range(0,3):
            print r,c


def frontrotate90(a):
    b=rcube.copy()
    a[0,2,2],a[0,1,2],a[0,0,2]=b[0,0,2],b[0,0,1],b[0,0,0]
    a[0,2,0],a[0,2,1]=b[0,2,2],b[0,1,2]
    a[0,0,0],a[0,1,0]=b[0,2,0],b[0,2,1]
    a[0,0,1]=b[0,1,0]
    return a
   
if __name__ == "__main__": 
    rcube=arange(1,28)
    rcube.shape=(3,3,3)
    rcube =frontrotate90(rcube)
    print "Rotate"
    print rcube
    



