def solution():

    def integers():
        counter = 1
        while True:
            yield counter
            counter += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        current_ind = 0
        while current_ind != n:
            result.append(next(seq))
            current_ind += 1

        return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

