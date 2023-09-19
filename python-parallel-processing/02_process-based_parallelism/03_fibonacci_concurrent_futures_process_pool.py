from concurrent.futures import ProcessPoolExecutor


def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(fib, range(40))
        for i, result in enumerate(results):
            print(f"fib({i}) = {result}")