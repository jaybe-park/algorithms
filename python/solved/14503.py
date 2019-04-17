import sys
N, M = map(int, sys.stdin.readline().split())
robot_x, robot_y, robot_dir = map(int, sys.stdin.readline().split())
room = []
for __ in range(N):
    room.append(list(map(int, sys.stdin.readline().split())))

result = 0
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3

def get_forward_xy(x, y, d):
    if d == NORTH:
        forward_x, forward_y = x - 1, y
    elif d == EAST:
        forward_x, forward_y = x, y + 1
    elif d == SOUTH:
        forward_x, forward_y = x + 1, y
    elif d == WEST:
        forward_x, forward_y = x, y - 1
    return forward_x, forward_y

        
def clean():
    global result, robot_x, robot_y, robot_dir
    if room[robot_x][robot_y] == 0:
        room[robot_x][robot_y] = 2
        result += 1
        return True
    else:
        for __ in range(4):
            robot_dir = (robot_dir - 1) % 4
            forward_x, forward_y = get_forward_xy(robot_x, robot_y, robot_dir)
            if room[forward_x][forward_y] == 0:
                robot_x, robot_y = forward_x, forward_y
                return True
        
        robot_dir = (robot_dir + 2) % 4
        forward_x, forward_y = get_forward_xy(robot_x, robot_y, robot_dir)
        if room[forward_x][forward_y] == 1:
            return False
        else:
            robot_x, robot_y = forward_x, forward_y
            robot_dir = (robot_dir + 2) % 4
            return True

while clean():
    # print(robot_x, robot_y, robot_dir, result)
    pass

print(result)