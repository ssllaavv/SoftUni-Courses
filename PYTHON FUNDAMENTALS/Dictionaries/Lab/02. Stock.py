stock_list = input().split()
stock_dict = {}
for el in range(0, len(stock_list), 2):
    stock_dict[stock_list[el]] = int(stock_list[el + 1])

request_list = input().split()

for key in request_list:
    if key in stock_dict.keys():
        print(f"We have {stock_dict[key]} of {key} left")
    else:
        print(f"Sorry, we don't have {key}")


