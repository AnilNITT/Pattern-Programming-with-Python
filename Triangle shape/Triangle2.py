Print Triangle look like this


            * 
          * * 
        *   * 
      *     * 
    *       * 
  *         * 
* * * * * * *  

==================================================

for row in range(7):
    for col in range(7):
        if(row-col==row)or(row==6)or(row==col):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    # for new line or row for print
