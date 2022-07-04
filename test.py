grid = [["5","3"," "," ","7"," "," "," "," "],["6"," "," ","1","9","5"," "," "," "],[" ","9","8"," "," "," "," ","6"," "],["8"," "," "," ","6"," "," "," ","3"],["4"," "," ","8"," ","3"," "," ","1"],["7"," "," "," ","2"," "," "," ","6"],[" ","6"," "," "," "," ","2","8"," "],[" "," "," ","4","1","9"," "," ","5"],[" "," "," "," ","8"," "," ","7","9"]]



def isSafe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
        

def solve(grid):      
    for i in range(0,9):
        for j in range(0,9):
            # empty cell
            if(grid[i][j]==' '):
                a = '123456789'
                for k in range(0,9):
                    if(isSafe(grid,i,j,a[k])):
                        grid[i][j]=a[k];                   
                        if(solve(grid)):
                            return True
                                
                        else:
                            grid[i][j]=' '
                                
                            
                        
                return False
                    
                
            

    return True

solve(grid)
dict={}     
for i in range(81):    
    dict[i]=grid[int(i/9)][(i-int(i/9)*9)%9]
print(dict)