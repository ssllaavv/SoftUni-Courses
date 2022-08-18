counter = 0
phonebook_dict = {}
while True:
    data_entry = input()
    if "-" not in data_entry:
        counter = int(data_entry)
        break
    data_entry_list = data_entry.split("-")
    phonebook_dict[data_entry_list[0]] = data_entry_list[1]

for i in range (counter):
    name = input()
    if name in phonebook_dict:
        print(f"{name} -> {phonebook_dict[name]}")
    else:
        print(f"Contact {name} does not exist.")

