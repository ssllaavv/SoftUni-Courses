# Task 1

class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)


# Task 2

class Party:
    def __init__(self):
        self.people = []


party = Party()

while True:
    person = input()
    if person == 'End':
        break

    party.people.append(person)

print(f'Going: {", ".join(party.people)}')
print(f'Total: {len(party.people)}')


# Task 3

class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []
while True:
    command = input()
    if command == 'Stop':
        break

    token = command.split(' ')
    sender = token[0]
    receiver = token[1]
    content = token[2]
    email = Email(sender, receiver, content)
    emails.append(email)

indexes = list(map(int, input().split(', ')))

for i in indexes:
    emails[i].send()

for email in emails:
    print(email.get_info())


# Task 4

class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'bird':
            self.birds.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        self.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            return f'Mammals in {self.name}: {", ".join(self.mammals)}' \
                   f'\nTotal animals: {self.__animals} '
        elif species == 'bird':
            return f'Birds in {self.name}: {", ".join(self.birds)}' \
                   f'\nTotal animals: {self.__animals} '
        elif species == 'fish':
            return f'Fishes in {self.name}: {", ".join(self.fishes)}' \
                   f'\nTotal animals: {self.__animals} '


zoo_name = input()
zoo = Zoo(zoo_name)

animals_count = int(input())

for a in range(animals_count):
    species, name = input().split(' ')
    zoo.add_animal(species, name)

species = input()
print(zoo.get_info(species))


# Task 5

class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return self.diameter * self.__pi

    def calculate_area(self):
        return (self.diameter / 2) ** 2 * self.__pi

    def calculate_area_of_sector(self, angle):
        return ((self.diameter / 2) ** 2 * self.__pi * angle) / 360


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")



























