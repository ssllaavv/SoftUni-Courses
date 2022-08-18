def data_type_processor(type, string):
    if type == "int":
        result = int(string) * 2
    elif type == "real":
        result = f"{(float(string) * 1.5):.2f}"
    elif type == "string":
        result = f"${string}$"
    return result

input_type = input()
input_string = input()
print(data_type_processor(input_type, input_string))