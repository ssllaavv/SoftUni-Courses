import re

pattern = r'((w{3})(\.[a-zA-Z0-9\-]+)(\.[a-z]+)+)'
text = input()
while text:
    match = re.findall(pattern, text)
    for element in match:
        print(element[0])
    text = input()

