N = int(input())

color_paper = []
for __ in range(N):
    color_paper.append([True if x == 1 else False for x in list(map(int, input().split()))])

def print_paper(paper):
    for row in paper:
        print(*row)

def slice_4(curr_paper):
    first_half = slice(0, int(len(curr_paper) / 2))
    second_half = slice(int(len(curr_paper) / 2), len(curr_paper))

    upper_paper = curr_paper[first_half]
    lower_paper = curr_paper[second_half]

    paper_ul = []
    paper_ur = []
    paper_ll = []
    paper_lr = []
    
    for row in upper_paper:
        paper_ul.append(row[first_half])
        paper_ur.append(row[second_half])
    
    for row in lower_paper:
        paper_ll.append(row[first_half])
        paper_lr.append(row[second_half])

    return paper_ul, paper_ur, paper_ll, paper_lr

def is_white(paper):
    row_result = []
    for row in paper:
        row_result.append(any(row))
    return not any(row_result)

def is_blue(paper):
    row_result = []
    for row in paper:
        row_result.append(all(row))
    return all(row_result)

def find_paper_count(paper):

    if is_white(paper):
        return 1, 0
    if is_blue(paper):
        return 0, 1
    
    paper1, paper2, paper3, paper4 = slice_4(paper)

    paper1_white, paper1_blue = find_paper_count(paper1)
    paper2_white, paper2_blue = find_paper_count(paper2)
    paper3_white, paper3_blue = find_paper_count(paper3)
    paper4_white, paper4_blue = find_paper_count(paper4)

    return sum([paper1_white, paper2_white, paper4_white, paper3_white]), sum([paper1_blue, paper2_blue, paper4_blue, paper3_blue])


result_white, result_blue = find_paper_count(color_paper)
print(result_white)
print(result_blue)