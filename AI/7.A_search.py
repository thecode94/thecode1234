import heapq
grid=[
    ['.','.','.','.'],
    ['.','#','#','.'],
    ['.','.','.','.'],
    ['#','.','#','.'],
    ]
start=(0,0)
goal=(3,3)

directions=[(-1,0),(1,0),(0,-1),(0,1)]


def heuristic(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def a_star(grid,start,goal):
    rows,cols=len(grid),len(grid[0])
    open_set=[]
    heapq.heappush(open_set,(0+heuristic(start,goal),0,start,[start]))
    visited=set()

    while open_set:
        f,g,current,path=heapq.heappop(open_set)
        if current==goal:
            return path
        if current in visited:
            continue
        visited.add(current)

        for dx,dy in directions:
            nx,ny=current[0]+dx,current[1]+dy
            neighbor=(nx,ny)

            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]!='#'and neighbor not in visited:
                heapq.heappush(open_set,(
                    g+1+heuristic(neighbor,goal),
                    g+1,
                    neighbor,
                    path + [neighbor]
                    ))
    return None
shortest_path=a_star(grid,start,goal)
if shortest_path:
    print("Shortest Path from  start to goal:")
    for step in shortest_path:
       print(f"Step:{step}")
else:
    print("No path found.")
