# Create a function wrapper that remembers previous results.
# When the same input appears:
# Return stored result.
# Do not recompute.
# No classes allowed.


def square(inp):
    return inp ** 2

def memoize(func):
    cache = {}

    def wrapper(inp):
        if inp in cache:
            return cache[inp]

        result = func(inp)
        cache[inp] = result
        return result

    return wrapper

res = memoize(square)
print(res(4))  # stores
print(res(4))  # Returns stored result from cache