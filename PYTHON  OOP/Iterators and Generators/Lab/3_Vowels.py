
class vowels:

    VOWELS = "AaEeIiOoUuYy"

    def __init__(self, text: str):
        self.text = text
        self.vowels_only = [l for l in text if l in vowels.VOWELS]

    def __iter__(self):
        self.vowels_only = [l for l in self.text if l in vowels.VOWELS]
        return self

    def __next__(self):
        if self.vowels_only:
            return self.vowels_only.pop(0)
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)


