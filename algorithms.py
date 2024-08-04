coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            amount -= num_coins * coin
            result[coin] = num_coins
    return result

def find_min_coins(amount):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    prev_coin = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                prev_coin[i] = coin

    result = {}
    while amount > 0:
        coin = prev_coin[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    return result

def find_min_coins_memo(amount):
    memo = {}

    def dp(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return (0, {})
        min_count = float('inf')
        best_combination = {}
        for coin in coins:
            if n >= coin:
                count, combination = dp(n - coin)
                count += 1
                if count < min_count:
                    min_count = count
                    best_combination = combination.copy()
                    best_combination[coin] = best_combination.get(coin, 0) + 1
        memo[n] = (min_count, best_combination)
        return memo[n]

    _, result = dp(amount)
    return result