
def reverse_text(text: str):
    text = list(text)
    while text:
        yield text.pop(-1)


for char in reverse_text("step"):
    print(char, end='')
