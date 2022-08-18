code_input = input().split(chr(32))
while chr(9) in code_input:
    code_input.remove(chr(9))

array_of_code = []
for e in code_input:
    element = list(e)
    array_of_code.append(element)

merged_elements = []
remaining_elements = array_of_code.copy()
command = input().split()


while command != ['3:1']:
    merged_elements.clear()
    remaining_elements = array_of_code.copy()
    if command[0] == "merge":
        first_index = int(command[1])
        second_index = int(command[2])
        if (first_index in range(len(array_of_code) - 1) or -first_index in range(1, len(array_of_code))) \
               and (second_index in range(len(array_of_code) - 1) or -second_index in range(1, len(array_of_code))):
            for el in range(first_index, second_index):
                merged_elements += remaining_elements.pop(first_index)
        elif first_index in range(len(array_of_code) - 1) or -first_index in range(1, len(array_of_code)):
            for el in range(first_index, len(array_of_code)):
                merged_elements += remaining_elements.pop(first_index)
        elif second_index in range(len(array_of_code) - 1) or -second_index in range(1, len(array_of_code)):
            for el in range(0, second_index):
                merged_elements += remaining_elements.pop(first_index)
                second_index -= 1
        else:
            command = input().split()
            continue

        array_of_code.clear()
        array_of_code = remaining_elements.copy()
        array_of_code.insert(first_index, merged_elements.copy())
        merged_elements.clear()
        remaining_elements.clear()

    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])
        elements_for_partition = (len(array_of_code[index])) // partitions
        if elements_for_partition < (len(array_of_code[index])) % partitions:
            elements_for_partition -= 1
        list_of_partitioned_element = partitions * ['', ]
        for p in range(partitions):
            for elm in range(elements_for_partition):
                list_of_partitioned_element[p] += array_of_code[index].pop(0)
        for some_el in array_of_code[index]:
            list_of_partitioned_element[partitions -1] += array_of_code[index].pop(0)
        array_of_code.pop(index)
        array_of_partitioned_elements = []
        for h in list_of_partitioned_element:
            list_h = list(h)
            array_of_partitioned_elements.append(list_h)
        for s in array_of_partitioned_elements:
            array_of_code.insert(index, s)
            index += 1
        array_of_partitioned_elements.clear()
    command = input().split()
for k in range(len(array_of_code)):
    print(*array_of_code[k], sep='', end=' ')


