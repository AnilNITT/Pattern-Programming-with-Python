Print hexagon like this

    *  *  *     
  *         *   
*             * 
  *         *   
    *  *  *     

======================================================

for row in range(5):
    for col in range(7):
        if(row+col==2 or col-row==4 or row+col==8 or row-col==2)or(row==0 and 1<col<5)or(row==4 and 1<col<5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
