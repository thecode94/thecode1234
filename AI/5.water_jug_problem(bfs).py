from collections import deque
#define jug capacitiesand goal

jug1_capacity = 4
jug2_capacity = 3
goal = 2

def is_goal(state):
    x,y = state
    return x == goal or y==goal

def get_next_states(x,y):
    states = []
    
    #fill either jug
    states.append((jug1_capacity,y)) #fill jug 1
    states.append((x,jug2_capacity)) #fill jug 2
    
    #empty either jug
    states.append((0,y)) #empty jug 1
    states.append((x,0)) #empth jug 2
    
    #pour jug1-> jug2
    pour = min(x,jug2_capacity-y)
    states.append((x-pour,y+pour))
    
     #pour jug2-> jug1
    pour = min(y,jug1_capacity-x)
    states.append((x+pour,y-pour))
    return states

def bfs():
    visited = set()
    queue = deque()
    start_state =(0,0)
    queue.append((start_state,[start_state]))
    
    while queue:
        (x,y),path = queue.popleft()
        if(x,y) in visited:
            continue
        visited.add((x,y))
        if is_goal((x,y)):
            return path
    
        for next_state in get_next_states(x,y):
            if next_state not in visited:
                queue.append((next_state,path+[next_state]))
    return None

solution_path = bfs()
if solution_path:
    print("steps to reach the goal(2liters in one jug):")
    for step in solution_path:
        print(f"jug1:{step[0]}L,jug2:{step[1]}L")
else:
    print("No solution found")
