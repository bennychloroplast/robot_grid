import os
import csv
my_dir = os.path.dirname(os.path.realpath(__file__))
with open('robot.map.20x20.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
print(csv_reader)
# x=csv_reader[0][1]
# y=csv_reader[0][0]
# num_move=csv_reader[1][0]
# xlen=len(grid[0])
# ylen=len(grid)
# list_moves=[]
#     for num in range(num_move):
#         grid[y][x]=0
#         value_list=[]
#         for itemy in range(-2,2):
#             for itemx in range(-2,2):
#                 value_list.append(grid[y+itemy][x+itemx]+(grid[y+itemy-1][x+itemx-1]+grid[y+itemy-1][x+itemx]+grid[y+itemy-1][x+itemx+1]+grid[y+itemy][x+itemx-1]+grid[y+itemy][x+itemx+1]+grid[y+itemy+1][x+itemx-1]+grid[y+itemy+1][x+itemx]+grid[y+itemy+1][x+itemx+1])/2)
#         high=max(value_list)
#         index=0
#         for search in range(24)
#             if high==value_list[search]
#                 then index=search
#         if index==(0,1,5,6)
#             then list_moves.append((-1,-1))
#             x-=1
#             y-=1
#         if index==(2,7)
#             then list_moves.append((-1,0))
#             y-=1
#         if index==(3,4,8,9)
#             then list_moves.append((-1,1))
#             x+=1
#             y-=1
#         if index==(10,11)
#             then list_moves.append((0,-1))
#             x-=1
#         if index==(13,14)
#             then list_moves.append((0,1))
#             x+=1
#         if index==(15,16,20,21)
#             then list_moves.append((1,-1)
#             y+=1
#             x-=1
#         if index==(17,22)
#             then list_moves.append((1,0))
#             y+=1
#         if index==(18,19,23,24)
#             then list_moves.append((1,1))
#             y+=1
#             x+=1
