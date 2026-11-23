"""Grade calculator: average and pass or fail."""

PASS_MARK = 10


def average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


def has_passed(grade):
    return grade >= PASS_MARK


def best(grades):
    return max(grades)


def worst(grades):
    return min(grades)


def count(grades):
    return len(grades)
