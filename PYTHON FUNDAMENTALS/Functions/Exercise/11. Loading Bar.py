def print_loading_visualization(percent):
    percent_string = str(percent)
    argument_str = percent_string[:1]
    argument_int = int(argument_str)
    if percent < 10:
        print("[..........]")
        print("Still loading...")
    elif percent != 100:
        print(f"{percent}% [{'%' * argument_int}{'.' * (10 - argument_int)}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")

percent_input = int(input())
print_loading_visualization(percent_input)
