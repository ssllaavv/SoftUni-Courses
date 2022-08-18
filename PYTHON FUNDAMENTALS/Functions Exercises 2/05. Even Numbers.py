# initial_list = list(map(int, input().split()))
initial_list = [int(el) for el in input().split()]

is_even = lambda x: x % 2 == 0

result = list(filter(is_even, initial_list))

print(result)
