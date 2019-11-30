N = int(input())
magnet = input()
unit = magnet[:2]
while magnet.count(unit) > 0:
    magnet = magnet.replace(unit, '')
if len(magnet) > 0:
    print('No')
else:
    print('Yes')