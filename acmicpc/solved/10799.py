s = input().replace('()', 'r')
result = 0
stick = 0
for c in s:
    if c == '(':
        stick += 1
    elif c == ')':
        result += 1
        stick -= 1
    elif c == 'r':
        result += stick
    
print(result)