count = int(input())

positives = []
negatives = []

for i in range(count):
    input_line = int(input())
    if input_line >= 0:
        positives.append(input_line)
    else:
        negatives.append(input_line)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")

