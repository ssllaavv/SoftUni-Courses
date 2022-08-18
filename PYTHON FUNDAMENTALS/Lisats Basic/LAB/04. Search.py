elements_count = int(input())
word = input()

my_list = []
filtered_list = []


for _ in range(elements_count):
    my_list.append(input())

print(my_list)

for i in range(elements_count -1, -1, -1):
    element = my_list[i]
    if word not in element:
        my_list.remove(element)

print(my_list)
