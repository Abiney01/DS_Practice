def buy_and_sell_stock(arr):
    max_profit = 0
    profit = 0
    buy_price = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < buy_price:
            buy_price = arr[i]
        else:
            profit = arr[i] - buy_price
            max_profit = max(max_profit,profit)
    return max_profit

prices = [10,1,5,6,7,1]
print(buy_and_sell_stock(prices))