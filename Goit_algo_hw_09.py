import time

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [None] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[amount] == float('inf'):
        return None

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Тестування та вимірювання часу
amount = 113
start_time = time.time()
greedy_result = find_coins_greedy(amount)
end_time = time.time()
print(f"Greedy Result: {greedy_result}, Time: {end_time - start_time:.6f}s")

start_time = time.time()
dp_result = find_min_coins(amount)
end_time = time.time()
print(f"DP Result: {dp_result}, Time: {end_time - start_time:.6f}s")