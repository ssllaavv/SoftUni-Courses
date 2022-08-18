class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

while True:
    command = input()
    if command == "Stop":
        break
    command_list = command.split()
    sender, receiver, content = command_list
    email = Email(sender, receiver, content)
    emails.append(email)

indexes = list(map(int, input().split(", ")))

for x in indexes:
    emails[x].send()

for email in emails:
    print(email.get_info())
