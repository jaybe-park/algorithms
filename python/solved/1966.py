T = int(input())

def find_max_inportance(print_queue):
    return max(map(lambda x : x[0], print_queue))

for _ in range(T):
    N, M = map(int, input().split())
    importances = list(map(int, input().split()))
    
    print_queue = []

    for importance in importances:
        print_queue.append([importance, False])
    
    print_queue[M][1] = True

    print_order = 1
    while len(print_queue) != 0:
        max_importance = find_max_inportance(print_queue)
        
        while print_queue[0][0] != max_importance:
            print_queue.append(print_queue.pop(0))
        
        printing_text = print_queue.pop(0)

        if printing_text[1]:
            print(print_order)
        else:
            print_order = print_order + 1