the_page = input()
list_page = the_page.split()
count_the = 0
for the_1 in list_page:
    the_2 = the_1.strip(',.')
    if the_2 == 'the':
        count_the += 1

print(count_the)
