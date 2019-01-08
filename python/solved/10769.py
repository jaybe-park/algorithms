text = input()
happy_count = len(text) - len(text.replace(':-)', ''))
sad_count = len(text) - len(text.replace(':-(', ''))

if happy_count == sad_count == 0:
    print('none')
elif happy_count == sad_count:
    print('unsure')
elif happy_count > sad_count:
    print('happy')
else:
    print('sad')