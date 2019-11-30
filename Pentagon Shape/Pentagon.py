print Pentagon like this

      *       
    *   *     
  *       *   
*           * 
*           * 
*           * 
* * * * * * * 

==========================================

for row in range(7):
    for col in range(7):
        if(row==6 or row+col==3 or col-row==3) or(col==0 and row in range(3,8))or(col==6 and row>2 and row%col!=0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
