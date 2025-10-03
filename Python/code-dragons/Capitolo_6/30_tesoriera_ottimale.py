'''Alla Tesoreria Ottimale, ogni tributo va minimizzato. Calcola con `min_coins(amount, coins)`: restituisci il **numero minimo** di monete per ottenere `amount`; se impossibile, torna `1_000_000_000`. Mantieni la firma e lascia che i test si aprano.'''

def min_coins(amount, coins):
    INF = 1_000_000_000
    dp = [INF] * (amount + 1)
    dp[0] = 0  # base case: 0 monete per 0

    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:  # se posso usare la moneta c
                dp[i] = min(dp[i], 1 + dp[i - c])

    return dp[amount] if dp[amount] != INF else INF
