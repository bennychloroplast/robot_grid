filename = 

#imports for csv interpretation
import os
import csv

#getting data out of csv
initialize = []
my_dir = os.path.dirname(os.path.realpath(__file__))
unepic = '/' + filename
with open(my_dir + unepic) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    for row in csv_reader:
        initialize.append(row)

#where the final list of moves will go, to be exported into a text file
move_list = ["row,col"]

#setting up the data from the initial reading
x = int(initialize[0][1])
y = int(initialize[0][0])
num_move = int(*initialize[1])
grid = []
for init_row in range(2,len(initialize)):
    grid.append(initialize[init_row])
ylen = len(grid)
xlen = len(grid[0])
for string_row in range(ylen):
    for string_col in range(xlen):
        grid[string_row][string_col] = int(grid[string_row][string_col])

#zero padding
for zero in range(3):
    for row in grid:
        row.insert(0,0)
        row.append(0)
    x += 1
temp_row_length = len(grid[0])
temp_zero_list = []
for zero_row in range(temp_row_length):
    temp_zero_list.append(0)
for zero_list in range(3):
    grid.insert(0,temp_zero_list)
    grid.append(temp_zero_list)
    y += 1


#start determining the moves
for num in range(num_move):
    grid[y][x] = 0
    temp_grid = grid
    for row in temp_grid:
        print(row)
    print(y,x)
    print("~~~")
    demo_grid = []
    for itemy in range(-2,3):
        # print(itemy)
        demo_row = []
        for itemx in range(-2,3):
            print(grid[y+itemy][x+itemx])
            new_value = grid[y+itemy][x+itemx]
            new_value_dis1 = 0
            for itemy_scan in range(-1,2):
                for itemx_scan in range(-1,2):
                    new_value_dis1 += grid[y+itemy+itemy_scan][x+itemx+itemx_scan]
            new_value += new_value_dis1/2
            temp_grid[y+itemy][x+itemx] = grid[y+itemy][x+itemx]+(grid[y+itemy-1][x+itemx-1]+grid[y+itemy-1][x+itemx]+grid[y+itemy-1][x+itemx+1]+grid[y+itemy][x+itemx-1]+grid[y+itemy][x+itemx+1]+grid[y+itemy+1][x+itemx-1]+grid[y+itemy+1][x+itemx]+grid[y+itemy+1][x+itemx+1])/2
            demo_row.append(temp_grid[y+itemy][x+itemx])
        demo_grid.append(demo_row)
    print("~~~")
    for row in demo_grid:
        print(row)
    print("~~~")
    analysis_grid_max = [0,0,0]
    for maxy in range(-2,3):
        cur_row_max = [0,0,0]
        for maxx in range(-2,3):
            # print(temp_grid[y+maxy][x+maxx],cur_row_max[0])
            if temp_grid[y+maxy][x+maxx] > cur_row_max[0]:
                cur_row_max = [temp_grid[y+maxy][x+maxx],y+maxy,x+maxx]
        if cur_row_max[0] > analysis_grid_max[0]:
            analysis_grid_max = cur_row_max
    target = analysis_grid_max[1:]
    # print(target)
    if target[0] < y:
        if target[1] < x:
            move_list.append("-1,-1")
            y -= 1
            x -= 1
        if target[1] == x:
            move_list.append("-1,0")
            y -= 1
        if target[1] > x:
            move_list.append("-1,1")
            y -= 1
            x += 1
    if target[0] == y:
        if target[1] < x:
            move_list.append("0,-1")
            x -= 1
        if target[1] == x:
            move_list.append("1,0")
            y += 1
        if target[1] > x:
            move_list.append("0,1")
            x += 1
    if target[0] > y:
        if target[1] < x:
            move_list.append("1,-1")
            y += 1
            x -= 1
        if target[1] == x:
            move_list.append("1,0")
            y += 1
        if target[1] > x:
            move_list.append("1,1")
            y += 1
            x += 1
    print()
    print()
    print()
    print("move over")
    print()
    print()
    print()
print(move_list)
# f = open("robot.moves", "w+")
# for item in move_list:
#     f.write("item")
#     f.write(" ")
# f.close()
