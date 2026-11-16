"""Заготовки задач на базовый Python."""

from grader_contracts.python_basics import PositiveIntegerInput, TextInput, VectorPairInput


def count_vowels(data: TextInput) -> int:
    text = data.value
    count = 0

    for char in text:
        if char.lower() in "aeiou":
            count += 1

    return count


def has_unique_characters(data: TextInput) -> bool:
    text = data.value
    unique_chars = set(text)
    return len(text) == len(unique_chars)


def count_one_bits(data: PositiveIntegerInput) -> int:
    number = data.value
    return bin(number).count("1")


def multiplicative_persistence(data: PositiveIntegerInput) -> int:
    number = data.value
    count = 0

    while number >= 10:
        product = 1

        for digit in str(number):
            product *= int(digit)

        number = product
        count += 1

    return count


def mse(data: VectorPairInput) -> float:
    predicted, expected = data.predicted, data.expected

    errors = [
        (x - y) ** 2
        for x, y in zip(predicted, expected)
    ]

    return sum(errors) / len(errors)


def prime_factorization(data: PositiveIntegerInput) -> str:
    number = data.value
    result = ""
    divisor = 2

    while divisor * divisor <= number:
        power = 0

        while number % divisor == 0:
            number //= divisor
            power += 1

        if power > 0:
            if power == 1:
                result += f"({divisor})"
            else:
                result += f"({divisor}**{power})"

        divisor += 1

    if number > 1:
        result += f"({number})"

    return result


def pyramid(data: PositiveIntegerInput) -> int | str:
    cube_count = data.value
    total = 0
    level = 0

    while total < cube_count:
        level += 1
        total += level ** 2

    if total == cube_count:
        return level

    return "It is impossible"


def is_balanced_number(data: PositiveIntegerInput) -> bool:
    digits = str(data.value)
    length = len(digits)
    left = digits[:(length - 1) // 2]
    right = digits[length // 2 + 1:]
    return sum(int(d) for d in left) == sum(int(d) for d in right)
