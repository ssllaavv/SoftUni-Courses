tickets_list = input().split(", ")


for el in tickets_list:
    is_winner = False
    ticket = el.strip()
    if len(ticket) == 20:
        left = ticket[:10]
        right = ticket[10:20]
        for symbol in "@#$^":
            if is_winner:
                break
            for count in range(10, 5, -1):
                result = count * symbol
                if (result in left) and (result in right):
                    if count == 10:
                        print(f'ticket "{ticket}" - {count}{symbol} Jackpot!')
                        is_winner = True
                        break
                    else:
                        print(f'ticket "{ticket}" - {count}{symbol}')
                        is_winner = True
                        break
        if not is_winner:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")
