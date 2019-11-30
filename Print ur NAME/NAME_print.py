# Print ur name in pixels format like this


      #         #           #   # # # # #   #         
    #   #       # #         #       #       #         
  #       #     #   #       #       #       #         
#           #   #     #     #       #       #         
# # # # # # #   #       #   #       #       #         
#           #   #         # #       #       #         
#           #   #           #   # # # # #   # # # # # 

========================================================

print("NAME\n")
for row in range(7):
    for col in range(27):
        if(col==8 or col==14 or col==18 or col==22) or(col-row==8) or(2<row and row-col==row)or(7>col>2 and col-row==3)or(col<4 and row+col==3) or(col==6 and row>=3)or(row==4 and col<=6)or (row==6 and 21<col<=28) or(row==0 and 15<col<21)or(row==6 and 15<col<21) :
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()
