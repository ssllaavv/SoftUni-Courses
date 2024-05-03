class Stack:
    def __init__(self, data=[]):
        self.data = data

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return True if len(self.data) == 0 else False

    def __str__(self):
        reversed_data = reversed(self.data)
        return f"[{', '.join(reversed_data)}]"


s = Stack(["Gosho", "pesho", "Ivan", "Mariya", "Kosta"])

print(s)
print(s.pop())
print(s)
s.push("Miro")
print(s)
s.pop()
s.pop()
print(s.top())
print(s)
print(s.is_empty())
s.pop()
print(s.pop())
s.pop()
print(s.is_empty())
print(s)


