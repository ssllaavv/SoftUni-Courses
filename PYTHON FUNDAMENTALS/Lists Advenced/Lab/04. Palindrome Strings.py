initial_list = input().split()
key_palindrome = input()

palindrome_list = [element for element in initial_list if element == element[::-1]]


#print(initial_list)
print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(key_palindrome)} times")