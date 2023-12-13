rus = input()
count = 0
for i in rus:
    if i in '!,.?;:-()"':
        count += 1
print(count)
