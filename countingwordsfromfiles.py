def countingwordsfromfile():
    filename=input("enter the file name")
    f=open(filename,'r')
    numberofwords=0
    for line in f:
        words=line.split()
        print(words)
        numberofwords=numberofwords+len(words)
        print(numberofwords)
    print(numberofwords)    
countingwordsfromfile()    