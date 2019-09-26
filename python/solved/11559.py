screen = []
for __ in range(12):
    screen.append(list(input()))

screen = list(map(lambda x: list(reversed(x)), zip(*screen)))

def is_in_screen(inx, jnx):
    if inx < 0 or inx >= 6 or jnx < 0 or jnx >= 12:
        return False
    else:
        return True

def find_same_color(screen, visited, inx, jnx, color):
    if not is_in_screen(inx, jnx):
        return 0

    if screen[inx][jnx] != color:
        return 0

    if visited[inx][jnx]:
        return 0
    visited[inx][jnx] = True

    result = 1
    result += find_same_color(screen, visited, inx + 1, jnx, color)
    result += find_same_color(screen, visited, inx - 1, jnx, color)
    result += find_same_color(screen, visited, inx, jnx + 1, color)
    result += find_same_color(screen, visited, inx, jnx - 1, color)

    return result

def pop(screen, inx, jnx, color):
    if not is_in_screen(inx, jnx):
        return

    if screen[inx][jnx] != color:
        return

    screen[inx][jnx] = '.'

    pop(screen, inx + 1, jnx, color)
    pop(screen, inx - 1, jnx, color)
    pop(screen, inx, jnx + 1, color)
    pop(screen, inx, jnx - 1, color)

    return
    

result = 0
while True:
    flag_pop = False
    pop_target = []

    visited = [[False] * 12 for __ in range(6)]
    for inx in range(6):
        for jnx in range(12):
            if screen[inx][jnx] == '.':
                break
            if not visited[inx][jnx]:
                curr_count = find_same_color(screen, visited, inx, jnx, screen[inx][jnx])
                if curr_count >= 4:
                    flag_pop = True
                    pop_target.append((inx, jnx))
    
    if not flag_pop:
        break

    result += 1
    for target_inx, target_jnx in pop_target:
        pop(screen, target_inx, target_jnx, screen[target_inx][target_jnx])
    
    for inx in range(6):
        next_row = list(filter(lambda x: x != '.', screen[inx]))
        next_row.extend('.' * (12 - len(next_row)))
        screen[inx] = next_row

print(result)