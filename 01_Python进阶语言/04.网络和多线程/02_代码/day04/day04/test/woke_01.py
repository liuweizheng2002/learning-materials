
'''

count = 0
for s in [str(i) for i in range(1234, 4322)]:
    if ('1' in s and '2'in s and '3' in s and '4' in s
            and '13' not in s and '31' not in s and s[0] != '4'):
        count += 1
        print(s, end='\n' if count % 5 == 0 else '\t')

'''


import copy
my_list = ['aa', 'bb', 'cc', 'bb', 'bb', 'bb', 'dd']
# new_list = [s for s in my_list if s != 'bb']

for s in copy.copy(my_list):
    if s == 'bb':
        my_list.remove(s)
print(my_list)


