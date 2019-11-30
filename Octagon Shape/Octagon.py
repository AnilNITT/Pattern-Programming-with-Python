print Octagon like this

    *  *  *     
  *         *   
*             * 
*             * 
*             * 
  *         *   
    *  *  *     

=======================================================

for row in range(7):
    for col in range(7):
        if(row+col==2 or col-row==4 or row+col==10 or row-col==4)or(row==6 and 1<col<5)or(row==0 and 1<col<5)or(col==0 and 1<row<5)or(col==6 and 1<row<5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
