
def foo2():
    x=100
    print "Local:" ,locals()
    print x

if __name__ == '__main__':
    print "this is the main program"
    foo2()


#to import a function you must call the file from the correct directory then call the specific function