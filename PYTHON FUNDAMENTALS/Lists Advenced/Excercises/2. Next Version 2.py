version = input()
ver_as_int = ""
for el in version:
    if el != ".":
        ver_as_int += el
ver_as_int = int(ver_as_int)
result_as_int = ver_as_int + 1
result = str(result_as_int)

print(".".join(result))
