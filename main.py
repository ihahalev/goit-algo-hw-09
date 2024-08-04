import timeit
from algorithms import find_coins_greedy, find_min_coins, find_min_coins_memo

amount = 113

print(f"Жадібний алгоритм для {amount}: {find_coins_greedy(amount)}")
print(f"Динамічне програмування (Bottom-Up): {amount}: {find_min_coins(amount)}")
print(f"Динамічне програмування (Top-Down): {amount}: {find_min_coins_memo(amount)}\n")


# Набір тестових сум
test_amounts = [113, 1234]

# Порівняння ефективності
for amount in test_amounts:
    greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=100)
    dynamic_time = timeit.timeit(lambda: find_min_coins(amount), number=100)
    memo_time = timeit.timeit(lambda: find_min_coins_memo(amount), number=100)

    print(f"Жадібний алгоритм для {amount}: {greedy_time:.6f} секунд")
    print(f"Динамічне програмування (Bottom-Up) для {amount}: {dynamic_time:.6f} секунд")
    print(f"Динамічне програмування (Top-Down) для {amount}: {memo_time:.6f} секунд\n")
