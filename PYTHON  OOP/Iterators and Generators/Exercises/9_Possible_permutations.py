

def possible_permutations(lst):
    # Helper function to generate permutations
    def generate_permutations(current, remaining):
        if not remaining:
            yield current
        else:
            for i in range(len(remaining)):
                # Create new current and remaining lists
                new_current = current + [remaining[i]]
                new_remaining = remaining[:i] + remaining[i + 1:]
                # Recursively generate permutations
                yield from generate_permutations(new_current, new_remaining)

    # Start the permutation generation with an empty current list
    yield from generate_permutations([], lst)


[print(n) for n in possible_permutations([1, 2, 3])]