# to make star pattern with user input no 
'''    *
     * * *           for n = 3
   * * * * *    '''
 
n= int(input("enter the number for the pattern"))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end = "")
    print("")




# to make star pattern with user input no 
'''     *
        * *          for n = 3
        * * *     '''

n= int(input("enter the number for the pattern"))
for i in range(1,n+1):
    print("*"*(i),end="")
    print("")




# to make the star pattern with user input 
''' 
     *
   * *        n=3
 * * *
'''

n= int(input("enter the number for the pattern"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(i),end = "")
    print("")



# to make the star pattern with user input 
''' 
  
    * * *
    *   *        n=3
    * * *
'''

n= int(input("enter the number for the pattern"))
for i in range (1,n+1):
    if(i==1 or i==n):
        print("*"* n,end="")
    else:
        print("*",end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")
