def get_primes(numbers: list):
    result = []

    for num in numbers:
        if num > 1:
            prime = True

            for i in range(2, num//2 + 1):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                yield num
                result.append(num)

    # return result


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

