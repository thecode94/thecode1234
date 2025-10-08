from collections import deque
grid = [
    ['.','.','.','#','.','.'],
    ['#','#','.','#','.','#'],
    ['.','.','.','.','.','.'],
    ['.','#','#','#','#','.'],
    ['.','.','.','#','#','.']
]
start=(0,0)
goal=(4,5)
directions=[(-1,0),(1,0),(0,-1),(0,1)]
    
def bfs(grid,start,goal):
    rows,cols=len(grid),len(grid[0])
    visited=set()
    queue=deque()
    queue.append((start,[start]))
    
    while queue:
        (x,y),path=queue.popleft()
        if(x,y)==goal:
            return path
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if(0<=nx<rows and 0<=ny<cols and grid[nx][ny]!='#'and(nx,ny)not in visited):
                visited.add((nx,ny))
                queue.append(((nx,ny),path+[(nx,ny)]))
    return None
        
path=bfs(grid,start,goal)
if path:
    print("shortest path:")
    for step in path:
        print(step)
else:
    print("No path found.")
