electrons_count = int(input())
shells_list = []
electrons_in_current_shell = 0
remaining_electrons = electrons_count
current_shell = 1

while remaining_electrons > 0:
    while electrons_in_current_shell < 2 * (current_shell ** 2) and remaining_electrons > 0:
        electrons_in_current_shell += 1
        remaining_electrons -= 1
    shells_list.append(electrons_in_current_shell)
    electrons_in_current_shell = 0
    current_shell += 1
print(shells_list)

